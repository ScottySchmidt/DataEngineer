## Overview
This project automates an ETL pipeline using Airflow (Astro) and AWS services.
- Source: GitHub repo via AWS CodePipeline
- Storage: S3 (`scott-data-redshift-test`)
- Transformation: AWS Glue
- Warehouse: Amazon Redshift
- Orchestration: Astro (Airflow Cloud)

## Workflow
1. Push to GitHub triggers CodePipeline → deploys files into S3.
2. S3 event triggers AWS Glue → transforms CSV to Parquet.
3. Redshift COPY command loads data for analytics.

## Tools
- Python
- Apache Airflow (Astro)
- AWS (S3, Glue, Redshift, CodePipeline)
