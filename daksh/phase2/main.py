from fastapi import FastAPI
app=FastAPI(title="Hello World!", description="this is my new web page ",version="1.0.0")

@app.get("/")
def read_route():
    return{
        "Name":"Daksh Pratap Singh",
        "Message": "hello world"
    }
    
@app.get("/calculate/{num1}")
def calculate(num1:int,operation:str="*"):
    for  i in range(1, 11):

        table=[]
        table.append(f"{num1} x {i} = {num1 * i}")
        
        return{"table:",table}

    