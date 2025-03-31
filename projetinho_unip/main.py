from controllers import ListarCursos
from controllers import Login
from controllers import RegisterCursos
from controllers import RegisterUsers
from controllers import SecurityCurso
from controllers import Cursos
import os

def main():

    usuario_logado = "amind"
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
        RegisterUsers.cadastrar_usuario()
    elif escolha == "3":
        Login.esqueci_senha()
    elif escolha == "0":
        print("Saindo...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
    
    if escolha == "3":
        exit()

        
    print("=== Menu Principal ===")
    print("1. Menu de Cursos Disponíveis")
    print("2. Solicitar Cadastro de Cursos")
    print("3. Último Curso Assistido")
    print("4. Informações de Segurança ( LGPD)")
    print("0. Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        ListarCursos.menu_cursos()
        print("Menu de Cursos Disponíveis")
    elif escolha == "2":
        RegisterCursos.cadastro_cursos()
    elif escolha == "3":
        Cursos.ultimo_curso_assistido()
    elif escolha == "4":
        SecurityCurso.ecurity()
    elif escolha == "0":
        print("Saindo...")
        exit()


if __name__ == "__main__":
    main()