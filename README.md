# 🍽️ Sistema de Gestão de Restaurantes

Sistema completo para gerenciamento de restaurantes, focado em eficiência, organização de pedidos e controle operacional.

Desenvolvido com boas práticas de arquitetura e Design Patterns modernos, garantindo um código limpo, escalável e de fácil manutenção.

---

## 🚀 Funcionalidades

### 📦 Gestão de Pedidos

* Registro de pedidos para consumo local (mesa)
* Registro de pedidos para delivery
* Cálculo automático de totais

### 🍕 Catálogo de Produtos

* Cadastro de produtos
* Edição e exclusão de itens
* Organização por categorias
* Controle de preços

### 👥 Controle de Clientes

* Cadastro rápido de clientes
* Histórico de pedidos (delivery)
* Organização de dados para atendimento ágil

### 📊 Resumo de Vendas

* Visualização de pedidos realizados
* Totais calculados automaticamente
* Histórico de vendas

---

## 🏗️ Arquitetura do Projeto

O sistema segue uma **arquitetura em camadas**, separando responsabilidades e facilitando manutenção e testes:

### 🔹 View (Interface)

* Construída com **CustomTkinter**
* Responsável pela interação com o usuário

### 🔹 Service Layer

* Contém as regras de negócio
* Validação de dados
* Cálculo de totais
* Formatação das informações

### 🔹 Repository Layer

* Responsável pelo acesso ao banco de dados
* Execução de operações CRUD
* Abstração das queries SQL

### 🔹 Database

* Gerenciamento da conexão com **SQLite**
* Inicialização do banco

---

## 📁 Estrutura de Pastas

```plaintext
src/
├── database/        # Conexão e inicialização do SQLite
├── repositories/    # Queries SQL (CRUD)
├── services/        # Regras de negócio e validações
├── assets/          # Imagens e ícones (futuro)
└── main.py          # Ponto de entrada do sistema
```

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Interface Gráfica:** CustomTkinter
* **Banco de Dados:** SQLite

---

## ⚙️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/gerenciamento-restaurantes.git
```

### 2. Acesse o diretório do projeto

```bash
cd gerenciamento-restaurantes
```

### 3. Instale as dependências

```bash
pip install customtkinter
```

### 4. Execute o sistema

```bash
python src/main.py
```

---

## 📈 Roadmap

O projeto está em evolução contínua. Próximas funcionalidades:

* [ ] 📊 Relatórios financeiros com gráficos
* [ ] 🧾 Impressão de cupons (impressora térmica 80mm)
* [ ] 🔐 Sistema de login (Garçom / Administrador)
* [ ] 📲 Integração com WhatsApp (confirmação de pedidos)

---

## 🤝 Contribuição

Contribuições são muito bem-vindas!

1. Faça um **Fork** do projeto
2. Crie uma branch:

   ```bash
   git checkout -b feature/NovaFeature
   ```
3. Commit suas alterações:

   ```bash
   git commit -m "Adicionando nova funcionalidade"
   ```
4. Envie para o repositório:

   ```bash
   git push origin feature/NovaFeature
   ```
5. Abra um **Pull Request**

---

## 👨‍💻 Autor

Desenvolvido por **Lucas**

---

## 📄 Licença

Este projeto está sob a licença MIT.
Sinta-se livre para usar, modificar e contribuir.

---
