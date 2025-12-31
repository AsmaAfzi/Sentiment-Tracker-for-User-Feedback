from flask import Flask, request, jsonify
from flask_cors import CORS
import db
import sentiment as st

app = Flask(__name__)
CORS(app)

@app.route('/feedback', methods=['POST'])
def post_feedback():
    try:
        data=request.json
    
        if not data:
            return jsonify({"error":"Message is required"}), 400
    
        message=data.get('message')
        sentiment = st.analyze_sentiment(message)
        db.insert_feedback(message, sentiment)
        return jsonify({"message": message, "sentiment": sentiment}), 201
    
    except Exception as e:
        print(f"Error in POST /feedback: {e}")
        return jsonify ({"error":"Internal Server Error"}), 500


@app.route('/feedback', methods=['GET'])
def get_feedback():
    feedback_list = db.get_all_feedback()
    result = []
    for row in feedback_list:
        result.append({
            "id": row[0],
            "message": row[1],
            "sentiment": row[2],
            "created_at": row[3]
        })
    return jsonify(result)


@app.route('/feedback/<int:id>', methods=['GET'])
def get_feedback_byID(id):
    feedback_=db.get_feedback_by_id(id)
    if feedback_:
        return jsonify({
            "id": feedback_[0],
            "message": feedback_[1],
            "sentiment": feedback_[2],
            "created_at": feedback_[3]
        })
    return jsonify ({"error":"Feedback not Found"}),404


@app.route('/feedback/<int:id>', methods=['PUT'])
def update_feedback(id):
    data=request.json
    new_message=data.get('message')

    if not new_message:
        return jsonify({"error":"Message is required"}), 400
    
    sentiment=st.analyze_sentiment(new_message)
    db.update_feedback(id,new_message, sentiment)
    return jsonify({" updated_message": new_message, "sentiment": sentiment}), 200

@app.route('/feedback/<int:id>', methods=['DELETE'])
def del_feedback(id):
    delete=db.delete_feedback(id)

    if delete:
        return jsonify({"success":"Feedback successfully deleted"})
    return jsonify({"error":"Feedback not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
