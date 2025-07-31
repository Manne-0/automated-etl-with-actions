# Simple Automation Using GitHub Actions

A simple demo showing how to automate data extraction from an API, transform it using Python, and load it into a MySQL database — all orchestrated with GitHub Actions.

---

## 🧩 Business Problem

A new request came from the sales department requiring a table to house specific logic and receive daily updates. Given the company’s current process, manually downloading data from the app, transforming it using Python, and uploading it into the database — this was not scalable and would add to an already heavy workload.

---

## ✅ The Solution

Automate the workflow using:

- **API access** to replace manual downloads
- **Python script** to handle transformation and database loading
- **GitHub Actions** to run the pipeline daily without manual effort

---

## ⚙️ Steps Taken

### 1. API Integration  
Requested access to the API endpoints for the required dataset. This step was key — APIs make automation possible.

### 2. Python Script  
Wrote a Python script that:

- Pulls JSON data from the API
- Flattens and cleans the data
- Transforms it (e.g., creates new columns or filters rows)
- Loads the final table into a MySQL database

### 3. GitHub Automation  
Created a GitHub repository and added:

- The Python script
- A `requirements.txt` file to specify dependencies
- A `.github/workflows/main.yml` file containing the GitHub Actions workflow

---

## 🤖 Automation with GitHub Actions

GitHub Actions allows automation directly from your repo. With a workflow file, you can run your Python script on a schedule (e.g., daily at midnight).

### Basic GitHub Actions Workflow

```yaml
name: Run ETL Script

on:
  schedule:
    - cron: '0 0 * * *'  # every day at 00:00 UTC
  workflow_dispatch:      # allows manual trigger

jobs:
  etl-job:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repo
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run ETL script
      run: python etl.py
