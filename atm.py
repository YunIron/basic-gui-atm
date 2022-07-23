from tkinter import *
from tkinter import messagebox
import time

global error
global main
global uygulama


main = Tk()


main.title("ATM")
main.geometry("300x200")


uygulama = Frame(main)
uygulama.grid()


class atm():
    def __init__(self):
        self.uygulamaS = uygulama
        self.mainS = main
        self.kullaniciD = "KullanıcıAdınız"
        self.sifreD = "Sıfrenız"
        self.sifre = sifreE.get()
        self.kullanici = kullaniciName.get()
        self.bakiye = 0
        self.cuzdan = 150
        self.kontroldeger()
        self.isleyis()

    def isleyis(self):
        self.kontrol()
        self.destroygirisall()
        self.panel()

    def panel(self):
        global welcome
        global bakiye
        global yatirButton
        main.geometry("250x200")
        welcome = Label(uygulama, text="Hosgeldin {} !".format(self.kullanici))
        welcome.grid(column=4, padx=7, pady=1)
        bakiye = Label(uygulama, text=f"Bakiye = {str(self.bakiye)}")
        bakiye.grid(padx=10,pady=50)
        yatirButton = Button(uygulama, text="Yatir", bd=3,borderwidth=1,border=1,command=self.yatirma)
        yatirButton.place(x=100, y=70)
        cekmeButton = Button(uygulama, text="Çekme", bd=3,borderwidth=1,border=1,command=self.cekme)
        cekmeButton.place(x=150, y=70)
    
    
    def yatirma_validation(self):
        entryY = miktarYatir.get()
        if entryY.isnumeric():
                if (self.cuzdan - int(entryY) < 0):
                    messagebox.showerror("Hata", "Cuzdaninizda yeterli miktarda nakit yok.")
                else:
                    self.cuzdan = (self.cuzdan - int(entryY))                   
                    self.bakiye = (self.bakiye + int(entryY))
                    welcome.destroy()
                    bakiye.destroy()
                    yatirButton.destroy()
                    self.panel()
        else:
            messagebox.showwarning("Hata","Sadece sayi giriniz.\nTekrar Deneyiniz!")

    def cekme_validation(self):
        entryC = miktarCekme.get()
        if entryC.isnumeric():
            if (self.bakiye - int(entryC) < 0):
                messagebox.showerror("Hata", "Yeterli miktarda bakiyeniz yok.")
            else:
                self.bakiye = (self.bakiye - int(entryC))
                self.cuzdan = (self.cuzdan + int(entryC))
                welcome.destroy()
                bakiye.destroy()
                yatirButton.destroy()
                self.panel()
        else:
            messagebox.showerror("Hata", "Sadece sayi giriniz. \nTekrar Deneyiniz!")

    def yatirma(self):
        yatirpanel = Tk()
        yatirpanel.title("Bakiye Yatirma")
        yatirpanel.geometry("125x100")
        yatiruyg = Frame(yatirpanel)
        yatiruyg.grid()
        miktarText = Label(yatiruyg, text="Miktar = ")
        global miktarYatir
        miktarYatir = Entry(yatiruyg, bd=1)
        yatirmaButton = Button(yatiruyg, text="Bakiye Yatir", command=self.yatirma_validation)
        miktarText.grid(padx=1,pady=1)
        miktarYatir.grid(padx=1, pady=1)
        yatirmaButton.grid(padx=1, pady=20)
        
        mainloop()

    def cekme(self):
        cekmepanel = Tk()
        cekmepanel.title("Bakiye Yatirma")
        cekmepanel.geometry("125x100")
        cekmeuyg = Frame(cekmepanel)
        cekmeuyg.grid()
        cekmemiktarText = Label(cekmeuyg, text="Miktar = ")
        global miktarCekme
        miktarCekme = Entry(cekmeuyg, bd=1)
        cekmeButton = Button(cekmeuyg, text="Bakiye Çekme", command=self.cekme_validation)
        cekmemiktarText.grid(padx=1,pady=1)
        miktarCekme.grid(padx=1, pady=1)
        cekmeButton.grid(padx=1, pady=20)
        
        mainloop()

    def destroygirisall(self):
        sifreE.destroy()
        sifreText.destroy()
        kullaniciName.destroy()
        kullaniciText.destroy()
        girisButton.destroy()

    def kontroldeger(self):
        if (self.kullanici == self.kullaniciD):
            self.kullanicidogru=0
        else:
            self.kullanicidogru=1
        if (self.sifre == self.sifreD):
            self.sifredogru=0
        else:
            self.sifredogru=1

    def kontrol(self):
        print(self.sifredogru)
        print(self.kullanicidogru)
        if self.sifredogru == 0 and self.kullanicidogru == 0:
            pass
        else:
            messagebox.showwarning("Hata","Yanlis kullanici adi ve ya sifre.\nTekrar Deneyiniz!")
            exit()
kullaniciText = Label(uygulama, text="Kullanici Ismi")
kullaniciText.grid(padx=90, pady= 5)
kullaniciName = Entry(uygulama, bd=1)
kullaniciName.grid(padx=90, pady=5)

sifreText = Label(uygulama, text="Sifre")
sifreText.grid(padx=90, pady= 5)

sifreE = Entry(uygulama, bd=1)
sifreE.grid(padx=90, pady=5)

girisButton = Button(uygulama, text="Giris yap", width=6, bd=3, command=atm)
girisButton.grid(padx=90, pady=5)

mainloop()
