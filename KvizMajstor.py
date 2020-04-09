#importanje bitnih library-a
from tkinter import *
import os
from random import *
from tkinter import messagebox

#stvaranje tkinter prozora
root=Tk()
root.resizable(width=False, height=False)
root.title("Kviz Majstor")
root.configure(background='white')

#konfiguracija grid-a
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#stvaranje varijabli i lista
lkviz=[]
settings=[]
tocan_odg=0
selected_odg=0
first=1
br_tocnih=0
br_netocnih=0
mode=0
br_joker=0
br_50=0
odg_lista=[]
b50_akt=0
odg_open=[]
game_end=0


odg_lista.append(0)
odg_lista.append(0)
odg_open.append(1)
odg_open.append(1)
odg_open.append(1)
odg_open.append(1)
odg_open.append(1)


#stvaranje glavnih gumba i pitanja za igru
lpitanje=Label(root,text="Pitanje??")
b_odg1=Button(root,text="ODG1")
b_odg2=Button(root,text="ODG2")
b_odg3=Button(root,text="ODG3")
b_odg4=Button(root,text="ODG4")
b_fin=Button(root,text="--->")

#stvaranje sporednih gumba
lime=Label(root,text='TEST')
ltocni=Label(root,text='0')
lnetocni=Label(root,text='0')
ljoker=Label(root,text='0/0')
b_joker=Button(root,text='Joker')
l50=Label(root,text='0/0')
b_50=Button(root,text='50/50')
ldno=Label(root)


#funkcija kraja igre
def game_over():
    global b_odg1
    global b_odg2
    global b_odg3
    global b_odg4
    global b_fin
    global lpitanje
    global ldno
    lpitanje.destroy()
    b_odg1.destroy()
    b_odg2.destroy()
    b_odg3.destroy()
    b_odg4.destroy()
    b_fin.destroy()
    ldno.configure(text="GAME OVER")
    print("end")


#odabir kviza
def select_kviz():
    global fkviz
    global b1
    b1.destroy()
    lbox.destroy()
    start_kviz()
    
#read teksta iz .txt-a
def showcontent(event):
    global fkviz
    global lkviz
    x = lbox.curselection()[0]
    file = lbox.get(x)
    with open('./Kvizovi/'+file) as file:
        file = file.read() 
    fkviz=file
    lkviz=file.split('\n')
    #print(lkviz)




#POČETAK KVIZA
def start_kviz():
    global lkviz
    global settings
    global b_odg1
    global b_odg2
    global b_odg3
    global b_odg4
    global lpitanje
    global b_fin
    global br_joker
    global br_50
    global mode
   # print("uspjeh")
    settings=lkviz[0].split()
    mode=int(settings[1])
    br_joker=int(settings[2])
    br_50=int(settings[3])
    
    #STVORI CIJELI KVIZ
       
    lpitanje.grid(row=0,column=0,rowspan=2,columnspan=4,sticky="NESW")
    lpitanje.config(height=5,background='white')
        
    b_odg1.grid(row=2,column=0,rowspan=2,columnspan=2,sticky=N+S+E+W)
    b_odg2.grid(row=2,column=2,rowspan=2,columnspan=2,sticky=N+S+E+W)
    b_odg3.grid(row=4,column=0,rowspan=2,columnspan=2,sticky=N+S+E+W)
    b_odg4.grid(row=4,column=2,rowspan=2,columnspan=2,sticky=N+S+E+W)
    bw=50
    bh=4
    bpx=0
    bpy=0
    bbg='white'
    b_odg1.config(width=bw,height=bh,padx=bpx,pady=bpy,background=bbg)
    b_odg2.config(width=bw,height=bh,padx=bpx,pady=bpy,background=bbg)
    b_odg3.config(width=bw,height=bh,padx=bpx,pady=bpy,background=bbg)
    b_odg4.config(width=bw,height=bh,padx=bpx,pady=bpy,background=bbg)
    
    b_fin.grid(column=0,columnspan=4,row=6)
    b_fin.config(width=10,bg='light green')
    

    lime.grid(row=0,column=4,columnspan=2,rowspan=2,sticky=N+S+E+W)
    ltocni.grid(row=2,column=4,rowspan=2,sticky=N+S+E+W)
    lnetocni.grid(row=2,column=5,rowspan=2,sticky=N+S+E+W)
    ljoker.grid(row=4,column=4,sticky=N+S+E+W)
    b_joker.grid(row=4,column=5,sticky=N+S+E+W)
    l50.grid(row=5,column=4,sticky=N+S+E+W)
    b_50.grid(row=5,column=5,sticky=N+S+E+W)
    ldno.grid(row=6,column=4,columnspan=2,sticky=N+S+E+W)

    lime.config(text=(settings[0].replace("_"," ")))
    ltocni.config(width=10,background='light green')
    lnetocni.config(width=10,background='red')
    ljoker.config(text=str(br_joker))
    l50.config(text=str(br_50))
    new_question()


#NOVO PITANJE
def new_question():
    global lkviz
    global lpitanje
    global b_odg1
    global b_odg2
    global b_odg3
    global b_odg4
    global tocan_odg
    global selected_odg
    global odg_lista50
    global b50_akt
    global odg_open
    odg_open[1]=1
    odg_open[2]=1
    odg_open[3]=1
    odg_open[4]=1
    b50_akt=0
    selected_odg=0
    
    l=[1,2,3,4]
    shuffle(l)
    tocan_odg=l[0]
    odg_lista[0]=l[1]
    odg_lista[1]=l[2]
    
    reset_b()
    
    pitanje_poz=randint(0,int((len(lkviz)-1)/5)-1)*5
    print(pitanje_poz)
    odgovori=[]
    pitanje=lkviz[pitanje_poz]
    
    for i in range(4):
        odgovori.append(lkviz[pitanje_poz+1+i])
    for i in range(5):
        del lkviz[pitanje_poz]
    
    for i in range(4):
        if l[i]==1:
            b_odg1.config(text=odgovori[i])
        if l[i]==2:
            b_odg2.config(text=odgovori[i])
        if l[i]==3:
            b_odg3.config(text=odgovori[i])
        if l[i]==4:
            b_odg4.config(text=odgovori[i])
            
    lpitanje.config(text=pitanje)
    
    print(pitanje)
    print(odgovori)
    print(tocan_odg)


