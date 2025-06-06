from fastapi import APIRouter, HTTPException
from app.dtos.product_schema import ProductSchema
from app.domain.services.product_service import ProductService
from app.infrastructure.data.product_repository_json import ProductRepositoryJson
from app.shared.exceptions import ProductNotFoundException
from app.dtos.mapper import product_to_schema

router = APIRouter()

repository = ProductRepositoryJson("app/infrastructure/data/products.json")
service = ProductService(repository)


@router.get("/{product_id}", response_model=ProductSchema)
def get_product_by_id(product_id: str):
    try:

        product = service.get_product(product_id)
        return product_to_schema(product)

    except ProductNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno ao buscar produto")