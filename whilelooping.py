pinAtm = 1234
saldoAtm = 5000000

print("== ATM BNI ==")
login = int(input("Masukan PIN : "))

while login != pinAtm:
    print("Pin Anda Salah")
    login = int(input("Mohon masukan kembali PIN : "))

while True:
    print("\n== ATM Menu ==")
    print("1. Cek Saldo")
    print("2. Setor Uang")
    print("3. Tarik Uang")
    print("4. Keluar")
    pilih = int(input("Pilih : "))

    if pilih == 1:
        print(f"Saldo anda : Rp. {saldoAtm}")
    elif pilih == 2:
        setoran = int(input("Jumlah setor : Rp. "))
        saldoAtm = saldoAtm + setoran 
        print(f"Anda berhasil menyetor sejumlah : Rp. {setoran}")
    elif pilih == 3:
        tarik = int(input("Jumlah tarik : Rp. "))

        if tarik > saldoAtm:
            print("GAGAL!")
            print(f"Saldo anda : Rp. {saldoAtm}")
        else:
            saldoAtm = saldoAtm - tarik
            print("Anda berhasil")
            print(f"Anda berhasil menarik sejumlah : Rp. {tarik}")

    elif pilih == 4:
        print("Terimakasih telah berkunjung di ATM kami")
        break
    else:
        print("Pilihan anda tidak valid!")