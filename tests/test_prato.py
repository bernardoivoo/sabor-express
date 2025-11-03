from .fixtures import prato_fixture

def test_aplicar_desconto_prato(prato_fixture):
    """
    Testa se o método aplicar_desconto da classe Prato
    aplica corretamente o desconto de 5%.
    """
    # 'prato_fixture' nos dá o prato com preço 100.0
    prato = prato_fixture
    
    # Chama o método que queremos testar
    prato.aplicar_desconto()
    
    # Comportamento esperado: 100.0 - (100.0 * 0.05) = 95.0
    # O 'assert' verifica se o resultado é o esperado [cite: 88]
    assert prato._preco == 95.0