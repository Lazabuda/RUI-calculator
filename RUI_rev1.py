from tkinter import *
from tkinter import messagebox as mb
#from Calc_interface import *
#from RUI_func import *
import Calc_interface
import RUI_func


#To do:
#Make clear label because when new string placed, the old one can be seen too.

#---------------------------------------------------------------------------------------#
#-----------------------------------MAIN WINDOW-----------------------------------------#
#---------------------------------------------------------------------------------------#
root = Tk()
root.geometry("600x600")
root.title("Some calculators for hardware boys and girls")


#Wire_calculate = Button(voltage_divider_window, text="Press to calculate Vout value", command=voltage_divider_calc_Vout)
#Wire_calculate.grid(row=10, column=1)


def main_menu_buttons():
    LED_calculate = Button(root, text="LED resistor calculator", font="30", command=led_calc)
    LED_calculate.grid(row=1, column=1)

    VolDiv_calculate = Button(root, text="Voltage divider calculator", font="30", command=voltage_divider)
    VolDiv_calculate.grid(row=3, column=1)

    Wire_calculate = Button(root, text = "Wire current calculator", font = "30", command=wire_calc)
    Wire_calculate.grid(row=5, column=1)

main_menu_buttons()


#---------------------------------------------------------#
#---------------------------------------------------------#
#---------------------------------------------------------#

topmenu = Menu(root)
calcmenu = Menu(topmenu, tearoff=0)
calcmenu.add_command(label="LED resistor", command=led_calc)
calcmenu.add_command(label="Voltage divider", command=voltage_divider)
calcmenu.add_command(label="Max current throw wire", command=wire_calc)
topmenu.add_cascade(label="Calculators", menu=calcmenu)

infomenu = Menu(topmenu, tearoff=0)
infomenu.add_command(label="Some jokes", command=infojokes)
infomenu.add_command(label="Info", command=infomessage)
topmenu.add_cascade(label="Info", menu=infomenu)

root.config(menu=topmenu)



root.mainloop()