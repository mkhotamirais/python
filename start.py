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
var_num = 10
var_str = 'Hello World!'
var_str_a = var_str_b = 'Hello'
var_str_x, var_str_y, var_str_z = 'World!', 'World1', 'World2'
var_unpack = ['one', 'two', 'three']
var_unpack_a, var_unpack_b, var_unpack_c = var_unpack
# tuple dan list outputnya sama, bedanya kalau list bisa dibuat variabl terpisah.
def myFunc():
    global var_num        # jika ingin mengakses variabel di luar function, gunakan keyword global
    i = 20                # jika tidak pakai global, maka variabel d di dalam function adalah variabel lokal
    print(i)

# --- Tipe Data

# 1. ------ String
# bisa pakai single quote ' atau double quote "" | 'hllo "world"' atau "hello 'world'"
# string adalah array unicode, jadi bisa diperlakukan seperti array.
ms = '''multiline string
menggunakan triple quote'''
str_constructor = str('Hello World!')  # string constructor
str_literal = 'Hello World!'      # string literal
# f-string with placeholder {}
str_f1 = f"Hello {var_num} World!"  # Hello 10 World!
str_f2 = f"Hello {var_num * 2} World!"  # Hello 20 World!
str_f3 = f"The Price is {var_num:.2f} World!"  # The Price is 10.00 World! (2 digit di belakang koma float)
# String Methods: .upper(), .lower(), .strip(), .replace(to, from), .split(','), .join(), others: https://www.w3schools.com/python/python_strings_methods.asp

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

# 4. ------ Python Collections (array): List
# List dengan String hapir mirip secara umum, bedanya berikut:
# - List adalah ordered, bisa diakses indexnya
# - List bisa diubah (mutable), bisa ditambah, dihapus, diubah isinya
# - List bisa berisi tipe data berbeda
# - List bisa di-nest (list di dalam list)
list_constructor = list(('satu', 'dua', 'tiga', 'empat', 'lima'))   # list constructor
list_literal = ['satu', 'dua', 'tiga', 'Empat', 'lima']          # list literal
list_literal_num = [100, 30, 20]

list_literal.sort()               # ['Empat', 'dua', 'lima', 'satu', 'tiga'] # mengurutkan item list secara ascending dan case-sensitive
list_literal_num.sort()            # [20, 30, 100] # mengurutkan item list angka secara ascending
list_literal.sort(reverse=True)   # ['tiga', 'satu', 'lima', 'empat', 'dua'] # mengurutkan item list secara descending
list_literal.reverse()        # ['dua', 'empat', 'lima', 'satu', 'tiga'] # membalik urutan item list
def myFunc2(n):
 return abs(n - 50)
