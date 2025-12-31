from textblob import TextBlob

def analyze_sentiment(message):
    blob = TextBlob(message)
    polarity = blob.sentiment.polarity  # Range: -1.0 (neg) to 1.0 (pos)

    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

