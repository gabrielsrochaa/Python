tabelaCb = ('Corinthians', 'Santos', 'Avaí', 'América-MG', 'Bragantino', 'Atlético-MG', 'São Paulo',
            'Botafogo', 'Internacional', 'Coritiba', 'Cuiabá', 'Athletico-PR', 'Palmeiras', 'Flamengo',
            'Fluminense', 'Goiás', 'Ceará', 'Juventude', 'Atlético-GO', 'Chapecoense')
print('#'*20, 'Tabela | Brasileirão Série A', '#'*20, '\n')
print('','-'*46)
print('| Os 5 primeiros colocados do Brasileirão são: |')
print('','-'*46)
for c in range(0, 5):
    print(tabelaCb[c])
    c += 1
    # p += 1
print('#'* 100)
print('', '-'*40)
print('| Os 4 últimos colocados da tabela são: |')
print('', '-'*40)
c2 = -1
for i in range(0, 4):
    print( tabelaCb[c2])
    c2 -= 1
print('#'* 100)
print('', '-'*40)
print('| Listando os times em ordem alfabética: |')
print('', '-'*40)
for t in range(0,len(tabelaCb)):
    org = sorted(tabelaCb)
    print(org[t])
pos = tabelaCb.index('Chapecoense') +1
print('#'* 100)
print(f'\n A Chapecoense está na {pos}° posição.')