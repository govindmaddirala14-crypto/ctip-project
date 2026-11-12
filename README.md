
# AWS Cost Analyzer

## Project Overview
AWS Cost Analyzer is a Python-based command-line tool that retrieves AWS billing information using the AWS Cost Explorer API.

It displays the cost of individual AWS services and calculates the total AWS cost.

## Features
- Fetches AWS billing data using Boto3.
- Groups costs by AWS service.
- Calculates total AWS cost.
- Displays a cost summary in the terminal.
- Generates a CSV report named `cost_report.csv`.

## Technologies Used
- Python
- AWS Cost Explorer
- AWS SDK for Python (Boto3)
- CSV

## Prerequisites
- An AWS account.
- AWS CloudShell or Python environment.
- Boto3 installed.
- AWS credentials with permission to access Cost Explorer.

## Installation

Install Boto3:

```bash
pip3 install boto3
```

## Run the Project

```bash
python3 main.py
```

The program displays the AWS cost summary and generates `cost_report.csv`.

## Output
The CSV report contains:
- AWS Service
- Cost (USD)
- Total AWS Cost

## Author
Advaith Sai

