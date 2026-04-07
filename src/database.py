import sqlite3

def conectar():
    return sqlite3.connect('sistema_restaurante.db')

def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()
    # Tabela de Produtos
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, 
        preco REAL NOT NULL, categoria TEXT)''')
    
    # Tabela de Pedidos
    cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, identificacao TEXT, 
        itens TEXT, total REAL, tipo TEXT, cliente_info TEXT, 
        data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP, status TEXT DEFAULT 'Pendente')''')

    # Tabela de Clientes
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, 
        telefone TEXT, endereco TEXT)''')
    
    conn.commit()
    conn.close()

# --- FUNÇÕES PRODUTOS ---
def adicionar_produto(nome, preco, categoria):
    conn = conectar(); cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco, categoria) VALUES (?,?,?)", (nome, preco, categoria))
    conn.commit(); conn.close()

def listar_produtos():
    conn = conectar(); cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos"); dados = cursor.fetchall()
    conn.close(); return dados

# --- FUNÇÕES CLIENTES ---
def adicionar_cliente(nome, telefone, endereco):
    conn = conectar(); cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, telefone, endereco) VALUES (?,?,?)", (nome, telefone, endereco))
    conn.commit(); conn.close()

def listar_clientes():
    conn = conectar(); cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes"); dados = cursor.fetchall()
    conn.close(); return dados

# --- FUNÇÕES PEDIDOS ---
def salvar_pedido(identificacao, itens, total, tipo, cliente_info):
    conn = conectar(); cursor = conn.cursor()
    cursor.execute("INSERT INTO pedidos (identificacao, itens, total, tipo, cliente_info) VALUES (?,?,?,?,?)",
                   (identificacao, itens, total, tipo, cliente_info))
    conn.commit(); conn.close()

if __name__ == "__main__":
    inicializar_banco()