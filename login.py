import tkinter as tk
import cx_Oracle


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, padx=50, pady=50)
        userlabel = tk.Label(self.master, text='User Name:')
        self.master.user = tk.Entry(self.master, show='')
        pwdlabel = tk.Label(self.master, text='Password:')
        self.master.password = tk.Entry(self.master, show='*')
        #self.master.password.bind('<Return>', self.check_password)
        userlabel.pack(side=tk.TOP)
        self.master.user.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
        pwdlabel.pack(side=tk.TOP)
        self.master.password.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
        b = tk.Button(self.master, borderwidth=7, text="Login", width=10, pady=6, command=self.check_password)
        b.pack(side=tk.BOTTOM)
        self.frame.pack()

    def check_password(self):
        user_name = self.master.user.get()
        print(user_name)
        pwd = self.master.password.get()
        print(pwd)
        cur = con.cursor()
        cur.execute('select * from arg.officer where name=:1 and passwd=:2', (user_name, int(pwd)))
        if len(cur.fetchall()) > 0:
            cur.close()
            print('Logged In')
            self.new_window()
        else:
            return

    def new_window(self):
        self.master.destroy()
        root = tk.Tk()
        root.geometry('600x200')
        root.title('TIJUANA POLICE DEPARTMENT: CRIMINAL DATA BASE')
        app = Demo2(root)
        root.mainloop()

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, padx=50, pady=50)
        createButton = tk.Button(self.master, borderwidth=7, text="Create User", width=10, pady=6, command=self.new_user)
        editButton = tk.Button(self.master, borderwidth=7, text="Edit User", width=10, pady=6, command=self.edit_user)
        delButton = tk.Button(self.master, borderwidth=7, text="Delete User", width=10, pady=6, command=self.del_user)
        createButton.pack()
        editButton.pack()
        delButton.pack()
        self.frame.pack()

    def new_user(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo3(self.newWindow)
        return
    def del_user(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo4(self.newWindow)
        return
    def edit_user(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo5(self.newWindow)
        return


class Demo3:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, padx=50, pady=50)
        userlabel = tk.Label(self.master, text='User Name:')
        self.master.user = tk.Entry(self.master, show='')
        pwdlabel = tk.Label(self.master, text='Password:')
        self.master.password = tk.Entry(self.master, show='*')
        # self.master.password.bind('<Return>', self.check_password)
        userlabel.pack(side=tk.TOP)
        self.master.user.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
        pwdlabel.pack(side=tk.TOP)
        self.master.password.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
        b = tk.Button(self.master, borderwidth=7, text="Add", width=10, pady=6, command=self.close_windows)
        b.pack(side=tk.BOTTOM)
        self.frame.pack()

    def close_windows(self):
        user_name = self.master.user.get()
        print(user_name)
        pwd = self.master.password.get()
        print(pwd)
        cur = con.cursor()
        cur.execute('insert into arg.officer(name,passwd) values (:1,:2)', (user_name, int(pwd)))

        con.commit()
        cur.execute('select * from arg.officer order by name')
        for result in cur:
            print(result)
        cur.close()
        print('User Added')
        self.master.destroy()

class Demo4:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, padx=50, pady=50)
        userlabel = tk.Label(self.master, text='User Name:')
        self.master.user = tk.Entry(self.master, show='')
        userlabel.pack(side=tk.TOP)
        self.master.user.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
        b = tk.Button(self.master, borderwidth=7, text="Delete", width=10, pady=6, command=self.close_windows)
        b.pack(side=tk.BOTTOM)
        self.frame.pack()

    def close_windows(self):
        user_name = self.master.user.get()
        print(user_name)
        cur = con.cursor()
        cur.execute('delete from arg.officer where name = :1', {'1':user_name})

        con.commit()
        cur.execute('select * from arg.officer order by name')
        for result in cur:
            print(result)
        cur.close()
        print('User Deleted')
        self.master.destroy()

class Demo5:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, padx=50, pady=50)
        userlabel = tk.Label(self.master, text='User Name:')
        self.master.user = tk.Entry(self.master, show='')
        ranklabel = tk.Label(self.master, text='Rank:')
        self.master.rank = tk.Entry(self.master, show='')
        ranklabel.pack(side=tk.TOP)
        self.master.rank.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
        userlabel.pack(side=tk.TOP)
        self.master.user.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
        b = tk.Button(self.master, borderwidth=7, text="Edit", width=10, pady=6, command=self.close_windows)
        b.pack(side=tk.BOTTOM)
        self.frame.pack()

    def close_windows(self):
        rank_lv = self.master.rank.get()
        print(rank_lv)
        user_name = self.master.user.get()
        print(user_name)
        cur = con.cursor()
        cur.execute('update arg.officer set rank = :1 where name = :2', (rank_lv, user_name))

        con.commit()
        cur.execute('select * from arg.officer order by name')
        for result in cur:
            print(result)
        cur.close()
        print('User Edit')
        self.master.destroy()

def main():
    global con
    con = cx_Oracle.connect('arg' + '/' + 'charizard' + '@' + 'localhost', mode=cx_Oracle.SYSDBA)
    print(con.version)
    cur = con.cursor()
    cur.execute('select * from arg.officer order by name')
    for result in cur:
        print(result)
    cur.close()
    root = tk.Tk()
    root.geometry('600x200')
    root.title('TIJUANA POLICE DEPARTMENT: CRIMINAL DATA BASE')
    app = Demo1(root)
    root.mainloop()


main()