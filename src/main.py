import customtkinter as ctk
from tkinter import messagebox

from database.connection import inicializar_banco
from services.cliente_service import ClienteService
from services.produto_service import ProdutoService
from services.pedido_service import PedidoService

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gestão - v1.0")
        self.geometry("1000x700")

        inicializar_banco()

        self.service_cliente = ClienteService()
        self.service_produto = ProdutoService()
        self.service_pedido = PedidoService()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.label_menu = ctk.CTkLabel(self.sidebar, text="ESFIHARIA", font=ctk.CTkFont(size=18, weight="bold"))
        self.label_menu.pack(padx=20, pady=30)

        self.btn_pedidos = ctk.CTkButton(self.sidebar, text="Novo Pedido", command=self.aba_pedidos)
        self.btn_pedidos.pack(padx=20, pady=10)

        self.btn_produtos = ctk.CTkButton(self.sidebar, text="Gerenciar Produtos", command=self.aba_produtos)
        self.btn_produtos.pack(padx=20, pady=10)

        self.btn_clientes = ctk.CTkButton(self.sidebar, text="Gestão de Clientes", command=self.aba_clientes)
        self.btn_clientes.pack(padx=20, pady=10)

        self.conteudo = ctk.CTkFrame(self, corner_radius=10)
        self.conteudo.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        self.after(100, self.aba_pedidos)

    def limpar_tela(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

    # ================= TELA DE PEDIDOS =================
    def aba_pedidos(self):
        self.limpar_tela()
        self.carrinho = [] 
        
        self.conteudo.grid_columnconfigure(0, weight=1)
        self.conteudo.grid_columnconfigure(1, weight=1)

        frame_esq = ctk.CTkFrame(self.conteudo)
        frame_esq.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(frame_esq, text="1. Identificação", font=("Arial", 16, "bold")).pack(pady=5)
        
        self.tipo_pedido = ctk.CTkSegmentedButton(frame_esq, values=["Local", "Delivery"], command=self.ajustar_campos_pedido)
        self.tipo_pedido.set("Local")
        self.tipo_pedido.pack(pady=5)

        clientes_formatados = self.service_cliente.listar_para_exibicao()
        clientes_lista = [f"{c[0]} | {c[1]}" for c in clientes_formatados]
        
        self.combo_cli = ctk.CTkComboBox(frame_esq, values=["Avulso"] + clientes_lista, width=250)
        self.combo_cli.pack(pady=5)

        ctk.CTkButton(frame_esq, text="+ Cadastro Rápido", width=150, height=20, fg_color="transparent", border_width=1, command=self.popup_novo_cliente).pack()

        self.ent_identificacao = ctk.CTkEntry(frame_esq, placeholder_text="Nº da Mesa", width=250)
        self.ent_identificacao.pack(pady=10)

        ctk.CTkLabel(frame_esq, text="2. Adicionar Itens", font=("Arial", 16, "bold")).pack(pady=5)
        
        produtos = self.service_produto.listar_para_combo()
        self.select_prod = ctk.CTkComboBox(frame_esq, values=produtos, width=250)
        self.select_prod.pack(pady=5)
        
        ctk.CTkButton(frame_esq, text="Adicionar ao Pedido", fg_color="#1f538d", command=self.add_ao_carrinho).pack(pady=10)

        frame_dir = ctk.CTkFrame(self.conteudo, fg_color="#1a1a1a")
        frame_dir.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(frame_dir, text="Resumo do Pedido", font=("Arial", 18, "bold")).pack(pady=10)
        self.txt_resumo = ctk.CTkTextbox(frame_dir, width=300, height=300)
        self.txt_resumo.pack(pady=10, padx=10)
        
        self.lbl_total = ctk.CTkLabel(frame_dir, text="TOTAL: R$ 0.00", font=("Arial", 20, "bold"), text_color="yellow")
        self.lbl_total.pack(pady=10)

        ctk.CTkButton(frame_dir, text="FINALIZAR PEDIDO", fg_color="green", height=50, font=("Arial", 16, "bold"), command=self.finalizar_pedido).pack(pady=20, fill="x", padx=20)

    def ajustar_campos_pedido(self, valor):
        self.ent_identificacao.configure(placeholder_text="Endereço de Entrega" if valor == "Delivery" else "Número da Mesa")

    def add_ao_carrinho(self):
        escolha = self.select_prod.get()
        if "|" in escolha:
            nome = escolha.split(" | ")[0]
            preco = float(escolha.split("R$ ")[1])
            self.carrinho.append((nome, preco))
            self.atualizar_resumo()

    def atualizar_resumo(self):
        self.txt_resumo.delete("1.0", "end")
        total = sum(item[1] for item in self.carrinho)
        for item in self.carrinho:
            self.txt_resumo.insert("end", f"• {item[0]} - R$ {item[1]:.2f}\n")
        self.lbl_total.configure(text=f"TOTAL: R$ {total:.2f}")

    def finalizar_pedido(self):
        try:
            total = self.service_pedido.processar_e_salvar(
                ident=self.ent_identificacao.get(),
                carrinho=self.carrinho,
                tipo=self.tipo_pedido.get(),
                cliente=self.combo_cli.get()
            )
            messagebox.showinfo("Sucesso", f"Pedido de R$ {total:.2f} Finalizado!")
            self.aba_pedidos()
        except ValueError as e:
            messagebox.showwarning("Erro", str(e))

    def popup_novo_cliente(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Cadastro Rápido")
        popup.geometry("400x350")
        popup.attributes("-topmost", True)
        
        n = ctk.CTkEntry(popup, placeholder_text="Nome", width=250); n.pack(pady=5)
        t = ctk.CTkEntry(popup, placeholder_text="Telefone", width=250); t.pack(pady=5)
        e = ctk.CTkEntry(popup, placeholder_text="Endereço", width=250); e.pack(pady=5)

        def salvar():
            try:
                self.service_cliente.cadastrar(n.get(), t.get(), e.get())
                popup.destroy()
                self.aba_pedidos() 
            except ValueError as err:
                messagebox.showwarning("Atenção", str(err))

        ctk.CTkButton(popup, text="Salvar", command=salvar).pack(pady=10)

    # ================= TELA DE PRODUTOS =================
    def aba_produtos(self):
        self.limpar_tela()
        ctk.CTkLabel(self.conteudo, text="Gestão de Produtos", font=("Arial", 20, "bold")).pack(pady=10)

        f_cad = ctk.CTkFrame(self.conteudo)
        f_cad.pack(pady=10, padx=20, fill="x")
        
        self.ent_nome_p = ctk.CTkEntry(f_cad, placeholder_text="Nome do Produto", width=200)
        self.ent_nome_p.pack(side="left", padx=5, pady=10)
        
        self.ent_preco_p = ctk.CTkEntry(f_cad, placeholder_text="Preço", width=100)
        self.ent_preco_p.pack(side="left", padx=5)

        self.ent_cat_p = ctk.CTkOptionMenu(f_cad, values=["Comidas", "Bebidas", "Sobremesas"], width=120)
        self.ent_cat_p.pack(side="left", padx=5)

        ctk.CTkButton(f_cad, text="Salvar", width=100, fg_color="green", command=self.salvar_produto).pack(side="left", padx=10)

        self.scroll_prod = ctk.CTkScrollableFrame(self.conteudo, width=700, height=350)
        self.scroll_prod.pack(pady=10, padx=20, fill="both", expand=True)
        self.listar_produtos_ui()

    def salvar_produto(self):
        try:
            nome = self.ent_nome_p.get()
            preco = float(self.ent_preco_p.get().replace(",", "."))
            cat = self.ent_cat_p.get()
            
            self.service_produto.cadastrar_produto(nome, preco, cat)
            self.listar_produtos_ui()
            self.ent_nome_p.delete(0, 'end')
            self.ent_preco_p.delete(0, 'end')
        except ValueError:
            messagebox.showerror("Erro", "Preço ou nome inválido!")

    def listar_produtos_ui(self):
        for w in self.scroll_prod.winfo_children(): w.destroy()
        for p in self.service_produto.listar_todos_puros():
            f = ctk.CTkFrame(self.scroll_prod, fg_color="transparent")
            f.pack(fill="x", pady=2)
            ctk.CTkLabel(f, text=f"{p[1]} | R$ {p[2]:.2f} ({p[3]})").pack(side="left", padx=10)
            ctk.CTkButton(f, text="X", width=30, height=20, fg_color="red", command=lambda id=p[0]: self.del_produto(id)).pack(side="right", padx=10)

    def del_produto(self, id_p):
        if messagebox.askyesno("Excluir", "Deseja remover este produto?"):
            self.service_produto.excluir_produto(id_p)
            self.listar_produtos_ui()

    # ================= TELA DE CLIENTES =================
    def aba_clientes(self):
        self.limpar_tela()
        ctk.CTkLabel(self.conteudo, text="Gestão de Clientes", font=("Arial", 20, "bold")).pack(pady=10)

        f_cad = ctk.CTkFrame(self.conteudo)
        f_cad.pack(pady=10, padx=20, fill="x")
        
        self.c_nome = ctk.CTkEntry(f_cad, placeholder_text="Nome", width=180); self.c_nome.pack(side="left", padx=5, pady=10)
        self.c_tel = ctk.CTkEntry(f_cad, placeholder_text="Telefone", width=130); self.c_tel.pack(side="left", padx=5)
        self.c_end = ctk.CTkEntry(f_cad, placeholder_text="Endereço", width=200); self.c_end.pack(side="left", padx=5)

        ctk.CTkButton(f_cad, text="Cadastrar", width=100, fg_color="green", command=self.salvar_cliente).pack(side="left", padx=10)

        self.scroll_cli = ctk.CTkScrollableFrame(self.conteudo, width=700, height=350)
        self.scroll_cli.pack(pady=10, padx=20, fill="both", expand=True)
        self.listar_clientes_ui()

    def salvar_cliente(self):
        try:
            self.service_cliente.cadastrar(self.c_nome.get(), self.c_tel.get(), self.c_end.get())
            self.listar_clientes_ui()
            self.c_nome.delete(0, 'end'); self.c_tel.delete(0, 'end'); self.c_end.delete(0, 'end')
        except ValueError as e:
            messagebox.showwarning("Erro", str(e))

    def listar_clientes_ui(self):
        for w in self.scroll_cli.winfo_children(): w.destroy()
        for c in self.service_cliente.listar_para_exibicao():
            f = ctk.CTkFrame(self.scroll_cli, fg_color="transparent")
            f.pack(fill="x", pady=2)
            ctk.CTkLabel(f, text=f"{c[1]} - Tel: {c[2]}").pack(side="left", padx=10)
            ctk.CTkButton(f, text="X", width=30, height=20, fg_color="red", command=lambda id=c[0]: self.del_cliente(id)).pack(side="right", padx=10)

    def del_cliente(self, id_c):
        if messagebox.askyesno("Excluir", "Deseja remover este cliente?"):
            self.service_cliente.excluir_cliente(id_c)
            self.listar_clientes_ui()

if __name__ == "__main__":
    app = App()
    app.mainloop()