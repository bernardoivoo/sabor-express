from components.cardapio.sobremesa import Sobremesa
from components.restaurantes import Restaurantes
from components.restaurante import Restaurante
from components.sabor_express import SaborExpress
from components.avaliacao_restaurante import AvaliacaoRestaurante
from components.cardapio.prato import Prato
import pytest

@pytest.fixture
def sabor_express_object_fixture():
    sabor_express_mock = SaborExpress()
    sabor_express_mock._restaurantes = Restaurantes({
            "restaurants": [
                {
                    "name": "restaurante 1",
                    "category": "tradicional",
                    "menu": [
                        {
                            "Item": "Item 1",
                            "Price": 5,
                            "Description": "An item 1"
                        },
                        {
                            "Item": "Item 2",
                            "Price": 10,
                            "Description": "An item 2"
                        },
                        {
                            "Item": "Item 1",
                            "Price": 6,
                            "Description": "An item 3"
                        }
                    ],
                    "ratings": {
                        "average": 3,
                        "individual_ratings": [
                            {
                                "rating": 3,
                                "description": "Don't like it that much"
                            }
                        ]
                    }
                },
                {
                    "name": "restaurante 2",
                    "category": "tradicional",
                    "menu": [
                        {
                            "Item": "Item 1",
                            "Price": 5,
                            "Description": "An item 1"
                        },
                        {
                            "Item": "Item 2",
                            "Price": 10,
                            "Description": "An item 2"
                        },
                        {
                            "Item": "Item 1",
                            "Price": 6,
                            "Description": "An item 3"
                        }
                    ],
                    "ratings": {
                        "average": 3,
                        "individual_ratings": [
                            {
                                "rating": 3,
                                "description": "Don't like it that much"
                            }
                        ]
                    }
                }
            ]
        })
    
    return sabor_express_mock

@pytest.fixture
def sobremesa_fixture():
    return Sobremesa(
        nome="Sorvete",
        preco=100,
        tipo="Gelados",
        tamanho="500ml"
    )

@pytest.fixture
def prato_fixture():
    """
    Cria um objeto Prato com preço de 100 para facilitar
    o cálculo do desconto.
    """
    return Prato(
        nome="Prato Teste",
        preco=100.0,
        descricao="Um prato para teste"
    )

@pytest.fixture
def sabor_express_vazio_fixture():
    """
    Cria uma instância de SaborExpress, mas com a lista
    interna de restaurantes vazia.
    """
    sabor_express_mock = SaborExpress()
    
    # Simula o objeto Restaurantes com uma lista vazia
    sabor_express_mock._restaurantes = Restaurantes({"restaurants": []}) 
    
    return sabor_express_mock

@pytest.fixture
def restaurante_fixture():
    """
    Cria uma instância de Restaurante isolada para testes unitários
    desta classe.
    """
    # 1. Dados mockados para as avaliações
    mock_avaliacoes_data = {
        "average": 4.5,
        "individual_ratings": [
            {"rating": 5, "description": "Otimo"},
            {"rating": 4, "description": "Bom"}
        ]
    }
    
    # 2. Dados mockados para o cardápio (do tipo Prato)
    mock_cardapio_data = [
        {
            "Item": "Prato Teste Unico",
            "Price": 25,
            "Description": "Descricao do prato teste"
        }
    ]

    # 3. A própria classe Restaurante processa os dados no __init__
    restaurante = Restaurante(
        nome="Restaurante Isolado",
        categoria="Teste Unitario",
        cardapio=mock_cardapio_data,
        avaliacoes=mock_avaliacoes_data
    )
    
    return restaurante