import helper

helper.header("Responsi SOP NOMOR 1")

RAM = int(input("Kapasitas RAM dalam MB : "))
Blok = int(input("Masukan Blok : "))
petabit = helper.hitungPetaBit(helper.ubahRamKeMbps(RAM), Blok)
kapasitas = petabit - RAM

print("-" * 50)
print("Kapasitas Petabit  : ", petabit)
print("Kapasitas /Petabit : ", kapasitas)

print("\nProgram dijalankan")

sisop = int(input("Kapasitas Sistem Operasi : "))
program1 = int(input("RAM yang digunakan oleh program 1: "))
program2 = int(input("RAM yang digunakan oleh program 2: "))


totalRAM = program1 + program2
totalRAMtdkterpakai = RAM - totalRAM

print("Total RAM Terpakai     : ", totalRAM)
print("Total RAM Tak Terpakai : ", totalRAMtdkterpakai)

blok1 = RAM / petabit
blok0 = Blok - blok1


print("Kapasitas RAM", RAM)
print("Jumlah blok bernilai 1 = ", blok1)
print("Jumlah blok bernilai 0 = ", blok0)