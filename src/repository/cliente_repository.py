from .base_repository import BaseRepository

class ClienteRepository(BaseRepository):
    def adicionar(self, nome, telefone, endereco):
        sql = "INSERT INTO clientes (nome, telefone, endereco) VALUES (?, ?, ?)"
        self.query(sql, (nome, telefone, endereco))

    def listar(self):
        return self.fetch_all("SELECT * FROM clientes ORDER BY nome")

    def deletar(self, id_cliente):
        self.query("DELETE FROM clientes WHERE id = ?", (id_cliente,))