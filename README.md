# AlphaCare-Insurance-Solutions-(ACIS)-Insurance-Claim-Data Analysis Project

This project involves a comprehensive analysis of insurance claim data using Data Version Control (DVC) and Exploratory Data Analysis (EDA) techniques.

---

## **Directory Structure**

```
project/
│
├── notebooks/                   # Jupyter Notebooks for tasks
│   ├── task1_user_overview.ipynb    # Task 1: User Overview Analysis
│   ├── task2_user_engagement.ipynb  # Task 2: User Engagement Analysis
│
├── scripts/                         # Modular scripts
│   ├── __init__.py
│   ├── database.py                  # Database connection and querying
│   ├── user_overview.py             # Functions for Task 1
│   ├── user_engagement.py           # Functions for Task 2
│   ├── analysis.py                  # Univariate and Bivariate analysis
│   └── utils.py                     # Helper functions (e.g., saving data)
│
├── data/                        # Intermediate data files
│
├── requirements.txt             # Required Python libraries
├── .env                         # Environment variables for database credentials
└── README.md                    # Project documentation
```

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone <https://github.com/gtnt-sileshi/AlphaCare-Insurance-Solutions--ACIS--Insurance-Claim-Data-Analysis>
cd <AlphaCare-Insurance-Solutions--ACIS--Insurance-Claim-Data-Analysis>
```

### **2. Install Required Libraries**

Use the `requirements.txt` file to install the necessary Python libraries.

```bash
pip install -r requirements.txt
```

````

### **3. Run Jupyter Notebooks**

Start Jupyter Notebook and open the respective tasks:

```bash
jupyter notebook
````

---

## **Usage**

Overview
This project aims to analyze insurance data to derive insights and perform data management using DVC. The analysis includes data loading, basic statistics, and visualizations.

Technologies Used
Python
Pandas
Matplotlib
DVC (Data Version Control)
Data Preparation
The dataset MachineLearningRating_v3.txt is loaded.
Non-numeric columns are identified and excluded for numerical operations.
The TransactionMonth column is converted to datetime format.
DVC Implementation
Remote storage was initialized for data management.
The dataset was tracked and pushed to remote storage.
Exploratory Data Analysis
Basic statistics were performed on the dataset.
Histograms, correlation matrices, and boxplots were created to visualize data distributions and relationships.
Visualizations
Histograms for TotalPremium.
Correlation matrices to show relationships between variables.
Boxplots for TotalPremium by Province.
Conclusion
The project successfully demonstrates how to manage and analyze insurance data using DVC and EDA techniques, providing valuable insights into the dataset.

## **Contributing**

If you wish to contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Submit a pull request.

---

## **License**

This project is licensed under the MIT License.
