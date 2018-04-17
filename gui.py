try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
# from http://effbot.org/tkinterbook/entry.htm
failure_max = 3
passwords = [('Daniel', 'Argel'), ('Carlos', 'CRICRIS')]
def make_entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry
def enter(event):
    check_password()
def check_password():
    """ Collect 1's for every failure and quit program in case of failure_max failures """
    #print(user.get(), password.get())
    if (user.get(), password.get()) in passwords:
        check_password.user = user.get()
        root.destroy()
        print('Logged In')
        return
    check_password.failures += 1
    if check_password.failures == failure_max:
        root.destroy()
        raise SystemExit('Unauthorized User')
    else:
        root.title('Try Again: Attempt %i/%i' % (check_password.failures + 1, failure_max))
check_password.failures = 0
root = tk.Tk()
root.geometry('600x185')
root.title('                                              TIJUANA POLICE DEPARTMENT: CRIMINAL DATA BASE')
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
#entrys with not shown text
user = make_entry(parent, "User Name:", 16, show='')
password = make_entry(parent, "Password:", 16, show="*")
#button to attempt to login
b = tk.Button(parent, borderwidth=7, text="Login", width=10, pady=8, command=check_password)
b.pack(side=tk.BOTTOM)
password.bind('<Return>', enter)
user.focus_set()
parent.mainloop()