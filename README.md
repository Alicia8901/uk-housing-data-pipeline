# UK Housing Data Pipeline #

## Overview ##

This project demonstrates an end-to-end cloud data engineering and analytics pipeline using UK housing transaction data from 2015 to 2024.

The pipeline ingests raw housing data, performs cleaning and transformation using PySpark in Databricks, stores processed data in Google BigQuery, and prepares the data for business intelligence reporting in Power BI.

## Architecture ##

![Architecture Diagram](architecture_diagram.png)

## Dataset ##

The dataset contains approximately 90,000 UK housing transactions and includes:

* Property prices
* Transaction dates
* Postcodes
* Property types
* New build indicators
* Freehold/leasehold information
* Towns and districts

## Technologies Used ##

* Python
* PySpark
* Databricks
* SQL
* Google BigQuery
* Google Cloud Storage
* Power BI

## Project Structure ##

| Path | Description |
|------|-------------|
| `data/raw/uk_house_prices.csv` | Original UK housing dataset downloaded from Kaggle |
| `data/processed/housing_processed.csv` | Cleaned and transformed dataset exported from BigQuery |
| `databricks_notebooks/01_data_ingestion.py` | Loads and validates the raw dataset in Databricks |
| `databricks_notebooks/02_data_cleaning.py` | Performs duplicate removal and data quality checks |
| `databricks_notebooks/03_data_transformation.py` | Creates new features and performs PySpark transformations |
| `sql/housing_analysis.sql` | BigQuery SQL queries used for analytics and reporting |
| `dashboards_powerBI/` | Power BI dashboard screenshots and visualisations |
| `databricks_screenshots/` | Screenshots demonstrating the Databricks workflow |
| `bigquery_screenshots/` | Screenshots demonstrating BigQuery analysis |
| `architecture_diagram.png` | End-to-end pipeline architecture diagram |
| `project_summary.md` | Detailed technical project summary |
| `README.md` | Project documentation and overview |
| `requirements.txt` | Python dependencies used in the project |
| `.gitignore` | Files and folders excluded from version control |

## Data Engineering Workflow ##

### 1. Data Ingestion ###

The raw dataset was loaded into Databricks using PySpark.

Key activities:

* Schema validation
* Data preview
* Row count verification

### 2. Data Cleaning ###

Data quality checks included:

* Duplicate detection
* Duplicate removal
* Missing value analysis

The dataset was reduced from 90,000 records to 89,957 records after duplicate removal.

### 3. Data Transformation ###

Transformations performed using PySpark:

* Created sale_year
* Created sale_month
* Average price by district
* Average price by property type
* New build analysis
* Freehold vs leasehold analysis
* Yearly transaction analysis

### 4. BigQuery Analytics ###

Processed data was loaded into BigQuery for analytical querying.

Example analyses:

* Average house price by year
* Transactions by year
* Average price by property type
* Top districts by average house price
* New build vs existing properties
* Freehold vs leasehold properties

SQL queries can be found in:

`sql/housing_analysis.sql`

### 5. Power BI Dashboard ###

The processed dataset is used to create an interactive dashboard displaying:

* Housing price trends
* Transaction volumes
* District-level insights
* Property type analysis
* Key performance indicators (KPIs)

## Screenshots ##

### Databricks ###

Screenshots demonstrating data ingestion, cleaning and transformation can be found in:

`databricks_screenshots/`

### BigQuery ###

Screenshots demonstrating BigQuery analytics can be found in:

`bigquery_screenshots/`

### Power BI ###

Dashboard screenshots can be found in:

`dashboards_powerBI/`

## Key Outcomes ##

* Built an end-to-end cloud data pipeline
* Processed and analysed UK housing transaction data
* Applied data cleaning and transformation using PySpark
* Performed cloud-based analytics using BigQuery
* Exported processed data for reporting
* Prepared data for business intelligence visualisation using Power BI
* Demonstrated modern data engineering workflows and cloud technologies

## Future Improvements ##

* Automate the pipeline using Apache Airflow for scheduled data ingestion and processing. 
* Implement data quality validation checks using Great Expectations. 
* Store transformed data in Parquet format to improve storage efficiency and query performance. 
* Enhance the Power BI dashboard with additional filters and interactive visualisations. 
* Develop a machine learning model to predict future UK house prices.