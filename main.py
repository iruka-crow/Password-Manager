import os
import random as rd
from getpass import getpass
path = "./passc/"



version = "1.0"



rd_num = [
    'v','3','w','1','G','q','m','9','O','Z',
    'E','P','d','t','7','n','Q','2','L','l',
    'R','4','b','r','[','T','_','@','W','e',
    'z','V','5','0','-','=','|',',','h','H',
    'y','Y','U','i','u','k','M','I','o','N',
    'x','8','X','6','g','D','S','A','?',']',
    '!','"','#','$','%','&',':','(',')','~',
    '{','}','a','s','C','>','c','<',';','`',
    '*','+','/','B','K','^','.','f','F','h',
    'v','L','g','q','d','9',':','4','o'
]
g_i = 0

#main_function
def main(self):    
    m_regw = ["register","input","1"]
    m_rdw = ["read","2"]
    m_hpw = ["help","9"]
    m_exw = ["exit","0","quit"]
    m_logow = ["logout","00"]
    m_logiw = ["login","11"]
    
    cer_chk = 0
    """
    cer_chk - ログイン状態のチェック
    == 1 :: パスワード登録済み
    == 2 :: パスワード未登録
    """

    with open(path+"6",'r') as f:
        fr = f.read()
        if int(fr) % 3 == 2:
            cer_chk = 1

    if self in m_regw:
        cer_chk = register()
    elif self in m_rdw:
        cer_chk = read()
    elif self in m_hpw:
        help()
    elif self in m_exw:
        if cer_chk==1:
            with open(path+"6",'w') as f:
                f.write("863264926964120736483639733")
        return 0
    elif self in m_logow:
        if cer_chk == 1:
            with open(path+"6",'w') as f:
                f.write("863264926964120736483639733")
        else:
            print("Not login now or not registered.")
    elif self == "abslogout" or self == "000":
        with open(path+"6",'w') as f:
            f.write("863264926964120736483639733")
    elif self in m_logiw:
        tmp,tmp1 = cert()
        if tmp == 1 and tmp1 == 1:
            print("login successfully.")
    else:
        tof = error(0)
        if tof == 1:
            with open(path+"6",'w') as f:
                f.write("863264926964120736483639733")
            return 0
    return 1

#Function to Register
def register():
    cer_chk1 = 0
    cer,cer_chk1 = cert()
    if cer == 1:
        print("ok\n")

        #Core Program
        def register_main(index,psw):
            with open(path+"5",'a') as f:
                f2 = open(path+"9",'a')
                #index
                rand = rd.randint(4567,7921)
                for i in range(rand):
                    f.write(rd_num[rd.randint(1,98)])
                f2.write(str(rand)+"913722")
                for i in range(len(index)):
                    rdm = rd.randint(1,98)
                    for j in range(rdm):
                        f.write(rd_num[rd.randint(1,98)])
                    f.write(index[i])
                    if 0 < rdm < 10:
                        f2.write("0" + str(rdm))
                    else:
                        f2.write(str(rdm))
                    if i == (len(index) - 1):
                        continue
                    else:
                        f2.write("00")
                f.write("!00dep00!")
                f2.write("!00dep00!")
                #psw
                rand = rd.randint(4567,7921)
                for i in range(rand):
                    f.write(rd_num[rd.randint(1,98)])
                f2.write(str(rand)+"913722")
                for i in range(len(psw)):
                    rdm = rd.randint(1,98)
                    for j in range(rdm):
                        f.write(rd_num[rd.randint(1,98)])
                    f.write(psw[i])
                    if 0 < rdm < 10:
                        f2.write("0" + str(rdm))
                    else:
                        f2.write(str(rdm))
                    if i == (len(psw) - 1):
                        continue
                    else:
                        f2.write("00")
                f.write("!00end00!")
                f2.write("!00end00!")
                f2.close()
            print("\n'" + index + "' is Registered Successfully.")

        def p():
            print("\n--- Register Mode ---")
            print("--- if you want to exit, type 'end' at Index form\n\n")

        p()
        while True:
            index = input("Password Index :")
            if index == "end":
                break
            elif index == "help":
                p()
            else:
                psw = getpass("Password :")
                register_main(index,psw)

        return cer_chk1
    else:
        print("Try again")
        return cer_chk1

