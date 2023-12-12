# Даны строки S и So. Удалить из строки S все подстроки, совпадающие с So.
# Если совпадающих подстрок нет, то вывести строку S без изменений.
def remove_substring(S, So):
    return S.replace(So, '')

S = "Hello, world! Hello, from the other side"
So = "o"
result = remove_substring(S, So)
print(result)