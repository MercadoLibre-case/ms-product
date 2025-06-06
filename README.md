# 🧩 Microserviço: `ms-product-detail`

Este microserviço faz parte do projeto **MercadoLibre Clone – Item Detail Page** e é responsável por fornecer os dados detalhados de produtos por meio de uma API RESTful.

---

## 🎯 Objetivo

Expor dados de produto via HTTP, com os seguintes campos:

- Título e descrição  
- Imagens  
- Preço (valor + moeda)  
- Estoque  
- ID do vendedor (referência cruzada para outro microserviço)  

---

## 🛠️ Stack utilizada

- **Linguagem:** Python 3.10+
- **Framework:** FastAPI
- **Validação de dados:** Pydantic
- **Testes:** Pytest
- **Cobertura mínima:** 80% (atualmente 96%)
- **Persistência simulada:** Arquivo JSON (`products.json`)
- **Documentação automática:** Swagger UI (`/docs`)

---

## 🗂 Estrutura de diretórios

```plaintext
ms-product-detail/
├── main.py                      # Ponto de entrada da aplicação FastAPI
├── app/
│   ├── controllers/             # Rotas da API (camada de apresentação)
│   │   └── product_controller.py
│   ├── domain/                  # Camada de domínio
│   │   ├── entities/            # Entidades (ex: Product, Price)
│   │   ├── interfaces/          # Contratos (ex: IProductRepository)
│   │   └── services/            # Regras de negócio (ex: ProductService)
│   ├── dtos/                    # Schemas Pydantic (entrada/saída de dados)
│   │   ├── product_schema.py
│   │   └── mapper.py            # Conversão entre entidades e DTOs
│   ├── infrastructure/
│   │   └── data/                # Repositórios concretos e dados simulados
│   │       ├── product_repository_json.py
│   │       └── products.json
│   ├── config/                  # Configurações da aplicação (ex: paths)
│   └── shared/                  # Utilitários e exceções
│       └── exceptions.py
├── tests/
│   ├── unit/                    # Testes de unidade (serviços, domínio, mapper)
│   │   └── test_product_service.py
│   │   └── test_mapper.py
│   └── integrations/            # Testes de API com TestClient
│       └── test_api_product.py
├── requirements.txt             # Dependências do projeto
├── pytest.ini                   # Configuração de testes e cobertura
└── README.md                    # Este documento
```