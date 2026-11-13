import pandas as pd

df = pd.read_csv("data/synthetic_heart_disease_dataset_model.csv", keep_default_na=False)

df.columns = df.columns.str.lower()
df.insert(0, "patient_id", range(1, len(df) +1)) # make them lower case becaus we will this in sql

bp_problems = df["diastolic_bp"] >= df["systolic_bp"] # check the differences in real life measurment where systolic should be higher 
print("Rows where diastolic >= systolic:", bp_problems.sum())

bmi_cal = (df["weight"] / (df["height"] / 100) ** 2).round(1)  # actual BMI measurement weight(kg)/height(m)
bmi_gaps = (df["bmi"] - bmi_cal).abs()
print("Rows where BMI differs by more that one:", (bmi_gaps > 1).sum())

df = df.rename(columns={"bmi": "bmi_reported"}) # rename it as reported
df["bmi_calculated"] = bmi_cal                     # numbers that follow from weight and height
df["bp_inconsistent"] = bp_problems.astype(int)   #
print(df["bp_inconsistent"].sum())                 


df.to_csv("data/health_clean.csv", index=False)
print(df.head())
print(df.dtypes)