# Expense Tracker Frontend

## Overview

This is the frontend application for the Expense Tracker project built using Streamlit.

The frontend communicates with FastAPI backend APIs using HTTP requests and displays data in a simple user-friendly interface.

Users can:

- Add expenses
- View expenses
- Update expenses
- Delete expenses
- Search expenses
- Sort expenses

The frontend is deployed using Streamlit Cloud.

---

# Frontend Repository

https://github.com/bhargaviraniganta/expense_tracker_fe/

---

# Tech Stack

- Python
- Streamlit
- Pandas
- Requests Library

---

# Project Structure

```bash
expense_tracker_fe/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/bhargaviraniganta/expense_tracker_fe.git
```

## Navigate to Project Folder

```bash
cd expense_tracker_fe
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
streamlit run app.py
```

Application runs on:

```text
http://localhost:8501
```

---

# Backend Connection

The frontend communicates with the FastAPI backend deployed on Render.

Example:

```python
BASE_URL="https://expense-tracker-be-1n3i.onrender.com"
```

---

# Features

## Add Expense

Users can:

- Enter expense title
- Enter amount
- Select category

The frontend sends a POST request to backend API.

---

## View Expenses

Displays all expenses in table format using Pandas DataFrame.

Example:

```python
df=pd.DataFrame(data)

st.dataframe(df)
```

---

## Update Expense

Users can update:

- Title
- Amount
- Category

Uses PUT API request.

---

## Delete Expense

Delete expenses using Expense ID.

Uses DELETE API request.

---

## Search Expense

Filter expenses by category.

Example:

```python
/search?category=Food
```

---

## Sort Expenses

Sort expenses using:

- Latest Date
- Oldest Date
- Highest Amount
- Lowest Amount

---

# API Communication

Frontend communicates with backend using Requests Library.

Example:

```python
response=requests.get(
    f"{BASE_URL}/expenses"
)
```

---

# requirements.txt

```txt
streamlit
requests
pandas
```

---

# Streamlit Deployment

Frontend deployed using Streamlit Cloud.

## Deployment Steps

1. Push frontend code to GitHub
2. Open Streamlit Cloud
3. Connect GitHub repository
4. Select `app.py`
5. Deploy application

---

# Concepts Used

- Streamlit UI
- API Integration
- CRUD Operations
- HTTP Requests
- DataFrames using Pandas
- Sidebar Navigation
- Forms and Buttons

---

# Future Improvements

- Authentication System
- Expense Analytics Dashboard
- Charts and Graphs
- Monthly Reports
- Export CSV
- Responsive UI

---

# Author

Bhargavi
