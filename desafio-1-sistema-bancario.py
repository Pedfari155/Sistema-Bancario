import textwrap

def menu():
  menu = """\n 
                    Bem vindo ao Banco do Brasil 
  ============================ M E N U ============================
  [1] \t Depositar
  [2] \t Sacar
  [3] \t Extrato 
  [4] \t Novo Usuario 
  [5] \t Listar Contas
  [6] \t Cadastrar conta
  [0] \t Sair 
  """     
  return input(textwrap.dedent(menu))
def depositar(saldo, valor, extrato, /):
  if valor > 0:
    saldo += valor
    extrato += f"Deposito: \t R${valor:.2f} \n"
    print("\n Deposito Realizado com Sucesso \n")
  else:
    print("\n Valor incorreto \n")

  return saldo, extrato  
def sacar(*, saldo, valor ,extrato, limite, numero_saques, limite_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques >= limite_saques

  if excedeu_saldo:
    print("Saldo insuficiente")
  elif excedeu_limite: 
    print("Excedeu valor limite diario")
  elif excedeu_saques:
    print("Excedeu a quantidade de saques diarios")

  elif valor > 0: 
    saldo -= valor
    extrato += f"Saque:\t \t R${valor:.2f} \n"
    numero_saques += 1 
    print("Saque realizado com sucesso")

  else:
    
    print("Operação falhou")

  return saldo, extrato
def exibir_extrato(saldo, /, *, extrato):
  print(f"Saldo: R${saldo:.2f}")
  print("Extrato: \n", extrato)
def criar_usuarios(usuarios):
  cpf = input("Informe o CPF: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario: 
      print("\n Já existe um usuário com esse CPF")
      return

  nome = input("Informe o nome completo: ")
  data_nascimento = input("Informe a data de nascimento: ")
  endereco = input("Informe o endereço: ")

  usuarios.append({"Nome": nome, "Data de Nascimento": data_nascimento, "Endereco": endereco, "CPF": cpf})

  print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
  return usuarios_filtrados[0]  if usuarios_filtrados  else None
def criar_conta(AGENCIA, numero_conta, usuarios):
  cpf = input("Informe o CPF do usuário:")
  usuario = filtrar_usuario(cpf, usuarios)
  
  if usuario: 
      print("\n Conta criada com sucesso!")
      return {"AGENCIA": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
  else:
      print("Usuário não encontrado, fluxo de criação encerrado")

def listar_conta(contas):
  for conta in contas:
      if 'AGENCIA' in conta and 'numero_conta' in conta and 'usuario' in conta:
          linha = f"""\
          Agencia:\t{conta['AGENCIA']}
          Numero da conta:{conta['numero_conta']}
          Titular:\t{conta['usuario']['Nome']}
          """
          print("=" * 100)
          print(textwrap.dedent(linha))
      else:
          print("Erro: Chave ausente no dicionário de conta.")

def main():
            LIMITE_SAQUES = 3 
            AGENCIA = 1 
            saldo = 0 
            limite = 500
            extrato = ""
            numero_saques = 0 
            usuarios = []
            contas = []

            while True: 
                opcao = menu()

                if opcao == '1':
                    valor = float(input("Informe o valor do depósito: "))
                    saldo, extrato = depositar(saldo, valor, extrato)

                elif opcao == '2':
                    valor = float(input("Informe o valor do saque: "))
                    saldo, extrato = sacar(
                        saldo=saldo,
                        valor=valor,
                        extrato=extrato,
                        limite=limite,
                        numero_saques=numero_saques,
                        limite_saques=LIMITE_SAQUES
                    )

                elif opcao == '3':
                    exibir_extrato(saldo, extrato=extrato)

                elif opcao == '4': 
                    criar_usuarios(usuarios)

                elif opcao == '5':
                    listar_conta(contas)

                elif opcao == '6':
                    numero_conta = len(contas) + 1 
                    conta = criar_conta(AGENCIA, numero_conta, usuarios)

                    if conta:
                        contas.append(conta)

                elif opcao == '0':
                    break

                else:
                    print("Opção inválida")

      


main ()





