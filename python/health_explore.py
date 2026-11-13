import pandas as pd 

pd.set_option('display.max_columns', None)

df = pd.read_csv('data/synthetic_heart_disease_dataset_model.csv')

print()
print("Rows and columnes:", df.shape) 
print()
print(df.head())
print()
df.info()

# check for missing values in the dataset.
print()
print("Missing values per column:") # counts empty values in each column. 
print(df.isna().sum())
print()

print("Duplicate rows:", df.duplicated().sum()) # check for duplicate rows in the dataset.
print()


print("Alcohol_Intake counts:") # ounts how often each value occurs, including the empty ones.
print(df['Alcohol_Intake'].value_counts(dropna=False))
print()

print(df.describe())

# returns NAN as None(it shows the personis not alcohol drinker)

print()
print("--reload with keep_default_na=False--")
df_raw = pd.read_csv("data/synthetic_heart_disease_dataset_model.csv", keep_default_na=False)
print(df_raw["Alcohol_Intake"].value_counts(dropna=False))

for col in ["Gender", "Smoking", "Physical_Activity", "Diet", "Stress_Level"]: 
    print()
    print(df_raw[col].value_counts())
