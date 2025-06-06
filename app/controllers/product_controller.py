from fastapi import APIRouter, HTTPException
from app.dtos.product_schema import ProductSchema
from app.domain.services.product_service import ProductService
from app.infrastructure.data.product_repository_json import ProductRepositoryJson
from app.shared.exceptions import ProductNotFoundException

router = APIRouter()

repository = ProductRepositoryJson("app/infrastructure/data/products.json")
service = ProductService(repository)


@router.get("/{product_id}", response_model=ProductSchema)
def get_product_by_id(product_id: str):
    try:

        product = service.get_product(product_id)

        return {
            "id": product.id,
            "title": product.title,
            "description": product.description,
            "price": {
                "amount": product.price.amount,
                "currency": product.price.currency,
            },
            "images": product.images,
            "stock": product.stock,
            "seller_id": product.seller_id,
        }

    except ProductNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno ao buscar produto")