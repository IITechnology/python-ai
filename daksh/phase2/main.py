from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/vote")
def check_eligibility(age: int):

    if age < 18:
        raise HTTPException(
            status_code=403,
            detail="You are not eligible to vote"
        )

    return {"message": "You are eligible to vote"}