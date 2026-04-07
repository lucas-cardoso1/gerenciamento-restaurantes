from .base_repository import BaseRepository

class ProdutoRepository(BaseRepository):
    def adicionar(self, nome, preco, categoria):
        sql = "INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)"
        self.query(sql, (nome, preco, categoria))

    def listar(self):
        return self.fetch_all("SELECT * FROM produtos ORDER BY categoria, nome")

    def deletar(self, id_produto):
        self.query("DELETE FROM produtos WHERE id = ?", (id_produto,))