import streamlit as st
import pandas as pd
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Set up Streamlit layout
st.set_page_config(page_title="AI Fraud Graph Visualizer", layout="wide")
st.title("🧠 AI Fraud Detection with Neo4j")
st.markdown("Visualize suspicious patterns using Neo4j graph database.")

# Load .env if running locally
load_dotenv()

# Safe fallback if not using .env (e.g. on Streamlit Cloud)
NEO4J_URI = os.getenv("NEO4J_URI", "neo4j+s://658ecbb9.databases.neo4j.io")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "fnP8gdAU3XfuItnVcpZsmvQ1WPac8Fm4aruFf7VoN3o")

# Load data
try:
    df_customers = pd.read_csv("data/customers.csv")
    df_accounts = pd.read_csv("data/accounts.csv")
    df_transactions = pd.read_csv("data/transactions.csv")
except FileNotFoundError as e:
    st.error(f"Data loading error: {e}")
    st.stop()

# Neo4j connection setup
@st.cache_resource
def get_neo4j_driver():
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

driver = get_neo4j_driver()

# UI Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📄 Customers", "🏦 Accounts", "💸 Transactions", "📊 Graph Summary"])

with tab1:
    st.subheader("Customer Overview")
    st.dataframe(df_customers)

with tab2:
    st.subheader("Accounts Linked to Customers")
    st.dataframe(df_accounts)

with tab3:
    st.subheader("Transaction Records")
    st.dataframe(df_transactions)

with tab4:
    st.subheader("Neo4j Pattern Lookup")
    selected_account = st.selectbox("Select Account ID", df_accounts["account_id"].unique())

    if st.button("Analyze Neo4j"):
        with driver.session() as session:
            cypher_query = """
            MATCH (c:Customer)-[:OWNS]->(a:Account {id: $account_id})-[:TRANSFERRED_TO]->(b:Account)
            RETURN c.name AS customer, a.id AS from_account, b.id AS to_account, b.balance AS suspicious_balance
            LIMIT 10
            """
            result = session.run(cypher_query, account_id=selected_account)
            findings = result.data()

        if not findings:
            st.warning("No suspicious patterns found.")
        else:
            st.subheader("Potential Transaction Links:")
            for f in findings:
                st.markdown(
                    f"- **{f['customer']}** sent from `{f['from_account']}` to `{f['to_account']}` — Balance: {f['suspicious_balance']}"
                )
