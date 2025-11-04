from .fixtures import restaurante_fixture

def test_exibir_cardapio_restaurante_isolado(restaurante_fixture, capsys):
    """
    Testa 'exibir_cardapio' da classe Restaurante.
    Verifica se os itens do cardápio (definidos na fixture)
    são impressos corretamente no console.
    """

    restaurante = restaurante_fixture

    restaurante.exibir_cardapio


    captured = capsys.readouterr()
    output = captured.out

    # Verificamos se o título e o item da fixture estão na saída
    assert "Cardapio do restaurante Restaurante Isolado" in output
    assert "1. Nome: Prato Teste Unico" in output
    assert "R$25" in output
    assert "Descrição: Descricao do prato teste" in output

def test_alternar_estado_restaurante(restaurante_fixture):
    """
    Testa o método alternar_estado().
    """
    
    restaurante = restaurante_fixture
    

    # Verificamos o estado padrão (definido no __init__ da classe Restaurante)
    # A property 'ativo' retorna o emoji.
    assert restaurante.ativo == '❌'
    
    # --- ACT 1 (Ativando) ---
    restaurante.alternar_estado()
    
    # --- ASSERT 2 (Estado Ativado) ---
    assert restaurante.ativo == '✅'
    
    # --- ACT 2 (Desativando) ---
    restaurante.alternar_estado()
    
    # --- ASSERT 3 (Estado Desativado) ---
    assert restaurante.ativo == '❌'