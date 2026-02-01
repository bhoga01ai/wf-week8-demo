# FastAPI Demo - Quick Start Guide

## What's Included

This demo includes:
- **FastAPI Backend** ([app.py](app.py)) - RESTful API with CRUD operations for items
- **Vanilla HTML Frontend** ([static/index.html](static/index.html)) - Interactive web interface

## API Endpoints

- `GET /api/items` - Get all items
- `GET /api/items/{id}` - Get specific item
- `POST /api/items` - Create new item
- `PUT /api/items/{id}` - Update item
- `DELETE /api/items/{id}` - Delete item

## How to Run

1. **Start the FastAPI server:**
   ```bash
   python app.py
   ```

   Or using uvicorn directly:
   ```bash
   uvicorn app:app --reload
   ```

2. **Open your browser and visit:**
   - Main App: http://localhost:8080
   - API Docs: http://localhost:8080/docs (Swagger UI)
   - Alternative API Docs: http://localhost:8080/redoc

## Features

- Add new items with name, description, and price
- View all items in a beautiful card layout
- Edit existing items
- Delete items with confirmation
- Real-time updates
- Responsive design

## Technology Stack

- **Backend:** FastAPI, Pydantic, Uvicorn
- **Frontend:** Vanilla HTML, CSS, JavaScript (no frameworks)
- **Data Storage:** In-memory (resets on server restart)

Enjoy exploring the demo!
