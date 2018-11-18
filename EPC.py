from tkinter import *

root = Tk()
windowSize = "960x540"
epc_mods = ["Passwords", "IP Address", "Gateway", "Subnet Mask"]
epc_defaults = ["CAL1108cal", "192.168.168.206", "192.168.168.168", "8.8.8.8", "1234"]

def epc_main():
    import refers
    epc = refers.funcss
    epc.login(Entry.get(e_4))
    epc.set_outlet()
    epc.set_delay()
    epc.set_powerloss()
    epc.set_wifi()
    epc.set_plaintext()
    epc.set_access()
    epc.set_admincred(Entry.get(e_0),Entry.get(e_4))
    epc.login(Entry.get(e_0))
    epc.set_outlet()
    epc.set_lan(Entry.get(e_1),Entry.get(e_2),Entry.get(e_3))
    return

root.title("Valkyrie EPC Programmer")
root.geometry(windowSize)
bt_submit = Button(root, text="Submit", command=epc_main)
bt_submit.place(x=420, y=420, width=120, height=25)

r = 0
for c in epc_mods:
    Label(text=c, relief=RIDGE,width=40).place(y=100*r)
    r = r + 1

v = StringVar(root, value=epc_defaults[0])
e_0 = Entry(textvariable=v)
e_0.place(x=95,y=60)

v = StringVar(root, value=epc_defaults[1])
e_1 = Entry(textvariable=v)
e_1.place(x=95,y=130)

v = StringVar(root, value=epc_defaults[2])
e_2 = Entry(textvariable=v)
e_2.place(x=95,y=230)

v = StringVar(root, value=epc_defaults[3])
e_3 = Entry(textvariable=v)
e_3.place(x=95,y=330)

v = StringVar(root, value=epc_defaults[4])
e_4 = Entry(textvariable=v)
e_4.place(x=95,y=30)

Label(text="Initial Password:").place(y=30)
Label(text="Final Password:").place(y=60)

root.mainloop()
