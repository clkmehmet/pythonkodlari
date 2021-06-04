import tkinter as tk

def ekle():
    box.insert(tk.END, e.get())
    e.delete(0, tk.END)
def sil():
    if len(box.curselection()) > 0:
        index = box.curselection()[0]
        box.delete(index)
def kaydet():
    f = open('yapdığınız.txt', 'w', encoding='utf-8')
    gorevler = box.get(0, tk.END)
    f.writelines('\n'.join(gorevler))
    f.close()
def yukle():
    f = open('yapdığınız.txt', 'r', encoding='utf-8')
    gorevler = f.readlines()
    box.delete(0, tk.END)
    for gorev in gorevler:
        if '\n' in gorev:
            gorev = gorev.replace('\n', '')
        box.insert(tk.END, gorev)

pencere = tk.Tk()
pencere.title(' ☪ | Yapacaklar listesi | 0.3')
ekrangenis=pencere.winfo_screenwidth()//2-160
ekranyuksek=pencere.winfo_screenheight()//2-150
pencere.geometry("420x270+{}+{}".format(ekrangenis, ekranyuksek))

sonuc = tk.Label(pencere, text="Mehmet Çalık Tarafından yapılmıştır",font="Courier 9 bold", width=50, justify="center")
sonuc.place(x=30, y=183)
turkbayagı = tk.Label(pencere, text="☪",font="Courier 40 bold", width=1, justify="center")
turkbayagı.place(x=30, y=200)
clkbayagı = tk.Label(pencere, text="CLK",font="Courier 20 bold", width=3, justify="center")
clkbayagı.place(x=324, y=220)
f = tk.Frame(pencere)
f.pack()
box = tk.Listbox(f, width=50, height=10)
box.pack(side=tk.LEFT)
scroll = tk.Scrollbar(f, command=box.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
box.config(yscrollcommand=scroll.set)



e = tk.Entry(pencere, width=40)
e.pack()
e.focus()
bekle=tk.Button(pencere, text='Görev ekle', width=10, command=ekle)
bekle.pack()
bekle.place(x=200, y=200)
bsil=tk.Button(pencere, text='Görev sil', width=10, command=sil)
bsil.pack()
bsil.place(x=90, y=200)
bkaydet=tk.Button(pencere, text='Görevleri kaydet', width=10, command=kaydet)
bkaydet.pack()
bkaydet.place(x=90, y=230)
byukle=tk.Button(pencere, text='Görevleri yükle', width=10, command=yukle)
byukle.pack()
byukle.place(x=200, y=230)



pencere.mainloop()
