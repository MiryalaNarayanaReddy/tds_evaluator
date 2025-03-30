import json

def a1_data():
    json_data = json.load(open("./mapping/a1.json"))
    
    # questions
    ids = [
        "q-vs-code-version",
        "q-uv-http-get",
        "q-npx-prettier",
        "q-use-google-sheets",
        "q-use-excel",
        "q-use-devtools",
        "q-count-wednesdays",
        "q-extract-csv-zip",
        "q-use-json",
        "q-multi-cursor-json",
        "q-css-selectors",
        "q-unicode-data",
        "q-use-github",
        "q-replace-across-files",
        "q-list-files-attributes",
        "q-move-rename-files",
        "q-compare-files",        
        "q-sql-ticket-sales"
    ]

    files = {
        "q-npx-prettier":   "./mapping/files/README.md",
        "q-extract-csv-zip": "./mapping/files/q-extract-csv-zip.zip",

        "q-multi-cursor-json": "./mapping/files/q-multi-cursor-json.txt",

        "q-unicode-data": "./mapping/files/q-unicode-data.zip",

        "q-replace-across-files": "./mapping/files/q-replace-across-files.zip",
        "q-move-rename-files": "./mapping/files/q-move-rename-files.zip",
        "q-list-files-attributes": "./mapping/files/q-list-files-attributes.zip",
        "q-compare-files": "./mapping/files/q-compare-files.zip",

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
