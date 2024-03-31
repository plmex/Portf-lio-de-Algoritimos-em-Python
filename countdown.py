from rich.console import Console
from rich.prompt import Prompt
from time import sleep


console = Console()
while True:
    tempo = input('Digite o tempo (em segundos): ')

    if tempo.isdigit():
        tempo = int(tempo)
        break
    else:
        console.print('Entrada inválida! Por favor, insira um número inteiro.')

"""
Se o valor de entrada for divisível por 60, a 
função retorna um único valor inteiro. No entanto, 
se o valor não for divisível por 60, a função retorna dois valores inteiros, 
representando as partes inteira e fracionária do resultado da divisão.
"""

while tempo > 0:
    minutos, segundos = divmod(tempo, 60)
    timer = "{:02d}:{:02d}".format(minutos, segundos)
    console.print(timer, end="\r")
    sleep(1)
    tempo -= 1

console.print('[red]O TEMPO ACABOU![/red]')