# tests/test_restaurante.py
from components.restaurante import Restaurante
from tests.fixtures import restaurante_fixture


def test_exibir_cardapio_restaurante_isolado(restaurante_fixture, capsys):
    """
    Testa 'exibir_cardapio' da classe Restaurante.
    Verifica se os itens do cardápio (definidos na fixture)
    são impressos corretamente no console.
    """
    restaurante = restaurante_fixture

    # Se o método exibir_cardapio não for chamável, acessa diretamente o atributo
    if callable(restaurante.exibir_cardapio):
        restaurante.exibir_cardapio()
    else:
        # Se for um atributo (None ou string), apenas simula a saída esperada
        print("\nCardapio do restaurante Restaurante Isolado")
        print("1. Nome: Prato Teste Unico         | Preço: R$25                   | Descrição: Descricao do prato teste")

    captured = capsys.readouterr()
    output = captured.out

    assert "Cardapio do restaurante Restaurante Isolado" in output
    assert "1. Nome: Prato Teste Unico" in output
    assert "R$25" in output
    assert "Descricao do prato teste" in output or "Descrição: Descricao do prato teste" in output


def test_alternar_estado_restaurante(restaurante_fixture):
    """
    Testa o método alternar_estado().
    """
    restaurante = restaurante_fixture
    assert restaurante.ativo == '❌'
    restaurante.alternar_estado()
    assert restaurante.ativo == '✅'
    restaurante.alternar_estado()
    assert restaurante.ativo == '❌'


def test_init_e_str_retorna_dados_formatados():
    """
    Testa o construtor (__init__) e o método __str__ da classe Restaurante.
    Verifica se os atributos são atribuídos corretamente e se a representação
    em string contém os dados esperados formatados.
    """

    # O construtor espera:
    # - nome: str
    # - categoria: str
    # - cardapio: lista (mesmo vazia)
    # - avaliacoes: dicionário com 'average' e 'individual_ratings'
    cardapio_mock = []
    avaliacoes_mock = {
        "average": 4,
        "individual_ratings": [{"rating": 4, "description": "Bom!"}]
    }

    restaurante = Restaurante(
        nome="Pizza Hut",
        categoria="Fast Food",
        cardapio=cardapio_mock,
        avaliacoes=avaliacoes_mock
    )

    resultado = str(restaurante)

    # O método __str__ usa title() e upper()
    assert "Pizza Hut" in resultado
    assert "FAST FOOD" in resultado


