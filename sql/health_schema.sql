-- ===========================================
-- patients syntetic data 
-- TINYINT holds small whole numbers (0 to 255 when unsigned), so it suits ages and 0/1 flags
-- SMALLINT is larger, which suits values up to a few hundred such as blood pressure
-- ==========================================
--(NO AUTO_INCREMENT, because we supply the ID)

CREATE TABLE patients(
    patient_id INT PRIMARY KEY, 
    age TINYINT NOT NULL,
    gender ENUM('Female', 'Male') NOT NULL,
    weight SMALLINT NOT NULL,
    height SMALLINT NOT NULL,
    bmi_reported	DECIMAL(4,1) NOT NULL,
    smoking ENUM('Never', 'Former', 'Current') NOT NULL,
    alcohol_intake ENUM('None', 'Low', 'Moderate', 'High') NOT NULL,
    physical_activity ENUM('Sedentary', 'Moderate', 'Active') NOT NULL,
    diet ENUM('Unhealthy', 'Average', 'Healthy') NOT NULL,
    stress_level ENUM('Low', 'Medium', 'High')	NOT NULL,
    hypertension TINYINT NOT NULL,
    diabetes TINYINT NOT NULL,
    hyperlipidemia TINYINT NOT NULL,
    family_history TINYINT NOT NULL,
    previous_heart_attack TINYINT NOT NULL,
    systolic_bp SMALLINT NOT NULL,
    diastolic_bp SMALLINT NOT NULL,
    heart_rate SMALLINT NOT NULL,
    blood_sugar_fasting SMALLINT NOT NULL,
    cholesterol_total SMALLINT NOT NULL,
    heart_disease TINYINT NOT NULL,
    bmi_calculated DECIMAL(4,1) NOT NULL,
    bp_inconsistent TINYINT NOT NULL
);