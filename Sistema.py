from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica, PessoaJuridica


def main():
    lista_pf=[]
    lista_pj=[]

    while True :
        opcao = int(input("Escolha uma opção: 1 - Pessoa fisica / 2 - Pessoa Juridica / 0 - Sair "))
        
        if opcao == 1:
            while True:
                opcao_pf = int(input("Escolha uma opção : 1 - cadastrar Pessoa Fisica / 2 - Listar Pessoa fisica / 3 - Remover pessoa fisica"))

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

                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome}")
                            print(f"Cpf: {cada_pf.cpf}")
                            print(f"Endereço: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}" )
                            print(f"imposto a ser pago:{cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            int(input("Digite 0 para sair"))

                    else: 
                        print("Opção inválida, por favor digite uma das opções inidicadas: ")
                elif opcao_pf == 3:
                 cpf_remover =   int(input("Digite o CPF da pessoa que deseja remover"))
                 for cada_pf in lista_pf:
                    if cada_pf.cpf == cpf_remover:
                        lista_pf.remove(cada_pf)
                        pessoa_encontrada = True
                        print("Pessoa fisica removida!")
                        
                        break

                    if not pessoa_encontrada:
                        print("Nenhuma pessoa encontrada!")
        elif opcao == 2: 
            while True:
                opcao_pj = int(input("Escolha uma opção : 1 - cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Remover pessoa Juridica / 4 - Editar lista"))

                if opcao_pj ==1:
                    novapj = PessoaJuridica()
                    novo_end_pj = Endereco()

                    novapj.nome= input("Digite o nome da pessoa Juridica: ")
                    novapj.cnpj = input("Digite o cnpj: ")
                    novapj.rendimento = float(input("Digite o rendimento mensal (somente numeros)"))

                    novo_end_pj.logradouro = input("Digite o logradouro: ")
                    novo_end_pj.numero = input("Digite o numero: ")
                    end_comercial = input("Este endereço é comercial? S ou N: ")
                    novo_end_pj.endereco_Comercial = end_comercial.strip().upper() =="S"

                    novapj.endereco = novo_end_pj

                    lista_pj.append(novapj)

                    print("Cadastro realizado com sucesso")

                    #LISTAR PESSOA JURIDICA

                elif opcao_pj == 2:
                    if lista_pj:
                        for cada_pj in lista_pj:
                            print(f"Nome {novapj.nome}")
                            print(f"CNPJ {novapj.cnpj}")
                            print(f"Endereço {novapj.endereco.logradouro}, {novapj.endereco.numero}")
                            print(f"imposto a ser pago: {novapj.calcular_imposto,{novapj.rendimento}}")
                            int(input("Digite 0 para sair"))

                elif opcao_pj==3:
                    cnpj_remover =int(input("Digite o cnpj que deseja que seja removido "))
                    for cada_pj in lista_pf:
                        if cada_pj.cpf == cnpj_remover:
                            lista_pj.remove(cada_pj)
                            pessoa_encontrada = True
                            print("Pessoa fisica removida!")
                        
                            break

                    if not pessoa_encontrada:
                        print("Nenhuma pessoa encontrada!")
                elif opcao_pj == 4:
                    cnpj_atualizado = int(input("Digite o novo cnpj: "))
                    for cada_pj in lista_pj:
                        if cnpj_atualizado == cada_pj.cnpj:
                            cada_pj.cnpj = cnpj_atualizado
                            print("CNPJ atualizado")
        elif opcao == 0:
            print("Obrigado por utilizar o nome sistema! Valeu!")
            break
        else: 
            print("Opção inválida, por favor digite uma das opções válidas!")

if __name__ == "__main__":
    main()
                            
