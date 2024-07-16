# Analizar se uma expressao matematica está certa

formula = list(str(input('\033[1;97mDigite a expressão: ')))

# Analizar
a = formula.count('(')
b = formula.count(')')
c = a + b

if c % 2 == 0:
    print('\033[1;32mSua expressão está certa!')
elif c % 2 >= 1:
    print('\033[1;31mSua expressão está errada!')
