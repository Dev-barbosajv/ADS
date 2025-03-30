class App:
    def __init__(self):
        self.users_db = {"user@exemplo.com": "senha123", "admin@exemplo.com": "admin"}
        self.current_user = None
        self.login()
        self.run()

    def login(self):
        print("Sistema de Login")
        while True:
            email = input("Email: ")
            senha = input("Senha: ")
            if email in self.users_db and self.users_db[email] == senha:
                print("Login bem-sucedido!")
                self.current_user = email
                break
            else:
                print("Email ou senha inválidos. Tente novamente.")

    def run(self):
        while True:
            self.main_menu()

    def main_menu(self):
        print("\nMenu Principal")
        print("1. Opção 1")
        print("2. Opção 2")
        print("3. Opção 3")
        print("4. Opção 4")
        print("5. Opção 5")
        print("6. Opção 6")
        if self.current_user == "admin@exemplo.com":
            print("6. Cadastrar Novo Usuário (Admin)")
        print("0. Sair")

        choice = input("Escolha uma opção: ")
        if choice == "0":
            print("Saindo...")
            exit()
        elif choice in [str(i) for i in range(1, 6)]:
            self.sub_menu(choice)
        elif choice == "6" and self.current_user == "admin@exemplo.com":
            self.register_user()
        else:
            print("Opção inválida. Tente novamente.")
            self.register_user()

    def sub_menu(self, option):
        while True:
            print(f"\nSubmenu da Opção {option}")
            print("1. Subopção 1")
            print("2. Subopção 2")
            print("3. Subopção 3")
            print("0. Voltar")

            choice = input("Escolha uma subopção: ")
            if choice == "0":
                return
            elif choice in ["1", "2", "3"]:
                self.show_message(option, choice)
            else:
                print("Opção inválida. Tente novamente.")

    def show_message(self, option, sub_option):
        print(f"Você escolheu Opção {option} -> Subopção {sub_option}")

    def register_user(self):
        print("\nCadastro de Novo Usuário (Apenas Admin)")
        while True:
            email = input("Digite o email do novo usuário: ")
            if email in self.users_db:
                print("Este email já está cadastrado. Tente novamente.")
            else:
                senha = input("Digite a senha do novo usuário: ")
                self.users_db[email] = senha
                print("Usuário cadastrado com sucesso!")
                break


if __name__ == "__main__":
    App()