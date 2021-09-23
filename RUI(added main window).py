from tkinter import *
from tkinter import messagebox as mb

#---------------------------------------------------------------------------------------#
#-----------------------------------MAIN WINDOW-----------------------------------------#
#---------------------------------------------------------------------------------------#

root = Tk()
root.geometry("600x600")
root.title("Some calculators for hardware boys and girls")

#------------------------------------FUNCTIONS------------------------------------------#

        #-------------------LED RESISTOR CALCULATION-------------------#

def led_resistor():
    try:
        float(Uin_input.get())
        float(U_led_input.get())
        float(I_led_input.get())
        pass
    except ValueError:
        mb.showerror("Error", "Enter digits, boy!")
    Uin = float(Uin_input.get())
    U_led = float(U_led_input.get())
    I_led = float(I_led_input.get())

    R = (Uin - U_led)/(I_led*0.001)
    R_result = R

    global led_window
    global counter
    global R_result_lab
    global R_discr_label

    R_result_lab = Label(led_window, text="Take about " + str(int(R_result)) + " Ohm")
    R_result_lab.grid(row=counter, column=2)
    R_discr_label = Label(led_window, text= "Vin = " + str(Uin) + "V" + " | U_led = " + str(U_led)+ "V" + " | I_led = " + str(I_led)+ "mA")
    R_discr_label.grid(row=counter, column=0, columnspan=2)
    if (counter == 15):
        counter = 3
    counter = counter + 1

#def voltage_divider_calc():


        #-----------------MAX WIRE CURRENT CALCULATION-----------------#

#def wire_current():


def infojokes():
    root = Tk()
    root.geometry("600x300")
    root.title("Some jokes for your good mood")
    Infotext = Label(root, text="Earth girls are easy")
    Infotext.grid(row=0, column=0)
    Infotext = Label(root, text="Who is so talented to write some jokes here?")
    Infotext.grid(row=1, column=0)

def infomessage():
    root = Tk()
    root.geometry("600x300")
    root.title("Information")
    Infotext = Label(root, text="This program was developed because of low self-assessment.")
    Infotext.grid(row=0, column=0)
    Infotext = Label(root, text="Only my best friend Kostyan belived in me. But sometimes he said that I am stupid")
    Infotext.grid(row=1, column=0)

#---------------------------------------------------------------------------------------#
#--------------------------THE LED CALCULATOR THINGS------------------------------------#
#---------------------------------------------------------------------------------------#

def led_calc():
    global led_window
    led_window = Tk()
    led_window.geometry("600x600")
    led_window.title("Led Resistor calculator basic")

    global counter
    global Uin_input
    global U_led_input
    global I_led_input
    global R_result_lab
    global R_discr_label

#Voltage insert string
    Uin_input_lab = Label(led_window, text="Enter input voltage in Volts")
    Uin_input_lab.grid(row=0, column=0)
    Uin_input = Entry(led_window, width=20)
    Uin_input.grid(row=0, column=1)

#LED drop voltage insert string
    U_led_input_lab = Label(led_window, text="Enter LED drop voltage in Volts")
    U_led_input_lab.grid(row=1, column=0)
    U_led_input = Entry(led_window, width=20)
    U_led_input.grid(row=1, column=1)

#LED drop voltage insert string
    I_led_input_lab = Label(led_window, text="Enter LED current in milliAmperes")
    I_led_input_lab.grid(row=2, column=0)
    I_led_input = Entry(led_window, width=20)
    I_led_input.grid(row=2, column=1)

    counter = 4

    R_result_lab = Label(led_window)
    R_discr_label = Label(led_window)

#Button to calculate resistor value
    R_calculate = Button(led_window, text="Press to calculate R value", command = led_resistor)
    R_calculate.grid(row=3, column=1)



#---------------------------------------------------------#
#Drawing elements
#---------------------------------------------------------#

#Drawing Voltage Source
    canvas_voltage = Canvas(led_window, width=130, height=50)
    canvas_voltage.create_line(50,0,50,50)
    canvas_voltage.create_polygon(40,15, 50,0, 60,15)
    canvas_voltage.grid(row=0, column=2)

#Draw LED
    canvas_led = Canvas(led_window, width=130, height=50)
    canvas_led.create_line(50,0,50,50)
    canvas_led.create_polygon(30,10, 50,35, 70,10)
    canvas_led.create_line(30,35, 70,35)
    canvas_led.create_line(70,30, 80,40)
    canvas_led.create_polygon(80,40, 75,40, 80,35)
    canvas_led.create_line(70,20, 80,30)
    canvas_led.create_polygon(80,30, 75,30, 80,25)
    canvas_led.grid(row=2, column=2)

#Draw Resistor
    canvas_resistor = Canvas(led_window, width=130, height=50)
    canvas_resistor.create_line(50,0,50,50)
    canvas_resistor.create_polygon(40,10, 60,10, 60,40, 40,40)
    canvas_resistor.grid(row=1, column=2)

#Draw Formula
    canvas_formula = Canvas(led_window, width=200, height=150)
    canvas_formula.create_line(30,70,120,70, fill="darkblue")
    canvas_formula.create_text(15,70,fill="darkblue",font="Times 12 italic bold",text="R = ")
    canvas_formula.create_text(75,55,fill="darkblue",font="Times 12 italic bold",text="Uin - U_led")
    canvas_formula.create_text(80,80,fill="darkblue",font="Times 12 italic bold",text="I_led")
    canvas_formula.grid(row=0, rowspan=4, column=3)

# ---------------------------------------------------------------------------------------#
# --------------------------THE LED CALCULATOR THINGS------------------------------------#
# ---------------------------------------------------------------------------------------#

