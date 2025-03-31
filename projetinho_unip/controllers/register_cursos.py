
class RegisterCursos:
    pass

    @staticmethod
    def cadastro_cursos():
        """Função para solicitar o cadastro de novos cursos."""
        print("=== Solicitar Cadastro de Cursos ===")
        curso_nome = input("Digite o nome do curso que deseja cadastrar: ").strip()
        if curso_nome:
            print(f"Solicitação de cadastro do curso '{curso_nome}' enviada com sucesso!")
        else:
            print("O nome do curso não pode estar vazio. Tente novamente.")