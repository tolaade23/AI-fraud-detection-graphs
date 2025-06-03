import streamlit as st
import pandas as pd

st.set_page_config(page_title="AML Graph Visualizer", layout="wide")

st.title("AML Graph Visualizer")
st.markdown("Visualize suspicious transactions using Neo4j and generate AI-powered SAR summaries.")

# Load sample data
try:
    df_customers = pd.read_csv("data/customers.csv")
    df_transactions = pd.read_csv("data/transactions.csv")
except FileNotFoundError:
    st.error("Could not load data files. Please make sure 'data/' folder is present.")
    st.stop()

# Show tabs
tab1, tab2, tab3 = st.tabs(["📄 Customers", "💸 Transactions", "🧠 Generate SAR"])

with tab1:
    st.subheader("Customer Accounts")
    st.dataframe(df_customers)

with tab2:
    st.subheader("Transaction Records")
    st.dataframe(df_transactions)

with tab3:
    st.subheader("Suspicious Activity Report")
    selected_account = st.selectbox("Select Account ID", df_customers["account_id"].unique())
    if st.button("Generate SAR"):
        # Basic logic — later replaced with LLM
        st.success(f"SAR Summary for Account {selected_account}: Possible suspicious pattern due to high volume or circular transactions.")
