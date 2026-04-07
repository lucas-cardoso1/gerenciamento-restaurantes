from repository.produto_repository import ProdutoRepository

class ProdutoService:
    def __init__(self):
        self.repo = ProdutoRepository()

    def cadastrar_produto(self, nome, preco, categoria):
        if not nome or preco <= 0:
            raise ValueError("Dados do produto inválidos!")
        self.repo.adicionar(nome, preco, categoria)

    def listar_para_combo(self):
        produtos = self.repo.listar()
        return [f"{p[1]} | R$ {p[2]:.2f}" for p in produtos]

    def listar_todos_puros(self):
        return self.repo.listar()

    def excluir_produto(self, id_produto):
        self.repo.deletar(id_produto)