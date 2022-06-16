from tkinter import *
import random

window = Tk()
window.title("가대 음식점 선택 프로그램_201720908 이경연")
photo = PhotoImage(file="name2.gif")
imageLabel = Label(window, image=photo).pack()


#정보
dic={'학식':{'시간대':'','대기 시간':'','가격':''},
     '맘스터치':{'시간대':'','대기 시간':'','가격':''},
     '쌀국수':{'시간대':'','대기 시간':'','가격':''},
     '메밀꽃':{'시간대':'','대기 시간':'','가격':''},
     '지지고':{'시간대':'','대기 시간':'','가격':''},
     '스페이스':{'시간대':'','대기 시간':'','가격':''},
     '가대돈스':{'시간대':'','대기 시간':'','가격':''},

     '학교 가는 길':{'시간대':'','대기 시간':'','가격':''},
     '신동':{'시간대':'','대기 시간':'','가격':''},
     '크라이치즈버거':{'시간대':'','대기 시간':'','가격':''},
     '승록이네':{'시간대':'','대기 시간':'','가격':''},

     '복사골':{'시간대':'','대기 시간':'','가격':''},
     '청진동':{'시간대':'','대기 시간':'','가격':''},
     '서브웨이':{'시간대':'','대기 시간':'','가격':''},
     '신의주':{'시간대':'','대기 시간':'','가격':''},
     '홍콩반점':{'시간대':'','대기 시간':'','가격':''}}

#거리 선택
schin=set(['학식','맘스터치','쌀국수','메밀꽃','지지고','스페이스','가대돈스'])
schout=set(['학교 가는 길','신동','크라이치즈버거','승록이네'])
subin=set(['복사골','청진동','서브웨이','신의주','홍콩반점'])

#시간 선택
half=set(['학식','맘스터치','쌀국수'])
hour=set(['학식','맘스터치','쌀국수','메밀꽃','지지고','스페이스',
          '가대돈스','학교 가는 길','신동','크라이치즈버거','승록이네'])
thour=set(['학식','맘스터치','쌀국수','메밀꽃','지지고','스페이스',
           '가대돈스','학교 가는 길','신동','크라이치즈버거','승록이네',
           '복사골','청진동','서브웨이','신의주','홍콩반점'])

#밥 종류 선택
rice=set(['학식','지지고','메밀꽃','스페이스','신동','신의주','복사골','청진동'])
noodle=set(['쌀국수','학교 가는 길','승록이네','홍콩반점'])
elseT=set(['맘스터치','가대돈스','크라이치즈버거','서브웨이'])

#음식 선택
western=set(['맘스터치','가대돈스','크라이치즈버거','서브웨이'])
snack=set(['학식','지지고','메밀꽃','스페이스','신의주','복사골','청진동','학교 가는 길','승록이네'])
elseTh=set(['쌀국수','신동','홍콩반점'])

#색깔 선택
color=['salmon','pink','lightgreen','yellow','lightblue','plum','orange']


#첫번째 버튼_음식 메뉴 결정하기
def option1():
    op=['학교 내','학교 밖','역곡역 근처']
    opt=['30분','1시간','2시간']

    global a
    a=Tk()
    a.title("음식 메뉴 결정하기1")

    var=IntVar(a)
    var2=IntVar(a)
   
    def sel():
        global total1
        total1=''
        global select
        select="당신이 선택한 사항1 : "+op[var.get()]
        print(var.get())
       
        if var.get()==0:
            total1=schin
            print(total1)
        if var.get()==1:
            total1=schout
            print(total1)
        if var.get()==2:
            total1=subin
            print(total1)
            
        label.config(text=select)
        label.pack(anchor=W)
        
    def sele():
        global total2
        total2=''
        
        select2="당신이 선택한 사항2 : "+opt[var2.get()]
        print(var2.get())
        
        if var2.get()==0:
            total2=half
            print(total2)
        if var2.get()==1:
            total2=hour
            print(total2)
        if var2.get()==2:
            total2=thour
            print(total2)
       
        global total3
        total3=total1&total2
        
        print('결과 : '+str(total3))
        
        if total3==set():
            select3="다시 선택해주세요"
            label3.config(text=select3)
            label3.pack(side='top')
        if total3!=set():
            select3="다음 단계로 넘어가세요"
            label3.config(text=select3)
            label3.pack(side='top')

        label2.config(text=select2)
        label2.pack(anchor=W)

    la=Label(a,text="반드시 1번을 선택 후 2번을 선택하세요").pack(anchor=W)
    la1=Label(a,text="주의) 만약 1번을 재선택할시 2번 다시 누르기!\n").pack(anchor=W)
    l1=Label(a,text="1. 거리 선택").pack(anchor=W)
    for i in range(0,3):
        Radiobutton(a,text=str(i+1)+'.'+op[i],value=i, variable=var,command=sel).pack(anchor=W)
        
    label=Label(a).pack()

    l2=Label(a,text="2. 시간 선택").pack(anchor=W)
    for j in range(0,3):
        Radiobutton(a,text=str(j+1)+'.'+opt[j],value=j, variable=var2,command=sele).pack(anchor=W)

    label=Label(a).pack(anchor=W)
    
    label=Label(a)
    label.pack()
    
    label2=Label(a)
    label2.pack()

    label3=Label(a)
    label.pack(side='top')
    
    label4=Label(a).pack()
    b1=Button(a,text="다음",command=option2).pack()

    a.mainloop()

