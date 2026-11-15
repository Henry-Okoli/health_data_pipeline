# Data dictionary

Table: `patients` (50,000 rows, 24 columns). All data is synthetic.

| Column | Type | Meaning | Values or unit |
|---|---|---|---|
| patient_id | integer | Row number I added as the primary key | 1 to 50000 |
| age | integer | Age of the patient | years |
| gender | text | Gender | Female, Male |
| weight | integer | Body weight | kg (assumed) |
| height | integer | Height | cm (assumed) |
| bmi_reported | decimal | BMI as given in the original data | kg/m² |
| smoking | text | Smoking status | Never, Former, Current |
| alcohol_intake | text | How much alcohol the patient drinks | None, Low, Moderate, High |
| physical_activity | text | How active the patient is | Sedentary, Moderate, Active |
| diet | text | Quality of diet | Unhealthy, Average, Healthy |
| stress_level | text | Reported stress | Low, Medium, High |
| hypertension | integer | Has high blood pressure | 0 = no, 1 = yes |
| diabetes | integer | Has diabetes | 0 = no, 1 = yes |
| hyperlipidemia | integer | Has high blood fats (cholesterol or triglycerides) | 0 = no, 1 = yes |
| family_history | integer | A close relative has had heart disease | 0 = no, 1 = yes |
| previous_heart_attack | integer | Patient has had a heart attack before | 0 = no, 1 = yes |
| systolic_bp | integer | Blood pressure when the heart beats (upper number) | mmHg (assumed) |
| diastolic_bp | integer | Blood pressure between beats (lower number) | mmHg (assumed) |
| heart_rate | integer | Resting heartbeats per minute | beats per minute (assumed) |
| blood_sugar_fasting | integer | Blood sugar after fasting | mg/dL (assumed) |
| cholesterol_total | integer | Total cholesterol in the blood | mg/dL (assumed) |
| heart_disease | integer | The outcome: whether the patient has heart disease | 0 = no, 1 = yes |
| bmi_calculated | decimal | BMI I calculated from weight and height | kg/m², 1 decimal place |
| bp_inconsistent | integer | Data quality flag I added: diastolic is not lower than systolic | 0 = ok, 1 = problem |