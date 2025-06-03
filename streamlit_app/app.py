import streamlit as st
import pandas as pd

st.set_page_config(page_title="AML Graph Visualizer", layout="wide")

st.title("AML Graph Visualizer")
st.markdown("Visualize suspicious transactions using Neo4j and generate AI-powered SAR summaries.")

# Load data
try:
    df_customers = pd.read_csv("data/customers.csv")
    df_accounts = pd.read_csv("data/accounts.csv")
    df_transactions = pd.read_csv("data/transactions.csv")
except FileNotFoundError as e:
    st.error(f"Could not load data file: {e}")
    st.stop()

# Show tabs
tab1, tab2, tab3, tab4 = st.tabs(["📄 Customers", "🏦 Accounts", "💸 Transactions", "🧠 Generate SAR"])

with tab1:
    st.subheader("Customer List")
    st.dataframe(df_customers)

with tab2:
    st.subheader("Customer Accounts")
    st.dataframe(df_accounts)

with tab3:
    st.subheader("Transaction Records")
    st.dataframe(df_transactions)

with tab4:
    st.subheader("Suspicious Activity Report")
    account_ids = df_accounts["account_id"].unique()
    selected_account = st.selectbox("Select Account ID", account_ids)
    if st.button("Generate SAR"):
        # Basic logic — can be replaced with LLM later
        st.success(f"SAR Summary for Account {selected_account}: Possible suspicious pattern due to high volume or circular transactions.")
