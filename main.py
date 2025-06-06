from fastapi import FastAPI
from app.controllers.product_controller import router as product_router

app = FastAPI(title="Product Detail Microservice")

app.include_router(product_router, prefix="/products")
