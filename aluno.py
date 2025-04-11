aluno = {
    "nome": "ana",
    "idade": "18",
    "curso": "engenharia da computação"
}
print(aluno['nome'])
print(aluno['idade'])
print(aluno['curso'])

aluno['matricula'] = "158251"
aluno['idade'] = "19"
print("Dados atualzados do aluno:")
for chave,valor in aluno.items():
  print(f"{chave} : {valor}")
