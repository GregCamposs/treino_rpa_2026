lote_estoque = [25, 80, "Produto_fora_de_linha", 150, "Estoque_negativo_erro", 10, 45]
for item in lote_estoque:
    if item == "Estoque_negativo_erro":
        print("Erro crítico no estoque! Parando o robô...")
    elif item == "Produto_fora_de_linha":
        print(f"Produto fora de linha!")
    elif item > 100:
        print(f"Pedido de {item} un. enviado para a gerência.")
    else:
        print(f"Pedido de {item} un. liberado")