list_literal_num.sort(key=myFunc2) # [30, 20, 100] # mengurutkan angka berdasarkan jarak dari 50
list_literal.sort(key=str.lower) # ['dua', 'Empat', 'lima', 'satu', 'tiga'] # mengurutkan item list secara ascending tanpa case-sensitive
# join list
# list_literal_join = list_literal + list_literal_num  # menggabungkan dua list
# for x in list_literal:
#    list_literal_num.append(x)  # menambah item list ke list lain
# print(list_literal_num)
# Copy list 3 cara: list2 = list1.copy() | list2 = list(list1) | list2 = list1[:]
list_literal[1] = 'two'                   # ['satu', 'two', 'tiga', 'empat', 'lima']  # mengubah item list
list_literal[2:4] = ['three', 'four']     # ['satu', 'two', 'three', 'four', 'lima']  # mengubah item list dengan mengganti beberapa item sekaligus
list_literal[2:4] = ['tiga']              # ['satu', 'two', 'tiga', 'lima']  # mengubah item list dengan mengganti beberapa item sekaligus, tapi jumlah item berbeda
list_literal.insert(2, 'ahmad')           # ['satu', 'two', 'ahmad', 'tiga', 'lima'] # menambah item list di posisi tertentu
list_literal.append('enam')               # ['satu', 'two', 'ahmad', 'tiga', 'lima', 'enam'] # menambah item list di akhir
list_literal.extend(['jeruk', 'apel'])    # ['satu', 'two', 'ahmad', 'tiga', 'lima', 'enam', 'jeruk', 'apel'] # menambah item list dari list lain
list_literal.extend(('pisang', 'jeruk'))  # ['satu', 'two', 'ahmad', 'tiga', 'lima', 'enam', 'jeruk', 'apel', 'pisang', 'mangga'] # menambah item list dari tuple
# .extend nilainya harus iterable (list, tuple, set, dict, string), tidak bisa number
list_literal.remove('jeruk')              # ['satu', 'two', 'ahmad', 'tiga', 'lima', 'enam', 'apel', 'pisang', 'mangga'] # menghapus item list berdasarkan nilai, jika ada duplikat hanya yang pertama yang dihapus
list_literal.pop(1)                       # ['satu', 'ahmad', 'tiga', 'lima', 'enam', 'apel', 'pisang', 'mangga'] # menghapus item list di posisi tertentu
list_literal.pop()                        # ['satu', 'ahmad', 'tiga', 'lima', 'enam', 'apel', 'pisang'] # menghapus item list di posisi terakhir
del list_literal[0]                       # menghapus item list di posisi tertentu
list_literal.clear()                      # [] menghapus semua item list
# del list_literal                          # menghapus list
# print(list_literal)

# 5. ------ Python Collections (array): Tuple
# Tuple item itu ordered, tidak bisa diubah (immutable), bida duplikat, bisa berisi tipe data berbeda
# kalau hanya ada satu item, harus ada koma di akhir
tuple_constructor = tuple(('satu', 'dua', 'tiga'))           # tuple constructor
tuple_literal = ('satu', 'dua', 'tiga', 'empat', 'lima')  # tuple literal
tuple_literal_single = ('satu',)  # tuple dengan satu item
(unpack_x, unpack_y, unpack_z) = tuple_constructor  # unpack tuple
(unpack_xx, *unpack_yy, unpack_zz) = tuple_literal # coba pindahkan bintangnya dan ekekusi
# print(len(tuple_literal))  # satu
# del tuple_constructor  # menghapus tuple
# Tuple Methods: .count(value), .index(value), others: https://www.w3schools.com/python/python_tuples_methods.asp

# 6. ------ Python Collections (array): Set
# Set item itu unordered, unchangeable, unindexed (membuat susunannya random setiap dieksekusi), tidak bisa duplikat (jika duplikat akan dihapus otomatis dan dipilih salah satu)
# Set belaku len, in, not in, methods
# looping set: for x in set: print(x)
set_constructor = set(('satu', 'dua', 'tiga'))  # set constructor
set_literal = {'a', 'b', 'c'}                   # set literal
# set_added = set_literal.add('d')              # menambah item set
set_literal.update(['d', 'e'])                  # memodifikasi item set dari set lain, list atau tuple
set_removed = set_literal.remove('a')           # menghapus item set, jika item tidak ada akan error
set_discarded = set_literal.discard('x')        # menghapus item set, jika item tidak ada tidak akan error
# set_popped = set_literal.pop()                # menghapus item set di posisi acak
# set_cleared = set_literal.clear()             # menghapus semua item set
# del set_literal                               # menghapus set
set_union_two_a = set_constructor.union(set_literal)  # menggabungkan dua set
set_union_two_b = set_constructor | set_literal  # menggabungkan dua set
set_union_many = set_constructor.union({'f', 'g'}, {'h', 'i'})      # menggabungkan banyak set
set_union_list = set_constructor.union(['f', 'g'], ['h', 'i'])      # menggabungkan set dengan list
set_union_tuple = set_constructor.union(('f', 'g'), ('h', 'i'))     # menggabungkan set dengan tuple
set_intersection_a = set_literal.intersection({'d', 'e', 'f', 'g'}) # mencari irisan dua set, jika tidak ada irisan hasilnya empty set
set_intersection_b = set_literal & {'d', 'e', 'f', 'g'}             # mencari irisan dua set, jika tidak ada irisan hasilnya empty set, dan hanya bisa dengan set lain
# set_literal.intersection_update({'d', 'e', 'f', 'g'})             # mengubah set_literal menjadi irisan dengan set lain
set_difference_a = set_literal.difference({'d', 'e', 'f', 'g'})     # mencari selisih dua set, hasilnya item di set_literal yang tidak ada di set lain
set_literal.difference_update({'d', 'e', 'f', 'g'})                 # mengubah set_literal menjadi selisih dengan set lain
set_symmetric_difference_a = set_literal.symmetric_difference({'d', 'e', 'f', 'g'}) # mencari selisih dua set, hasilnya item yang ada di salah satu set tapi tidak ada di kedua set
set_symmetric_difference_b = set_literal ^ {'d', 'e', 'f', 'g'}           # mencari selisih dua set, hasilnya item yang ada di salah satu set tapi tidak ada di kedua set, dan hanya bisa dengan set lain
# print(set_difference_a)

