from fastapi import APIRouter, HTTPException
from typing import List

from app.dtos.product_details_schema import ProductDetailsSchema
from app.dtos.products_list_schema import ProductListSchema
from app.domain.services.products_service import ProductsService
from app.infrastructure.data.products_respository_json import ProductsRepositoryJson
from app.shared.exceptions import ProductNotFoundException, EmptyProductListException
from app.dtos.mapper import product_to_details_schema, products_list_to_schema

router = APIRouter()

repository = ProductsRepositoryJson("app/infrastructure/data/product.json")
service = ProductsService(repository)


@router.get("/", response_model=List[ProductListSchema])
def get_products():
    try:
        products = service.get_products()
        return products_list_to_schema(products)
    except EmptyProductListException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno ao buscar produtos")


@router.get("/{product_id}", response_model=ProductDetailsSchema)
def get_product_by_id(product_id: str):
    try:
        product = service.get_product(product_id)
        return product_to_details_schema(product)
    except ProductNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno ao buscar produto")


@router.get("/{product_id}/related", response_model=List[ProductListSchema])
def get_related_products(product_id: str):
    try:
        products = service.get_related_products(product_id)
        return products_list_to_schema(products)
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao buscar produtos relacionados")
