from .fixtures import sabor_express_object_fixture
import json
import pytest   

def teste_escolher_restaurante(sabor_express_object_fixture):
    sabor_express = sabor_express_object_fixture
    restaurante_escolhido = sabor_express.escolher_restaurante(1)

    assert restaurante_escolhido._nome == "Restaurante 1"

def teste_escolher_pedido(sabor_express_object_fixture):
    sabor_express = sabor_express_object_fixture
    restaurante_escolhido = sabor_express.escolher_restaurante(1)

    pedido_escolhido = sabor_express.escolher_pedido(restaurante_escolhido, 1)

    assert pedido_escolhido._nome == "Item 1"

#
# 👇 A NOVA FUNÇÃO COMEÇA AQUI, NO NÍVEL CORRETO (sem indentação)
#
def test_avaliar_pedido_registra_nota_e_calcula_media(sabor_express_object_fixture, monkeypatch, capsys):
    """
    Testa se o método avaliar_pedido:
    1. Registra corretamente a nova nota e comentário.
    2. Recalcula e atualiza a média de avaliações do restaurante.
    """
    # --- ARRANGE (Preparação) ---
    app = sabor_express_object_fixture
    
    nota_teste = "5"
    comentario_teste = "Perfeito!"
    inputs_simulados = iter([nota_teste, comentario_teste])

    # Substitui o 'input()' e o 'json.dump' para não rodar de verdade
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_simulados))
    
    monkeypatch.setattr('json.dump', lambda *args, **kwargs: None)

    idx_restaurante = 0 # "restaurante 1"
    
    # Pegamos o estado ANTES da ação
    restaurante_avaliado = app._restaurantes._lista_de_restaurantes[idx_restaurante]
    media_antiga = restaurante_avaliado._avaliacoes.media
    
    # Verificamos o estado inicial (garantia da fixture)
    assert media_antiga == 3
    assert len(restaurante_avaliado._avaliacoes.avaliacoes_individuais) == 1

    # --- ACT (Ação) ---
    app.avaliar_pedido(idx_restaurante)

    # --- ASSERT (Verificação) ---
    
    # 1. Testamos se a nova avaliação foi adicionada (ISSO VAI PASSAR)
    ultima_avaliacao = restaurante_avaliado._avaliacoes.avaliacoes_individuais[-1]
    assert ultima_avaliacao['rating'] == int(nota_teste)
    assert ultima_avaliacao['description'] == comentario_teste

    # 2. Testamos se a mensagem de sucesso foi impressa (ISSO VAI PASSAR)
    captured = capsys.readouterr()
    assert "Obrigado pela avaliação!" in captured.out
    
    # 3. Testamos se a média foi recalculada (ISSO VAI FALHAR)
    # Comportamento Esperado: (3 (antiga) + 5 (nova)) / 2 = 4.0
    media_esperada = 4.0
    media_atual = restaurante_avaliado._avaliacoes.media
    
    # Este 'assert' vai falhar, pois 'media_atual' será 3 (o bug)
    # e 'media_esperada' é 4.0
    assert media_atual == media_esperada


def test_calcular_preco_sem_desconto(sabor_express_object_fixture, capsys):
    """
    Testa o método calcular_preco quando o usuário responde 'N'
    para o desconto. O preço não deve mudar.
    """
    # --- ARRANGE (Preparação) ---
    app = sabor_express_object_fixture
    
    # Pegamos o Restaurante 1 e o Pedido 1 (Item 1, Preço 5)
    restaurante_escolhido = app.escolher_restaurante(1)
    pedido_escolhido = app.escolher_pedido(restaurante_escolhido, 1)
    
    # Verificamos o preço original do item
    assert pedido_escolhido._preco == 5
    
    # Definimos a resposta do usuário
    tem_desconto = "N"

    # --- ACT (Ação) ---
    app.calcular_preco(pedido_escolhido, tem_desconto)
    
    # --- ASSERT (Verificação) ---
    
    # 1. Verificamos se o preço do objeto NÃO mudou
    assert pedido_escolhido._preco == 5
    
    # 2. Verificamos se o print() está correto
    captured = capsys.readouterr()
    assert "O pedido ficou por 5.00" in captured.out


