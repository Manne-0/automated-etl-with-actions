# Simple Automation Using GitHub Actions

A simple demo showing how to automate data extraction from an API, transform it using Python, and load it into a MySQL database, all orchestrated with GitHub Actions.

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
I requested access to the necessary API endpoints. This was crucial, it allowed me to bypass the GUI and download data programmatically.

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

There are many ways to schedule and automate Python scripts (cron jobs, Airflow, etc.), but for simplicity and availablity, I used GitHub Actions.

GitHub Actions is a built-in CI/CD tool that allows you to automate workflows directly from your repository. It can run your Python script on a schedule, install dependencies, and execute your code, without needing a separate cloud server.

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
```
---
## ⚠️ Possible Issues

- **Secrets:** Make sure to store API keys, DB credentials, etc., securely in GitHub Actions Secrets.
- **Rate Limits:** Watch out for API rate limits if triggering frequently.
- **Logging & Monitoring:** Consider adding logging or error notifications (e.g., email, Slack) for long-term use.

---
## 🚀 Result

This automation now runs daily without manual intervention. It ensures the Sales team always has fresh data in their reporting table, saving hours of manual work each week.

---
## 📎 Summary

This automation now runs daily without manual intervention. It ensures the Sales team always has fresh data in their reporting table—saving hours of manual work each week.

This project shows how automation can drastically reduce manual workflows. Using GitHub Actions to schedule Python scripts makes it easy to maintain, scalable, and hands-free.
