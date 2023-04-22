print("=" * 30)
print("{:^30}".format(" TABUADA "))
print("=" * 30)
while True:
        print("." * 30)
        escolhe = int(input("""Selecione um número para sinais
[ 1 ] + Soma 
[ 2 ] - Subtração
[ 3 ] * Multiplicação
[ 4 ] / Divisão
[ 5 ] Fechar: """))
        if escolhe == 1:
            numero = int(input("Digite um número: "))
            for a in range(1, 11):
                print(f"{a} + {numero} = {a + numero}")
        if escolhe == 2:
            numero = int(input("Digite um número: "))
            for a in range(1, 11):
                print(f"{a} - {numero} = {a - numero}")
        if escolhe == 3:
            numero = int(input("Digite um número: "))
            for a in range(1, 11):
                print(f"{a} * {numero} = {a * numero}")
        if escolhe == 4:
            numero = int(input("Digite um número: "))
            for a in range(1, 11):
                print(f"{a} / {numero} = {a / numero:^.1f}")
        if escolhe == 5:
            break
print("="*30)    
print("{:^30}".format("OBRIGADO VOLTE SEMPRE!"))
print("="*30)
