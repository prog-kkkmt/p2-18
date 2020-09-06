'''
String4. Дано целое число N (1 ≤ N ≤ 26).
Вывести N первых прописных (т. е. заглавных) букв латинского алфавита.
'''
n = int(input())
alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 1
if n < 1 or n > 26:
    print("под таким номером нет букв")
else:
    while i <= n:
       print(alf[i-1])
       i += 1
