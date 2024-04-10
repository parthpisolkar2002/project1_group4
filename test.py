'''import os
import pandas as pd

housing = os.path.join("..","Housing Data.xlsb.csv")
housing_data = pd.read_csv(housing)
housing_data.head()'''
import pandas as pd
import os
from pathlib import Path

# Construct the file path
twenty_one = "/Users/parthpisolkar/Desktop/Bootcamp Materials/Project 1/project1_group4/c2021_a.csv"
twenty = ""
# Read the CSV file into a pandas DataFrame
degrees_2021 = pd.read_csv(housing)

# Display the first few rows of the DataFrame
num_rows, num_columns = degrees_2021.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")
degrees_2021.head(10)

Institution = "/Users/parthpisolkar/Desktop/Research Fellowship/2022-2023/LinkedIn Data/Data/InstitutionFile.dta"
ins_data = pd.read_stata(Institution)
print(ins_data.head())