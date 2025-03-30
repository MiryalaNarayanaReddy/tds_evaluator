from flask import Flask, render_template, request, jsonify
import requests
from mapping import a1_data  # Ensure this function returns data correctly

app = Flask(__name__)

# API_URL = "http://localhost:8000/api/"
API_URL = "https://tds-solver-sigma.vercel.app/api/"

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


# send file to API
    files = None
    if q_data.get("filepath"):
        files = {"file": open(q_data["filepath"], "rb")}
   

    print(payload)

    try:
        response = requests.post(API_URL, data=payload, files=files)
        response_data = response.json()

        answer = response_data.get("answer")
        expected_answer = q_data["answer"]

        if q_id == "q-use-json":
            import json 
            expected_answer = json.loads(expected_answer)
            answer = json.loads(answer)
    

        status = "✅ Matches" if answer == expected_answer else f"❌ Mismatch - Expected: {expected_answer}, Got: {answer}"

        return jsonify({"response": response_data, "status": status})

    except Exception as e:
        return jsonify({"response": None, "status": f"❌ Error - {str(e)}"})


if __name__ == '__main__':
    app.run(debug=True)
