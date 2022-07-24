import math
x = float(input('Digite o ângulo: '))
y = math.radians(x)
sen = math.sin(y)
cos = math.cos(y)
tg = math.tan(y)
print('O seno do ângulo de {:.0f}° é {:.1f}, o cosseno é {:.1f} e a tangente é {:.1f}'
      .format(x,sen,cos,tg))
