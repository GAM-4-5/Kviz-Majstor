#importanje bitnih library-a
from tkinter import *
import os
from random import *
from tkinter import messagebox
import shutil

#stvaranje tkinter prozora
root=Tk()
root.resizable(width=False, height=False)
root.title("Kviz Mejker")
root.configure(background='white')


#konfiguracija grid-a
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#STVARANJE SVEGA

tpitanje=Text(root,height=2,width=40,font=("Helvetica", 22))
todg1=Text(root,height=1,width=30,font=("Helvetica", 18),background="#90ee90")
todg2=Text(root,height=1,width=30,font=("Helvetica", 18),background="#ff3f34")
todg3=Text(root,height=1,width=30,font=("Helvetica", 18),background="#ff3f34")
todg4=Text(root,height=1,width=30,font=("Helvetica", 18),background="#ff3f34")

tpitanje.grid(row=0,column=0,rowspan=2,columnspan=4,sticky="NESW")
todg1.grid(row=2,column=0,rowspan=1,columnspan=4,sticky="NESW")
todg2.grid(row=3,column=0,rowspan=1,columnspan=4,sticky="NESW")
todg3.grid(row=4,column=0,rowspan=1,columnspan=4,sticky="NESW")
todg4.grid(row=5,column=0,rowspan=1,columnspan=4,sticky="NESW")

tpitanje.insert(END, "'Pitanje'")
todg1.insert(END, "'Tocan odgovor'")
todg2.insert(END, "'Krivi odgovor'")
todg3.insert(END, "'Krivi odgovor'")
todg4.insert(END, "'Krivi odgovor'")

lime=Label(root,text="Ime kviza:")
eime=Entry(root)
lbrpitanja=Label(root,text="1")
gnazad=Button(root,text="<---")
gnaprijed=Button(root,text="--->")
gendless=Button(root,width=20,text="Endless")
gsurvival=Button(root,width=20,text="Survival")
lbrjokera=Label(root,text="Br. jokera:")
ebrjokera=Entry(root)
lbr50=Label(root,text="Br. 50/50:")
ebr50=Entry(root,text="0")
gsave=Button(root,text="SAVE & EXIT")

ebr50.insert(END, '0')
eime.insert(END, "'Ime kviza'")
ebrjokera.insert(END, '0')

lime.grid(row=0,column=4,columnspan=1,sticky="NESW")
eime.grid(row=0,column=5,columnspan=3,sticky="NESW")
lbrpitanja.grid(row=1,column=4,columnspan=2,sticky="NESW")
gnazad.grid(row=1,column=6,columnspan=1,sticky="NESW")
gnaprijed.grid(row=1,column=7,columnspan=1,sticky="NESW")
gendless.grid(row=2,column=4,columnspan=2,sticky="NESW")
gsurvival.grid(row=2,column=6,columnspan=2,sticky="NESW")
lbrjokera.grid(row=3,column=4,columnspan=2,sticky="NESW")
ebrjokera.grid(row=3,column=6,columnspan=2,sticky="NESW")
lbr50.grid(row=4,column=4,columnspan=2,sticky="NESW")
ebr50.grid(row=4,column=6,columnspan=2,sticky="NESW")
gsave.grid(row=5,column=4,columnspan=4,sticky="NESW")


lkviz=[]
cur_pitanje=1
br_modea=1



#spremanje trenutnog pitanja
def cur_save():
    global lkviz
    global cur_pitanje
    global tpitanje
    global todg1
    global todg2
    global todg3
    global todg4
    pitanje=tpitanje.get("1.0","end")
    odg1=todg1.get("1.0","end")
    odg2=todg2.get("1.0","end")
    odg3=todg3.get("1.0","end")
    odg4=todg4.get("1.0","end")
    
    if cur_pitanje>len(lkviz):
        lkviz.append([pitanje,odg1,odg2,odg3,odg4])
    else:
        lkviz[cur_pitanje-1]=[pitanje,odg1,odg2,odg3,odg4]