#Function to Read
def read():
    cer_chk1 = 0
    cer,cer_chk1 = cert()
    if cer == 1:
        print("\n -- Print the registered Password --")
        print("loading...\n\n")
        f = open(path+'5','r')
        f2 = open(path+'9','r')
        fr = f.read()
        fr2 = f2.read()
        f.close()
        f2.close()
        tmp = []
        tm = []
        tmp3 = []
        tm3 = []
        tmp6 =[]

        Index = []
        Password = []

        tmp2 = ""
        tm2 = ""
        tmp4 = ""
        tm4 = ""
        ind_and_pw = ""
        tmp5 = 0
        tm = fr.split("!00end00!")
        tmp = fr2.split("!00end00!")
        for i in range(len(tmp)):
            #i個目のindex,pswの取り出し
            tmp2 = tmp[i]
            tm2 = tm[i]
            #i個目のindex,pswの仕分け
            tmp3 = tmp2.split("!00dep00!")
            tm3 = tm2.split("!00dep00!")
            for j in range(2):
                tmp6 = []
                ind_and_pw = ""
                #1回目index/2回目psw
                tmp4 = tmp3[j]
                tm4 = tm3[j]
                #最初のやつの長さ取り出し
                #終了分岐含む
                try:
                    tmp5 = int(tmp4[:4])
                except:
                    break

                #長さを詰める
                tmp4 = tmp4[10:]
                #tmp6に数のリスト取り出し
                while True:
                    if tmp4 == "":
                        break
                    tmp6.append(int(tmp4[:2]))
                    tmp4 = tmp4[4:]
                #tm4のカット
                tm4 = tm4[tmp5:]
                for x in range(len(tmp6)):
                    ind_and_pw += tm4[tmp6[x]]
                    tm4 = tm4[(tmp6[x]+1):]
                if j == 0:
                    Index.append(ind_and_pw)
                else:
                    Password.append(ind_and_pw)
        print("loaded.")
        print("Registered Password : "+str(len(Index)) + "\n")
        #表示
        print("--- Password Read Mode ---")
        inp = ""
        tmp = ""
        def pswp(self):
            print("Password : " + self)

        while True:
            inp = input("Mode >>")
            if inp == "all":
                for i in range(len(Index)):
                    print("Index No."+str(i+1)+" : "+Index[i])
                    pswp(Password[i])
                    print("")
            elif inp == "index":
                for i in range(len(Index)):
                    print("Index No."+str(i+1)+" : "+Index[i])
            elif inp == "exit":
                break
            elif inp == "help":
                help(22)
            else:
                try:
                    #index No探し
                    print("Index No."+inp+" : "+Index[int(inp)-1])
                    pswp(Password[int(inp)-1])
                except:
                    if inp in Index:
                        #index 内容探し
                        tmp = Index.index(inp)
                        print("Index No."+str(tmp)+" : "+Index[tmp])
                        pswp(Password[tmp])
                        print()
                    else:
                        print("'"+inp+"'"+" is not exist or mistake order.")
        return cer_chk1
    else:
        return cer_chk1

#認証
def cert():
    f = open(path+"6",'r')
    fr = f.read()
    f.close()

    #登録(初期化)
    if int(fr) % 3 == 0:
        for i in range(10):
            with open(path+str(i),'w') as f:
                if i == 6:
                    continue
                else:
                    f.write("")
        print("--- login password register ---")
        i = 0
        inp = ""
        inp2 = ""
        while True:
            inp = input("new passwd -->")
            inp2 = input("vertificate -->")
            if inp != inp2:
                print("ignore password.")
                if i == 2:
                    return 0,0
                i += 1
            else:
                break
        with open(path+"6",'w') as f:
            f.write("863264926964120736483639731")
        with open(path+"8",'w') as f:
            f2 = open(path+"1","w")
            for i in range(len(inp)):
                rdm = rd.randint(1,98)
                for j in range(rdm):
                    f.write(rd_num[rd.randint(1,98)])
                if i == (len(inp) - 1):
                    f2.write(str(rdm))
                else:
                    if 0 <= rdm < 10:
                        f2.write("0" + str(rdm))
                    else:
                        f2.write(str(rdm))
                    f2.write("00")
                f.write(inp[i])
            f2.close()
        g_i = 1
        return 1,1
    #ログイン
    elif int(fr) % 3 == 1:
        ps = ""
        with open(path+"8",'r') as f:
            f2 = open(path+"1",'r')
            fr = f.read()
            fr2 = f2.read()
            fr2_li = []
            while True:
                if fr2 == "":
                    break
                fr2_li.append(int(fr2[:2]))
                fr2 = fr2[4:]
            for i in range(len(fr2_li)):
                ps += fr[fr2_li[i]]
                fr = fr[(fr2_li[i] + 1):]
            f2.close()
        i = 0
        inp1 = ""
        while True:
            inp1 = getpass("password :")
            if ps != inp1:
                print("ignore password.  try again.")
                if i == 2:
                    return 0,1
                i += 1
            else:
                break
        with open(path+"6",'w') as f:
            f.write("863264926964120736483639731")
        g_i = 1
        return 1,1
    #ログイン中
    elif int(fr) % 3 == 2:
        print("log in now.")
        return 1,1

