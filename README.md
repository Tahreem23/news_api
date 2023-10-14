# news_api
News App API using Python (FastAPI)

# Installation:

1. Clone the repository:
2. Create a virtual environment:

   ```python3 -m venv venv```
4. Activate the virtual environment:
   
     ```source venv/bin/activate```
  
6. Install dependencies:
   
   ```pip install -r requirements.txt```


# Usage:

1. Run the FastAPI application:

   
     ```uvicorn main:app --reload```
3. Access the API using the following URL:

   
     ```http://127.0.0.1:8000/articles```
5. To specify a query term, add the query parameter to the URL:

   
     ```http://127.0.0.1:8000/articles?query=apple```
7. To specify a language, add the language parameter to the URL:

   
     ```http://127.0.0.1:8000/articles?query=apple&language=ar```
