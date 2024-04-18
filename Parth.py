
import pandas as pd
import os
import numpy as np
from sklearn.linear_model import LinearRegression
from pathlib import Path
import matplotlib.pyplot as plt
import statsmodels.api as sm
import matplotlib.ticker as mtick

#Import merged final
final_merged = "/Users/parthpisolkar/Desktop/Bootcamp Materials/Project 1/project1_group4/merged_final.csv"
final = pd.read_csv(final_merged)
final_dataset = pd.DataFrame(final)

#Pre Analysis Set Up
ivy = final_dataset
ivy_league = ["Brown University",
                "Columbia University in the City of New York",
                "Cornell University",
                "University of Massachusetts-Dartmouth",
                "Harvard University",
                "University of Pennsylvania",
                "Princeton University",
                "Yale University"]

ivy = ivy[ivy['instnm.x'].isin(ivy_league)].reset_index()
ivy = ivy.dropna(subset=['sevcrime'])
ivy.to_excel("ivy_leagues.xlsx",index=False)


ivy['instnm.x'].nunique()
# Define a dictionary to map original names to shortened versions
name_map = {
    "Brown University": "Brown",
    "Columbia University in the City of New York": "Columbia",
    "Cornell University": "Cornell",
    "University of Massachusetts-Dartmouth": "Dartmouth",
    "Harvard University": "Harvard",
    "University of Pennsylvania": "UPenn",
    "Princeton University": "Princeton",
    "Yale University": "Yale"
}


#Analysis 1 - Difference between Median Earnings between Ivy League Schools
mean_wmearn_unitid = ivy.groupby('instnm.x')['wmearn_unitid'].mean().sort_values(ascending = False)
bar1 = mean_wmearn_unitid.plot(kind = 'bar')
plt.xlabel('Institution')
plt.gca().set_xticklabels([name_map.get(tick.get_text(), tick.get_text()) for tick in plt.gca().get_xticklabels()])
plt.ylabel('Mean Earnings')
plt.title('Mean Earnings by Institution')
plt.xticks(rotation = 45, ha='right')
plt.tight_layout()
plt.ylim(50000,80000)
plt.show()


#Analysis 2 - Percent of Grads choosing institutions home state after graduation
mean_pginstate_unitid = ivy.groupby('instnm.x')['pginstate'].mean().sort_values(ascending=False)
bar2 = mean_pginstate_unitid.plot(kind = 'bar')
plt.xlabel('Institution')
plt.ylabel('In-State Grads %')
plt.title('Post-Graduation Migration')
plt.gca().set_xticklabels([name_map.get(tick.get_text(), tick.get_text()) for tick in plt.gca().get_xticklabels()])
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#Analysis 3
mean_stateliv_unitid = ivy.groupby('st')['share_state'].sum().sort_values(ascending=False) / 8
top_10_states = mean_stateliv_unitid.head(10)

plt.figure(figsize=(6, 6))

# Plot the pie chart for the top 10 states
top_10_states.plot(kind='pie', autopct='%1.1f%%', startangle=180, fontsize= 10,
                    pctdistance=0.85, counterclock = False)
plt.title('Top 10 States with Ivy League Graduates')
plt.ylabel('') 
plt.axis('equal') 
plt.tight_layout()
plt.show()


# Analysis 4 How does income get affected by attending IVY league school
final_dataset['is_ivy_league'] = final_dataset['instnm.x'].apply(lambda x: 1 if x in ivy_league else 0)
final2 = final_dataset.dropna(subset=['wmearn_unitid'])
X = final2['is_ivy_league']
Y = final2['wmearn_unitid']
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
print(model.summary())

#Export Summary to Excel
summary_table = pd.read_html(model.summary().tables[1].as_html(), header=0, index_col=0)[0]
summary_table.to_excel('summary_table.xlsx')