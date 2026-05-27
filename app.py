import streamlit as st
import requests
import pandas as pd

BASE_URL = "http://127.0.0.1:8000"

st.title("Expense Tracker")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Add Expense",
        "View Expenses",
        "Update Expense",
        "Delete Expense",
        "Search Expense",
        "Sort Expenses"
    ]
)

# Add Expense
if menu == "Add Expense":

    st.header("Add Expense")

    title = st.text_input("Title")

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Other"
        ]
    )

    if st.button("Add"):

        payload = {
            "title": title,
            "amount": amount,
            "category": category
        }

        response = requests.post(
            f"{BASE_URL}/expenses",
            json=payload
        )

        if response.status_code == 200:
            st.success("Expense Added")
        else:
            st.error("Failed")


# View Expenses
elif menu == "View Expenses":

    st.header("All Expenses")

    response = requests.get(
        f"{BASE_URL}/expenses"
    )

    data = response.json()

    df = pd.DataFrame(data)

    st.dataframe(df)


# Update Expense
elif menu == "Update Expense":

    st.header("Update Expense")

    expense_id = st.number_input(
        "Expense ID",
        min_value=1
    )

    title = st.text_input("New Title")

    amount = st.number_input(
        "New Amount",
        min_value=0.0
    )

    category = st.selectbox(
        "New Category",
        [
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Other"
        ]
    )

    if st.button("Update"):

        payload = {
            "title": title,
            "amount": amount,
            "category": category
        }

        response = requests.put(
            f"{BASE_URL}/expenses/{expense_id}",
            json=payload
        )

        if response.status_code == 200:
            st.success("Updated Successfully")
        else:
            st.error("Expense Not Found")


# Delete Expense
elif menu == "Delete Expense":

    st.header("Delete Expense")

    expense_id = st.number_input(
        "Expense ID",
        min_value=1
    )

    if st.button("Delete"):

        response = requests.delete(
            f"{BASE_URL}/expenses/{expense_id}"
        )

        if response.status_code == 200:
            st.success("Deleted Successfully")
        else:
            st.error("Expense Not Found")


# Search Expense
elif menu == "Search Expense":

    st.header("Search By Category")

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Other"
        ]
    )

    if st.button("Search"):

        response = requests.get(
            f"{BASE_URL}/search?category={category}"
        )

        data = response.json()

        df = pd.DataFrame(data)

        st.dataframe(df)


# Sort Expenses
elif menu == "Sort Expenses":

    st.header("Sort Expenses")

    sort_by = st.selectbox(
        "Sort By",
        [
            "date_desc",
            "date_asc",
            "price_desc",
            "price_asc"
        ]
    )

    if st.button("Sort"):

        response = requests.get(
            f"{BASE_URL}/sort?sort_by={sort_by}"
        )

        data = response.json()

        df = pd.DataFrame(data)

        st.dataframe(df)