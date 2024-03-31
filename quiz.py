from rich.console import Console
from rich.prompt import Prompt
from random import sample
from time import sleep

#Lendo o arquivo de perguntas

def reading_questions(questions):
    perguntas = []
    with open(questions, 'r', encoding='utf-8') as arquivo:
       perguntas_do_arquivo = arquivo.read().split('\n\n')

       for question in perguntas_do_arquivo:
           lines = question.strip().split('\n')
           pergunta = lines[0].split('#')[1].strip() # Coletando cada pergunta 
           opcoes_resposta = [opcao.strip() for opcao in lines[1:-1]] # Coletando as opções de resposta
           resposta = lines[-1].split(':')[1].strip() # Coletando a resposta correta
           perguntas.append({"pergunta":pergunta, "opcoes_resposta":opcoes_resposta, "respostas":resposta})
    return perguntas


questoes = reading_questions("questions.txt")
perguntas_aleatorias = sample(list(questoes),5)

console = Console()

saudacao = "Seja muito bem-vindo(a) ao quiz!"
print('='*len(saudacao))
print(saudacao)
print('='*len(saudacao))
nome = str(input('Informe o nick name: '))
print(f'{nome}, você deseja jogar? Digite S para sim e N para não.')
answerUser = str(input('Opção: ')).upper()[0]

contador = 0
if answerUser not in "SN":
    while answerUser not in "SN":
        console.print('Opção inválida! Tente novamente.')
        console.print(f'{nome}, você deseja jogar? Digite S para sim e N para não.')
        answerUser = str(input('Opção: ')).upper()[0]
elif answerUser == 'N':
    quit()
elif answerUser == 'S':
    for questao in perguntas_aleatorias:
        console.print(questao["pergunta"])
        for opcoes in questao["opcoes_resposta"]:
            console.print(opcoes)
        questionAnswer = Prompt.ask('Sua resposta (a,b,c,d)').lower()


        #Verificando as respostas
        if questionAnswer == questao["respostas"].split(')')[0].strip().lower():
            console.print("Sua resposta está [green]correta[/green]!\n")
        else:
            console.print("Sua resposta está [red]incorreta[/red]!\n")
        contador += 1
        if contador < 4:
            console.print('Prepare-se! A próxima pergunta vem aí!')
            sleep(3)
        if contador == 4:
            console.print('Prepare-se! A última pergunta já está chegando!')
            sleep(3)

console.print("Fim do Quiz!")