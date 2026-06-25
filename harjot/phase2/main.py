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
    
@app.get("/calculate/{num1}/{num2}")

def calculate(num1:int,num2:int, opertaion: str="add"):
        
        if opertaion == "add":
            return {
                "result":num1 + num2
    }
        elif opertaion == "-":
            return {
                "result":num1 - num2
    
    }
        elif opertaion == "*":

            return {
                "result":num1 * num2
    }
    
        elif opertaion == "/":

            return {
                "result":num1 / num2
            }
        else:
            print()  

