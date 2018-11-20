from tkinter import *

root = Tk()
windowSize = "960x540"
epc_mods = ["Passwords", "Network Settings", "Outlet Names"]
epc_defaults = ["1234", "CAL1108cal", "192.168.168.206", "192.168.168.168", "8.8.8.8"]
outl_defaults = ["DLI Controller", "Outlet 1", "Outlet 2", "Outlet 3", "Outlet 4", "Outlet 5", "Outlet 6", "Outlet 7", "Outlet 8"]

def epc_main():
    import refers
    epc = refers.funcss
    epc.login(Entry.get(e_0))
    epc.set_outlet()
    epc.set_delay()
    #epc.set_units(Entry.get(e_5),Entry.get(e_6),Entry.get(e_7),Entry.get(e_8),Entry.get(e_9),Entry.get(e_10),Entry.get(e_11),Entry.get(e_12),Entry.get(e_13))
    epc.set_powerloss()
    epc.set_wifi()
    epc.set_plaintext()
    epc.set_access()
    epc.set_admincred(Entry.get(e_0),Entry.get(e_1))
    epc.login(Entry.get(e_1))
    epc.set_outlet()
    epc.set_lan(Entry.get(e_2),Entry.get(e_3),Entry.get(e_4))
    return

root.title("Valkyrie EPC Programmer")
root.geometry(windowSize)

bt_submit = Button(root, text="Submit", command=epc_main)
bt_submit.place(x=550, y=360, width=120, height=25)


Label(text=epc_mods[0], relief=RIDGE,width=40).place(x=480,y=0)

Label(text="Initial Password:").place(x=480,y=40)
v = StringVar(root, value=epc_defaults[0])
e_0 = Entry(textvariable=v)
e_0.place(x=580,y=40)
Label(text="Final Password:").place(x=480,y=80)
v = StringVar(root, value=epc_defaults[1])
e_1 = Entry(textvariable=v)
e_1.place(x=580,y=80)


Label(text=epc_mods[1], relief=RIDGE,width=40).place(x=480,y=120)

Label(text="IP Address:").place(x=480,y=160)
v = StringVar(root, value=epc_defaults[2])
e_2 = Entry(textvariable=v)
e_2.place(x=580,y=160)
Label(text="Gateway:").place(x=480,y=200)
v = StringVar(root, value=epc_defaults[3])
e_3 = Entry(textvariable=v)
e_3.place(x=580,y=200)
Label(text="DNS Server:").place(x=480,y=240)
v = StringVar(root, value=epc_defaults[4])
e_4 = Entry(textvariable=v)
e_4.place(x=580,y=240)


Label(text=epc_mods[2], relief=RIDGE,width=40).place(x=0)

Label(text="Controller Name:").place(x=0,y=40)
v = StringVar(root, value=outl_defaults[0])
e_5 = Entry(textvariable=v)
e_5.place(x=100,y=40)
Label(text="Outlet 1 Name:").place(x=0,y=80)
v = StringVar(root, value=outl_defaults[1])
e_6 = Entry(textvariable=v)
e_6.place(x=100,y=80)
Label(text="Outlet 2 Name:").place(x=0,y=120)
v = StringVar(root, value=outl_defaults[2])
e_7 = Entry(textvariable=v)
e_7.place(x=100,y=120)
Label(text="Outlet 3 Name:").place(x=0,y=160)
v = StringVar(root, value=outl_defaults[3])
e_8 = Entry(textvariable=v)
e_8.place(x=100,y=160)
Label(text="Outlet 4 Name:").place(x=0,y=200)
v = StringVar(root, value=outl_defaults[4])
e_9 = Entry(textvariable=v)
e_9.place(x=100,y=200)
Label(text="Outlet 5 Name:").place(x=0,y=240)
v = StringVar(root, value=outl_defaults[5])
e_10 = Entry(textvariable=v)
e_10.place(x=100,y=240)
Label(text="Outlet 6 Name:").place(x=0,y=280)
v = StringVar(root, value=outl_defaults[6])
e_11 = Entry(textvariable=v)
e_11.place(x=100,y=280)
Label(text="Outlet 7 Name:").place(x=0,y=320)
v = StringVar(root, value=outl_defaults[7])
e_12 = Entry(textvariable=v)
e_12.place(x=100,y=320)
Label(text="Outlet 8 Name:").place(x=0,y=360)
v = StringVar(root, value=outl_defaults[8])
e_13 = Entry(textvariable=v)
e_13.place(x=100,y=360)

root.mainloop()
