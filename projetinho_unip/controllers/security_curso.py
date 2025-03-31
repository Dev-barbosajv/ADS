

class SecurityCurso:
    def __init__(self, security1):
        self.security1 = security1()
    
    def security(self):
        while True:
            """Função para exibir informações de segurança (LGPD)."""
            print("=== Informações de Segurança (LGPD) ===")
            print("\n")
            print("Este sistema respeita a Lei Geral de Proteção de Dados (LGPD).")
            print("Seus dados pessoais estão protegidos e não serão compartilhados sem sua autorização.")
            print("Para mais informações, consulte nossa política de privacidade.")
            print("Caso tenha alguma dúvida, entre em contato com o suporte.")
            print("\n")
            print("=== Fim das Informações de Segurança (LGPD) ===")
            print("1. Próxima página")
            print("0. Voltar ao Menu Principal")
            escolha = input("Escolha uma opção: ").strip()
            if escolha == "1":
                self.security1()
            elif escolha == "0":
                print("Voltando ao Menu Principal...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def security1(self):
        while True:
            """Função para exibir informações de segurança (LGPD) - Página 1."""
            print("=== Informações de Segurança (LGPD) - Página 1 ===")
            print("\n")
            print("A segurança de dados é essencial para proteger informações pessoais e acadêmicas em plataformas educacionais. \nA LGPD (Lei Geral de Proteção de Dados) regula o uso de dados pessoais, garantindo direitos como acesso, correção e exclusão de informações.")
            print("A LGPD exige que plataformas adotem medidas de segurança, como criptografia e controle de acesso, para proteger os dados dos usuários. \nEssas práticas ajudam a criar um ambiente digital mais seguro e confiável.")
            print("Boas práticas incluem o uso de senhas fortes, autenticação de dois fatores (2FA) e evitar o compartilhamento de credenciais. \nAlém disso, é importante estar ciente de como os dados são coletados, armazenados e utilizados pelas instituições.")
            print("A segurança de dados é uma responsabilidade compartilhada entre usuários e instituições. \nMantenha-se informado sobre as melhores práticas e proteja suas informações pessoais.")
            print("Cuidado com ataques de phishing, evitando clicar em links suspeitos. Sempre faça logout em dispositivos compartilhados \ne leia as políticas de privacidade antes de aceitar termos.")
            print("\n")
            print("=== Fim das Informações de Segurança (LGPD) - Página 1 ===")
            print("0. Voltar ao Menu Principal")
            escolha = input("Escolha uma opção: ").strip()
            if escolha == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")