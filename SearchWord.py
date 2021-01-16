## ORIGINAL
from GetImage import p,ANS,HM_ROW,COL

from tkinter import *

def fun():


    global first


    rows = HM_ROW#14#int(e1.get())  # int(input('No of rows :'))
    column = COL#16#int(e2.get())
    s=p
    s = list(s)

    s5=s
    s5=list(s5)
    l2=[]
    a=0
    for i in range(rows):
        C = []
        for j in range(column):
            C.append(s[a])
            a = a + 1
        l2.append(C)

    for i in range(len(s)):
        c = s.count(s[i])
        cc = 0
        if c > 1:
            for j in range(i + 1, len(s)):

                if s[i] == s[j]:

                    s[j] = s[j] + str(cc)
                    cc = cc + 1

    # 14,16

    #s=list(s)
    #print(s)
    #rows = int(e1.get())  # int(input('No of rows :'))
    #column = int(e2.get())  # int(input('No of coloumn :'))
    l = []
    a = 0

    for i in range(rows):
        C = []
        for j in range(column):
            C.append(s[a])
            a = a + 1
        l.append(C)
    #print('llll:',l)

    MM = l2
    My_ans = []
    answer = []
    #Answer = ['VYTW','Witch', 'Black', 'Orange', 'Ghost', 'Bat', 'Candy', 'Trick', 'Teat ', 'Broom']
    #Answer=['LNC']#['NJZ','BOK','CPG','MIK']
    #Answer = ['RSRRT','ERD','AJTTN','UNYA','GIR','RRAL','RTI','EERL','TOAST','RESU','AGIA','ASTRONOMER', 'ATTAR', 'CLAMORINC','DINCO','DYING', 'ELECTOR', 'ENDOWS', 'FLITS','ALSO','ALTER','APPAL','ASKS','BAWL','BRISKS','BURG','BUXOM','CREMATES','DETACH']
    #Answer=['ASTRONOMER','APPAL','TOAST','ENDOWS','ATTAR', 'CLAMORINC','DINCO','DYING', 'ELECTOR', 'FLITS','ALSO','ALTER','ASKS','BAWL','BRISKS','BURG','BUXOM','CREMATES','DETACH']
    Answer=ANS
    #print(Answer)
    # Answer=['KLM','KHI','KMS']
    for elementes in Answer:
        answer.append(elementes.upper())

    #####                                        Horizamtal Search                             ####################

    for k in range(rows):
        for i in range(rows):
            for j in range(i, column):
                m = []
                L = (l2[k][i:j + 1])
                h = ''.join(L)
                #print('ho ans:',h)
                if h in answer or h[::-1] in answer:
                    for ans in range(i, j + 1):
                        ma = [k, ans]
                        My_ans.append(ma)
                    My_ans.append('*')


    # print('HOR MY ANS:',My_ans)
   # print('HOR MY ANS:',My_ans)
    #####                                     VARTICAL Search                            #####################

    L = []
    mydict = {}
    for k in range(column):
        mydict = {}
        for i in range(column):
            m = []
            m2 = []
            for j in range(i, rows):
                v = l[j][k]
                mydict[v] = [j, k]
                m2.append(l[j][k])
                m.append(l[j][k][0])
                mm1=''.join(m)
                for vr1 in range(len(mm1)):
                    for vr2 in range(len(mm1)):
                        if mm1[vr1:vr2+1] in answer or mm1[vr1:vr2+1][::-1] in answer:
                            for e22 in m2[vr1:vr2+1]:
                                My_ans.append(mydict[e22])
                            My_ans.append('*')

    #########################  TRIANGLE (NORTH -EAST)  ########################

    z=2
    for nn in range(2):
        if nn==1:
            z=rows-1
            z=-z
        for k in range(column):  # 3 so as to reduce m which wil be alone of no use
            dicm = {}
            Z = []
            m3 = []
            for i in range(0, rows):
                for j in range(column):
                    if j == i + z:
                        m3.append(l[i][j])
                        Z.append(l[i][j][0])
                        ZZ = ''.join(Z)
                        dicm[l[i][j]] = [i, j]
                        for utl9 in range(len(ZZ)):
                            for utl8 in range(len(ZZ)):
                                if ZZ[utl9:utl8 + 1] in answer or ZZ[utl9:utl8 + 1][::-1] in answer:
                                    for e111 in m3[utl9:utl8 + 1]:
                                        My_ans.append(dicm[e111])
                                    My_ans.append('*')

                        break
            z = z + 1

    ######                                              LOWER Triangle (SOUTH - EAST)                            ##################

    a=1
    p2=1
    for kk1 in range(2):
        if kk1==1:
            p2=-1
            a=0
        for i in range(rows-1, -1, -1):
            if kk1==0:
                i = rows - 1
            n = []
            dind = {}
            m5 = []
            for j in range(a, i + abs(column - rows) + p2):  # devlop i+3
                if(i>=HM_ROW or j >= COL):
                    break
                if kk1==1:
                    a=0


                m5.append((l[i][j]))
                n.append(l[i][j][0])
                c = ''.join(n)
                dind[l[i][j]] = [i, j]
                i = i - 1
                for rltl9 in range(len(c)):
                    for rltl8 in range(len(c)):
                        if c[rltl9:rltl8 + 1] in answer or c[rltl9:rltl8 + 1][::-1] in answer:
                            for e113 in m5[rltl9:rltl8 + 1]:
                                My_ans.append(dind[e113])
                            My_ans.append('*')
            if kk1==0:
                a = a + 1

            #print('C:',c)


    ##print(My_ans)
    #####                                        TKINTER  APPLIED                            #######################

    import random  ##      To choose random colour for printing        ###

    ####                                       Forth  Window                                  ######################

    def first():  ####     This function Genetets the final Window       ###



        window = Tk()
        window.title(' * SOLVED * ')
        window.geometry('600x700+400+100')
        fram1 = Frame(window)
        frame21 = Frame(window)
        fram1.pack(side=TOP)
        frame21.pack(side=BOTTOM, fill=BOTH)
        a = 0

        #print(My_ans)
        l = My_ans

        colour = ['#ffd966', '#03a9f4', '#03a9f4','#ff9800', '#ff5722', '#e51c23']
        colour = random.choice(colour)

        for i in range(rows):
            c = a
            m = []

            for j in range(column):
                Label(fram1, text=s5[j + c], fg='black', font=10, bg='light gray').grid(column=j, row=i)
                a = a + 1

        for el in l:
            if el == '*':
                colour = random.choice(['#ffd966', '#03a9f4', '#ff9800', '#ff5722', '#e51c23'])
                continue

            else:
                # colour = random.choice(['#ffd966', '#03a9f4', '#ff9800', '#ff5722', '#e51c23'])
                Button(fram1, text=l2[el[0]][el[1]], bg=colour, font=7, bd=3).grid(column=el[1], row=el[0])

        Button(frame21, text='E X I T'.center(20), font=('bold', 10), bd='10', relief='sunken', bg='red',
               command=lambda: window.destroy()).grid(column=column + 15, row=rows + 15)
        mainloop()

        ####                                 Third  Window                                       #############

    w3 = Tk()
    w3.geometry('600x700+500+10')
    w3.title('Given INPUT ')
    fram=Frame(w3)
    frame2=Frame(w3)
    fram.pack(side=TOP)
    frame2.pack(side=BOTTOM,fill=BOTH)

    for i in range(rows):
        for j in range(column):  # ,font=('bold',15),bg='red',relief='sunken',
            b = Button(fram, text=MM[i][j], fg='black', font=(4)).grid(column=j, row=i)  # column+  first()
    Button(frame2, text='S O L V E'.center(17), fg='white', bg='red', bd='10', relief='sunken',
           command=lambda: first()).grid()

    w3.mainloop()

    ####                                    Secound   Window                                          ###############


fun()
