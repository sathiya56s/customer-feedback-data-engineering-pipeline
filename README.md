Customer Feedback Analytics Pipeline

This project is a mini analytics workflow demonstrating how to clean, merge, analyze, and visualize customer feedback data. It simulates a real-world data engineering + decision science pipeline using Python, CSV datasets, and a simple visualization dashboard.

 Project Overview
This project performs:

- Collection of multi-channel feedback (survey, chat, NPS)
- Standardized data cleaning and formatting
- Data merging using customer identifiers
- Exploratory analysis on ratings and NPS
- Visualization using charts and dashboards
- End-to-end structure aligned with analytics project standards

Project Structure

customer-feedback-data-engineering-pipeline/
│
├── data/
│ ├── survey_data.csv
│ ├── chat_feedback.csv
│ └── nps_scores.csv
│
├── scripts/
│ └── data_cleaning.py
│
├── notebooks/
│ └── analysis.ipynb
│
├── images/
│ └── dashboard.png
│
└── README.md


 How to Run

Install required packages:

pip install pandas matplotlib

Run the cleaning script:

python scripts/data_cleaning.py

Open the notebook:

1. Go to notebooks/analysis.ipynb
2. Run all cells to see merged tables and charts

 Dashboard Preview

A simple dashboard showing key customer feedback insights:

![Dashboard](images/dashboard.png)

 Tech Stack

- Python  
- Pandas  
- Matplotlib  
- CSV datasets  
- Jupyter Notebook  

 Insights You Can Derive

- Low ratings strongly correlate with long waiting times  
- Positive sentiment appears when resolutions are quick  
- NPS score distribution reflects both promoters and detractors  
- Chat sentiment trends match survey pain points  


Author

Project created bySathiya S 






