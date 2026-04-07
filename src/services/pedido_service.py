from repository.pedido_repository import PedidoRepository

class PedidoService:
    def __init__(self):
        self.repo = PedidoRepository()

    def processar_e_salvar(self, ident, carrinho, tipo, cliente):
        if not carrinho:
            raise ValueError("O carrinho está vazio!")
            
        itens_nomes = [item[0] for item in carrinho]
        itens_str = ", ".join(itens_nomes)
        total = sum(item[1] for item in carrinho)
        
        self.repo.salvar_novo(ident, itens_str, total, tipo, cliente)
        
        return total