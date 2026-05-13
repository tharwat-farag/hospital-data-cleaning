# Hospital Dataset Cleaning Script (Python)

import pandas as pd

# =============================
# Load Raw Datasets
# =============================
patients_df = pd.read_csv("hospital_patients_raw.csv")
appointments_df = pd.read_csv("hospital_appointments_raw.csv")

# =====================================================
# Cleaning Patients Dataset
# =====================================================

# Remove duplicate rows
patients_cleaned = patients_df.drop_duplicates()

# Handle missing values
patients_cleaned["Age"] = patients_cleaned["Age"].fillna(
    patients_cleaned["Age"].median()
)

patients_cleaned["Gender"] = patients_cleaned["Gender"].fillna("Unknown")

patients_cleaned["Diagnosis"] = patients_cleaned["Diagnosis"].fillna("General Checkup")

patients_cleaned["Bill_Amount"] = patients_cleaned["Bill_Amount"].fillna(
    patients_cleaned["Bill_Amount"].median()
)

patients_cleaned["Room_Number"] = patients_cleaned["Room_Number"].fillna(-1)

# Convert dates to datetime format
patients_cleaned["Admission_Date"] = pd.to_datetime(patients_cleaned["Admission_Date"])

patients_cleaned["Discharge_Date"] = pd.to_datetime(patients_cleaned["Discharge_Date"])

# Fix invalid discharge dates
mask = patients_cleaned["Discharge_Date"] < patients_cleaned["Admission_Date"]

patients_cleaned.loc[mask, "Discharge_Date"] = patients_cleaned.loc[
    mask, "Admission_Date"
]

# Save cleaned patients dataset
patients_cleaned.to_csv("hospital_patients_cleaned.csv", index=False)

# =====================================================
# Cleaning Appointments Dataset
# =====================================================

# Remove duplicate rows
appointments_cleaned = appointments_df.drop_duplicates()

# Handle missing values
appointments_cleaned["Department"] = appointments_cleaned["Department"].fillna(
    "General"
)

appointments_cleaned["Status"] = appointments_cleaned["Status"].fillna("Pending")

appointments_cleaned["Waiting_Time_Minutes"] = appointments_cleaned[
    "Waiting_Time_Minutes"
].fillna(appointments_cleaned["Waiting_Time_Minutes"].median())

appointments_cleaned["Consultation_Fee"] = appointments_cleaned[
    "Consultation_Fee"
].fillna(appointments_cleaned["Consultation_Fee"].median())

appointments_cleaned["Insurance"] = appointments_cleaned["Insurance"].fillna("Unknown")

# Convert date column
appointments_cleaned["Appointment_Date"] = pd.to_datetime(
    appointments_cleaned["Appointment_Date"]
)

# Save cleaned appointments dataset
appointments_cleaned.to_csv("hospital_appointments_cleaned.csv", index=False)

print("Data Cleaning Completed Successfully")
