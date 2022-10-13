angka1 = float(input("ini Angka 1 : "))
angka2 = float(input("ini Angka 2 : "))
operasi = input("Silahkan pilih x / + - : ")
if operasi == 'x':
    result = angka1 * angka2
elif operasi == '/':
    result = angka1 / angka2
elif operasi == '+':
    result = angka1 + angka2
elif operasi == '-':
    result = angka1 - angka2

print(result)
