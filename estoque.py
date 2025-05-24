from datetime import datetime, timedelta

estoque = []
compras = []


def calcular_desconto(valor_total):
    desconto = valor_total * 0.05
    valor_com_desconto = valor_total - desconto
    return valor_com_desconto, desconto


def inserir_peca():
    produto = input("Nome da peça: ")
    qnt = int(input(f"Quantidade de {produto}: "))
    valor_peca = float(input(f"Valor unitário de {produto}: "))

    valor_com_desconto, desconto = calcular_desconto(valor_peca)

    peca = {
        "nome": produto,
        "quantidade": qnt,
        "valor": valor_peca,
        "valor_com_desconto": valor_com_desconto
    }

    estoque.append(peca)

    print("\n" + "-" * 30)
    print(f"{produto} foi cadastrado com sucesso!")
    print(f"Valor original: R$ {valor_peca:.2f}")
    print(f"Desconto aplicado (5%): R$ {desconto:.2f}")
    print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")
    print("\n" + "-" * 30)


def listar_pecas():
    if not estoque:
        print("Nenhuma peça cadastrada.")
    else:
        print("Lista de peças cadastradas:")
        for i, peca in enumerate(estoque):
            print(f"{i + 1}. {peca['nome']} - Quantidade: {peca['quantidade']} - "
                  f"Valor: R${peca['valor']:.2f} - Valor com desconto: R${peca['valor_com_desconto']:.2f}")


