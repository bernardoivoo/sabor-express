from .fixtures import bebida_fixture

def test_aplicar_desconto_bebida(bebida_fixture):
    """
    Testa se o método aplicar_desconto da classe Bebida
    aplica corretamente o desconto de 8%.
    """
    # --- ARRANGE (Preparação) ---
    # 'bebida_fixture' nos dá a bebida com preço 100.0
    bebida = bebida_fixture
    
    # --- ACT (Ação) ---
    # Chama o método que queremos testar
    bebida.aplicar_desconto()
    
    # --- ASSERT (Verificação) ---
    # Comportamento esperado: 100.0 - (100.0 * 0.08) = 92.0
    assert bebida._preco == 92.0