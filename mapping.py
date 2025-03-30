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
        "q-npx-prettier":   "./mapping/a1/README.md",
        "q-extract-csv-zip": "./mapping/a1/q-extract-csv-zip.zip",

        "q-multi-cursor-json": "./mapping/a1/q-multi-cursor-json.txt",

        "q-unicode-data": "./mapping/a1/q-unicode-data.zip",

        "q-replace-across-files": "./mapping/a1/q-replace-across-files.zip",
        "q-move-rename-files": "./mapping/a1/q-move-rename-files.zip",
        "q-list-files-attributes": "./mapping/a1/q-list-files-attributes.zip",
        "q-compare-files": "./mapping/a1/q-compare-files.zip",

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



def a2_data():
    json_data = json.load(open("./mapping/a2.json"))
    
    # questions
    ids = [
        "q-markdown",
        "q-image-compression",
        "q-github-pages",
        "q-use-colab",
        "q-use-colab-image-library",
        "q-vercel-python",
        "q-github-action",
        "q-docker-hub-image",
        "q-fastapi",
        "q-llamafile",
    ]

    files = {
        "q-image-compression": "./mapping/a2/shapes.png",
        "q-use-colab-image-library": "./mapping/a2/lenna.webp",

        "q-vercel-python": "./mapping/a2/q-vercel-python.json",
        "q-fastapi": "./mapping/a2/q-fastapi.csv",
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

def a3_data():
    json_data = json.load(open("./mapping/a3.json"))
    
    # questions
    ids = [
        "q-llm-sentiment-analysis",
        "q-token-cost",
        "q-generate-addresses-with-llms",
        "q-llm-vision",
        "q-llm-embeddings",
        "q-embedding-similarity",
        "q-vector-databases",
        "q-function-calling",
        "q-get-llm-to-say-yes",
    ]

    files = {
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


def a4_data():
    json_data = json.load(open("./mapping/a4.json"))
    
    # questions
    ids = [
        "g-google-sheets-importhtml",
        "q-scrape-imdb-movies",
        "q-wikipedia-outline",
        "q-bbc-weather-api",
        "q-nominatim-api",
        "q-hacker-news-search",
        "q-find-newest-github-user",
        "q-scheduled-github-actions",
        "q-extract-tables-from-pdf",
        "q-pdf-to-markdown",
    ]

    files = {
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


def a5_data():
    json_data = json.load(open("./mapping/a5.json"))
    
    # questions    
    ids = [
        "q-clean-up-excel-sales-data",
        "q-clean-up-student-marks",
        "q-apache-log-requests",
        "q-apache-log-downloads",
        "q-clean-up-sales-data",
        "q-parse-partial-json",
        "q-extract-nested-json-keys",
        "q-duckdb-social-media-interactions",
        "q-transcribe-youtube",
        "q-image-jigsaw",
    ]

    files = {
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