import React from 'react';

export default function SentimentBAdge({ value }) {
  let color = '';
  let label = '';

  switch (value) {
    case 'positive':
      color = '#6cda96ff';
      label = '😊';
      break;
    case 'negative':
      color = '#DA6C6C';
      label = '😠';
      break;
    case 'neutral':
    default:
      color = '#bcbcbcff';
      label = '😐';
      break;
  }

  return (
    <span style={{
      color: 'white',
      backgroundColor: color,
      padding: '4px 8px',
      borderRadius: '8px',
      fontSize: '0.9rem'
    }}>
      {label}
    </span>
  );
}
