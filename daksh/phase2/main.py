from fastapi import FastAPI, HTTPException, status

app = FastAPI(title="Welcome to exception handling")

ITEMS = {
    101: "PYTHON LAB MANUAL",
    102: "COMPUTER NETWORK NOTES",
    103: "DBMS NOTES"
}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in ITEMS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} was not found on this server"
        )

    return {"item_id": item_id, "item": ITEMS[item_id]}