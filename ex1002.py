'''A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.'''
R = float(input())
A = 3.14159 * (R ** 2)
print('A={:.4f}'.format(A))
