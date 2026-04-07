# gerenciamento-restaurantes
📝 Sistema de Gestão de Restaurantees
Este é um sistema de gerenciamento de restaurantes focado em eficiência e organização de pedidos (Mesa e Delivery), cadastro de produtos e controle de clientes.

O projeto foi desenvolvido aplicando Design Patterns modernos para garantir que o código seja limpo, testável e fácil de manter.

🚀 Funcionalidades
📦 Gestão de Pedidos: Registro de vendas para consumo local ou entrega.

🍕 Catálogo de Produtos: Cadastro, edição e exclusão de itens com categorias e preços.

👥 Controle de Clientes: Cadastro rápido e histórico de clientes para delivery.

📊 Resumo de Vendas: Cálculo automático de totais e histórico de pedidos.

🏗️ Arquitetura do Projeto (Design Patterns)
O sistema utiliza a arquitetura em camadas para separar as responsabilidades:

View (Main): Interface gráfica construída com CustomTkinter.

Service Layer: Onde residem as regras de negócio. Responsável por validar dados, calcular totais e formatar informações antes de chegarem à tela.

Repository Layer: Responsável exclusiva pela comunicação com o banco de dados SQL. Abstrai as queries complexas.

Database: Camada de infraestrutura que gerencia a conexão com o SQLite.

Estrutura de Pastas:
Plaintext
src/
├── database/      # Conexão e inicialização do SQLite
├── repositories/  # Queries SQL (CRUD)
├── services/      # Regras de negócio e validações
├── assets/        # Imagens e ícones (futuro)
└── main.py        # Ponto de entrada do sistema
🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Interface Gráfica: CustomTkinter

Banco de Dados: SQLite (nativo Python)

⚙️ Como Executar
Clone o repositório:

Bash
git clone https://github.com/seu-usuario/gerenciamento-restaurantes.git
Instale as dependências:

Bash
pip install customtkinter
Inicie o sistema:

Bash
python src/main.py
📈 Roadmap de Evolução
Este projeto está em constante evolução. Próximas melhorias planejadas:

[ ] Relatórios Financeiros: Geração de gráficos de faturamento mensal.

[ ] Impressão de Cupom: Integração com impressoras térmicas 80mm.

[ ] Sistema de Login: Diferenciação entre Garçom e Administrador.

[ ] Notificação WhatsApp: Envio automático de confirmação de pedido.

🤝 Contribuição
Contribuições são sempre bem-vindas!

Faça um Fork do projeto.

Crie uma Branch para sua Feature (git checkout -b feature/NovaFeature).

Dê um Commit nas suas alterações (git commit -m 'Adicionando nova funcionalidade X').

Dê um Push na Branch (git push origin feature/NovaFeature).

Abra um Pull Request.

Desenvolvido por [Lucas]