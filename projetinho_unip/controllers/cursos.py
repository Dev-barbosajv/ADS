from .listar_cursos import ListarCursos

class Cursos:
    def __init__(self):
        pass


    def menu_cursos(self):
        """Função para exibir o submenu de cursos disponíveis."""
        while True:
            print("\n=== Menu de Cursos Disponíveis ===")
            print("1. Listar Todos os Cursos")
            print("2. Buscar Curso por Nome")
            print("0. Voltar ao Menu Principal")
            escolha = input("Escolha uma opção: ").strip()
            if escolha == "1":
                print("Listando todos os cursos disponíveis...")
                ListarCursos.listar_cursos()
            elif escolha == "2":
                curso_nome = input("Digite o nome do curso que deseja buscar: ").strip()
                print(f"Buscando informações sobre o curso: {curso_nome}...")
            elif escolha == "0":
                print("Voltando ao Menu Principal...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    

    def cadastro_cursos(self):
        """Função para solicitar o cadastro de novos cursos."""
        print("=== Solicitar Cadastro de Cursos ===")
        curso_nome = input("Digite o nome do curso que deseja cadastrar: ").strip()
        if curso_nome:
            print(f"Solicitação de cadastro do curso '{curso_nome}' enviada com sucesso!")
        else:
            print("O nome do curso não pode estar vazio. Tente novamente.")

    def ultimo_curso_assistido(self):
        """Função para exibir o último curso assistido."""
        print("=== Último Curso Assistido ===")
        print("Nenhum curso assistido registrado.")

    
    