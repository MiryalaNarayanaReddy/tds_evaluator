from flask import Flask, render_template, request, jsonify
import requests
import json
from mapping import a1_data, a2_data, a3_data, a4_data, a5_data  # Ensure this function returns data correctly

app = Flask(__name__)

API_URL = "http://localhost:8000/api/"

# Load questions
A1_QUESTIONS = [
    {"id": item["id"], "question": item["question"], "answer": item["answer"], "filepath": item.get("filepath", None)}
    for item in a1_data()
]

A2_QUESTIONS = [
    {"id": item["id"], "question": item["question"], "answer": item["answer"], "filepath": item.get("filepath", None)}
    for item in a2_data()
]

A3_QUESTIONS = [
    {"id": item["id"], "question": item["question"], "answer": item["answer"], "filepath": item.get("filepath", None)}
    for item in a3_data()
]    

A4_QUESTIONS = [
    {"id": item["id"], "question": item["question"], "answer": item["answer"], "filepath": item.get("filepath", None)}
    for item in a4_data()
]

A5_QUESTIONS = [
    {"id": item["id"], "question": item["question"], "answer": item["answer"], "filepath": item.get("filepath", None)}
    for item in a5_data()
]

# Store assignments in a list
QUESTIONS_DATA = [A1_QUESTIONS, A2_QUESTIONS, A3_QUESTIONS, A4_QUESTIONS, A5_QUESTIONS]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/get_questions', methods=['GET'])
def get_questions():
    try:
        index = int(request.args.get("index", 0))  # Default to A1 if not provided
        if index < 0 or index >= len(QUESTIONS_DATA):
            return jsonify({"error": "Invalid index"}), 400
        return jsonify(QUESTIONS_DATA[index])
    except ValueError:
        return jsonify({"error": "Index must be an integer"}), 400

@app.route('/api/send_request', methods=['POST'])
def send_request():
    try:
        q_id = request.form.get("id")
        index = int(request.args.get("index", 0))  # Default to A1 if not provided

        if index < 0 or index >= len(QUESTIONS_DATA):
            return jsonify({"error": "Invalid index"}), 400

        # Find question by ID
        q_data = next((item for item in QUESTIONS_DATA[index] if item["id"] == q_id), None)

        if not q_data:
            return jsonify({"error": "Question not found"}), 404

        payload = {"question": q_data["question"]}

        # Handle file upload
        files = None
        if q_data.get("filepath"):
            try:
                files = {"file": open(q_data["filepath"], "rb")}
            except FileNotFoundError:
                return jsonify({"error": f"File not found: {q_data['filepath']}"}), 400

        # Send request to API
        response = requests.post(API_URL, data=payload, files=files)
        response_data = response.json()

        # Validate response
        answer = response_data.get("answer")
        expected_answer = q_data["answer"]

        if q_id == "q-use-json":
            expected_answer = json.loads(expected_answer)
            answer = json.loads(answer)

        status = "✅ Matches" if answer == expected_answer else f"❌ Mismatch - Expected: {expected_answer}, Got: {answer}"

        return jsonify({"response": response_data, "status": status})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
