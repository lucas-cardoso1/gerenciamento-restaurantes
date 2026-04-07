from repository.cliente_repository import ClienteRepository

class ClienteService:
    def __init__(self):
        self.repo = ClienteRepository()

    def cadastrar(self, nome, telefone, endereco):
        nome = nome.strip()
        telefone = telefone.strip()
        
        if not nome:
            raise ValueError("O nome do cliente é obrigatório!")
        
        if len(telefone) < 8:
            raise ValueError("O telefone informado é muito curto!")

        self.repo.adicionar(nome, telefone, endereco)

    def listar_para_exibicao(self):
        return self.repo.listar()

    def filtrar_clientes_por_nome(self, termo):
        todos = self.repo.listar()
        return [c for c in todos if termo.lower() in c[1].lower()]

    def excluir_cliente(self, id_cliente):
        self.repo.deletar(id_cliente)