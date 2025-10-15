# 🧠 Data Preprocessing Challenge 

This project demonstrates **data preprocessing** using **Apache Spark (PySpark)**.  
It handles missing values, duplicates, data type inconsistencies, normalization, and feature engineering.


## 🚀 Features
- 🧩 Handle missing values (numeric + categorical)
- 🔢 Fix inconsistent data types
- 🧹 Remove duplicates
- ⚖️ Normalize/Standardize numerical features
- 🧠 Create engineered features


## 🧰 Tools & Technologies
- **Apache Spark (PySpark)**
- **Python 3.8+**
- **Parquet** (for optimized output)


## 📦 Setup Instructions

### 1️⃣ Clone Repository

cd data-preprocessing-challenge

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Preprocessing Script
Make sure your raw data is inside the data/ folder.

cd src
python preprocess.py

data/processed_dataset.parquet

📂 Input/Output
Type	Format	Path
Input	CSV	data/raw_dataset.csv
Output	Parquet	data/processed_dataset.parquet

⚙️ Example Operations
Task	Description
Missing values	Numeric → Mean fill, Categorical → “Unknown”
Data types	Convert string-numeric to DoubleType
Duplicates	Drop identical rows
Normalization	StandardScaler (zero mean, unit variance)
Feature Engineering	e.g., total_amount = price × quantity

🏁 Output Example
price	quantity	total_amount	scaled_features
100.0	3	300.0	[0.12, -0.43, ...]
**output :**
<img width="1888" height="833" alt="image" src="https://github.com/user-attachments/assets/f3a80307-99e2-4db1-aec4-b3dc79759b59" />
<img width="1663" height="864" alt="image" src="https://github.com/user-attachments/assets/94c8424c-55fa-4f39-9f62-f6f3fad6996c" />
<img width="1882" height="896" alt="image" src="https://github.com/user-attachments/assets/4eb6ca92-cde5-45c2-92e6-2800aa57d5f1" />
<img width="1375" height="647" alt="image" src="https://github.com/user-attachments/assets/111015cb-49c4-4037-8528-b2ab917c20cf" />




