from tkinter import *
import refers

epc = refers.funcss
root = Tk()

epc.login("1234")
epc.set_outlet()
epc.set_delay()
epc.set_powerloss()
epc.set_wifi()
epc.set_plaintext()
epc.set_access()
epc.set_admincred()
epc.login("CAL1108cal")
epc.set_outlet()
epc.set_lan()

windowSize = "960x540"
