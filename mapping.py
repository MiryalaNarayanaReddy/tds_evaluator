import json



def a1_data():
    json_data = json.load(open("./mapping/a1.json"))
    
    # questions
    ids = [
        "q-vs-code-version",
        "q-uv-http-get",
        "q-npx-prettier"
    ]

    files = {
        "q-npx-prettier":   "./mapping/files/README.md",
    }

    data = []

    for id in ids:
        data.append({
            "id": id,
            "question": json_data[id]["question"],
            "filepath": files.get(id, None),
            "answer": json_data[id]["answer"]
        })

    return data
