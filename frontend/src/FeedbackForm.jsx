import React, { useState } from "react";

export default function FeedbackForm() {
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();  // Prevent page reload
    const res = await fetch('http://localhost:5000/feedback', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message }),
    });
    setMessage('');  // Clear the form
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1>Feedback Form</h1>
      <p>Your feedback is valuable to us!</p>

      <textarea
        id="message"
        name="message"
        rows="5"
        cols="40"
        placeholder="Type your feedback here!"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        required
      />

      <button type="submit" id="submit">SUBMIT</button>
    </form>
  );
}
