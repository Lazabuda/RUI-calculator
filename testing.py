from tkinter import *
"""
#------------------------------------FUNCTIONS------------------------------------------#

def led_resistor():
    Uin = float(Uin_input.get())
    U_led = float(U_led_input.get())
    I_led = float(I_led_input.get())
    R = (Uin - U_led)/(I_led*0.001)
    R_result = "Value of R = " + R
    #print("Here I need to paste formula!")   # ATTENTION!
    R_result_lab = Label(root, text=R_result)


#---------------------------------------------------------------------------------------#
"""

root = Tk()
root.geometry("600x600")
root.title("Led Resistor calculator basic")

#Voltage insert string
Uin_input_lab = Label(root, text="Enter input voltage")
Uin_input_lab.grid(row=0, column=0)
Uin_input = Entry(root, width=20)
Uin_input.grid(row=0, column=1)

#LED drop voltage insert string
U_led_input_lab = Label(root, text="Enter LED drop voltage")
U_led_input_lab.grid(row=1, column=0)
U_led_input = Entry(root, width=20)
U_led_input.grid(row=1, column=1)

#LED drop voltage insert string
I_led_input_lab = Label(root, text="Enter LED current")
I_led_input_lab.grid(row=2, column=0)
I_led_input = Entry(root, width=20)
I_led_input.grid(row=2, column=1)

counter = 4

def led_resistor():
    Uin = float(Uin_input.get())
    U_led = float(U_led_input.get())
    I_led = float(I_led_input.get())
    R = (Uin - U_led)/(I_led*0.001)
    R_result = R
    #print("Here I need to paste formula!")   # ATTENTION!
    global counter
    R_result_lab = Label(root, text="Take about " + str(int(R_result)) + "Ohm")
    R_result_lab.grid(row=counter, column=1)
    R_discr_label = Label(root, text= "Vin = " + str(Uin) + "V" + " | U_led = " + str(U_led)+ "V" + " | I_led = " + str(I_led)+ "mA")
    R_discr_label.grid(row=counter, column=0)
    counter = counter + 1

    #Добавить уходящий вниз список через цикл с разными номиналами

#Button to calculate resistor value
R_calculate = Button(root, text="Press to calculate R value", command = led_resistor)
R_calculate.grid(row=3, column=1)


root.mainloop()

