# 🏥 Hospital Data Cleaning Project

A complete data cleaning project for hospital datasets using Python and Pandas.

This project focuses on cleaning and preparing raw hospital data for analysis and reporting by handling common real-world data quality issues.

---

# 📌 Project Overview

The datasets contained several data quality problems such as:

* Missing Values
* Duplicate Records
* Invalid Date Values
* Inconsistent Data

The project applies different data cleaning techniques to prepare the datasets for further analysis.

---

# 📂 Datasets

The project includes:

## Raw Datasets

* `hospital_patients_raw.csv`
* `hospital_appointments_raw.csv`

## Cleaned Datasets

* `hospital_patients_cleaned.csv`
* `hospital_appointments_cleaned.csv`

---

# ⚙️ Cleaning Operations

## ✅ Handling Missing Values

Filled missing values using:

* Median values for numerical columns
* Default values for categorical columns

## ✅ Removing Duplicates

Removed duplicated rows to improve data quality.

## ✅ Date Validation

Corrected invalid discharge dates where:

`Discharge_Date < Admission_Date`

## ✅ Data Standardization

Standardized inconsistent and incomplete values.

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* CSV Files

---

# 🚀 How to Run

## 1️⃣ Install Required Libraries

```bash
pip install pandas numpy
```

## 2️⃣ Run the Cleaning Script

```bash
python hospital_data_cleaning.py
```

---

# 📊 Project Goal

The main goal of this project is to:

* Practice Data Cleaning techniques
* Prepare datasets for analysis
* Improve data quality
* Simulate real-world healthcare datasets

---

# 👨‍💻 Author

**Tharwat Farag**

GitHub: [https://github.com/tharwat-farag](https://github.com/tharwat-farag)

---

#Digilians 🚀
