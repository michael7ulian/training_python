import os
from os import path
from datetime import datetime as dt
import time

# Cek OS
# name = os.name
# print(name)

# Cek apakah file tertentu ada atau tidak
# print(path.exists("direktori.py"))
# print(path.isfile("direktori.py"))
# print(path.isdir("new"))

# work with file path
# dir = path.realpath("list.txt")
# print(dir)
# dir = path.split(path.realpath('list.txt'))
# print(f"Nama file: {dir[1]}")
# print(f"Path: {dir[0]}")

# Melihat waktu modifikasi file
# t = time.ctime(path.getmtime('list.txt'))
# print(t)
# t = time.ctime(path.getatime('list.txt'))
# print(t)

# get modification time
# t = time.ctime(path.getmtime('operasi_file.py'))
# print(t)
# print(dt.fromtimestamp(path.getmtime('operasi_file.py')))


# Kalkulasi sudah sudah berapa lama modifikasi terakhirnya
td = dt.now() - dt.fromtimestamp(path.getmtime('operasi_file.py'))

print(td)
print(td.total_seconds())
