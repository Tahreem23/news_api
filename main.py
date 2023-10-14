from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
import datetime

app = FastAPI()

origins = [
    "*",  # Allow all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "eff0da1b31144e8da7ba3ff9df6876e2"

@app.get("/articles")
async def get_all_articles(query: str = Query(None), language: str = Query("en")):
    try:
        url = f"https://newsapi.org/v2/everything?q={query}&language={language}&from={get_from_date()}&sortBy=publishedAt&apiKey={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        articles = data["articles"]
        return articles
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_from_date():
  today = datetime.date.today()
  from_date = today - datetime.timedelta(days=7)
  return from_date.strftime("%Y-%m-%d")