def option2():
    op=['밥','면','기타']
    opt=['양식','분식','기타']

    def sel():
        global total4
        total4=''
        if var.get()==0:
            total4=rice
            print(total4)
        if var.get()==1:
            total4=noodle
            print(total4)
        if var.get()==2:
            total4=elseT
            print(total4)
        
        select="당신이 선택한 사항1 : "+op[var.get()]
        label.config(text=select)
        
    def sele():
        select2="당신이 선택한 사항2 : "+opt[var2.get()]
        label2.config(text=select2)

        global total5
        total5=''
        
        if var2.get()==0:
            total5=western
            print(total5)
        if var2.get()==1:
            total5=snack
            print(total5)
        if var2.get()==2:
            total5=elseTh
            print(total5)
       
        global total6
        total6=total4&total5
        
        global total7
        total7=total3&total6
        
        print('결과 : '+str(total6))
        print('최종 결과 : '+str(total7))
        
        if total6==set():
            select3="다시 선택해주세요"
            label3.pack(side='top')
        else :
            select3="다음 단계로 넘어가세요"
            label3.config(text=select3)
            label3.pack(side='top')

        if total7==set():
            select3="최종 선택할 음식점들이 없습니다. 다시 선택해주세요"
            label3.config(text=select3)
            label3.pack(side='top')

    global b 
    b=Tk()
    b.title("음식 메뉴 결정하기2")

    var=IntVar(b)
    var2=IntVar(b)

    la=Label(b,text="반드시 1번을 선택 후 2번을 선택하세요").pack(anchor=W)
    la1=Label(b,text="주의) 만약 1번을 재선택할시 2번 다시 누르기!\n").pack(anchor=W)
    
    l1=Label(b,text="1. 음식 종류_1").pack(anchor=W)
    for i in range(0,3):
        Radiobutton(b,text=str(i+1)+'.'+op[i],value=i, variable=var,command=sel).pack(anchor=W)
    
    label=Label(b).pack(anchor=W)
    
    l2=Label(b,text="2. 음식 종류_2").pack(anchor=W)
    for j in range(0,3):
        Radiobutton(b,text=str(j+1)+'.'+opt[j],value=j, variable=var2,command=sele).pack(anchor=W)

    label=Label(b).pack(anchor=W)
    label=Label(b)
    label.pack(anchor=W)

    label2=Label(b)
    label2.pack(anchor=W)

    label3=Label(b)
    label.pack(side='top')

    label4=Label(b).pack()
    b1=Button(b,text="다음",command=game).pack()

    a.destroy()
    b.mainloop()


#첫번째 버튼_음식 메뉴 결정하기_게임 리스트
def game():
    e=Tk()
    e.geometry("250x200")

    global listbox
    listbox=Listbox(e)
    e.title("게임 선택하기")
    listbox.insert(0,"가위 바위 보")
    listbox.insert(1,"랜덤 버튼 선택하기")
    listbox.pack()
    
    listbox.curselection()
        
    button=Button(e,text="확인",command=choose).pack()
    
    b.destroy()
    e.mainloop()

def choose():
    if list(listbox.curselection())[0]==0:
        rsp()
    if list(listbox.curselection())[0]==1:
        ball()


