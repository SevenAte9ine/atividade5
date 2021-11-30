pilha = []
while True:
  pilhainput = input("Esta pilha aceita 3 valores. Se um quarto valor for inserido, ela começará a remover todos. Insira um valor para adicionar na pilha: ")
  pilha.append(pilhainput)
  print(pilha)
  if len(pilha) > 3:
    print("Valor removido: ", pilha.pop())
    print("Valor removido: ", pilha.pop())
    print("Valor removido: ", pilha.pop())
    print("Valor removido: ", pilha.pop())
    print("Valores removidos da pilha.")
    print(pilha)