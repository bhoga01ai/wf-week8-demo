from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Simple API Demo")

# Enable CORS for frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database (just a list)
items_db = []
next_id = 1


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    price: float


@app.get("/")
async def root():
    return FileResponse("static/index.html")


@app.get("/api/items", response_model=List[Item])
async def get_items():
    """Get all items"""
    return items_db


@app.get("/api/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Get a specific item by ID"""
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/api/items", response_model=Item)
async def create_item(item: Item):
    """Create a new item"""
    global next_id
    new_item = item.dict()
    new_item["id"] = next_id
    next_id += 1
    items_db.append(new_item)
    return new_item


@app.put("/api/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    """Update an existing item"""
    for idx, existing_item in enumerate(items_db):
        if existing_item["id"] == item_id:
            updated_item = item.dict()
            updated_item["id"] = item_id
            items_db[idx] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/api/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item"""
    for idx, item in enumerate(items_db):
        if item["id"] == item_id:
            items_db.pop(idx)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
