from tkinter import *
from tkinter import messagebox as mb
import RUI_func
import Calc_interface


#---------------------------------------------------------------------------------------#
#-----------------------------------MAIN WINDOW-----------------------------------------#
#---------------------------------------------------------------------------------------#
root = Tk()
root.geometry("600x600")
root.title("Some calculators for hardware boys and girls")

#Define main menu buttons
def main_menu_buttons():
    LED_calculate = Button(root, text="LED resistor calculator", font="30", command=Calc_interface.led_calc)
    LED_calculate.grid(row=1, column=1)

    VolDiv_calculate = Button(root, text="Voltage divider calculator", font="30", command=Calc_interface.voltage_divider)
    VolDiv_calculate.grid(row=3, column=1)

    Wire_calculate = Button(root, text = "Wire current calculator", font = "30", command=Calc_interface.wire_calc)
    Wire_calculate.grid(row=5, column=1)

main_menu_buttons()

topmenu = Menu(root)
calcmenu = Menu(topmenu, tearoff=0)
calcmenu.add_command(label="LED resistor", command=Calc_interface.led_calc)
calcmenu.add_command(label="Voltage divider", command=Calc_interface.voltage_divider)
calcmenu.add_command(label="Max current throw wire", command=Calc_interface.wire_calc)
topmenu.add_cascade(label="Calculators", menu=calcmenu)

infomenu = Menu(topmenu, tearoff=0)
infomenu.add_command(label="Some jokes", command=RUI_func.infojokes)
infomenu.add_command(label="Info", command=RUI_func.infomessage)
topmenu.add_cascade(label="Info", menu=infomenu)

root.config(menu=topmenu)



root.mainloop()