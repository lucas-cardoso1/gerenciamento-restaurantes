from .base_repository import BaseRepository

class PedidoRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def salvar_novo(self, identificacao, itens, total, tipo, cliente):
        sql = """
            INSERT INTO pedidos (identificacao, itens, total, tipo, cliente)
            VALUES (?, ?, ?, ?, ?)
        """
        self.query(sql, (identificacao, itens, total, tipo, cliente))

    def listar_todos(self):
        sql = "SELECT * FROM pedidos ORDER BY data DESC"
        return self.fetch_all(sql)

    def buscar_por_data(self, data_inicio, data_fim):
        sql = "SELECT * FROM pedidos WHERE data BETWEEN ? AND ?"
        return self.fetch_all(sql, (data_inicio, data_fim))

    def calcular_faturamento_diario(self):
        sql = "SELECT SUM(total) FROM pedidos WHERE date(data) = date('now')"
        resultado = self.fetch_all(sql)
        return resultado[0][0] if resultado[0][0] else 0.0

    def deletar_pedido(self, id_pedido):
        sql = "DELETE FROM pedidos WHERE id = ?"
        self.query(sql, (id_pedido,))