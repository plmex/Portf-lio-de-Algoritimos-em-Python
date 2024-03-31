from rich.console import Console

console = Console()
string = input('Digite uma palavra ou frase: ')
string = string.replace(" ", "").lower()

if string == string[::-1]:
    console.print('[green]É UM PALÍNDROMO.[/green]')
else:
    console.print('[red]NÃO É UM PALÍNDROMO.[/red]')