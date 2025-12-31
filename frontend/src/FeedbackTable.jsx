import React, { useEffect } from "react";
import SentimentBAdge from "./SentimentBAdge";
import { useState } from "react";

export default function FeedbackTable() {

    const [feedbackList, setFeedbackList] = useState([]);

    const fetchFeedback = async () => {
        const res = await fetch('http://localhost:5000/feedback');
        const data = await res.json();
        setFeedbackList(data);
    };

    useEffect(() => {
        fetchFeedback();
    });

    return (
        <div>
            <div className="row">
                <h3>Previous Feedbacks: </h3>
                <button onClick={fetchFeedback}>Reload</button>
            </div>
            <div>
                {feedbackList.map((item) => (
                    <ul key={item.id}>{item.message} — <SentimentBAdge value={item.sentiment} /></ul>
                ))}
            </div>
        </div>


    )
}