#help
def help(self=0):
    def p(self):
        print(self)
    #Main内
    if self == 0:
        p("\n\n---  Password Manager  ver."+version+"  ---\n")
        p("\nローカル保存のパスワード管理ツール")
        p(">>パスワードをローカルで管理します\n>>軽い不可視化処理をしているためセキュリティは少しですが確保されています。")
        p("")
        p("モード選択:")
        p("1.パスワード登録モード")
        p("--> 入力文字 | register , 1 , input")
        p("--> 初期起動時にはパスワードを登録し認証します。")
        p("--> 登録時、パスワードとともに識別子(index)を付けます。これらは登録順に番号付けされます。")
        p("--> 現在のところ、並べ替え機能などは搭載していません。")
        p("--> 数に制限はありません。容量がある限り登録できますので登録のし過ぎに注意してください。")
        p("--> 設定ファイル(passc)を消去すると認証パスワードも、データも消えます。")
        p("--> ver.1.0 では、パスワード再設定機能がないため、忘れるとすべてリセットするしかありません。")
        p("\n--使い方--")
        p("--> 1. 入力文字のどれかを入力して起動")
        p("--> 2. 初期起動ならば、このシステム用のパスワードを設定")
        p("-->    登録済みならば、パスワードを入力")
        p("--> 3. 識別するインデックスを入力 (例：サイトＵＲＬ、メモなど)")
        p("--> 4. パスワード入力")
        p("--> 5. 3-4の繰り返し。連続で登録できます。")
        p("--> 6. 終了時、Index入力待ちのときに'end'と入力するとパスワード登録モードを終了します。")
        p("-->    これに伴い、'end'という識別子(index)は使えません。この場合、'End'とする必要があります。")
        p("")
        p("2.パスワード読込モード")
        p("--> 入力文字 | read , 2 ")
        p("--> 登録パスワードを読み込みます。")
        p("--> すべて、登録識別子(index)から検索、識別子順の番号を選択などの方法があります。")
        p("--> 識別子検索では全ワードに一致するもののみ検索できます。部分一致検索はまだ対応していません。")
        p("--> 詳しくはこのモード内の 'Mode >>' 入力待ちの時に 'help' と入力してください。")
        p("")
        p("3.終了")
        p("--> 入力文字 | exit , 0 , quit")
        p("--> このプログラムを終了し、ログアウトします。")
        p("--> エラー等でこの方法以外で終了した場合、正常なログアウトができず、ログイン状態の維持により危険にさらされる恐れがあります。")
        p("")
        p("4.ログイン")
        p("--> 入力文字 | login , 11")
        p("--> ログインします。")
        p("")
        p("5.ログアウト")
        p("--> 入力文字 | logout , 00")
        p("--> ログアウトします。")
    #Read内用
    else:
        pass

#error出力
def error(self):
    
    def ctn():
        inp = input("continue? (N or any keys):")
        if inp == "n" or inp == "N":
            return 1
        else:
            return 0

    if self == 0:
        print("Error0 : This word is not registered in this system")
        return ctn()
    elif self == 1:
        print("Error1 : System error/ file I/O permission might be denied")
        return ctn()

try:
    os.mkdir("passc")
    path = "./passc/"
    for i in range(10):
        with open(path+str(i),'r'):
            continue
except:
    try:
        for i in range(10):
            with open(path+str(i),'r'):
                continue
    except:
        try:
            for i in range(10):
                with open(path+str(i),'w') as f:
                    if i == 6:
                        f.write("863264926964120736483639732")
        except:
            error(1)

tof = 1

print("Password Manager for Python\n")

try:
    while True:
        inp = input("Main -->")
        tof = main(inp)
        if tof == 0:
            break
except:
    #強制ログアウト
    with open(path+"6",'w') as f:
        f.write("863264926964120736483639733")
