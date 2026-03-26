from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any

app = FastAPI()

# Dummy in-memory database to simulate backend data
farmers = []

@app.get("/farmers", response_model=List[Dict[str, Any]])
async def get_farmers():
    """
    Retrieve the list of farmers.
    ",
    return farmers

@app.post("/farmers", response_model=Dict[str, Any])
async def create_farmer(farmer: Dict[str, Any]):
    """
    Create a new farmer record.
    ",
    farmers.append(farmer)
    return farmer

@app.get("/farmers/{farmer_id}", response_model=Dict[str, Any])
async def get_farmer(farmer_id: int):
    """
    Retrieve a farmer by their ID.
    ",
    farmer = next((f for f in farmers if f["id"] == farmer_id), None)
    if farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return farmer

@app.put("/farmers/{farmer_id}", response_model=Dict[str, Any])
async def update_farmer(farmer_id: int, updated_farmer: Dict[str, Any]):
    """
    Update an existing farmer record.
    ",
    farmer = next((f for f in farmers if f["id"] == farmer_id), None)
    if farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    farmers.remove(farmer)
    farmers.append(updated_farmer)
    return updated_farmer

@app.delete("/farmers/{farmer_id}")
async def delete_farmer(farmer_id: int):
    """
    Delete a farmer record by ID.
    ",
    farmer = next((f for f in farmers if f["id"] == farmer_id), None)
    if farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    farmers.remove(farmer)
    return {"detail": "Farmer deleted"}
