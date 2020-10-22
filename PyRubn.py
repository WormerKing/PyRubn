"""
utf-8

This program is free software.

Coding by:Wormer

"""

#imports

import tkinter as tk,tkinter.messagebox
from tkinter import filedialog as fd
import os,sys
import requests
from bs4 import BeautifulSoup
import socket
from threading import Thread

def linuxorwin(*args):
    git = os.path.join(os.getcwd(),*args)
    os.chdir(git)

def PyRubn():

    def PythonPackage():
        sql.destroy()
        def Anasayfa():
            pencere.destroy()
            PyRubn()
        def remove():
            data1 = değer1.get()
            try:
                __import__(data1)
            except ModuleNotFoundError:
                widget.insert("1.0","Bu modül\nyüklü bile değil\n")
            except ValueError:
                widget.insert("1.0","Havayı silemem\n")
            else:
                widget.insert("1.0","Silinen Paketler\ngeri gelmez\nTekrar yüklemeniz gerekir\n")

                def program():
                    java = tkinter.messagebox.askquestion("Paket Sil","{} Paketini silmek istiyormusun ?".format(data1),icon="warning")
                    if java == "yes":
                        os.system("pip3 uninstall {}".format(data1))
                        os.system("y")
                    else:
                        widget.insert("1.0","Paket Silme İptal\n")
                        pass
                program()


        def info():
            if os.name == "posix":
                a = os.getcwd()
                b = "".join(a+"/İnfo/Python")
                os.chdir(b)
                data1 = değer1.get()
                url = ("https://pypi.org/project/{}/").format(data1)
                try:
                    dosya = open("{}.txt".format(data1),"w")
                    r = requests.get(url)
                    soup = BeautifulSoup(r.text,'html.parser')
                    for tag in soup.find_all('p'):
                        strings = "".join(line.strip() for line in str(tag.string).split("\n"))
                        if strings != "None":
                            dosya.write(strings)
                    os.chdir(a)

                except FileNotFoundError:
                    os.chdir(a)
                except requests.exceptions.ConnectionError:
                    widget.insert("1.0","Bağlantı yok\n")

                else:
                    if data1 == "":
                        widget.insert("1.0","Kütüphane adı boş kalamaz\n")
                    else:
                        widget.insert("1.0","Done\n{}\n".format(url))
                        widget.insert("1.0","Modül hakkında Bilgiye\n{}.txt dosyasından\nulaşabilirsiniz\n".format(data1))
            elif os.name == "nt":
                a = os.getcwd()
                b = "".join(a+"\\İnfo\\Python")
                os.chdir(b)
                data1 = değer1.get()
                url = ("https://pypi.org/project/{}/").format(data1)
                try:
                    dosya = open("{}.txt".format(data1),"w")
                    r = requests.get(url)
                    soup = BeautifulSoup(r.text,'html.parser')
                    for tag in soup.find_all('p'):
                        strings = "".join(line.strip() for line in str(tag.string).split("\n"))
                        if strings != "None":
                            dosya.write(strings)

                    os.chdir(a)

                except FileNotFoundError:
                    os.chdir(a)
                except requests.exceptions.ConnectionError:
                    widget.insert("1.0","Bağlantı yok\n")

                else:
                    if data1 == "":
                        widget.insert("1.0","Kütüphane adı boş kalamaz\n")
                    else:
                        widget.insert("1.0","Done\n{}\n".format(url))
                        widget.insert("1.0","Modül hakkında Bilgiye\n{}.txt dosyasından\nulaşabilirsiniz\n".format(data1))

        def upgrade():
            if os.name == "posix":
                try:
                    os.system("pip3 install -U pip")
                except Exception as e:
                    tkinter.messagebox.showerror(f"Error","Error : {e}")
                else:
                    tkinter.messagebox.showinfo("Pip updated","Python pip updated")
            elif os.name == "nt":
                try:
                    os.system("python -m pip install -U pip")
                except Exception as e:
                    tkinter.messagebox.showerror(f"Error","Error : {e}")
                else:
                    tkinter.messagebox.showinfo("Pip updated","Python Pip updated!")

        def indir():
            rand = ["2","3"]

            data1 = değer1.get()
            data2 = değer2.get()

            if data2 == "":
                widget.insert("1.0","Sürüm boş kalamaz\n")
            elif data1 == "":
                widget.insert("1.0","Kütüphane adı boş kalamaz\n")
            elif data2 not in rand:
                widget.insert("1.0","Lütfen Default Kısma\n(3 veya 2) girin\n")
            else:
                try:
                    __import__(data1)
                except ModuleNotFoundError:
                    os.system("pip{} install {}".format(data2,data1))

                    try:
                        __import__(data1)
                    except ModuleNotFoundError:
                        widget.insert("1.0","Adı {} olan bir modül\nyok !\n".format(data1))
                    except ConnectionError:
                        widget.insert("1.0","Bağlantı yok")
                    else:
                        widget.insert("1.0","Module İnstalled\nİnfo button\nModule info")
                else:
                    widget.insert("1.0","This Module is has dowloand\n")
                    



        pencere = tk.Tk()
        pencere.geometry("380x320")
        pencere.title("Paket Yükleyici v0.1")
        pencere.resizable(False,False)
        pencere.configure(background="GREY")

        değer1 = tk.Entry(font="Verdana 13",fg="AQUA",bg="GREY")
        değer1.place(x=20,y=20)

        değer2 = tk.Entry(font="Verdana 13",fg="BROWN",bg="GREY")
        değer2.place(x=20,y=60)
        değer2.insert(0,"3")

        buton1 = tk.Button(text="İnstall",fg="GREEN",bg="BLACK",font="Verdana 15",command=indir)
        buton1.place(x=20,y=110)

        buton2 = tk.Button(text="Exit",fg="RED",bg="BLACK",font="Verdana 15",command=sys.exit)
        buton2.place(x=20,y=160)

        buton3 = tk.Button(text="Pip upgrade",fg="BLUE",bg="BLACK",font="Verdana 14",command=upgrade)
        buton3.place(x=20,y=210)

        buton4 = tk.Button(text="Remove Pack",font="Verdana 14",fg="AQUA",bg="BROWN",command=remove)
        buton4.place(x=20,y=260)

        lamel1 = tk.Label(text="Module name",fg="RED",bg="GREY")
        lamel1.place(x=250,y=25)

        lamel2 = tk.Label(text="Python source",fg="GREEN",bg="GREY")
        lamel2.place(x=250,y=65)

        widget = tk.Text(height=10,width=30,fg="RED",bg="BLACK")
        widget.place(x=165,y=165)
        widget.config(state="normal")

        wormer = tk.Menu(pencere)

        wormer.add_command(label="Ana sayfa",font="Times 12",foreground="BLACK",command=Anasayfa)
        wormer.add_command(label="Bilgi al",font="Times 12",foreground="Black",command=info)

        pencere.config(menu=wormer)

        if os.name == "posix":
            pencere.iconphoto(False,tk.PhotoImage(file="Photos/pip.png"))
        elif os.name == "nt":
            pencere.iconphoto(False,tk.PhotoImage(file="Photos\\pip.png"))

        pencere.mainloop()

    def Rubyexe():
        def back():
            root.destroy()
            PyRubn()
        def settings():
            pass
        sql.destroy()
        root = tk.Tk()
        root.title("Ruby => exe")
        root.resizable(False,False)
        root.geometry("300x300")

        new = tk.Menu(root)

        new.add_command(label="Home",command=back)
        new.add_command(label="Settind",command=settings)

        root.config(menu=new)
        if os.name == "posix":
            root.iconphoto(False,tk.PhotoImage(file="Photos/ruby.png"))
        elif os.name == "nt":
            root.iconphoto(False,tk.PhotoImage(file="Photos\\ruby.png"))
        root.mainloop()
    def RubyGem():
        sql.destroy()

        def indir():
            gems = entry1.get()
            if gems == "Ruby gem name" or gems == "":
                tkinter.messagebox.showerror("Error","Gem name error")
            else:    
                new = open("Ruby.rb","w")
                new.write(f"a = File.open('Çıktı.txt','w')\nbegin\n\trequire '{gems}'\nrescue LoadError\n\ta.write('False')\nelse\n\ta.write('True')\nend")
                new.close()
                try:
                    os.system("irb Ruby.rb")
                except Exception as e:
                    print(e)
                for i in os.listdir():
                    if i == "Çıktı.txt":
                        with open("Çıktı.txt","r") as hi:
                            for i in hi.readlines():
                                if i == "True":
                                    tkinter.messagebox.showinfo("Gem is was downloaded",f"{gems} is was download")
                                    os.remove("Ruby.rb")
                                    os.remove("Çıktı.txt")
                                else:
                                    if os.name == "posix":
                                        os.system(f"sudo gem install {gems}")
                                        
                                        new = open("Ruby.rb","w")
                                        new.write(f"a = File.open('Çıktı.txt','w')\nbegin\n\trequire '{gems}'\nrescue LoadError\n\ta.write('False')\nelse\n\ta.write('True')\nend")
                                        new.close()
                                        try:
                                            os.system("irb Ruby.rb")
                                        except Exception as e:
                                            print(f"[Error] {e}")
                                        for j in os.listdir():
                                            if j == "Çıktı.txt":
                                                with open("Çıktı.txt","r") as yeni:
                                                    for l in yeni.readlines():
                                                        if l == "True":
                                                            tkinter.messagebox.showinfo("Gems İnstalled","Ruby gem installed")
                                                            os.remove("Ruby.rb")
                                                        elif l == "False":
                                                            tkinter.messagebox.showinfo("Gem not install","Ruby gem is not installed")
                                                            os.remove("Ruby.rb")
                                                        else:
                                                            pass
                                    elif os.name == "nt":
                                        os.system(f"gem install {gems}")
                                        
                                        new = open("Ruby.rb","w")
                                        new.write(f"a = File.open('Çıktı.txt','w')\nbegin\n\trequire '{gems}'\nrescue LoadError\n\ta.write('False')\nelse\n\ta.write('True')\nend")
                                        new.close()
                                        try:
                                            os.system("irb Ruby.rb")
                                        except Exception as e:
                                            print(f"[Error] {e}")
                                        for j in os.listdir():
                                            if j == "Çıktı.txt":
                                                with open("Çıktı.txt","r") as yeni:
                                                    for l in yeni.readlines():
                                                        if l == "True":
                                                            tkinter.messagebox.showinfo("Gems İnstalled","Ruby gem installed")
                                                            os.remove("Çıktı.txt")
                                                            os.remove("Ruby.rb")
                                                        elif l == "False":
                                                            tkinter.messagebox.showinfo("Gem not install","Ruby gem is not installed")
                                                            os.remove("Çıktı.txt")
                                                            os.remove("Ruby.rb")
                                                        else:
                                                            pass                
        def Rbinfo():
            slime = entry1.get()
            if slime == "Ruby gem name" or slime == "":
                tkinter.messagebox.showerror("Gem error","Ruby gem not name")
            else:
                url = f"https://rubygems.org/gems/{slime}"
                if os.name == "posix":
                    hi = os.getcwd()
                    sa = "".join(hi+"/İnfo/Ruby")
                    os.chdir(sa)
                    dosya = open(f"{slime}.txt","w")
                    r = requests.get(url)
                    sopa = BeautifulSoup(r.text,"html.parser")
                    for i in sopa.find_all("p"):
                        if i != "None":
                            dosya.write(i.text)
                    dosya.close()
                    os.chdir(hi)
                elif os.name == "nt":
                    he = os.getcwd()
                    os.chdir("".join(he+"\\İnfo\\Ruby"))
                    os.chdir(he)
        def ekran():
            pencere.destroy()
            PyRubn()

        pencere = tk.Tk()
        pencere.title("Ruby Gem İnstaller v0.1")
        pencere.geometry("380x320")
        pencere.configure(background="GREY")
        pencere.resizable(False,False)

        entry1 = tk.Entry(pencere,font="Verdana 14",bg="GREY",fg="AQUA")
        entry1.place(x=20,y=20)
        entry1.insert(0,"Ruby gem name")

        buton1 = tk.Button(pencere,text="İnstall gem",font="Verdana 14",fg="GREY",bg="GREEN",command=indir)
        buton1.place(x=20,y=120)

        buton2 = tk.Button(pencere,text="Exit",font="Verdana 14",fg="GREY",bg="RED",command=sys.exit)
        buton2.place(x=20,y=160)

        loop = tk.Frame(pencere,width=130,height=380)
        loop.place(x=0,y=200)

        if os.name == "posix":
            tkinter.messagebox.showerror("Permission Error","İf you using Unix/Linux super user do password on terminal.")
        else:
            pass
        alpler = tk.Menu(pencere)

        alpler.add_command(label="Anasayfa",font="Times 12",foreground="BLACK",command=ekran)
        alpler.add_command(label="Bilgi al",font="Times 12",command=Rbinfo)

        pencere.config(menu=alpler)

        if os.name == "posix":
            pencere.iconphoto(False,tk.PhotoImage(file="Photos/gems.png"))
        elif os.name == "nt":
            pencere.iconphoto(False,tk.PhotoImage(file="Photos\\gems.png"))

        pencere.mainloop()
    def Pythonexe():
        sql.destroy()
        def settings():
            pencere.destroy()
            def back():
                new.destroy()
                Pythonexe()
            new = tk.Tk()
            new.title("Python exe settings")
            new.geometry("300x300")
            new.resizable(False,False)
            hi = tk.Label(new,text="Coming soon :)").pack()
                
            swift = tk.Menu(new)

            swift.add_command(label="Back",command=back)

            new.configure(menu=swift)

            new.mainloop()
            
        def geri():
            pencere.destroy()
            PyRubn()


        def çağır():
            file = fd.askopenfilename(title="Select file",filetypes=(("Python files","*.py"),("Ruby","*.rb")))
            print(file)
            
            if os.path.exists(os.path.join(os.getcwd(), "Executable", "Python")):
                w = os.getcwd()
                linuxorwin("Executable","Python")
                os.system(f"pyinstaller --onefile {file}")
                tkinter.messagebox.showinfo("Python => exe","python script convert exe")
                os.chdir(w)
                print(os.getcwd())
            else:
                print("Klasör yok")
        pencere = tk.Tk()
        pencere.geometry("380x320")
        pencere.title("Python => exe")
        pencere.resizable(False,False)
        pencere.configure(background="GREY")

        win = tk.Menu(pencere)

        win.add_command(label="Ana sayfa",command=geri)
        win.add_command(label="Settings",command=settings)

        pencere.configure(menu=win)

        buton = tk.Button(pencere,text="Select File",font="Verdana 14",fg="White",bg="GREEN",command=çağır)
        buton.place(x=20,y=20)



        if os.name == "posix":
            pencere.iconphoto(False,tk.PhotoImage(file="Photos/python.png"))
        elif os.name == "nt":
            pencere.iconphoto(False,tk.PhotoImage(file="Photos\\python.png"))

        pencere.mainloop()

    def Mymessage():
        sql.destroy()
        def geri():
            pool.destroy()
            PyRubn()

        pool = tk.Tk()
        pool.geometry("300x300")
        pool.title("My messages")

        rubyrails = tk.Menu(pool)

        rubyrails.add_command(label="Back",font="Times 15",command=geri)

        pool.configure(menu=rubyrails)
        pool.mainloop()
    def comment():
        def back():
            os.remove("Send.txt")
            loot.destroy()
            PyRubn()
        sql.destroy()
        def message():
            try:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect(("localhost",8131))
            except ConnectionRefusedError:
                tkinter.messagebox.showerror("Connecting lost","Network not connect")
                os.remove("Send.txt")
                back()
            else:
                for i in dosya.readlines():
                    s.sendall(bytes(i,"utf-8"))
                tkinter.messagebox.showinfo("Message sending","This message is sending")
                os.remove("Send.txt")
                back()

        loot = tk.Tk()
        loot.geometry("300x300")

        tkinter.messagebox.showinfo("Message","Please message write is Send.txt")
        dosya = open("Send.txt","w+")

        send = tk.Button(loot,text="send message",command=message)
        send.pack()

        remove = tk.Button(loot,text="Back",command=back).pack()

        if os.name == "posix":
            loot.iconphoto(False,tk.PhotoImage(file="Photos/message.png"))
        elif os.name == "nt":
            loot.iconphoto(False,tk.PhotoImage(file="Photos\\message.png"))

        loot.mainloop()


    sql = tk.Tk()
    sql.title("PyRubn v0.1")
    sql.configure(background="GREY")
    sql.resizable(False,False)
    sql.geometry("300x300")

    Python = tk.Button(text="Python Package İnstaller",font="Verdana 14",fg="BLUE",bg="GREY",command=PythonPackage)

    Ruby = tk.Button(text="Ruby Gems",font="Verdana 14",fg="BLUE",bg="GREY",command=RubyGem)

    Pythonexe = tk.Button(text="Python exe",font="Verdana 14",fg="BLUE",bg="GREY",command=Pythonexe)

    Rubyexe = tk.Button(text="Ruby exe",font="Verdana 14",fg="BlUE",bg="GREY",command=Rubyexe)

    Python.grid(row=0,column=0,pady=2)
    Ruby.grid(row=1,column=0,pady=5)
    Pythonexe.grid(row=2,column=0,pady=5)
    Rubyexe.grid(row=3,column=0,pady=5)

    kotlin = tk.Menu(sql)

    kotlin.add_command(label="Fixed bug",font="Times 15",command=comment)
    kotlin.add_command(label="Exit",font="Times 15",foreground="RED",command=sys.exit)
    kotlin.add_command(label="Message",font="Times 15",foreground="BLUE",command=Mymessage)

    sql.config(menu=kotlin)

    if os.name == "posix":
        sql.iconphoto(False,tk.PhotoImage(file="Photos/tool.png"))
    elif os.name == "nt":
        sql.iconphoto(False,tk.PhotoImage(file="Photos\\tool.png"))

    sql.mainloop()

if __name__ == "__main__":
    PyRubn()
else:
    print("This file is not Module")
    sys.exit()
