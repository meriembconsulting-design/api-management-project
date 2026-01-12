from fastapi import FastAPI, HTTPException
from app.data import orders

app = FastAPI(title="Order Service")

@app.get("/orders")
def get_orders():
    return orders

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order["id"] == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")
# --- Ajoutez ce healthcheck endpoint ---
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
# --------------------------------------