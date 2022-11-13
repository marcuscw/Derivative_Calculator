function = input('function to differentiate: ')
function = function.replace(' ', '')

functions = []  # eg ['2x^3', 'x^4']
signs = []  # eg ['+', '+', '-']

cursor = 0
if function[0] != '-':  # eg is the function is 'x^2', it implies a positive sign so this accounts for it
    signs.append('+')
for i in range(len(function)):  # splits function at a sum or minus sign (sum rule)
    if function[i] == '+':
        signs.append('+')
        functions.append(function[cursor:i])
        cursor = i
    if function[i] == '-':
        signs.append('-')
        functions.append(function[cursor:i])
        cursor = i

if cursor != 0:  # if there is more than one function
    functions.append(function[cursor + 1:])
else:  # if there is one function
    functions = [function]
functions = list(filter(None, functions))  # remove empty strings


print(functions)
print(signs)

dydx = []

for func in functions:

    if func.isdigit():  # if the function is a constant then the derivative is 0, ie add/subract nothing which is why it can be skipped
        continue
    if func.count('^') == 0 or func[func.index('^') + 1] == '1':  # the following checks if the function does not have a power and deals with it accordingly eg 6x -> 6
        if func[:func.index('x')] == '':
            dydx.append('1')
        elif func[:func.index('x')] == '-':
            dydx.append('-1')
        else:
            dydx.append(func[:func.index('x')])
        continue

    for i in range(len(func)):
        if func[i] == '^':  # check for caret

            coefficient = func[:i-1]
            if coefficient == '':  # checks for no coefficient
                coefficient = 1
            if coefficient == '+':  # checks is coefficient is a negative sign
                coefficient = 1
            if coefficient == '-':  # checks is coefficient is a negative sign
                coefficient = -1

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
if not dydx:
    print(0)
else:
    print(*dydx, sep=' + ')
