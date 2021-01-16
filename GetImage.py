
import pyautogui
from skimage.filters import threshold_mean,threshold_otsu,threshold_triangle
import pytesseract
import cv2

def preprocess(IMG):
    img=IMG.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return  img
def get_text(img):
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
    custom_oem_psm_config = r'--oem 3 --psm 6'
    return pytesseract.image_to_string(img, config=custom_oem_psm_config)

def Win(name):
    global X,Y,W,H
    from tkinter import Tk, Button
    root = Tk()
    root.title(name)
    root.geometry("300x300+100+100")
    root.attributes('-alpha', 0.85)

    flag=0
    def click():
        global X, Y, W, H,flag
        X, Y, W, H = (root.winfo_x(), root.winfo_y()+40, root.winfo_width(), root.winfo_height()-28)
        root.destroy()
    b = Button(text="Get position", command=click)
    b.pack(side='bottom')
    # if(flag==1):
    #     root.destroy()
    root.mainloop()
    #print('VAL IN SI : ',(X, Y, W, H))
    return (X, Y, W, H)

val=Win('SEARCH WORD GRID')
image=pyautogui.screenshot(region=val)


'''                         If You Want the BOT THO SOLVE THE WHOLE GAME SET VAL=0                 '''

VAL=0

def get_Answ(tital,img_name):

    ans=Win('{}'.format(tital))
    ans=pyautogui.screenshot(region=ans)
    ans.save('{}.png'.format(img_name))
    ans1=cv2.imread('{}.png'.format(img_name))
    return  preprocess(ans1)

ans1=get_Answ('ANSWER','ans1')
ans2=get_Answ('If More Ans ??','ans2')

txt=get_text((ans1))
txt=txt+get_text(ans2)

#print('ANININ :\n',txt)
def get_ans(a):
    ll = []
    for i in range(len(a)):
        ll.append(a[i])

    ll = ''.join(ll)
    ll = ll.split('\n')
    ANS = ll
    ANS2 = []
    for ans in ANS:
        if (len(ans) != 0):
            ANS2.append(ans)

    return ANS2
ANS=get_ans(txt)


image.save('test.png')
img0=cv2.imread('test.png')
img=preprocess(img0)

# plt.imshow(img,cmap='gray')
# plt.show()


img2=preprocess(img0)
img3=preprocess(img0)
th=threshold_mean(img)
img=img>th#-5
th2=threshold_triangle(img2)
img2=img2>th2
th3=threshold_otsu(img3)
img3=img3>th3


p=get_text(img)
p2=get_text(img2)
p3=get_text(img3)

# p=pytesseract.image_to_string(img, config=custom_oem_psm_config)
# p2=pytesseract.image_to_string(img, config=custom_oem_psm_config)
# p3=pytesseract.image_to_string(img, config=custom_oem_psm_config)

# print('\n',p,len(p),'\n\n')
# print(p2,'\n',len(p2))
# print(p3,'\n',len(p3))


if len(p2)<len(p) and len(p2)<len(p3):
    p=p2
elif len(p3)<len(p) and len(p3)<len(p):
    p=p3
else:
    p=p

#print('Final len :',len(p))

p=p.split('\n')

col=len(p[0])
#print('No of col is : \n',p)

for row in range(len(p)):

    l=len(p[row])
    x=list(p[row])
    for i in  p[row]:
        if i==' ' :
            x.remove(' ')
        elif i=="'":
            x.remove("'")
        elif(i=='('):
            x.remove("(")
        elif(i=='/'):
            x.remove("/")
        elif(i=='|'):
            ind=x.index(i)
            x[ind]='I'
        elif ((i.isalpha()) != True):
            x.remove(i)
    x=''.join(x)
    p[row]=x
    if l>col:
        p[row]=list(p[row])


        for elem in p[row]:

            if elem=='!':
                p[row].remove('!')
            elif elem=='|':
                ind=p[row].index('|')
                p[row][ind]='I'
                #p[row].remove('|')
            elif elem==')':
                p[row].remove(')')
            elif((elem.isalpha())!=True):
                p[row].remove(elem)

        p[row]=''.join(p[row])

# print('HMMM colm : ',len(p[0]),len(p[1]),len(p[2]))
# print('Final \n\n',p)


COL=[]
for r in p:
    COL.append(len(r))


col=max(COL,key=COL.count)
COL=col

HM_ROW=len(p)
for r in range(len(p)):
    if len(p[r])>col:
        #v=col-len(p[r])
        p[r]=p[r][:col]
    #print(len(p[r]),p[r])
    elif len(p[r])<col:
        for _ in range(len(p[r]),col):
            p[r]=p[r]+'A'
        #p[r]=p[r]+"A"

p=''.join(p)
p=p.upper()
#print('@@@@@@@@@@@@@@')


p=list(p)

#print('########')
#print(p)

for e in range(len(p)):

    if p[e]=='1' :
        p.pop(e)
        p.insert(e,'I')

    if p[e] == '!':
        p.pop(e)
        p.insert(e, 'I')
    if p[e] == '|':
        p.pop(e)
        p.insert(e, 'I')
    if p[e]=='0':
        p.pop(e)
        p.insert(e, 'O')
    if p[e]=='2':
        p.pop(e)
        p.insert(e, 'Z')
    if p[e]==')':
        p.pop(e)
        p.insert(e, 'O')
    if p[e]=='}':
        p.pop(e)
        p.insert(e, 'J')

p=''.join(p)
p=p[:HM_ROW*COL]


