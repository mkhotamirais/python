# --- Pendahuluan
# Python bahasa pemrograman tingkat tinggi yang mudah dibaca. Oleh Guido van Rossum, rilis 1991. Untuk web development (server-side), software development, mathematics, system scripting.
# Kebanyakan PC ddan MAC sudah default terinstall python. cek di terminal "python --version"
# pertama-tama buat file hello.py isinya "print('hello world')". buka terminal, arahkan path ke file itu dan ketik "python hello.py"
# jika ingin coba di terminal ketik saja "python" atau "py" di terminal, lalu ketik syntax python.


# --- Aturan Variabel
# Variabel harus dimulai dengan huruf atau underscore (_) tidak boleh dimulai angka, hanya mengandung alphanumeric A-z0-9 dan underscore.
# Variabel itu case-sensitive dan tidak boleh python keyword berikut: and, as, assert, break, class, continue, def, del, elif, else, except, false, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, true, try, while, with, yield
# Variabel bisa berupa: camelCase: myVariable, PascalCase: MyVariable, camel_case: my_variable.
# python menganut block scope: ada Global Variabel dan Local Variabel. Global bisa dipanggil di manapun. sedangkan local hanya bisa di fungsi terkait kecuali dengan keyword 'global'
a_num = 10
a = 'Hello World!'
b = b1 = 'Hello'
c, d, e = 'World!', 'World1', 'Wrld2'   # unpacking tuple
fgh = ['enam', 'tujuh', 'delapan']  # list
f, g, h = fgh                       # unpacking list
# tuple dan list outputnya sama, bedanya kalau list bisa dibuat variabl terpisah.
i = 'tujuh'
def myFunc():
 global i          # jika ingin mengakses variabel di luar function, gunakan keyword global
 i = "tujuh update"    # jika tidak pakai global, maka variabel d di dalam function adalah variabel lokal
 print(i)


# --- Tipe Data

# 1. ------ String
# bisa pakai single quote ' atau double quote "" | 'hllo "world"' atau "hello 'world'"
# string adalah array unicode, jadi bisa diperlakukan seperti array.
# akses index pakai kurung siku [1, -1], jika nilai positif dari kiri index pertama 0, negatif dari kanan index pertama -1
k = '''multiline string
menggunakan triple quote'''
myStrings = [
    len(a),             # 12 - panjang string
    'world' in a,       # true - cek ada tidaknya substring
    'world' not in a,   # false - cek tidak ada substring
    a[0],               # H - akses index ke 0
    a[2:5],             # llo - akses index ke 2 sampai 5 (tidak termasuk)
    a[:5],              # Hello - akses index dari awal sampai 5 (tidak termasuk)
    a[2:],              # llo World! - akses index dari 2 sampai akhir
    a[-1],              # ! - akses index ke -1
    a[-5:-2],           # orl - akses index ke -5 sampai -2 (tidak termasuk)
    a.upper(),          # HELLO WORLD! - mengubah ke huruf besar
    a.lower(),          # hello world! - mengubah ke huruf kecil
    a.strip(),          # menghilangkan spasi di awal dan akhir string
    a.replace('H', 'Y'),    # Yello World! - mengganti karakter
    a.split(' '),           # ['Hello', 'World!'] - memisahkan string dengan spasi
    b + ' ' + c,            # Hello World! - menggabungkan string
    # b + 10,               # error - tidak bisa menggabungkan string dengan number maka butuh f-string
    f"I am {a_num} years",  # Hello World! - f-string (formatted string)
    f"I am {2 + 5} years",  # I am 15 years - f-string dengan operasi
    f("The price is {a_num:.2f} dollars"), # The price is 10.00 dollars - f-string dengan modifier placeholder dengan :.2f (2 digit di belakang koma float)
    "hello \"world\""       # hello "world" - escape character \' \\ \n \r \t \b \f \ooo \xhh
    "https://www.w3schools.com/python/python_strings_methods.asp" # referensi string methods
]
# print(myStrings[-1])

# 2. ------ Numbers
# int
l = 10
m = int("10")
n = 10.5
o = float("10.5")
p = 1j
q = complex("1j")

# 3. ------ Boolean (bool)
# hampir semua nilai dievaluasi "True"
# semua string kecuali empty ("")
# semua number kecuali 0
# semua list, tuple, set, dan dictionary kecuali yang kosong
# print(bool(False), bool(None), bool(0), bool(""), bool(()), bool([]), bool({}))

# - list | x = ['a', 'b', 'c'] | x = list(['a', 'b', 'c'])
# - tuple | x = ('a', 'b', 'c') | x = tuple(('a', 'b', 'c'))
# - range | x = range(10)
# - dict | x = {'nama': 'ahmad', 'umur': 20} | x = dict(nama='ahmad', umur: 20)
# - set | x = {'a', 'b', 'c'} | x = set(('a', 'b', 'c'))
# - frozenset | x = frozenset({'a', 'b', 'c'})
# - bytes | x = b"Hello" | x = bytes('hello')
# - bytearray | x = bytearray(5)
# - memoryview | x = memoryview(bytes(5))
# - NoneType | x = None