def editar_peca():
    listar_pecas()
    if estoque:
        try:
            indice = int(
                input("Digite o número da peça que deseja editar: ")) - 1
            if 0 <= indice < len(estoque):
                peca = estoque[indice]
                print(f"Editando {peca['nome']}")
                peca['nome'] = input("Novo nome da peça: ")
                peca['quantidade'] = int(
                    input(f"Nova quantidade de {peca['nome']}: "))
                novo_valor = float(
                    input(f"Novo valor unitário de {peca['nome']}: "))

                peca['valor'], desconto = calcular_desconto(novo_valor)
                peca['valor_com_desconto'] = novo_valor - desconto

                print(
                    f"Peça editada com sucesso! Novo valor com desconto: R${peca['valor_com_desconto']:.2f}")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def excluir_peca():
    listar_pecas()
    if estoque:
        try:
            indice = int(
                input("Digite o número da peça que deseja excluir: ")) - 1
            if 0 <= indice < len(estoque):
                peca = estoque.pop(indice)
                print(f"{peca['nome']} foi excluída com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def registrar_compra():
    nome_peca = input("Nome da peça: ")
    valor_compra = float(input("Valor da compra: R$ "))
    data_compra = datetime.now()

    compra = {
        "nome_peca": nome_peca,
        "valor_compra": valor_compra,
        "data_compra": data_compra
    }

    compras.append(compra)
    print(f"Compra de {nome_peca} registrada com sucesso!")


def calcular_porcentagem(valor, total):
    """Calcula a porcentagem que um valor representa do total"""
    if total == 0:
        return 0
    return (valor / total) * 100


def relatorio_compras(periodo):
    agora = datetime.now()
    compras_filtradas = []

    if periodo == "dia":
        inicio = agora.replace(hour=0, minute=0, second=0, microsecond=0)
        fim = inicio + timedelta(days=1)
        periodo_str = "hoje"
    elif periodo == "semana":
        inicio = agora - timedelta(days=agora.weekday())
        inicio = inicio.replace(hour=0, minute=0, second=0, microsecond=0)
        fim = inicio + timedelta(weeks=1)
        periodo_str = "esta semana"
    elif periodo == "mes":
        inicio = agora.replace(day=1, hour=0, minute=0,
                               second=0, microsecond=0)
        fim = (inicio + timedelta(days=32)).replace(day=1)
        periodo_str = "este mês"
    elif periodo == "ano":
        inicio = agora.replace(month=1, day=1, hour=0,
                               minute=0, second=0, microsecond=0)
        fim = inicio.replace(year=inicio.year + 1)
        periodo_str = "este ano"
    else:
        print("Período inválido.")
        return

    for compra in compras:
        if inicio <= compra["data_compra"] < fim:
            compras_filtradas.append(compra)

    total_brl = sum(compra["valor_compra"] for compra in compras_filtradas)

    print(f"\n--- Relatório de Compras {periodo_str.capitalize()} ---")
    print(f"Total de compras: {len(compras_filtradas)}")
    print(f"Total gasto: R$ {total_brl:.2f}")

    for compra in compras_filtradas:
        porcentagem = calcular_porcentagem(compra["valor_compra"], total_brl)
        print(f"Peça: {compra['nome_peca']} - Valor: R$ {compra['valor_compra']:.2f} - {porcentagem:.1f}% do total - Data: {compra['data_compra'].strftime('%d/%m/%Y %H:%M:%S')}")

    print("----------------------------")


def menu_relatorio():
    while True:
        print("\n--- Menu ---")
        print("1. Registrar nova compra")
        print("2. Relatório de compras do dia")
        print("3. Relatório de compras da semana")
        print("4. Relatório de compras do mês")
        print("5. Relatório de compras do ano")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_compra()
        elif opcao == "2":
            relatorio_compras("dia")
        elif opcao == "3":
            relatorio_compras("semana")
        elif opcao == "4":
            relatorio_compras("mes")
        elif opcao == "5":
            relatorio_compras("ano")
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_funcionario():
    while True:
        print("\n" + "-" * 30)
        print("---- Menu de Funcionário ----")
        print("1 - Cadastrar nova peça")
        print("2 - Alterar uma peça")
        print("3 - Excluir uma peça")
        print("4 - Mostrar peças cadastradas")
        print("5 - registrar uma nova compra")
        print("6 - relatorio de compras")
        print("7 - voltar ao menu principal")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            inserir_peca()
        elif opcao == "2":
            editar_peca()
        elif opcao == "3":
            excluir_peca()
        elif opcao == "4":
            listar_pecas()
        elif opcao == "5":
            registrar_compra()
        elif opcao == "6":
            menu_relatorio()
        elif opcao == "7":
            print("\nVoltando ao menu principal...")
            break
        else:
            print("\n -------> Vish! Opção inválida! Tente novamente.")


def menu_cliente():
    while True:
        print("\n" + "-" * 30)
        print("---- Menu de Cliente ----")
        print("1 - Visualizar peças disponíveis")
        print("2 - Simular compra")
        print("3 - Voltar ao menu principal")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            listar_pecas()
        elif opcao == "2":
            simular_compra()
        elif opcao == "3":
            print("\nVoltando ao menu principal...")
            break
        else:
            print("\n -------> Vish! Opção inválida! Tente novamente.")


def simular_compra():
    listar_pecas()
    if not estoque:
        print("Não há peças disponíveis para compra.")
        return

    try:
        indice = int(input("Digite o número da peça que deseja comprar: ")) - 1
        if 0 <= indice < len(estoque):
            peca = estoque[indice]
            quantidade_desejada = int(
                input(f"Quantas unidades de {peca['nome']} deseja comprar? "))

            if quantidade_desejada > peca['quantidade']:
                print("Quantidade indisponível no estoque.")
            else:
                total = quantidade_desejada * peca['valor_com_desconto']
                print("\n--- Resumo da Compra ---")
                print(f"Produto: {peca['nome']}")
                print(f"Quantidade: {quantidade_desejada}")
                print(
                    f"Valor unitário (com desconto): R$ {peca['valor_com_desconto']:.2f}")
                print(f"Total a pagar: R$ {total:.2f}")
                print("\nCompra simulada com sucesso! (Pagamento não processado)")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")


def menu_principal():
    while True:
        print("\n" + "-" * 30)
        print("---- Bem-vindo ao Sistema de Peças ----")
        print("1 - Entrar como Funcionário")
        print("2 - Entrar como Cliente")
        print("3 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            menu_funcionario()
        elif opcao == "2":
            menu_cliente()
        elif opcao == "3":
            print("\n[3] Você escolheu sair do programa. Adeus! :( ")
            break
        else:
            print("\n -------> Vish! Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu_principal()
