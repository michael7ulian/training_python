import os
from os import path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

auth = True
email_list = []

def menu():
    print("--- Menu ---")
    print("1. Daftar Email")
    print("2. Tambah Email")
    print("3. Kirim Pesan Broadcast ke Email yang ada pada Daftar")
    print("4. Keluar\n")

def form_tambah_email():
    email = input("Masukkan Email : ")
    fwrite = open("receiver_list.txt", "a")
    fwrite.write(email + "\n")
    fwrite.close()

    print("Email berhasil ditambahkan!!\n")
    
def read_data_txt():
    if(path.exists("receiver_list.txt")):
        fread = open("receiver_list.txt","r")
        print(fread.read())
        fread.close()
    else:
        f = open("receiver_list.txt", "w+")
        f.close()
    
def remove_txt():
    os.remove("receiver_list.txt")

def kirim_email():
    fread = open("receiver_list.txt","r")
    content = fread.read()
    email_list = content.split("\n")
    fread.close()
    
    # Setup Mail
    mail_content = input("Masukkan isi email : ")
    subject = input("Masukkan judul email : ")
    sender_address = 'tpython777@gmail.com'
    sender_pass = 'testing554'
    
    for i in email_list:
        receiver_address = i
        # Setup MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = subject

        # Mail Body & attachment
        message.attach(MIMEText(mail_content, 'plain'))

        # SMPT Session
        session = smtplib.SMTP('smtp.gmail.com', 587) # use gmail with port
        session.starttls() #e nable security
        session.login(sender_address, sender_pass) # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    print('Mail Sent')    
    
menu()
choose = input("Pilih Menu : ")

while auth:
    if choose == "1":
        print("\nDAFTAR EMAIL\n")
        read_data_txt()
        menu()
        choose = input("Pilih Menu : ")
    elif choose == "2":
        form_tambah_email()
        menu()
        choose = input("Pilih Menu : ")
    elif choose == "3":
        kirim_email()
        menu()
        choose = input("Pilih Menu : ")
    elif choose == "4":
        print("Program Selesai, Sampai Jumpa Lagi")
        auth = False
    else:
        print("\nMenu Tidak Ditemukan")
        menu()
        choose = input("Pilih Menu : ")