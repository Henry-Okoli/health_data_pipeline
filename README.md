# Health Data Pipeline

   A Python and SQL project that loads a 50,000 synthetic heart disease dataset, checks it for problems, cleans it and stores it in a MariaDB database.

   The data is synthetic, so no real patients are involved and no health conclusions should be drawn from it.

## What it does

1. Reads the raw CSV file
2. Checks the data against real-world rules (blood pressure and BMI)
3. Saves a cleaned CSV with two new columns that flag problems
4. Loads the cleaned data into a MariaDB table called `patients`

## Data

The data is a synthetic heart disease dataset from Kaggle, called "Heart Disease Prediction Dataset" (https://www.kaggle.com/datasets/miadul/heat-disease-predication-dataset/data). It was chosen maily for the need to work with health data. Synthetic means the records are enerated, so no real patients are involved.

The dataset has 50,000 rows. I used a selected set of columns from it, including age, gender, weight, height, BMI, blood pressure and heart disease. The raw CSV is not stored in this repository. To run the project, download it from the link above and place it in the `data/` folder.

## Project structure
```
health_data_pipeline/
├── README.md              this file
├── requirements.txt       the Python packages needed
├── .gitignore             files Git must not track (secrets, data)
├── data/                  raw and cleaned CSV files (not in Git)
├── docs/                  extra documentation
├── python/
│   ├── health_explore.py      look at the raw data
│   ├── health_clean.py        check, flag and save the cleaned CSV
│   └── load_health_data.py    load the cleaned CSV into MariaDB
└── sql/
    └── health_schema.sql      creates the patients table
```

## Data quality checks

I compared the data against two real-world rules.

| Check | Rule | Rows affected |
|---|---|---|
| Blood pressure | Systolic pressure should be higher than diastolic pressure | 2,235 |
| BMI | BMI equals weight in kg divided by height in metres squared | 46,225 |

**What I did about it**

- Blood pressure: I added a column `bp_inconsistent` (1 means the row breaks the rule, 0 means it does not). I did not delete the rows.
- BMI: I kept the original value as `bmi_reported` and added `bmi_calculated`. A row counts as a mismatch when the two differ by more than 1.

I flagged these rows instead of deleting them, so the original data stays intact and anyone using it can decide how to treat the flagged rows.

   ## Author

   Okoli Henry Onyeka