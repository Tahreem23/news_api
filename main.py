from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/articles")

@app.get("/articles")
async def get_all_articles():
    try:
        response = requests.get("https://newsapi.org/v2/everything?q=apple&language=en&from=2023-10-05&sortBy=publishedAt&apiKey=eff0da1b31144e8da7ba3ff9df6876e2")
        response.raise_for_status()
        data = response.json()
        articles = data["articles"]
        return articles
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))