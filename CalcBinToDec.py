# Calculadora que converte números binários em decimais e vice-versa

def transformaBinParaDec():
    DecFinal = 0
    expoente = 0
    Bin = int(input('''
    Digite um número em binário:
    '''))
    NumeroBinario = Bin
    while Bin != 0:
        resto = Bin % 10
        Bin = Bin // 10
        Dec = resto * (2 ** expoente)
        expoente = expoente + 1
        DecFinal = DecFinal + Dec
    print('''
   ''',NumeroBinario,'''em decimal é''',DecFinal,'''
    ''')
    chama = main()

def transformaDecParaBin():
    BinFinal = 0
    expoente = 0
    Dec = int(input('''
    Digite um número em decimal:
    '''))
    NumeroDecimal = Dec
    while Dec != 0:
        resto = Dec % 2
        Dec = Dec // 2
        Bin = resto * (10 ** expoente)
        expoente = expoente + 1
        BinFinal = BinFinal + Bin
    print('''
   ''',NumeroDecimal,'''em binário é''',BinFinal,'''
    ''')
    chama = main()
    
def main():
    opcao = int(input('''
    Bem vindo a Calculadora de Conversão de binário para decimal e vice-versa!
    
    Se você quer transformar Binário em Decimal, digite 1. 
    Se quer o contrário, digite 2. 
    Se quer sair do programa, digite 3.
    Qual sua opção? 1, 2 ou 3?
    '''))
    if opcao == 1:
        chama = transformaBinParaDec()
    elif opcao == 2:
        chama = transformaDecParaBin()
    elif opcao == 3:
        print('''
    A Calculadora de Conversão será encerrada.
        ''')
    else:
        print('''
    Opção inválida.
        
    Você será redirecionado para o início do programa.
    ''')
        chama = main()

inicializador = main()