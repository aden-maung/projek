import os
os.system('cls')
import random
import time

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Projek taruhan balap kuda

print(30*("="))
print("Selamat datang di program balap kuda")
print(30*("="))


def kuda_resink(kuda_balap):
    print("Taruhan Kuda Resink")
    for idx, kuda in enumerate (kuda_balap, start=1):
        print(f"{idx}. {kuda}")

def get_user_bet(kuda_balap): 
    global duit
    global taruhan
    taruhan = int(input("Berani Berapa?? "))
    duit = taruhan * 15
    pilih = int(input("Pilih Kuda Kepercayaan Mu Dengan Memasukan Nomer Kuda Resink: "))
    if 1 <= pilih <= len(kuda_balap):
        return kuda_balap[pilih - 1]
    else:
        print ("INPUT INVALID:0101!")
        return get_user_bet(kuda_balap)
            
def balap(kuda_balap):
    print("\nThe resink is starting!!")
    time.sleep(1)
    balap_progress = {kuda: 0 for kuda in kuda_balap}
    while True:
        for kuda in kuda_balap:
            balap_progress[kuda] += random.randint(1, 10)
            print(f"{kuda} DI POSISI {balap_progress[kuda]}")
            time.sleep(0.5)

            if balap_progress[kuda] >= 100:

                print(f"\n {kuda} MENANG BALAP!")
                return kuda
            
def main():
    kuda_balap = ["AMBATUKAM", "KUDA HYTAM", "AMBATRON", "APOKADO", "PAGIAN NGAWI", "MUWANI", "DODOT", "RUSDI","MR.IRONI","SI IMUT","AMBAHORSE", "ADIT SLEBEW", "RUSDI SUPER", "SUPERSTAR JUMBO", "PANGERAN NGAWI"]
    kuda_resink(kuda_balap)

    user_bet = get_user_bet(kuda_balap)
    print(f"ANDA MEMILIH: {user_bet}")

    winner = balap(kuda_balap)

    if user_bet == winner:
        print("Selamat Anda Menang Taruhan")
        print("Jumlah Uang Yang Anda Menangkan adalah", duit, "RUPIAH")
    else:
        print("YAHHHH TEKOR BOS")
        print("DUIT -", taruhan,"RUPIAH")

if __name__ == "__main__":
    main()