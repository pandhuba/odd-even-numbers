# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:11:31 2020

@author: Tulenesia
"""

def callBack():
    pilih = str(input("Ingin cek lagi? (y/n) : "))         
    if pilih == 'y':
        return True
    elif pilih == 'n':
        menu()
    else:
        print("Masukkan Salah!")
        menu()

def odd_even():
    while True:
        print("----------------------------------------------------")
        bil = int(input("Masukkan bilangan integer : "))
    
        
        if bil % 2 == 0:
            print("Angka ", bil, " adalah bilangan GENAP")
            callBack()
        
        else:
            print("Angka ", bil, " adalah bilangan GANJIL")
            callBack()   
            

def primes():
    while True:
        print("----------------------------------------------------")
        print("1. Cek bilangan prima")
        print("2. Cetak bilangan prima antara dua angka")
        print("3. Kembali")
        menuPrimes = int(input("Pilih (1/2/3) : "))
        
        if menuPrimes == 1:
            print("----------------------------------------------------")
            bil = int(input("Masukkan bilangan integer : "))
            
            if bil > 1:
                for i in range(2,bil):
                    if bil%i == 0:
                        print("Angka ", bil, " BUKAN bilangan prima")
                        print("karena ", i, " x ", bil/i, " = ", bil)
                        callBack()
                        break
                else:
                    print("Angka " , bil, " ADALAH bilangan prima")
                    callBack()
            else:
                print("Angka ", bil, " BUKAN bilangan prima")
                callBack()
            
                
        elif menuPrimes == 2:
            print("----------------------------------------------------")
            bil1 = int(input("Masukkan bilangan pertama : "))
            bil2 = int(input("Masukkan bilangan kedua : "))
            
            print("Bilangan prima antara ", bil1, " dan ", bil2, " adalah :")
            for num in range(bil1,bil2 + 1): 
                if num > 1: 
                    for i in range(2,num): 
                        if (num % i) == 0: 
                            break 
                    else: 
                        print(num) 
            
            callBack()
                          
        elif menuPrimes == 3:
            menu()
        
        else:
            print("Menu tidak tersedia!")
            return True
              
def menu():
    while True:
        print("\n")
        print("############# PANDHU BRIAN ALDHIANSYAH #############")
        print("----------------------------------------------------")
        print("1. Bilangan Genap / Ganjil")
        print("2. Bilangan Prima")
        print("3. Keluar")
        menu = int(input("Pilih menu (1/2/3) : "))
        
        if menu == 1:
            odd_even()
        elif menu == 2:
            primes()
        elif menu == 3:
            return False
        else:
            print("Menu tidak tersedia!")
            return True
         
if __name__=="__main__":
    menu()