def voltage_divider():
    global voltage_divider_window
    voltage_divider_window = Tk()
    voltage_divider_window.geometry("600x600")
    voltage_divider_window.title("Voltage divider calculator")

    # Voltage insert string
    Uin_input_lab = Label(voltage_divider_window, text="Enter input voltage in Volts")
    Uin_input_lab.grid(row=4, column=0)
    Uin_input = Entry(voltage_divider_window, width=20)
    Uin_input.grid(row=4, column=1)

    # R1 value
    R1_lab = Label(voltage_divider_window, text="Enter R1 resistance in Ohms")
    R1_lab.grid(row=5, column=0)
    R1_input = Entry(voltage_divider_window, width=20)
    R1_input.grid(row=5, column=1)

    # LED drop voltage insert string
    R2_lab = Label(voltage_divider_window, text="Enter R2 resistance in Ohms")
    R2_lab.grid(row=6, column=0)
    R2_input = Entry(voltage_divider_window, width=20)
    R2_input.grid(row=6, column=1)

    counter = 4

    # Buttons to calculate
    R1_calculate = Button(voltage_divider_window, text="Press to calculate R1 value", command=led_resistor)
    R1_calculate.grid(row=7, column=1)

    R2_calculate = Button(voltage_divider_window, text="Press to calculate R2 value", command=led_resistor)
    R2_calculate.grid(row=8, column=1)

    V_calculate = Button(voltage_divider_window, text="Press to calculate Vout value", command=led_resistor)
    V_calculate.grid(row=9, column=1)

    #Radio buttons

    global radioValue
    radioValue = IntVar()

    rdioOne = Radiobutton(voltage_divider_window, text='Calculate R1', variable=radioValue, value=1)
    rdioTwo = Radiobutton(voltage_divider_window, text='Calculate R2', variable=radioValue, value=2)
    rdioThree = Radiobutton(voltage_divider_window, text='Calculate Vout', variable=radioValue, value=3)

    rdioOne.grid(column=0, row=0)
    rdioTwo.grid(column=0, row=1)
    rdioThree.grid(column=0, row=2)

    # ---------------------------------------------------------#
    # Drawing elements
    # ---------------------------------------------------------#

    # Drawing Voltage Source
    canvas_voltage = Canvas(voltage_divider_window, width=130, height=50)
    canvas_voltage.create_line(50, 0, 50, 50)
    canvas_voltage.create_polygon(40, 15, 50, 0, 60, 15)
    canvas_voltage.grid(row=4, column=2)

    # Draw Resistor R1
    canvas_resistor1 = Canvas(voltage_divider_window, width=130, height=50)
    canvas_resistor1.create_line(50, 0, 50, 50)
    canvas_resistor1.create_polygon(40, 10, 60, 10, 60, 40, 40, 40)
    canvas_resistor1.create_text(75, 25, fill="black", font="Times 12 italic bold", text="R1")
    canvas_resistor1.grid(row=5, column=2)

    # Draw Resistor R2
    canvas_resistor2 = Canvas(voltage_divider_window, width=130, height=50)
    canvas_resistor2.create_line(50, 0, 50, 50)
    canvas_resistor2.create_polygon(40, 10, 60, 10, 60, 40, 40, 40)
    canvas_resistor2.create_text(75, 25, fill="black", font="Times 12 italic bold", text="R2")
    canvas_resistor2.create_line(50, 2, 130, 2)
    canvas_resistor2.create_line(50, 50, 130, 50)
    canvas_resistor2.grid(row=6, column=2)

    # Draw Ground sumbol
    canvas_ground = Canvas(voltage_divider_window, width=130, height=50)
    canvas_ground.create_line(50, 0, 50, 25)
    canvas_ground.create_line(30, 25, 70, 25)
    canvas_ground.create_line(35, 30, 65, 30)
    canvas_ground.create_line(40, 35, 60, 35)
    canvas_ground.create_line(45, 40, 55, 40)
    canvas_ground.create_line(48, 45, 52, 45)
    canvas_ground.grid(row=7, column=2)

    # Draw Vout symbol
    canvas_vout = Canvas(voltage_divider_window, width=50, height=50)
    canvas_vout.create_line(0, 2, 50, 2)
    canvas_vout.create_line(0, 50, 50, 50)
    canvas_vout.create_line(0, 10, 10, 0)
    canvas_vout.create_line(10, 0, 20, 10)
    canvas_vout.create_line(0, 40, 10, 50)
    canvas_vout.create_line(10, 50, 20, 40)
    canvas_vout.create_line(10, 0, 10, 50)
    canvas_vout.create_text(30, 25, fill="black", font="Times 12 italic bold", text="Vout")



    canvas_vout.grid(row=6, column=3)


    # Draw Formula
    canvas_formula = Canvas(voltage_divider_window, width=200, height=150)
    canvas_formula.create_line(30, 70, 120, 70, fill="darkblue")
    canvas_formula.create_text(15, 70, fill="darkblue", font="Times 12 italic bold", text="R = ")
    canvas_formula.create_text(75, 55, fill="darkblue", font="Times 12 italic bold", text="Uin - U_led")
    canvas_formula.create_text(80, 80, fill="darkblue", font="Times 12 italic bold", text="I_led")
    canvas_formula.grid(row=4, rowspan=4, column=4)


#---------------------------------------------------------------------------------------#
#------------------------------THE MAX CURRENT THROW WIRE CALCULATOR--------------------#
#---------------------------------------------------------------------------------------#

def wire_calc():
    global wire_window
    wire_window = Tk()
    wire_window.geometry("600x600")
    wire_window.title("Max currunt throw wire calculator")
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