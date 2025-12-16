# 🛵 Food Delivery Performance Analysis

## 📌 Overview

This project involves an Exploratory Data Analysis (EDA) of a food delivery dataset. The primary goal is to analyze the operational efficiency of delivery agents, understand order distributions across different timeframes, and visualize workforce workload patterns.

## 🎯 Objectives

  * **Data Cleaning:** Handling format inconsistencies in date columns (`Order_Date`) and removing hidden whitespace in column headers.
  * **Performance Metrics:** Calculating the average number of orders handled by delivery agents per day.
  * **Visualization:** Plotting the distribution of agent workloads to identify staffing imbalances or high-performing agents.

## 🛠️ Tech Stack

  * **Language:** Python
  * **Libraries:**
      * `pandas` (Data Manipulation & Aggregation)
      * `matplotlib` (Data Visualization)
      * `numpy` (Numerical computations)
  * **Environment:** Google Colab / Jupyter Notebook

## 📊 Key Insights & Visualizations

  * **Workload Distribution:** A histogram analysis showing the frequency of average daily orders per agent.
  * **Time Series Analysis:** (Planned) Analyzing how order volume fluctuates over weekends vs. weekdays.

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/delivery-analysis.git
    ```
2.  **Install dependencies:**
    ```bash
    pip install pandas matplotlib
    ```
3.  **Run the analysis:**
    Open the notebook `Analysis.ipynb` in Jupyter or Google Colab and execute the cells.

## 📂 Dataset

The dataset includes the following key features:

  * `Delivery_person_ID`: Unique identifier for the rider.
  * `Order_Date`: Date of the transaction.
  * *(Add other columns here, e.g., Time\_Orderd, City, etc.)*

## 📝 Code Snippet

*Example of aggregating agent performance:*

```python
# Convert date column and calculate mean orders per agent
train_df["Order_Date"] = pd.to_datetime(train_df["Order_Date"], format="%d-%m-%Y")

orders_per_agent_day = (train_df.groupby(["Delivery_person_ID", "Order_Date"])
                       .size().groupby("Delivery_person_ID").mean())

-----

### 💡 Tips for your GitHub:

1.  **Screenshots:** Since you generated a Histogram in your code, save that image and upload it to your repo, then link it in the "Key Insights" section. Visuals make READMEs much better.
2.  **File Name:** Make sure this file is named exactly `README.md` (all caps for README, lowercase for .md).
