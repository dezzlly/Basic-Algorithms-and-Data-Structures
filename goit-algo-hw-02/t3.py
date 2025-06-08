brackets = {'(': ')', '[': ']', '{': '}'}
stack = []

def check_string(string):
    for char in string:
        # проверяем есть ли символ в словаре ключей
        # если есть, добавляем в стек
        if char in brackets:
            stack.append(char)
        # проверяем есть ли символ в словере значений
        elif char in brackets.values():
            # проверяем пустой ли стек
            if not stack:
                return "Asymmetrical"
            # если не пустой, удаляем последний добавленный символ
            # т.е. мы нашли пару символов, например "()"
            last = stack.pop()
            # если последний добавленный не в паре с текущим символом
            # т.к. мы обращаемся по к словарю по ключу, получаем значение этого ключа и сравниваем его с текущим символом
            # если они не равны, то ассметрично
            if brackets[last] != char:
                return "Asymmetrical"
    # эта проверка в самом конце
    # и если в стеке что-нибудь осталось, то это ассиметрично
    # т.к. мы не нашли пару для этого символа
    if stack:
        return "Asymmetrical"
    return "Symmetrical"



print(check_string('( ){[ 1 ]( 1 + 3 )( ){ }}'))
print(check_string('( 23 ( 2 - 3);'))
print(check_string('( 11 }'))