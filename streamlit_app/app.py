
import streamlit as st
import pandas as pd
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Load environment variables for local dev
load_dotenv()

st.set_page_config(page_title="AI Fraud Graph Visualizer", layout="wide")
st.title("🧠 AI Fraud Detection with Neo4j")
st.markdown("Visualize suspicious patterns using Neo4j graph database.")

# Debug: display loaded secrets
st.write("Loaded secrets keys:", list(st.secrets.keys()))

# Smart fallback to secrets first, then .env
NEO4J_URI = st.secrets.get("NEO4J_URI", os.getenv("NEO4J_URI"))
NEO4J_USERNAME = st.secrets.get("NEO4J_USERNAME", os.getenv("NEO4J_USERNAME"))
NEO4J_PASSWORD = st.secrets.get("NEO4J_PASSWORD", os.getenv("NEO4J_PASSWORD"))

# Load data
try:
    df_customers = pd.read_csv("data/customers.csv")
    df_accounts = pd.read_csv("data/accounts.csv")
    df_transactions = pd.read_csv("data/transactions.csv")
except FileNotFoundError as e:
    st.error(f"Data loading error: {e}")
    st.stop()

@st.cache_resource
def get_neo4j_driver():
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

driver = get_neo4j_driver()

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
                st.markdown(f"- **{f['customer']}** sent from `{f['from_account']}` to `{f['to_account']}` — Balance: {f['suspicious_balance']}")

import openai

OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
openai.api_key = OPENAI_API_KEY

tab5 = st.tabs(["🧠 Generate SAR"])[0]

with tab5:
    st.subheader("LLM-Generated Suspicious Activity Report (SAR)")
    account_options = df_accounts["account_id"].unique()
    selected_id = st.selectbox("Select Account ID to Analyze", account_options)

    if st.button("Generate LLM SAR"):
        with driver.session() as session:
            query = """
            MATCH (c:Customer)-[:OWNS]->(a:Account {id: $acc_id})-[:TRANSFERRED_TO]->(b:Account)
            RETURN c.name AS customer, a.id AS from_account, b.id AS to_account, b.balance AS suspicious_balance
            LIMIT 10
            """
            tx_result = session.run(query, acc_id=selected_id)
            tx_data = tx_result.data()

        if not tx_data:
            st.info("No graph data found for this account.")
        else:
            summary_prompt = f"""
            You are an anti-money laundering analyst. Based on the following transaction graph data, write a concise Suspicious Activity Report summary:

            {tx_data}

            Emphasize suspicious transaction flows, sudden balance increases, or circular money movements.
            """
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": summary_prompt}],
                    max_tokens=300
                )
                sar_output = response['choices'][0]['message']['content']
                st.success("Generated SAR Summary:")
                st.markdown(sar_output)
            except Exception as e:
                st.error(f"OpenAI error: {e}")