def test_calcular_preco_com_desconto(sabor_express_object_fixture, capsys):
    """
    Testa o método calcular_preco quando o usuário responde 'S'
    para o desconto. O preço deve ser atualizado.
    
    (Nota: O 'Item 1' é um Prato, então o desconto é de 5%)
    """
    app = sabor_express_object_fixture
    
    # Pegamos o Restaurante 1 e o Pedido 1 (Item 1, Preço 5)
    restaurante_escolhido = app.escolher_restaurante(1)
    # Nota: Este pedido é um 'Prato', pois não tem 'tipo' na fixture
    pedido_escolhido = app.escolher_pedido(restaurante_escolhido, 1)
    
    # Verificamos o preço original
    assert pedido_escolhido._preco == 5
    
    # Definimos a resposta do usuário
    tem_desconto = "S"

    app.calcular_preco(pedido_escolhido, tem_desconto)
    # 1. Verificamos se o preço do objeto FOI atualizado
    # O 'Item 1' é um Prato (desconto de 5%)
    # Preço esperado: 5 - (5 * 0.05) = 4.75
    assert pedido_escolhido._preco == 4.75
    
    # 2. Verificamos se o print() reflete o novo preço
    captured = capsys.readouterr()
    assert "O pedido ficou por 4.75" in captured.out

def test_lista_restaurantes_sao_exibidos_corretamente(sabor_express_object_fixture, monkeypatch, capsys):
    app = sabor_express_object_fixture
    
    # 1. Vamos mockar o 'input' para que ele levante uma exceção
    #    Isso vai PARAR o método 'iniciar_interface_de_pedidos'
    #    imediatamente após ele listar os restaurantes e tentar pedir o input.
    def mock_input_que_para(prompt_do_input):
        # A 'prompt_do_input' é a string dentro do input, ex: "Restaurante escolhido: "
        # Verificamos se é o input que esperamos
        if "Restaurante escolhido" in prompt_do_input:
            raise StopIteration("Parada de teste controlada")
        
        # (Não devemos chegar aqui neste teste)
        return "" 

    monkeypatch.setattr('builtins.input', mock_input_que_para)

    # --- ACT (Ação) ---
    # Usamos 'pytest.raises' para 'capturar' a exceção StopIteration
    # que nós mesmos criamos. Isso é esperado, e impede o teste de falhar.
    with pytest.raises(StopIteration):
        app.iniciar_interface_de_pedidos()

    # --- ASSERT (Verificação) ---
    # Agora, verificamos o que foi impresso ANTES da exceção parar a função
    captured = capsys.readouterr()
    output_do_print = captured.out
    
    # Verificamos se a lista foi impressa como esperado
    assert "Digite o número do restaurante" in output_do_print
    assert "1 - Restaurante 1" in output_do_print
    assert "2 - Restaurante 2" in output_do_print

    
def test_escolher_pedido_inexistente_levanta_erro(sabor_express_object_fixture):
    """
    Testa se o método 'escolher_pedido' levanta um IndexError
    se um índice inválido (um pedido que não existe) for usado.
    """
    # --- ARRANGE (Preparação) ---
    app = sabor_express_object_fixture
    
    # Pegamos o Restaurante 1 (que tem 3 itens no cardápio, índices 0, 1, 2)
    restaurante_escolhido = app.escolher_restaurante(1)
    
    # Definimos um índice que com certeza não existe
    indice_do_pedido_inexistente = 99

    # --- ACT & ASSERT (Ação e Verificação) ---
    
    # Verificamos se o código DENTRO do 'with' levanta um IndexError
    # Se o IndexError acontecer, o teste PASSA.
    # Se não acontecer (ou outro erro acontecer), o teste FALHA.
    with pytest.raises(IndexError):
        app.escolher_pedido(restaurante_escolhido, indice_do_pedido_inexistente)