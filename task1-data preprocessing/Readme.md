##🧠 Data Preprocessing Challenge

This project demonstrates data preprocessing using Apache Spark (PySpark).
It handles missing values, duplicates, data type inconsistencies, normalization, and feature engineering.

**🚀 Features**
🧩 Handle missing values (numeric + categorical)
🔢 Fix inconsistent data types
🧹 Remove duplicates
⚖️ Normalize/Standardize numerical features
🧠 Create engineered features

**🧰 Tools & Technologies**
Apache Spark (PySpark)
Python 3.8+
Parquet (for optimized output)

****📦 Setup Instructions**
1️⃣ Clone Repository
cd data-preprocessing-challenge

2️⃣ Create Virtual Environment python -m venv venv venv\Scripts\activate # Windows

3️⃣ Install Dependencies pip install -r requirements.txt

4️⃣ Run the Preprocessing Script Make sure your raw data is inside the data/ folder.

cd src python preprocess.py
data/processed_dataset.parquet

📂 Input/Output Type Format Path Input CSV data/raw_dataset.csv Output Parquet data/processed_dataset.parquet

⚙️ Example Operations Task Description Missing values Numeric → Mean fill, Categorical → “Unknown” Data types Convert string-numeric to DoubleType Duplicates Drop identical rows Normalization StandardScaler (zero mean, unit variance) Feature Engineering e.g., total_amount = price × quantity

🏁 Output Example price quantity total_amount scaled_features 100.0 3 300.0 [0.12, -0.43, ...]
output : <img width="1916" height="896" alt="image" src="https://github.com/user-attachments/assets/28bc689a-e66c-4a37-b633-6d21ef1fcf2a" />
<img width="1865" height="935" alt="image" src="https://github.com/user-attachments/assets/a2c151ec-3bc7-4e93-9306-aa5e0bf6ce92" />
<img width="1877" height="1033" alt="image" src="https://github.com/user-attachments/assets/88408821-03ff-49d1-8f48-6607e1041ccc" />
<img width="1717" height="773" alt="image" src="https://github.com/user-attachments/assets/9a2ffe6a-4a84-48e6-85af-678fafda23a5" />



