from fastapi import FastAPI
app=FastAPI(title="hello world",description="This is our fist API",version="1.0.0")

#http get request
@app.get("/") #annotation
def read_route():
    return {
        "message": "Welcome to development lab", #key: #value
        "phase": "21",
        "satus": "active"
    }