times = ('Palmeiras','Corinthians','Athletico-PR','Internacional',
         'Atlético-MG','Fluminense','Santos','São Paulo','Flamengo','Botafogo')
print(f'Lista de times: {times}')
print(f'Top 5: {times[0:5]}')
print(f'4 últimos: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O trikas está na {times.index("São Paulo")+1}ª posição')