# 7. ------ Python Collections (array): Dictionary
# Dictionary item itu ordered (sejak python 3.7), mutable, tidak bisa duplikat
# Dictionary itu key:value, key harus unik, bisa string atau number, value bisa tipe data apapun
dict_constructor = dict(nama='Ahmad', umur=20, wni=True)  # dictionary constructor
dict_literal = {'nama': 'Ahmad', 'umur': 20, 'wni': True}  # dictionary literal
dict_len = len(dict_literal)            # menghitung jumlah item dictionary
dict_nama = dict_literal['nama']        # mengakses item dictionary berdasarkan key
dict_nama2 = dict_literal.get('nama')   # mengakses item dictionary berdasarkan key
dict_keys = dict_literal.keys()         # mengakses semua key dictionary
dict_values = dict_literal.values()     # mengakses semua value dictionary
dict_items = dict_literal.items()       # mengakses semua item (key, value) dictionary
dict_check = 'nama' in dict_literal     # mengecek apakah key ada di dictionary
dict_literal['nama'] = 'Budi'           # mengubah item dictionary berdasarkan key
dict_literal['asal'] = 'Jakarta'        # mengubah item dictionary berdasarkan key
dict_literal.update({'umur': 30, 'wni': False}) # menambah atau mengubah item dictionary dari dictionary lain
dict_literal.pop('umur')                # menghapus item dictionary berdasarkan key
dict_literal.popitem()                  # menghapus item dictionary terakhir yang dimasukkan
# del dict_literal['wni']                 # menghapus item dictionary berdasarkan key
# dict_literal.clear()                   # menghapus semua item dictionary
# del dict_literal                       # menghapus dictionary
# Looping dictionary:
# for key_name in dict_literal: print(key_name)              # looping semua key dictionary
# for value in dict_literal.values(): print(value)           # looping semua value dictionary
# for key, value in dict_literal.items(): print(key, value)  # looping semua item dictionary
dict_copy_a = dict_literal.copy()  # copy dictionary
dict_copy_b = dict(dict_literal)   # copy dictionary
# Other dictionary methods: https://www.w3schools.com/python/python_dictionaries_methods.asp

# - range | x = range(10)
# - frozenset | x = frozenset({'a', 'b', 'c'})
# - bytes | x = b"Hello" | x = bytes('hello')
# - bytearray | x = bytearray(5)
# - memoryview | x = memoryview(bytes(5))
# - NoneType | x = None


# --- Operators
# Arithmetic: + - * / % ** //
# Assignment: = += -= *= /= %= **= //= &= |= ^= >>= <<= :=
# Comparison: == != > < >= <=
# Logical: and or not
# Identity: is is not
# Membership: in not in
# Bitwise: & | ^ ~ << >>
# Precedence, operator yang dieksekusi lebih dulu: () | ** += -= ~= | * / // % | + - | << >> | & | ^ | | | == != > >= < <= is is not in not in | not | and | or