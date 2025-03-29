from flask import Flask, render_template, request, jsonify
import requests
from mapping import a1_data  # Ensure this function returns data correctly

app = Flask(__name__)

API_URL = "http://localhost:8000/api/"

A1_QUESTIONS = [
    {"id": item["id"], "question": item["question"], "answer": item["answer"], "filepath": item.get("filepath", "N/A")}
    for item in a1_data()
]

@app.route('/')
def index():
    return render_template("index.html", questions=a1_data())


@app.route('/api/get_questions', methods=['GET'])
def get_questions():
    questions_data = A1_QUESTIONS
    return jsonify(questions_data)  # ✅ Proper JSON response


@app.route('/api/send_request', methods=['POST'])
def send_request():
    q_id = request.form.get("id")

    q_data = [item for item in A1_QUESTIONS if item["id"] == q_id][0]

    payload = {"question": q_data["question"]}

    print(payload)

    try:
        response = requests.post(API_URL, data=payload)
        response_data = response.json()

        actual_answer = response_data.get("answer")
        # print(actual_answer)
        print(response_data)
        return jsonify({"response": response_data["answer"], "status": "✅ Matches"})
        # status = "✅ Matches" if actual_answer == expected_answer else f"❌ Mismatch - Expected: {expected_answer}, Got: {actual_answer}"

        return jsonify({"response": response_data, "status": status})

    except Exception as e:
        return jsonify({"response": None, "status": f"❌ Error - {str(e)}"})


if __name__ == '__main__':
    app.run(debug=True)
