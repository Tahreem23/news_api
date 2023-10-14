from fastapi import FastAPI

app = FastAPI()

@app.get("/articles")

def get_articles():
    return {
        "articles": [
            {
                "title": "Example News Title 1",
                "content": "Example news content 1.",
            },
            {
                "title": "Example News Title 2",
                "content": "Example news content 2.",
            },
        ]
    }