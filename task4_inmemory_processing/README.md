**In-Memory Data Processing**
**Overview**

This task demonstrates in-memory data processing using Apache Spark. The goal is to process large datasets efficiently by leveraging Resilient Distributed Datasets (RDDs) and DataFrames to optimize processing time and perform real-time analytics.
Tools Used

**Apache Spark**

Python (PySpark)

In-memory data structures: RDDs and DataFrames
Files in this Task

**File	Description**
inmemory_rdd.py	Demonstrates processing a dataset using Spark RDDs, applying transformations and actions.
inmemory_dataframe.py	Demonstrates processing a dataset using Spark DataFrames, including column operations and analytics.
requirements.txt	Python dependencies required to run this task in the virtual environment.
Instructions to Run

****Activate your Python virtual environment**
source streaming_env/bin/activate

**Run the RDD :**
python3 inmemory_rdd.py

**Run the DataFrame:**
python3 inmemory_dataframe.py

**Expected Output**

RDD processing: Displays transformed RDD data.
DataFrame processing: Displays DataFrame with transformed columns and computed values.

**Key Concepts Demonstrated**
Efficient in-memory processing with Spark.
Transformations and actions on RDDs.
DataFrame operations and analytics.
Performance improvement through in-memory computation
