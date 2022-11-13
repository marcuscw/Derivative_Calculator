function = input('function to differentiate: ')
function = function.replace(' ', '')
functions = function.split('+')

dydx = []

for func in functions:

    if func.count('^') == 0:  # the following checks if the function does not have a power and deals with it accordingly eg 6x -> 6
        if func[:func.index('x') - 1] == '':
            dydx.append('1')
        else:
            dydx.append(func[:func.index('x')])
        continue

    for i in range(len(func)):
        if func[i] == '^':  # check for carret

            coefficient = func[:i-1]
            if coefficient == '':  # checks for no coefficient
                coefficient = 1

            if func[i + 1] == '(':  # check for brackets surrounding the indicie for example x^(-56)
                indiceStart = i + 1

                try:  # check for closing bracket
                    indiceFinish = func.index(')', indiceStart)
                except:  # if its not present, THROWS AN ERROR MESSAGE!
                    print('OOPS! ERROR: did you forget a closing bracket?')
                    exit()

                indice = func[indiceStart + 1:indiceFinish]
                dydx.append(f'{int(indice) * int(coefficient)}x^({int(indice) - 1})')

            else:  # if the indice isnt in brackets
                indice = func[i + 1]
                if (int(indice) - 1) == 1:
                    dydx.append(f'{int(coefficient) * 2}x')
                else:
                    dydx.append(f'{int(indice) * int(coefficient)}x^{int(indice) - 1}')
print(*dydx, sep=' + ')