#첫번째 버튼_첫번째 게임
def rsp():
    global w
    w=Tk()
    w.title('정보 추가 입력')

    global out
    out=random.sample(list(total7),len(list(total7)))

    global out1
    out1=out[0]

    global out2
    if len(out)!=1:
        out2=out[1]
    if len(out)==1:
        out2=out[0]
    
    you=Label(w,text='가위 바위 보 입력해주세요').grid(row=0,column=1)
    
    if len(list(total7))!=1:
        you1=Label(w,text='당신이 이기거나 비기면 '+out1+', '+'컴퓨터가 이기면 '+out2).grid(row=1,column=1)
        b1=Button(w,text="가위!",command=sissor).grid(row=2,column=0)
        b2=Button(w,text="바위!",command=rock).grid(row=2,column=1)
        b3=Button(w,text="보!",command=paper).grid(row=2,column=2)
        
    if len(list(total7))==1:
        you1=Label(w,text='이미 최종 결과가 나왔습니다!'+' '+'결과는 '+list(total7)[0]).grid(row=1,column=1)
        b1=Button(w,text="가위!").grid(row=2,column=0)
        b2=Button(w,text="바위!").grid(row=2,column=1)
        b3=Button(w,text="보!").grid(row=2,column=2)

    if len(out2)==out1[0]:
        you1=Label(w,text='이미 최종 결과가 나왔습니다!'+' '+'결과는 '+list(total7)[0]).grid(row=1,column=1)
        b1=Button(w,text="가위!").grid(row=2,column=0)
        b2=Button(w,text="바위!").grid(row=2,column=1)
        b3=Button(w,text="보!").grid(row=2,column=2)
        
    global listgame
    listgame=['가위','바위','보']
    global computer
    computer=random.choice(listgame)

def rock():
    if computer=='가위':
        s=Label(w,text="이겼습니다"+', '+out1).grid(row=3,column=1)
        b4=Button(w,text="추가 정보 보기",command=foodinfo1).grid(row=5,column=1)
        global choi1
        choi1=str(dic.get(out1))
        
    if computer=='바위':
        s=Label(w,text="비겼습니다"+', '+out1).grid(row=3,column=1)
        choi1=str(dic.get(out1))
        b4=Button(w,text="추가 정보 보기",command=foodinfo1).grid(row=5,column=1)
        
    if computer=='보':
        s=Label(w,text="   졌습니다"+', '+out2+'   ').grid(row=3,column=1)
        global choi2
        choi2=str(dic.get(out2))
        b4=Button(w,text="추가 정보 보기",command=foodinfo3).grid(row=5,column=1)

def sissor():
    if computer=='가위':
        s=Label(w,text="비겼습니다"+', '+out1).grid(row=3,column=1)
        global choi1
        choi1=str(dic.get(out1))
        b4=Button(w,text="추가 정보 보기",command=foodinfo1).grid(row=5,column=1)
        
    if computer=='바위':
        s=Label(w,text="   졌습니다"+', '+out2+'   ').grid(row=3,column=1)
        global choi2
        choi2=str(dic.get(out2))
        b4=Button(w,text="추가 정보 보기",command=foodinfo3).grid(row=5,column=1)
        
    if computer=='보':
        s=Label(w,text="이겼습니다"+', '+out1).grid(row=3,column=1)
        choi1=str(dic.get(out1))
        b4=Button(w,text="추가 정보 보기",command=foodinfo1).grid(row=5,column=1)

def paper():
    if computer=='가위':
        s=Label(w,text="    졌습니다"+', '+out2+'    ').grid(row=3,column=1)
        global choi2
        choi2=str(dic.get(out2))
        b4=Button(w,text="추가 정보 보기",command=foodinfo3).grid(row=5,column=1)
        
    if computer=='바위':
        s=Label(w,text="이겼습니다"+', '+out1).grid(row=3,column=1)
        global choi1
        choi1=str(dic.get(out1))
        b4=Button(w,text="추가 정보 보기",command=foodinfo1).grid(row=5,column=1)
        
    if computer=='보':
        s=Label(w,text="비겼습니다"+', '+out1).grid(row=3,column=1)
        choi1=str(dic.get(out1))
        b4=Button(w,text="추가 정보 보기",command=foodinfo1).grid(row=5,column=1)

def foodinfo1():
    s=Tk()
    s.geometry("500x100")
    s.title("음식 정보")
    l4=Label(s,text="").pack()
    food=Label(s,text=out1+'에 대한 추가 정보'+"\n"+choi1).pack()
    b1=Button(s,text="확인",command=s.destroy).pack()

