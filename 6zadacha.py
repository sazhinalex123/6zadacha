import os
k=0
a=0
p=0
s=0
filename="zxc.txt"
def File(filename):
    try:
        if(os.stat(filename).st_size>=0):
            f=open(filename,"r")
            check=f.read()
            if(len(check)==0):
                print("Pustoi fail")
                f.close()
                raise Exception("Pustoi fail iskluch.")
            f.close()
            return 0
    except Exception:
        print("Oshibka")
        return 1
err=File(filename)
if err!=0:
    exit()

with open("zxc.txt") as f:
    for t in f:
        l=len(t)
        if l==1:
            print("1 chislo")
            exit()
        print("t=",t)
        for i in t.split(' '):
            if k==0:
                a=int(i)
                k=k+1
                print("a=",a)
            else:
                b=int(i)
                if b>a:
                    p=p+1
                    print("p=",p)
                elif b<a:
                    s=s+1
    if s<p:
        print("bolshih bolshe")
    elif s>p:
        print("menshih bolshe")
    elif s==p:
        print("NEt takih")
f.close()
