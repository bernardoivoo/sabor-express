from .fixtures import restaurante_fixture

def test_exibir_cardapio_restaurante_isolado(restaurante_fixture, capsys):
    """
    Testa a property 'exibir_cardapio' da classe Restaurante.
    
    Verifica se os itens do cardápio (definidos na fixture)
    são impressos corretamente no console.
    """
    # --- ARRANGE (Preparação) ---
    restaurante = restaurante_fixture # Pega o restaurante da nova fixture
    
    # --- ACT (Ação) ---
    # Acessamos a property, que vai executar o print
    restaurante.exibir_cardapio

    # --- ASSERT (Verificação) ---
    # Capturamos o que foi impresso
    captured = capsys.readouterr()
    output = captured.out

    # Verificamos se o título e o item da fixture estão na saída
    assert "Cardapio do restaurante Restaurante Isolado" in output
    assert "1. Nome: Prato Teste Unico" in output
    assert "R$25" in output
    assert "Descrição: Descricao do prato teste" in output