#učitavanje trenutnog pitanja       
def cur_load():
    global lkviz
    global cur_pitanje
    global tpitanje
    global todg1
    global todg2
    global todg3
    global todg4
    pitanje=tpitanje.get("1.0","end")
    odg1=todg1.get("1.0","end")
    odg2=todg2.get("1.0","end")
    odg3=todg3.get("1.0","end")
    odg4=todg4.get("1.0","end")
    
    if cur_pitanje>len(lkviz):
        pitanje=""
        odg1=""
        odg2=""
        odg3=""
        odg4=""
    else:
        pitanje=lkviz[cur_pitanje-1][0]
        odg1=lkviz[cur_pitanje-1][1]
        odg2=lkviz[cur_pitanje-1][2]
        odg3=lkviz[cur_pitanje-1][3]
        odg4=lkviz[cur_pitanje-1][4]
        
    tpitanje.delete("1.0", END)
    todg1.delete("1.0", END)
    todg2.delete("1.0", END)
    todg3.delete("1.0", END)
    todg4.delete("1.0", END)
    tpitanje.insert(END, pitanje)
    todg1.insert(END, odg1)
    todg2.insert(END, odg2)
    todg3.insert(END, odg3)
    todg4.insert(END, odg4)

#iduće pitanje
def naprijed():
    global cur_pitanje
    global lbrpitanja
    global tpitanje
    global todg1
    global todg2
    global todg3
    global todg4
    pitanje=tpitanje.get("1.0","end")
    odg1=todg1.get("1.0","end")
    odg2=todg2.get("1.0","end")
    odg3=todg3.get("1.0","end")
    odg4=todg4.get("1.0","end")
    if pitanje!="\n" and odg1!="\n" and odg2!="\n" and odg3!="\n" and odg4!="\n":
        if pitanje!="" and odg1!="" and odg2!="" and odg3!="" and odg4!="":
            #print(","+pitanje+",")
            cur_save()
            cur_pitanje+=1;
            cur_load()
    lbrpitanja.configure(text=str(cur_pitanje))
    #print(cur_pitanje)

#prijašnje pitanje   
def nazad():
    global cur_pitanje
    global lbrpitanja
    global tpitanje
    global todg1
    global todg2
    global todg3
    global todg4
    pitanje=tpitanje.get("1.0","end")
    odg1=todg1.get("1.0","end")
    odg2=todg2.get("1.0","end")
    odg3=todg3.get("1.0","end")
    odg4=todg4.get("1.0","end")
    if pitanje!="\n" and odg1!="\n" and odg2!="\n" and odg3!="\n" and odg4!="\n":
        if pitanje!="" and odg1!="" and odg2!="" and odg3!="" and odg4!="":
            cur_save()
    if cur_pitanje>1:
        cur_pitanje+=-1;
    cur_load()
    lbrpitanja.configure(text=str(cur_pitanje))
    #print(cur_pitanje)

#spremanje cijelog kviza u .txt file i gašenje programa
def save():
    global eime
    global br_modea
    global ebr50
    global ebrjokera
    global lkviz
    ime=str(eime.get())
    br50=abs(int(ebr50.get()))
    brjokera=abs(int(ebrjokera.get()))
    
    cur_save()
    ime=ime.replace(" ","_")
    #print(ime," ",br_modea," ",brjokera," ",br50)
    for i in range(len(lkviz)):
        for j in range(5):
            lkviz[i][j]=lkviz[i][j].replace('\n','')
    #        print(lkviz[i][j])
    #print(lkviz)
            
    f=open((ime+".txt"),"w+")
    f.write(ime+" "+str(br_modea)+" "+str(brjokera)+" "+str(br50))
    for i in range(len(lkviz)):
        if(lkviz[i][0]!=""):
            for j in range(5):
                f.write("\n"+str(lkviz[i][j]))
    
    f.close()
    shutil.move((ime+".txt"), 'Kvizovi/')
    os._exit(1)

#odabir mode-a "Endless"
def select_endless():
    global br_modea
    global gendless
    global gsurvival
    gendless.configure(fg='white',bg='black')
    gsurvival.configure(fg='black',bg='white')
    br_modea=1

#odabir mode-a "Survival"
def select_survival():
    global br_modea
    global gendless
    global gsurvival
    gendless.configure(fg='black',bg='white')
    gsurvival.configure(fg='white',bg='black')
    br_modea=0
    
#konfiguracija gumba
gnaprijed.configure(command=naprijed)
gnazad.configure(command=nazad)
gsave.configure(command=save)
gendless.configure(command=select_endless)
gsurvival.configure(command=select_survival)

select_endless()

mainloop()
