# Frontend – Sentiment Tracker (Vite + React Web Application)

## Overview
This frontend is a web application built using **Vite + React** that allows users to:

- Submit textual user feedback
- View stored feedback from the backend
- See sentiment labels (Positive, Negative, Neutral)

This is a **React.js web application created using Vite**.

---

## Tech Stack
- Vite
- React.js
- JavaScript (ES6)
- HTML5
- CSS3
- Fetch API 

---

## Folder Structure

frontend/
├── public/
├── src/
│   ├── components/
│   │   ├── FeedbackForm.jsx      # Feedback input form
│   │   ├── FeedbackTable.jsx     # Displays feedback list
│   │   └── SentimentBadge.jsx   # Color-coded sentiment labels
│   ├── App.jsx                  # Main application component
│   └── main.jsx                 # Application entry point
├── index.html
├── package.json
├── vite.config.js
└── README.md

---

## Components

### FeedbackForm
- Accepts user feedback input
- Sends POST request to Flask backend

### FeedbackTable
- Fetches and displays feedback from the backend
- Shows sentiment label for each message

### SentimentBadge
- Displays sentiment with color coding:
  - Green → Positive
  - Red → Negative
  - Gray → Neutral

---

## API Communication
The frontend communicates with the Flask backend using HTTP requests.

Example using Fetch API:

fetch("http://localhost:5000/feedback")

---

## Application URL
The frontend runs on:

http://localhost:4000

---

## Notes
- Only Create and Read operations are available through the UI
- Update and Delete operations are performed using Postman
- Minimal validation is implemented (basic text length check)
