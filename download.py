from ftplib import FTP
from tkinter import *

class downBody:
    def __init__(self):
        self.cnt = 0
        self.root = Tk()
        self.root.geometry('505x385')  # window 크기조정
        self.root.resizable()

        self.fList = Listbox(self.root,width=69,height=20,bg='white') # width ==> 한 줄에 들어갈 '문자 수', height==> 줄 수
        self.fList.grid(padx=9,pady=5,row=0,column=0,columnspan=3,sticky=E+W) # colmnspan 가로로 덮을 공간 따라서 0~3만큼의 공간을 덮는다.
        self.fList.config(selectmode='multiple')

        self.downBtn = Button(self.root, text="파일 다운", width=20, height=2,command=self.download)
        self.downBtn.grid(pady=5,row=1,column=0)

    def start(self):
        self.root.mainloop()

    def isEmpty(self): # 파일 리스트가 비워지지 않았는지 체크
        if self.fList.index("end") != 0: return True
        return False

    def download(self):
        ftp = FTP()
        if self.cnt == 0:
            files = ftp.nlst();files.remove('html')
            for file in files:
                self.fList.insert(0, file)
            self.cnt+=1
        else:
            if self.isEmpty():  # 마지막 index가 0이 아니라면
                fnum = self.fList.curselection()
                for num in fnum:
                    file = self.fList.get(num)
                    print('Downloading.....', file)
                    ftp.retrbinary('RETR ' + file, open("C:\\Users\\Administrator\\Downloads\\"+file, 'wb').write)
            print('Done')
        ftp.close()
skeleton = downBody()
skeleton.start()