print('Vamos jogar!')
print('Pedra / Papel / Tesoura')
print()
jogador_1 = input('Jogador 1, Digite seu nome: ')
jogador_2 = input('Jogador 2, Digite seu nome: ')
print()
while True:
    escolha_j1 = input(f'{jogador_1} -> Pedra / Papel / Tesoura ? ').upper()
    escolha_j2 = input(f'{jogador_2} -> Pedra / Papel / Tesoura ? ').upper()
    while escolha_j1 == escolha_j2:
        print(f'< {escolha_j1} X {escolha_j2} > EMPATOU, VAMOS NOVAMENTE')
        print()
        escolha_j1 = input(f'{jogador_1} -> Pedra / Papel / Tesoura ? ').upper()
        escolha_j2 = input(f'{jogador_2} -> Pedra / Papel / Tesoura ? ').upper()
    if escolha_j1 == 'PEDRA' and escolha_j2 == 'TESOURA':
        print(f'< {escolha_j1} X {escolha_j2} >  < {escolha_j1} quebra a {escolha_j2} > O VENCEDOR FOI: {jogador_1} !')
    elif escolha_j1 == 'PEDRA' and escolha_j2 == 'PAPEL':
        print(f'< {escolha_j1} X {escolha_j2} >  < {escolha_j2} embrulha a {escolha_j1} > O VENCEDOR FOI: {jogador_2} !')
    elif escolha_j1 == 'TESOURA' and escolha_j2 == 'PEDRA':
        print(f'< {escolha_j1} X {escolha_j2} >  < {escolha_j2} quebra a {escolha_j1} > O VENCEDOR FOI: {jogador_2} !')
    elif escolha_j1 == 'TESOURA' and escolha_j2 == 'PAPEL':
        print(f'< {escolha_j1} X {escolha_j2} >  < {escolha_j1} corta o {escolha_j2} > O VENCEDOR FOI: {jogador_1} !')
    elif escolha_j1 == 'PAPEL' and escolha_j2 == 'PEDRA':
        print(f'< {escolha_j1} X {escolha_j2} >  < {escolha_j1} embrulha a {escolha_j2} > O VENCEDOR FOI: {jogador_1} !')
    elif escolha_j1 == 'PAPEL' and escolha_j2 == 'TESOURA':
        print(f'< {escolha_j1} X {escolha_j2} >  < {escolha_j2} corta o {escolha_j1} > O VENCEDOR FOI: {jogador_2} !')
    print()
    continuar = input('Você deseja continuar jogando ? [S] para "SIM" ou [N] para "NÃO" ')
    print()
    if continuar in 'Nn':
        break
print('Partida encerrada, até breve!')