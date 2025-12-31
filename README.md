# Sentiment-Tracker-for-User-Feedback

## 📖 Project Overview
The Sentiment Tracker is a full-stack web application that analyzes textual user feedback and classifies it as **Positive**, **Negative**, or **Neutral** using Machine Learning techniques.

Users submit feedback through a **React.js web interface**.  
The backend, built with **Flask**, processes the text using an ML-based sentiment analyzer and stores the result in a **MySQL database**.

All advanced operations like update and delete, are tested using **Postman**, making this project ideal for understanding **ML integration with REST APIs**.

---

## 🧠 Why AI / ML?
Manual sentiment tagging is inefficient and inconsistent.  
This project uses **TextBlob**, an NLP-based ML library, to:

- Automatically analyze sentiment
- Provide consistent results
- Avoid the need for GPUs or cloud-based LLM APIs

Sentiment is derived from **polarity scores**:
- `> 0.2` → Positive
- `< -0.2` → Negative
- Otherwise → Neutral

---

## 🏗️ System Architecture
React.js Frontend
|
v
Flask REST API
| |
v v
ML Module MySQL Database

---

## 🧩 Tech Stack

| Layer      | Technology |
|------------|-----------|
| Frontend   | React.js (Web) |
| Backend    | Flask (Python) |
| ML         | TextBlob |
| Database   | MySQL |
| API Testing| Postman |

---

## 📂 Project Structure


sentiment-tracker/
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── sentiment.py
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
│
└── README.md


---

## 🔄 End-to-End Data Flow

1. User submits feedback via React UI
2. React sends POST request to Flask
3. Flask calls ML sentiment module
4. Sentiment is classified
5. Data is stored in MySQL
6. React fetches feedback using GET API
7. Feedback and sentiment labels are displayed
8. Admin tests PUT/DELETE using Postman

---

## 🚀 How to Run
Detailed steps are provided in:
- `/backend/README.md`
- `/frontend/README.md`


