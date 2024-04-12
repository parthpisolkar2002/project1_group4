'''import os
import pandas as pd

housing = os.path.join("..","Housing Data.xlsb.csv")
housing_data = pd.read_csv(housing)
housing_data.head()'''
import pandas as pd
import os
import numpy as np
from pathlib import Path

# Construct the file path
twenty_one = "/Users/parthpisolkar/Desktop/Bootcamp Materials/Project 1/project1_group4/c2021_a.csv"
# Read the CSV file into a pandas DataFrame
degrees_2021 = pd.read_csv(twenty_one)

# Display the first few rows of the DataFrame
num_rows, num_columns = degrees_2021.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")
degrees_2021.head(10)

#Importing Institution files
Institution = "/Users/parthpisolkar/Desktop/Research Fellowship/2022-2023/LinkedIn Data/Data/InstitutionFile.dta"
ins_data = pd.read_stata(Institution)
print(ins_data.head())

#Importing CIPCODE defintions (through excel)
cc = "/Users/parthpisolkar/Desktop/Bootcamp Materials/Project 1/project1_group4/CCIHE2021-CIPMap.xlsx"
cipcode = pd.read_excel(cc)


#Conversion into dataframes
education = pd.DataFrame(degrees_2021)
cip_codes = pd.DataFrame(cipcode)
institutions = pd.DataFrame(ins_data)

#Renaming Columns for merge
cip_codes = cip_codes.rename(columns = {'CIPCD':'CIPCODE'})
institutions = institutions.rename(columns={'unitid':'UNITID'})

#Merging the DataFrames
educip = pd.merge(education,cip_codes,how= "outer", on = "CIPCODE")
merged = pd.merge(educip,institutions, how='outer',on="UNITID")
merged.to_csv('merged.csv',index=False)
unitid_view = merged[['UNITID','instnm']].drop_duplicates()
unitid_view.to_csv('inst_nm.csv',index=False)

#get variable list for future reference
var_list = merged.columns.tolist()
var_len = len(var_list))
df_var_names = pd.DataFrame(index = range(10),columns=range(15))
for i in range(min(var_list,var_len, 10)):
    for j in range(min(var_list,var_len,15)):
         df_var_names.at[i, j] = var_list[i * 15 + j] if i * 15 + j < var_len else None

#Analysis Begins ;-D

    #Analysis 1
ivy = merged
ivy_league = ["Brown University",
                      "Columbia University",
                      "Cornell University",
                      "Dartmouth University",
                      "Harvard University",
                      "University of Pennsylvania",
                      "Princeton University",
                      "Yale University"]
ivy = ivy[ivy['instnm'].isin(ivy_league)].reset_index()
ivy