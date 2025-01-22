from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet():
    return {"message": "Hello, welcome to the FastAPI GCP project!"}

@app.get("/fetch_weather_today")
def fetch_weather_today():
    # Simulating fetching weather data
    return {"weather": "Sunny", "temperature": "25°C"}
