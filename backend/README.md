# Backend – Sentiment Tracker (Flask API)

## Overview
This backend is a RESTful API built using Flask that:

- Accepts user feedback
- Performs ML-based sentiment analysis
- Stores results in a MySQL database
- Exposes CRUD APIs for testing via Postman

---

## Tech Stack
- Python 3.x
- Flask
- TextBlob (ML / NLP)
- MySQL
- Flask-CORS

---

## Folder Structure

backend/
├── app.py            # Main Flask application and API routes
├── db.py             # MySQL connection and database queries
├── sentiment.py      # ML-based sentiment analysis logic
├── requirements.txt  # Python dependencies
└── README.md

---

## ML Logic (sentiment.py)
- Uses TextBlob to analyze text polarity
- Converts polarity scores into sentiment labels:
  - > 0.2  → Positive
  - < -0.2 → Negative
  - Otherwise → Neutral
- Lightweight and fast
- No GPU or internet connection required

---

## MySQL Schema

CREATE TABLE feedback (
  id INT AUTO_INCREMENT PRIMARY KEY,
  message TEXT NOT NULL,
  sentiment VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

---

## API Endpoints

### Create Feedback
POST /feedback

{
  "message": "This app is amazing!"
}

---

### Get All Feedback
GET /feedback

---

### Get Feedback by ID
GET /feedback/{id}

---

### Update Feedback
PUT /feedback/{id}

{
  "message": "Service was slow"
}

Sentiment is automatically re-analyzed after updating the message.

---

### Delete Feedback
DELETE /feedback/{id}

---

## How to Run Backend

cd backend  
pip install -r requirements.txt  
python app.py  

---

## Server Details
Backend runs on:

http://localhost:5000

---

## Testing
All API endpoints are tested using Postman.
