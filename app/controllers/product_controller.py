from fastapi import APIRouter, HTTPException
from typing import List

from app.dtos.product_details_schema import ProductDetailsSchema
from app.domain.services.product_details_service import ProductService
from app.infrastructure.data.product_details_repository_json import ProductDetailsRepositoryJson
from app.shared.exceptions import ProductNotFoundException
from app.dtos.mapper import product_details_to_schema
from app.dtos.products_schema import ProductSchema
from app.domain.services.products_service import ProductsService
from app.infrastructure.data.products_respository_json import ProductsRepositoryJson
from app.shared.exceptions import EmptyProductListException
from app.dtos.mapper import products_to_schema

router = APIRouter()

repositoryDetails = ProductDetailsRepositoryJson("app/infrastructure/data/products_details.json")
serviceDetails = ProductService(repositoryDetails)

repositoryProducts = ProductsRepositoryJson("app/infrastructure/data/products.json")
serviceProducts = ProductsService(repositoryProducts)


@router.get("/{product_id}", response_model=ProductDetailsSchema)
def get_product_by_id(product_id: str):
    try:

        product = serviceDetails.get_product(product_id)
        return product_details_to_schema(product)

    except ProductNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno ao buscar produto")


@router.get("/", response_model=List[ProductSchema])
def get_products():
    try:

        product = serviceProducts.get_products()
        return products_to_schema(product)

    except EmptyProductListException as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno ao buscar produto")
