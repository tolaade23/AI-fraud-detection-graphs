# 🔍 AI Fraud Detection with Graphs (Neo4j + LLM)

An end-to-end Anti-Money Laundering (AML) system that detects suspicious activity using a graph-based model powered by Neo4j, Streamlit, and OpenAI LLMs.

## ✨ Key Features

- 📊 **Interactive Graph Analysis**  
  Visualize customer-to-account relationships and trace transaction flows.

- 🔎 **Suspicious Pattern Detection**  
  Run dynamic Neo4j Cypher queries to uncover potential money laundering behaviors.

- 🧠 **AI-Powered SAR Generation**  
  Automatically generate Suspicious Activity Report summaries using OpenAI’s GPT.

- 📁 **Data Ingestion & Exploration**  
  Load, preview, and analyze structured customer, account, and transaction data.

- 🔐 **Secure & Extensible**  
  Uses `.env` for secret management. Easily extendable with ML scoring or REST APIs.

---

## 🗂️ Project Structure

```
ai-fraud-detection-graphs/
├── app.py                 # Streamlit interface
├── .env                   # Local credentials (excluded)
├── requirements.txt       # Python dependencies
├── .gitignore             # Excludes .env and other local files
└── data/
    ├── customers.csv
    ├── accounts.csv
    └── transactions.csv
```

---

## 🚀 Getting Started

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your `.env` file**  
   Create a `.env` file in the root directory:
   ```
   NEO4J_URI=bolt://your_neo4j_host:7687
   NEO4J_USERNAME=neo4j
   NEO4J_PASSWORD=your_password
   OPENAI_API_KEY=your_openai_key
   ```

3. **Launch the Streamlit app**  
   ```bash
   streamlit run app.py
   ```

4. **(Optional) Deploy to Streamlit Cloud**  
   - Add your secrets in the **Streamlit Cloud secrets manager**.  
   - App gracefully falls back to `.env` if secrets are not found.

---

## 🧠 Optional: Add ML Risk Scoring Engine

Use a simple logistic regression or anomaly detection model to score transactions for fraud risk and display the results in the Streamlit dashboard.

```python
# Example scoring logic
if transaction_amount > threshold:
    score = 'High Risk'
```

You can extend the current app to load ML predictions and show risk levels.

---

## 📄 Sample SAR Format

```text
Suspicious Activity Report (SAR)
----------------------------------
Customer: Jane Doe
From Account: 10391  → To Account: 20984
Unusual Behavior: Circular transfers totaling $85,000 within 2 hours.
Risk Level: High
Summary: Activity suggests rapid fund movement across connected accounts to avoid detection.
```

---

## 🎥 Demo & Screenshots

Coming soon: Hosted version + walk-through video  
(*You can link Loom/YouTube demo here later for interviews or freelance gigs*)

---

## 📌 Technologies Used

- **Neo4j** – Graph database for relationship modeling  
- **Streamlit** – UI for real-time visualizations  
- **OpenAI GPT-3.5** – LLM-powered SAR summary generation  
- **Pandas** – Data loading and preprocessing  
- **dotenv** – Secure secret handling  
- *(Optional: FastAPI or ML model for backend scoring)*

---

## 👤 Author

**Adetola Adeniyi**  
AI Engineer | Data Scientist  
📧 [adetola.molara@gmail.com](mailto:adetola.molara@gmail.com)  
🌐 [LinkedIn](https://linkedin.com/in/adetola-adeniyi) | [GitHub](https://github.com/yourusername)

---

<!-- Social Preview -->