#resetiranje oblikovanja gumba
def reset_b():
    global b_odg1
    global b_odg2
    global b_odg3
    global b_odg4
    global odg_open
    if odg_open[1]==1:
        b_odg1.config(background='white',fg='black')
    if odg_open[2]==1:
        b_odg2.config(background='white',fg='black')
    if odg_open[3]==1:
        b_odg3.config(background='white',fg='black')
    if odg_open[4]==1:
        b_odg4.config(background='white',fg='black')


#odabir prvog odgovora
def select_odg1():
    global selected_odg
    global b_odg1
    global first
    global odg_open
    if first and odg_open[1]:
        reset_b()
        selected_odg=1
        print(1)
        b_odg1.config(background='black',fg='white')

#odabir drugog odgovora
def select_odg2():
    global selected_odg
    global b_odg2
    global odg_open
    if first and odg_open[2]:
        reset_b()
        selected_odg=2
       # print(2)
        b_odg2.config(background='black',fg='white')

#odabir trećeg odgovora
def select_odg3():
    global selected_odg
    global b_odg3
    global odg_open
    if first and odg_open[3]:
        reset_b()
        selected_odg=3
       # print(3)
        b_odg3.config(background='black',fg='white')

#odabir četvrtog odgovora
def select_odg4():
    global selected_odg
    global b_odg4
    global odg_open
    if first and odg_open[4]:
        reset_b()
        selected_odg=4
       # print(4)
        b_odg4.config(background='black',fg='white')

#korištenje jokera
def use_joker():
    global br_joker
    global ljoker
    global first
    if first==1:
        if br_joker>0:
            br_joker+=-1
            reset_b()
            new_question()
            ljoker.configure(text=str(br_joker))
        else:
            messagebox.showwarning("Čekaj malo!!", "Nemaš više jokera.")


#korištenje 50/50
def use_50():
    global br_50
    global l50
    global first
    global b50_akt
    global odg_open
    global odg_lista
    global b_odg1
    global b_odg2
    global b_odg3
    global b_odg4
    global selected_odg
    if first==1 and b50_akt==0:
        if br_50>0:
            selected_odg=0
            b50_akt=1
            br_50+=-1
            reset_b()
            if odg_lista[0]==1 or odg_lista[1]==1:
                b_odg1.config(fg='white')
                odg_open[1]=0
            if odg_lista[0]==2 or odg_lista[1]==2:
                b_odg2.config(fg='white')
                odg_open[2]=0
            if odg_lista[0]==3 or odg_lista[1]==3:
                b_odg3.config(fg='white')
                odg_open[3]=0
            if odg_lista[0]==4 or odg_lista[1]==4:
                b_odg4.config(fg='white')
                odg_open[4]=0
            l50.configure(text=str(br_50))
        else:
            messagebox.showwarning("Čekaj malo!!", "Nemaš više 50/50.")


#"zaključivanje" odgovora
def fin_odg():
    global selected_odg
    global tocan_odg
    global first
    global lpitanje
    global b_odg1
    global b_odg2
    global b_odg3
    global b_odg4
    global br_tocnih
    global br_netocnih
    global ltocni
    global lnetocni
    global mode
    global lkviz
    global game_end
    end_it=0

    if selected_odg==0:
        messagebox.showwarning("Čekaj malo!!", "Prvo odaberi odgovor.")
    else:
        if first:
            if selected_odg==tocan_odg:
                root.config(background='light green')
                lpitanje.config(background='light green')
                br_tocnih+=1
                ltocni.config(text=str(br_tocnih))
                if len(lkviz)<5:
                    game_end=1
            else:
                root.config(background='red')
                lpitanje.config(background='red')
                if mode==1:
                    br_netocnih+=1
                    lnetocni.config(text=str(br_netocnih))
                else:
                    end_it=1
                if len(lkviz)<5 or end_it:
                    game_end=1
            if tocan_odg==1:
                b_odg1.config(fg='black',background='light green')
            if tocan_odg==2:
                b_odg2.config(fg='black',background='light green')
            if tocan_odg==3:
                b_odg3.config(fg='black',background='light green')
            if tocan_odg==4:
                b_odg4.config(fg='black',background='light green')
            first=0
        else:
            if game_end:
                game_over()
            else:
                root.config(background='white')
                lpitanje.config(background='white')
                new_question()
                first=1
        


#stvaranje liste file-ova
flist = os.listdir('./Kvizovi')
 
#stvaranje listbox-a i dodavanje liste file-ova
lbox = Listbox(root)
lbox.pack()
for item in flist:
    lbox.insert(END, item)
lbox.bind("<<ListboxSelect>>", showcontent)

    
#stvaranje gumba za selekciju
b1 = Button(root,text="SELECT", command=select_kviz)
b1.pack()

#dodavanje funkcija gumbima
b_odg1.configure(command=select_odg1)
b_odg2.configure(command=select_odg2)
b_odg3.configure(command=select_odg3)
b_odg4.configure(command=select_odg4)
b_fin.configure(command=fin_odg)
b_50.configure(command=use_50)
b_joker.configure(command=use_joker)

mainloop()
