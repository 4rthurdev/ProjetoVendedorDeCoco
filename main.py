import datetime

# Classe para o vendedor e seu negócio


class VendedorCoco:
    def __init__(self, nome, preco_por_coco):
        self.nome = nome
        self.preco_por_coco = preco_por_coco
        self.estoque = 0
        self.vendas = []
        self.total_vendas = 0.0

    def adicionar_estoque(self, quantidade):
        """Adiciona cocos ao estoque"""
        self.estoque += quantidade
        print(f"{quantidade} cocos adicionados ao estoque. Estoque atual é: {self.estoque} cocos.")

    def registrar_venda(self, quantidade):
        """Registra uma venda, e desconta do estoque"""
        if quantidade > self.estoque:
            print("Estoque insuficiente para realizar essa venda.")
        else:
            self.estoque -= quantidade
            valor_venda = quantidade * self.preco_por_coco
            self.vendas.append({
                'data': datetime.datetime.now(),
                'quantidade': quantidade,
                'valor': valor_venda
            })
            self.total_vendas += valor_venda
            print(
                f"Venda registrada: {quantidade} cocos vendidos por R$ {valor_venda:.2f}. "
                f"Estoque restante: {self.estoque} cocos.")

    def gerar_relatorio_mensal(self):
        """Gera um relatório de vendas do mês atual"""
        mes_atual = datetime.datetime.now().month
        vendas_mes = [venda for venda in self.vendas if venda['data'].month == mes_atual]

        if not vendas_mes:
            print("Nenhuma venda registrada este mês.")
            return

        print(f"\nRelatório de vendas - Mês {mes_atual}:")
        total_quantidade = sum(venda['quantidade'] for venda in vendas_mes)
        total_valor = sum(venda['valor'] for venda in vendas_mes)
        print(f"Total de cocos vendidos: {total_quantidade}")
        print(f"Total arrecadado: R$ {total_valor:.2f}")
        print(f"Estoque atual: {self.estoque} cocos.\n")


# Exemplo de uso do sistema
if __name__ == "__main__":
    # Criando o vendedor com preço de R$ 3 por coco
    vendedor = VendedorCoco(nome="João", preco_por_coco=3.0)

    # Adiciona cocos ao estoque
    vendedor.adicionar_estoque(30)

    # Registra as vendas
    vendedor.registrar_venda(15)
    vendedor.registrar_venda(8)

    # Se tentar vender mais cocos do que tem em estoque
    vendedor.registrar_venda(40)

    # Gera o relatório do mês
    vendedor.gerar_relatorio_mensal()
