from datetime import date
from datetime import datetime
# Waktu Sekarang
now = date.today()
print(now)

# Format Tanggal
time = datetime.now()

# %y/%Y = Tahun, %a/%A = Pekan, %b/%B = Bulan, %d = Hari
print(time.strftime("Sekarang adalah: Tahun %y, Tanggal %d %b"))

# %c = Local time date, %x = local date, %X = local time
print(time.strftime("Sekarang: %c"))
print(time.strftime("Sekarang: %X"))
print(time.strftime("Sekarang: %x"))

# hari apa sekarang?
# 0 = Monday, 6 = Sunday
print(now.weekday())
days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabut', 'Ahad']
print(f"Hari ini adalah {days[now.weekday()]}")

# Time Formatting
# %I = jam format 12, %H = jam format 24, %M = Menit, %S = Detik, %P = AM/PM
print(time.strftime("Sekarang Pukul %I, menit ke %M, detik ke %S, %P"))