from collections import deque


def is_palindrom(string):
    d = deque()
    word = string.replace(" ", "").lower()
    for char in word:
        d.append(char)

  

    while len(d) > 1:
        beginning = d.pop()
        # print(beginning)
        end = d.popleft()
        # print(end)

        if beginning != end:
            return f'Word {string} is not palindrom'

    return f'Word {string} is palindrom'



print(is_palindrom(" DASAD DASAD"))
print(is_palindrom("DASADA DASAD"))
print(is_palindrom("ADASSADA"))
print(is_palindrom("ADASSEADA"))