def foodinfo3():
    s=Tk()
    s.geometry("500x100")
    s.title("음식 정보")
    l4=Label(s,text="").pack()
    food=Label(s,text=out2+'에 대한 추가 정보'+"\n"+choi2).pack()
    b1=Button(s,text="확인",command=s.destroy).pack()

        
#첫번째 버튼_두번째 게임
def ball():
    c=Tk()
    c.geometry("300x300")
    c.title("랜덤 선택하기")

    rando=random.sample(color,len(list(total7)))
    
    for i in range(0,len(list(total7))):
        b1=Button(c,text="선택"+str(i+1),background=rando[i],command=process).pack(side='left',fill=X,expand=YES)

def process():
    d=Tk()
    d.geometry("200x50")
    global fchoice
    fchoice=random.choice(list(total7))
    l1=Label(d,text="당신의 선택은, "+fchoice).pack()
    b2=Button(d,text="추가 정보 보기",command=foodinfo2).pack()
    
def foodinfo2():
    s=Tk()
    s.geometry("500x100")
    s.title("음식 정보")
    l4=Label(s,text="").pack()
    food=Label(s,text=fchoice+'에 대한 추가 정보'+"\n"+str(dic.get(fchoice))).pack()
    b1=Button(s,text="확인",command=s.destroy).pack()

        
#두번째 버튼_정보 추가 입력
def info():
    global d
    d=Tk()
    d.geometry("350x230")
    d.title('정보 추가 입력')

    notice=Label(d,text='가게 이름을 정확히 작성해주세요!').grid(row=0,column=2)
    
    global name
    lbname=Label(d,text='가게 이름 입력').grid(row=1,column=1)
    name=StringVar(d)
    enname=Entry(d,textvariable=name).grid(row=1,column=2)
    
    global time
    lbtime=Label(d,text='시간대 입력').grid(row=2, column=1)
    time=StringVar(d)
    entime=Entry(d,textvariable=time).grid(row=2, column=2)
    
    global long
    lblong=Label(d,text='대기 시간 입력').grid(row=3, column=1)
    long=StringVar(d)
    enlong=Entry(d,textvariable=long).grid(row=3, column=2)

    global price
    lbprice=Label(d,text='가격 입력').grid(row=4, column=1)
    price=StringVar(d)
    enprice=Entry(d,textvariable=price).grid(row=4, column=2)
    
    def ok():
        if name.get() in dic:
            dic[name.get()]['시간대']=time.get()
            dic[name.get()]['대기 시간']=long.get()
            dic[name.get()]['가격']=price.get()
            show=Label(d,text='\n'+'방문 시간대 : '+dic[name.get()]['시간대']+'\n'
                           +'대기 시간 : '+dic[name.get()]['대기 시간']+'\n'
                           +'가격 : '+dic[name.get()]['가격']).grid(row=5,column=2)

    bt1=Button(d,text='확인',command=ok).grid(row=6,column=2)
    bt2=Button(d,text='취소',command=d.destroy).grid(row=7,column=2)


#세번째 버튼_랜덤 돌리기
def foodrand():
    b=Tk()
    b.geometry("500x120")
    b.title("랜덤 돌리기")

    keys=list(dic)
    global e
    e=random.choice(keys)
    
    l4=Label(b,text="").pack()
    food=Label(b,text="랜덤 음식점 선택 결과 : "+e).pack()
    b1=Button(b,text="확인",command=b.destroy).pack()
    b2=Button(b,text="추가 정보 보기",command=foodinfo).pack()
    
    b.mainloop()

def foodinfo():
    s=Tk()
    s.geometry("500x100")
    s.title("음식 정보")

    cho=str(dic.get(e))
    
    l4=Label(s,text="").pack()
    food=Label(s,text=e+'에 대한 추가 정보'+"\n"+cho).pack()
    b1=Button(s,text="확인",command=s.destroy).pack()
    

#첫 화면

b1 = Button(window, text='음식 메뉴 결정하기', command=option1)
b2 = Button(window, text='랜덤 돌리기', command=foodrand)
b3 = Button(window, text='정보 입력하기', command=info)
b1.pack(side='left', fill=X, expand=YES)
b2.pack(side='right',fill=X, expand=YES)
b3.pack(side='left',fill=X,expand=YES)

window.mainloop()
