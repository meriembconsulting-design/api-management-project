from fastapi import FastAPI, HTTPException
from app.data import clients

app = FastAPI(title="Client Service")

@app.get("/clients")
def get_clients():
    return clients

@app.get("/clients/{client_id}")
def get_client(client_id: int):
    for client in clients:
        if client["id"] == client_id:
            return client
    raise HTTPException(status_code=404, detail="Client not found")
# --- Ajoutez ce healthcheck endpoint ---
# --- Ajoutez ce healthcheck endpoint ---
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
# --------------------------------------
