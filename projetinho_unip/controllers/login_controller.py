
class Login:
    def __init__(self):
        pass

    def login(self):
        """Função para realizar o login do usuário.
        Exibe a página de login e solicita o nome do usuário até que ele seja fornecido.
        também foi criado uma variavel para sempre que o usuario logar, o nome dele ser armazenado na variavel usuario_logado"""
        global usuario_logado
        print("=== Página de Login ===")
        while not usuario_logado:
            usuario_logado = input("Digite seu login: ").strip()
            if not usuario_logado:
                print("O login não pode estar vazio. Tente novamente.")
        print(f"Bem-vindo, {usuario_logado}!")

    
    def esqueci_senha():
        """Função para lidar com a recuperação de senha.
        Utilizei apenas a """
        print("=== Recuperação de Senha ===")
        ra = input("Digite seu ra cadastrado: ").strip()
        if ra:
            print(f"O administrador foi acionado para realizar o reset da senha do RA: {ra}.")
        else:
            print("Este RA não está cadastrado. Tente novamente. \nCaso não tenha cadastro, entre em contato com o suporte.")