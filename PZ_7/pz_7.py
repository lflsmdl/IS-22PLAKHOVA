# Даны целые положительные числа N1 и N2 и строки S1 и S2.
# Получить из этих строк новую строку, содержащую первые N1 символов
# строки S1 и последние N2 символов строки S2(в указанном порядке).
def combine_strings(N1,N2, S1, S2):
    result = S1[:N1] + S2[-N2:]
    return result

N1 = 3
N2 = 4
S1 = "PythonProgramming"
S2 = "ExampleString"
combined_string = combine_strings(N1, N2, S1, S2)
print(combined_string)