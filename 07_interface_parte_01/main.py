import classes
import os

if __name__ == "__main__":
    usuario = classes.PessoaFisica("", "", "", "", "", "")
    empresa = classes.PessoaJuridica("", "", "", "", "", "")

    def banner():
        base_dir = os.path.dirname(os.path.abspath(__file__))
        caminho_banner = os.path.join(base_dir, "ascii", "banner.txt")

        try:
            with open(caminho_banner, "r", encoding="utf-8") as f:
                print(f.read())
        except FileNotFoundError:
            print("[ERRO] Arquivo banner.txt não encontrado")

    while True:
        banner()
        print("")
        print('-'*24, "Inserir Dados", '-'*24)
        print("[1] Inserir dados de usuário")
        print("[2] Inserir dados de empresa")
        print("[3] Exibir dados")
        print("[4] Sair do programa")
        print('-'*67)
        print("")

        choose = input("Escolha uma Opção >_  ").strip()

        match choose:
            case "1":
                os.system("cls" if os.name == "nt" else "clear")
                print('-'*24, "Inserindo dados de Usuário", '-'*24)
                print("")
                usuario.nome = input("Digite o nome: ").strip()
                usuario.cpf = input("Digite o CPF: ").strip()
                usuario.profissao = input("Informe o Profissão: ").strip()
                usuario.email = input("Informe o Email: ").strip()
                usuario.endereco = input("Informe o Endereço: ").strip()
                usuario.telefone = input("Digite o Número de Telefone: ").strip()
                print('-'*67)
                print("")
                print("Empresa Cadastrada...")
                input("Pressione enter para continuar...")
                os.system("cls" if os.name == "nt" else "clear")
                continue
            case "2":
                os.system("cls" if os.name == "nt" else "clear")
                print('-'*24, "Inserindo dados de Empresa", '-'*24)
                print("")
                empresa.razao_social = input("Digite a Razão Social: ").strip()
                empresa.nome_fantasia = input("Digite o Nome Fantasia: ").strip()
                empresa.cnpj = input("Informe o CNPJ: ").strip()
                empresa.email = input("Informe o Email: ").strip()
                empresa.endereco = input("Informe o Endereço: ").strip()
                empresa.telefone = input("Digite o Número de Telefone: ").strip()
                print('-'*67)
                print("")
                print("Empresa Cadastrada...")
                input("Pressione enter para continuar...")
                os.system("cls" if os.name == "nt" else "clear")
                continue
            case "3":
                os.system("cls" if os.name == "nt" else "clear")
                if usuario.nome != "" and empresa.nome_fantasia != "":
                    print('-'*24, "Dados de Usuário", '-'*24)
                    usuario.exibir_dados()
                    print('-'*67)
                    print('-'*24, "Dados de Empresa", '-'*24)
                    empresa.exibir_dados()
                    print('-'*67)
                elif usuario.nome == "" and empresa.nome_fantasia != "":
                    print('-'*24, "Dados Empresa", '-'*24)
                    empresa.exibir_dados()
                    print('-'*67)
                elif usuario.nome != "" and empresa.nome_fantasia == "":
                    print('-'*24, "Dados Empresa", '-'*24)
                    usuario.exibir_dados()
                    print('-'*67)
                input("Aperte enter para continuar...")
                os.system("cls" if os.name == "nt" else "clear")
                continue

            case "4":
                os.system("cls" if os.name == "nt" else "clear")
                break
            case _:
                input("Opção Inválida. Pressione Enter para continuar...")
                os.system("cls" if os.name == "nt" else "clear")
                continue