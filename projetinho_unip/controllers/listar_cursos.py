

class ListarCursos:
    def __init__(self):
        pass

    @staticmethod
    def menu_cursos():
        """Função para listar todos os cursos disponíveis."""
        while True:
            print("\n=== Listar Todos os Cursos ===")
            print("1. Curso de Python")
            print("2. Curso de Algoritimos")
            print("3. Cybersecurity")
            print("4. Desenvolvimento Web")
            print("0. Voltar ao Menu Principal")
            escolha = input("Escolha uma opção: ").strip()
            if escolha == "1":
                print("Curso de Python: Aprenda a programar em Python do básico ao avançado.")
            elif escolha == "2":
                print("Curso de Algoritimos: Entenda os fundamentos dos algoritmos e estruturas de dados.")
            elif escolha == "3":
                print("Curso de Cybersecurity: Aprenda sobre segurança cibernética e proteção de dados.")
            elif escolha == "4":
                print("Curso de Desenvolvimento Web: Crie sites e aplicações web do zero.")
            elif escolha == "0":
                print("Voltando ao Menu Principal...")
                break
            else:
                print("Opção inválida. Tente novamente.")