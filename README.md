# Assignment 01


[CodeLab Documentation](https://codelabs-preview.appspot.com/?file_id=1n8mE3_f0qTe8m5An2pvlBcXlbylzqpmeve8I6kLEqpc/#0)

[Marketing Dashboard](https://app.snowflake.com/qefqbdp/ryb09972/#/final-dashboard-dUwVOcGJT)

[TPC-DS Dataset](https://www.tpc.org/tpc_documents_current_versions/pdf/tpc-ds_v2.5.0.pdf)

[Github Repository](https://github.com/AlgoDM-Fall2023-Team4/Assignment01.git)

**Overview**

This assignment helps us in understanding how companies leverage or improve marketing strategies while serving their stakeholders. In the first part of the assignment, we evaluate a company and find the products they are selling, how they are selling, pricing techniques, marketing and campaigning strategies, how they can stand different from their counterparts in the market.

We are also using [TPC-DS Dataset](https://www.tpc.org/tpc_documents_current_versions/pdf/tpc-ds_v2.5.0.pdf) to figure out what different types of business questions need to be served in order to implement solutions for the company. We are also reviewing the SQL queries, the business value they have and how the result data can be used to gain insights .
Designing a dashboard for the same can be helpful to analytics teams and business decision-makers.

After getting a detailed understanding of the business questions from the [TPC-DS Dataset](https://www.tpc.org/tpc_documents_current_versions/pdf/tpc-ds_v2.5.0.pdf), we are building a [Streamlit](https://streamlit.io/) application to connect to [Snowflake](https://www.snowflake.com/en/) and fetch the respective SQL queries for the business questions that need to be answered.
Streamlit can then be used to edit any parameters in the query and get results accordingly. Analyzing these results can be useful to improve strategies of different departments(promotions, marketing, recommendations etc.) of the company.

## Use Case Diagram
![img.png](https://github.com/AlgoDM-Fall2023-Team4/Assignment01/blob/pranitha_dev/Assets/Use_Case_diagram.png)

## Project Structure
```
  ├── Assets            
  │   ├── Use_Case_diagram.png
  │   ├── Total Sales of Electronics.png
  │   ├── Inventory Analysis_ COV vs. Mean.png
  │   ├── Increment of Web & Store Sales Quaterly in each County  (1).png
  │   ├── Gross Margin vs. Rank Category Distribution.png
  │── requirements.txt                  # relevant package requirements file for main
  └──  streamlit
      ├── validate.py                      # application code for the application
      └── sql.json                         # to store the data related to queries
```
