# AI Fraud Detection with Graphs (Neo4j)

End-to-end AML app with Neo4j, Streamlit, FastAPI, LLM summaries, and machine learning risk scoring.
# 
This app visualizes suspicious transaction patterns using a graph-based model powered by Neo4j and Streamlit.

## Features
- Load and explore customer, account, and transaction data
- Visualize relationships between customers and transactions
- Query suspicious patterns with Neo4j
- Secure connection using `.env` file (never commit this)

##  Project Structure

```
ai-fraud-detection-graphs/
├── app.py                 # Streamlit app
├── .env                  # Local-only secrets (excluded from GitHub)
├── .gitignore            # Prevents secrets from being committed
└── data/
    ├── customers.csv
    ├── accounts.csv
    └── transactions.csv
```

##  Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add a `.env` file to the project root:
```
NEO4J_URI=your_neo4j_url
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```

3. Run the app locally:
```bash
streamlit run app.py
```

4. Deploy on Streamlit Cloud (it will fall back to hardcoded values if no `.env` is found)

##  Demo
Ready for deployment via [Streamlit Cloud](https://streamlit.io/cloud)

## Author
Developed by Adetola Adeniyi — AI Engineer & Data Scientist.
