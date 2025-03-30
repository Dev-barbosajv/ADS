

"""

    ========================= Comentarios =========================
    "O código abaixo é um exemplo de um menu simples em Python.
    Ele utiliza funções para organizar o código e criar um menu interativo.

    Funções explicadas:

    def define uma função de utilização unica para aquela unica variavel
    while cria um laço infinito, onde ele não para até que uma condição seja atendida"




"""

# Variável global para armazenar o login do usuário
usuario_logado = None

def login():
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

def cadastrar_usuario():
        """Função para informar sobre o processo de cadastro de um novo usuário."""
        print("=== Cadastro de Novo Usuário ===")
        print("Por gentileza, buscar a secretaria ou seu representante imediato para solicitar o registro de teu acesso.")

def esqueci_senha():
    """Função para lidar com a recuperação de senha.
    Utilizei apenas a """
    print("=== Recuperação de Senha ===")
    ra = input("Digite seu ra cadastrado: ").strip()
    if ra:
        print(f"O administrador foi acionado para realizar o reset da senha do RA: {ra}.")
    else:
        print("Este RA não está cadastrado. Tente novamente. \nCaso não tenha cadastro, entre em contato com o suporte.")

def login():
    """Função para realizar o login do usuário."""
    global usuario_logado
    while not usuario_logado:
        print("=== Página de Login ===")
        print("1. Fazer Login")
        print("2. Cadastrar Novo Usuário")
        print("3. Esqueci a Senha")
        print("0. Sair")
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            usuario_logado = input("Digite seu login: ").strip()
            if not usuario_logado:
                print("O login não pode estar vazio. Tente novamente.")
            else:
                print(f"Bem-vindo, {usuario_logado}!")
        elif escolha == "2":
            cadastrar_usuario()
        elif escolha == "3":
            esqueci_senha()
        elif escolha == "0":
            print("Saindo...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")

def menu_cursos():
    """Função para exibir o submenu de cursos disponíveis."""
    while True:
        print("\n=== Menu de Cursos Disponíveis ===")
        print("1. Listar Todos os Cursos")
        print("2. Buscar Curso por Nome")
        print("3. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            print("Listando todos os cursos disponíveis...")
            # Adicione a lógica para listar os cursos aqui
        elif escolha == "2":
            curso_nome = input("Digite o nome do curso que deseja buscar: ").strip()
            print(f"Buscando informações sobre o curso: {curso_nome}...")
            # Adicione a lógica para buscar o curso aqui
        elif escolha == "3":
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastro_cursos():
    """Função para solicitar o cadastro de novos cursos."""
    print("=== Solicitar Cadastro de Cursos ===")
    curso_nome = input("Digite o nome do curso que deseja cadastrar: ").strip()
    if curso_nome:
        print(f"Solicitação de cadastro do curso '{curso_nome}' enviada com sucesso!")
    else:
        print("O nome do curso não pode estar vazio. Tente novamente.")

def ultimo_curso_assistido():
    """Função para exibir o último curso assistido."""
    print("=== Último Curso Assistido ===")
    # Aqui você pode adicionar a lógica para exibir o último curso assistido
    print("Nenhum curso assistido registrado.")



def menu():
    """Função para exibir o menu principal."""
    global usuario_logado
    print(f"\nUsuário logado: {usuario_logado}")
    print("=== Menu Principal ===")
    print("1. Menu de Cursos Disponíveis")
    print("2. Solicitar Cadastro de Cursos")
    print("3. Último Curso Assistido")
    print("4. Informações de Segurança ( LGPD)")
    print("0. Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        menu_cursos()
        print("Menu de Cursos Disponíveis")
        # Aqui você pode adicionar a lógica para exibir os cursos disponíveis
    elif escolha == "2":
        cadastro_cursos()
        # Aqui você pode adicionar a lógica para solicitar o cadastro de cursos
    elif escolha == "3":
        print("Último Curso Assistido")
        # Aqui você pode adicionar a lógica para exibir o último curso assistido
    elif escolha == "4":
        print("Informações de Segurança (LGPD)")
        # Aqui você pode adicionar a lógica para exibir informações de segurança
    elif escolha == "0":
        print("Saindo...")
        exit()
    

def main():
    """Função principal que controla o fluxo do programa."""
    login()  # Exibe a página de login primeiro
    while True:
        menu()  # Exibe o menu após o login

if __name__ == "__main__":
    main()


# Este código tem como objetivo demonstrar um menu simples em Python.
# Atividade NP1 da faculdade UNIP, curso ADS 1° Semestre 2025.
# O código pode ser melhorado e expandido conforme necessário.
# Adicionei comentários para explicar as funções e o fluxo do programa.
# Código adpatado conforme fui aprendendo e testando.
# Código não foi 100% original, fui acompanhando aulas, videos e outros materiais.
# O código é apenas um exemplo e pode ser melhorado.