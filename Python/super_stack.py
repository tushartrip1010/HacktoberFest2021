def superStack(operations):
    a=[]
    c=[]
    for i in operations:
        if i=='pop':
            a.pop()
            if len(c)>1:
                c[-2]=int(c[-1])+int(c[-2])
            c.pop()
            if len(a)==0:
                print("EMPTY")
            else:
                print(int(a[-1])+int(c[-1]))
        else:
            b=i.split()
            if b[0]=='push':
                a.append(b[1])
                c.append(0)
                print(int(a[-1])+int(c[-1]))
            elif b[0]=='inc':
                c[int(b[1])-1]=int(c[int(b[1])-1)+int(b[2])
                print(int(c[-1])+int(a[-1]))
