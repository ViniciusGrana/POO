from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica


def main():
    lista_pf=[]
    

    while True :
        opcao = int(input("Escolha uma opção: 1 - Pessoa fisica / 2 - Pessoa Juridica / 0 - Sair"))

        if opcao == 1:
            while True:
                opcao_pf = int(input("Escolha uma opção : 1 - cadastrar Pessoa Fisica / 2 - Listar Pessoa fisica / 3 - Voltar ao menu anterior"))

                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome= input("Digite o nome da pessoa fisica: ")
                    novapf.cpf = input("Digite o CPF: ")
                    novapf.rendimento = float(input("Digite o rendimento mensal (somente numeros)"))

                    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa)")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
                    idade = (date.today() - novapf.dataNascimento).days //365

                    if idade >= 18:
                        print("A pessoa é maior idade! ")
                    else:
                        print("A pessoa tem menos de 18 anos. Retornando ao menu...")
                        continue
                novo_end_pf.logradouro = input("Digite o logradouro: ")
                novo_end_pf.numero = input("Digite o numero: ")
                end_comercial = input("Este endereço é comercial? S ou N: ")
                novo_end_pf.endereco_Comercial = end_comercial.strip().upper() =="S"

                novapf.endereco = novo_end_pf

                lista_pf.append(novapf)

                print("Cadastro realizado com sucesso")

            #listar pessoa fisica
        elif opcao_pf == 2:
            if lista_pf:
                for cada_pf in lista_pf:
                    print(f"Nome: {cada_pf.nome}")
                    print(f"Cpf: {cada_pf.cpf}")
                    print(f"Endereço: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}" )
                    print(f"Data Nascimento: {cada_pf.data_Nascimento.strftime('%d/%m/%Y')}")
                    print(f"imposto a ser pago:{cada_pf.calcular_imposto(cada_pf.rendimento)}")
                    print("Digite 0 para sair")
            else: 
                    print("Opção inválida, por favor digite uma das opções inidicadas: ")
        elif opcao == 2: 
            pass
        elif opcao == 0:
            print("Obrigado por utilizar o nome sistema! Valeu!")
            break
        else: 
            print("Opção inválida, por favor digite uma das opções válidas!")

if __name__ == "__main__":
    main()
                            
