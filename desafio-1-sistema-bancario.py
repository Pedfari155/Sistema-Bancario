menu = """
[1] - Depositar 
[2] - Sacar 
[3] - Extrato 
[0] - Sair
=> """ 

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3 

while True: 

  opcao = input(menu)

  if opcao == "1":
    valor = float(input("Informe o valor a ser Depositado : "))    
    if valor <= 0:
      print("Valor inválido")
      continue
    else: 
      print(f"Seu saldo anterior é {saldo}")
      saldo += valor
      extrato += f"O deposito foi de R$ {valor:.2f} \n"
      print(f"Seu novo saldo é {saldo}")
  
  elif opcao == "2":
    valor = float(input("Informe o valor a ser Sacado : "))
    if valor <= 0:
      print("Valor inválido")
      continue
    elif valor > 500:
      print(f"Valor superior ao limite de saque. \n Seu limite de saque é {limite}")
      continue
    
    elif valor > saldo:
      print("Saldo insuficiente")
      continue
    
    else: 
      if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques excedido")
        continue 
    numero_saques += 1 
    saldo -= valor 
    extrato += f"O Saque foi de R$ {valor:.2f} \n"
    print(f"Seu novo saldo é {saldo}")
  
  elif opcao == "3":
    print(f"Extrato \n {extrato}")
    
  elif opcao == "0":
    break 
    
  else:
    print("Operação Invalida , Por favor selecione novamente a operação desejada")
