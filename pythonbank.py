from tkinter import *
nish=Tk()
nish.configure(bg='yellow')
count=0
def firstrec():
    f=open("bankdb.txt",'r')       
    k=f.readlines()[0]
    j=k.split()
    print(j)
    s1.set(j[0])
    s2.set(j[1])
    s3.set(j[2])
    s4.set(j[3])
    s5.set(j[4])
    f.close()
def lastrec():
    f=open("bankdb.txt",'r')       
    de=sum(1 for i in open("bankdb.txt"))
    print(de)
    k=f.readlines()[de]
    j=k.split()
    s1.set(j[0])
    s2.set(j[1])
    s3.set(j[2])
    s4.set(j[3])
    s5.set(j[4])
    f.close()
def addrec():
    f=open('bankdb.txt','a')            
    bankbranchno=s1.get()
    accountname=s2.get()
    accountid=s3.get()
    balance=s4.get()
    adhaarcardno=s5.get()
    f.writelines(bankbranchno.ljust(20)+accountname.ljust(20)+accountid.ljust(20)+balance.ljust(20)+adhaarcardno.ljust(20)+"\n")
    f.close()
def delrec():
    prt_rcd=[s1.get(),s2.get(),s3.get(),s4.get(),s5.get()]
    f=open('bankdb.txt','r')           
    lines=f.readlines()
    print(lines)
    print(prt_rcd)
    f.close()
    f=open('bankdb.txt','w')           
    for i in lines:
        m=i.split()
        print(m)
        if(m!=prt_rcd):
             f.writelines(m[0].ljust(20)+m[1].ljust(20)+m[2].ljust(20)+m[3].ljust(20)+m[4].ljust(20)+"\n")
    f.close()
def updaterec():
    a1=s1.get()
    a2=s2.get()
    a3=s3.get()
    a4=s4.get()
    a5=s5.get()
    f=open('bankdb.txt','r')          
    h=f.readlines()
    f.close()
    f=open('bankdb.txt','w')          
    flag=0
    for i in h:
        j=i.split()
        if(j[0]!=a1):
            f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(10)+"\n")
    
        else:
            f.writelines(a1.ljust(20)+a2.ljust(20)+a3.ljust(20)+a4.ljust(10)+a5.ljust(10)+"\n")
            flag=1
    f.close()
def searchrec():
    var=s1.get()
    f=open('bankdb.txt','r')         
    h=f.readlines()
    for i in h:
        j=i.split()
        if(j[0]==var): 
            print(j)
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
    f.close()  
def nextrec():
    f=open('bankdb.txt','r')         
    i=0
    global count
    while(i<=count):
        l=f.readline()
        i=i+1
    info=l.split()
    s1.set(info[0])	
    s2.set(info[1])
    s3.set(info[2])
    s4.set(info[3])
    s5.set(info[4])
    count=count+1
    f.close()
def prevrec():
    global count
    i=0
    count=count-1
    print(count)
    f=open("bankdb.txt","r")        
    while(i<=count-1):
        l=f.readline()
        i=i+1
        print(l)
    rec=l.split()
    s1.set(rec[0])
    s2.set(rec[1])
    s3.set(rec[2])
    s4.set(rec[3])
    s5.set(rec[4])

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
l1=Label(nish,text="BANK BRANCH NO.")
l2=Label(nish,text="ACCOUNT NAME")
l3=Label(nish,text="ACCOUNT ID")
l4=Label(nish,text="BALANCE")
l5=Label(nish,text="ADHAAR CARD NO.")
t1=Entry(nish,textvariable=s1)
t2=Entry(nish,textvariable=s2)
t3=Entry(nish,textvariable=s3)
t4=Entry(nish,textvariable=s4)
t5=Entry(nish,textvariable=s5)
b1=Button(nish,text="ADD",command=addrec)
b2=Button(nish,text="DELETE",command=delrec)
b3=Button(nish,text="UPDATE",command=updaterec)
b4=Button(nish,text="SEARCH",command=searchrec)
b5=Button(nish,text="NEXT",command=nextrec)
b6=Button(nish,text="PREVIOUS",command=prevrec)
b7=Button(nish,text="FIRST",command=firstrec)
b8=Button(nish,text="LAST",command=lastrec)

l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
l4.grid(row=4,column=1)
l5.grid(row=5,column=1)	
t1.grid(row=1,column=2)
t2.grid(row=2,column=2)
t3.grid(row=3,column=2)
t4.grid(row=4,column=2)
t5.grid(row=5,column=2)

b1.grid(row=7,column=1)
b2.grid(row=7,column=2)
b3.grid(row=7,column=3)
b4.grid(row=8,column=3)
b5.grid(row=8,column=1)
b6.grid(row=8,column=2)
b7.grid(row=9,column=1)
b8.grid(row=9,column=2)

nish.mainloop()

