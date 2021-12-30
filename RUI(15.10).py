from tkinter import *
from tkinter import messagebox as mb

#To do:
#Make clear label because when new string placed, the old one can be seen too.


#---------------------------------------------------------------------------------------#
#-----------------------------------MAIN WINDOW-----------------------------------------#
#---------------------------------------------------------------------------------------#

root = Tk()
root.geometry("600x600")
root.title("Some calculators for hardware boys and girls")


#------------------------------------FUNCTIONS------------------------------------------#

        #-------------------LED RESISTOR CALCULATION-------------------#

def led_resistor():
    global led_window
    global counter
    global led_calc_result_lab
    global led_calc_discr_label

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



    led_calc_result_lab = Label(led_window, text="Take about " + str(int(R_result)) + " Ohm")
    led_calc_result_lab.grid(row=counter, column=2)
    led_calc_discr_label = Label(led_window, text= "Vin = " + str(Uin) + "V" + " | U_led = "
                                                   + str(U_led)+ "V" + " | I_led = " + str(I_led)+ "mA")
    led_calc_discr_label.grid(row=counter, column=0, columnspan=2)
    if (counter == 20):
        counter = 3
    counter = counter + 1

def voltage_divider_calc_R1():
    global voltage_divider_window
    global counter_vd
    global R1_result_lab
    global voltage_dividerR1_result
    global voltage_dividerR2_result
    global voltage_dividerVout_result

    try:
        float(R2_input.get())
        float(Vout_input.get())
        float(Vin_input.get())
        pass
    except ValueError:
        mb.showerror("Error", "Enter digits, boy!")

    R2 = float(R2_input.get())
    Vout = float(Vout_input.get())
    Vin = float(Vin_input.get())

    R1 = ((Vin - Vout)*R2)/Vout
    R1_result = R1

    voltage_dividerR1_result_lab = Label(voltage_divider_window, text="Take value of R1 about " + str(int(R1_result)) + " Ohm",fg='darkblue')
    voltage_dividerR1_result_lab.grid(row=counter_vd, column=2, columnspan=2)
    voltage_dividerR1_discr_label = Label(voltage_divider_window, text="Vin = " + str(Vin) + "V" + " | Vout = "
                                                  + str(Vout) + "V" + " | R2 = " + str(R2) + "Ohm")
    voltage_dividerR1_discr_label.grid(row=counter_vd, column=0, columnspan=2)
    voltage_dividerR1_result = Label(voltage_divider_window, text=str(int(R1_result)) + " Ohm" ,fg='darkblue')
    voltage_dividerR1_result.grid(row=5, column=1, sticky="e")

    if ((((Vin**2)/R1) >= 0.0625) or (((Vin**2)/R2) >= 0.0625)):
        attention_message = Label(voltage_divider_window, text="Attention! Take care of resistor's power!", fg='red')
        attention_message.grid(row=counter_vd, column=4, columnspan=5)
    if (Vin < Vout):
        mb.showerror("Error", "Input Voltage must be higher than output Voltage!")

    if (counter_vd == 25):
        counter_vd = 11
    counter_vd = counter_vd + 1



def voltage_divider_calc_R2():
    global voltage_divider_window
    global counter_vd
    global R2_result_lab
    global voltage_dividerR1_result
    global voltage_dividerR2_result
    global voltage_dividerVout_result

    try:
        float(R1_input.get())
        float(Vout_input.get())
        float(Vin_input.get())
        pass
    except ValueError:
        mb.showerror("Error", "Enter digits, boy!")

    R1 = float(R1_input.get())
    Vout = float(Vout_input.get())
    Vin = float(Vin_input.get())

    R2 = (R1 * Vout)/(Vin - Vout)
    R2_result = R2

    voltage_dividerR2_result_lab = Label(voltage_divider_window,
                                         text="Take value of R2 about " + str(int(R2_result)) + " Ohm", fg='darkblue')
    voltage_dividerR2_result_lab.grid(row=counter_vd, column=2, columnspan=2)
    voltage_dividerR2_discr_label = Label(voltage_divider_window, text="Vin = " + str(Vin) + "V" + " | Vout = "
                                                                       + str(Vout) + "V" + " | R1 = " + str(R1) + "Ohm")
    voltage_dividerR2_discr_label.grid(row=counter_vd, column=0, columnspan=2)
    voltage_dividerR2_result = Label(voltage_divider_window, text=str(int(R2_result)) + " Ohm", fg='darkblue')
    voltage_dividerR2_result.grid(row=6, column=1, sticky="e")

    if (counter_vd == 20):
        counter_vd = 11
    counter_vd = counter_vd + 1

def voltage_divider_calc_Vout():
    global voltage_divider_window
    global counter_vd
    global Vout_result_lab
    global voltage_dividerR1_result
    global voltage_dividerR2_result
    global voltage_dividerVout_result

    try:
        float(R1_input.get())
        float(R2_input.get())
        float(Vin_input.get())
        pass
    except ValueError:
        mb.showerror("Error", "Enter digits, boy!")

    R1 = float(R1_input.get())
    R2 = float(R2_input.get())
    Vin = float(Vin_input.get())

    Vout = (R2 * Vin) / (R1 + R2)
    Vout_result = Vout

    voltage_dividerVout_result_lab = Label(voltage_divider_window,
                                         text="Vout = " + str(float(round((Vout_result),2))) + " Volts", fg='darkblue')
    voltage_dividerVout_result_lab.grid(row=counter_vd, column=2, columnspan=2)
    voltage_dividerVout_discr_label = Label(voltage_divider_window, text="Output voltage result with entered values are:")
    voltage_dividerVout_discr_label.grid(row=counter_vd, column=0, columnspan=2)
    voltage_dividerVout_result = Label(voltage_divider_window, text=str(int(Vout_result)) + " Volts", fg='darkblue')
    voltage_dividerVout_result.grid(row=6, column=4, sticky="w")

    if (counter_vd == 15):
        counter_vd = 11
    counter_vd = counter_vd + 1


        #-----------------MAX WIRE CURRENT CALCULATION-----------------#

#def wire_current():


def infojokes():
    root = Tk()
    root.geometry("600x300")
    root.title("Some jokes for your good mood")
    Infotext = Label(root, text="Earth girls are easy. It is the first joke. They are not easy in real.")
    Infotext.grid(row=0, column=0)
    Infotext = Label(root, text="Do you have a dream? Maybe you want to be a landowner in a red jumpsuit,\n"
                                " with stick out from huge pockets, like a clown's, buttles of wine. And in\n"
                                " case, if you have a sip from this bottle didn't mop the running drop, it's\n"
                                " nothing scary, it doesn't see on the red costume. And nobody said to rich \n"
                                "landowner - Hey, mutherfucker, there is a red spot on your costume, shame on you!\n"
                                " To be in durty clothes in public place - what's wrong with you? Horrible, horrible,\n"
                                " then landowner. And this passer-by with a sense of accomplishment he goes home\n"
                                " where he is waited by wife and children. And, sitting on the coach and turning\n"
                                " on the TV, he will think - I would like to have that kombinezon. But I never would\n"
                                " getting dirty in wine. If I would have that kombinezon and if I would be landowner,\n"
                                " I would behave myself another way. But he didn't landowner, like he didn't communist\n"
                                " or baptist. So, if on his clothes would finded a drop of wine or something else, he \n"
                                "would perceivable as bedragged in durty clothes. Landowner could let himself more.\n"
                                " He can wear huge wide trousers with paintings of cosmic ships and it would considered,\n"
                                " that it is excentric and even when he was find with that bottle of wine in puddle\n"
                                " of red liquid on the expensive floor in the bathroom, people will smile and say:\n"
                                " Excentric!\n")
    Infotext.grid(row=1, rowspan=20, column=0, sticky="e")

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
    global led_calc_result_lab
    global led_calc_discr_label

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

    led_calc_result_lab = Label(led_window)
    led_calc_discr_label = Label(led_window)

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
# --------------------------Configure Voltage Divider window-----------------------------#
# ---------------------------------------------------------------------------------------#

def voltage_divider():
    global voltage_divider_window
    global Vin_input
    global R1_input
    global R2_input
    global Vout_input
    global counter_vd
    global voltage_dividerR1_result
    global voltage_dividerR2_result
    global voltage_dividerVout_result

    voltage_divider_window = Tk()
    voltage_divider_window.geometry("800x600")
    voltage_divider_window.title("Voltage divider calculator")

    # Voltage insert string
    Vin_input_lab = Label(voltage_divider_window, text="Enter input voltage in Volts")
    Vin_input_lab.grid(row=4, column=0, sticky="e")
    Vin_input = Entry(voltage_divider_window, width=5)
    Vin_input.grid(row=4, column=1, sticky="e")

    # R1 value
    R1_lab = Label(voltage_divider_window, text="Enter R1 resistance in Ohms")
    R1_lab.grid(row=5, column=0, sticky="e")
    R1_input = Entry(voltage_divider_window, width=5)
    R1_input.grid(row=5, column=1, sticky="e")

    # R2 Value
    R2_lab = Label(voltage_divider_window, text="Enter R2 resistance in Ohms")
    R2_lab.grid(row=6, column=0, sticky="e")
    R2_input = Entry(voltage_divider_window, width=5)
    R2_input.grid(row=6, column=1, sticky="e")

    # Vout value
    Vout_lab = Label(voltage_divider_window, text="Enter Vout in Volts")
    Vout_lab.grid(row=6, column=5, sticky="w")
    Vout_input = Entry(voltage_divider_window, width=5)
    Vout_input.grid(row=6, column=4, sticky="w")

    counter_vd = 11

    # Buttons to calculate

    R1_calculate = Button(voltage_divider_window, text="Press to calculate R1 value", command=voltage_divider_calc_R1)
    R1_calculate.grid(row=8, column=1)

    R2_calculate = Button(voltage_divider_window, text="Press to calculate R2 value", command=voltage_divider_calc_R2)
    R2_calculate.grid(row=9, column=1)

    V_calculate = Button(voltage_divider_window, text="Press to calculate Vout value", command=voltage_divider_calc_Vout)
    V_calculate.grid(row=10, column=1)

    Clear_button = Button(voltage_divider_window, text="Press to clear", command=lambda: [
                                                                        voltage_divider_window.update()
                                                                                        ])
    Clear_button.grid(row=8, column=2)

    #Voltage_divider_result_clear = Button(voltage_divider_window, text="Press to clear all results", command=voltage_divider_clear)
    #Voltage_divider_result_clear.grid(row=11, column=1)

    # Buttons to choose calculator

    voltage_dividerR1_result = Label(voltage_divider_window, text="Just a crutch", fg='darkblue')
    voltage_dividerR2_result = Label(voltage_divider_window, text="Just a crutch", fg='darkblue')
    voltage_dividerVout_result = Label(voltage_divider_window, text="Just a crutch", fg='darkblue')

    Show_R1 = Button(voltage_divider_window, text="R1 CALCULATOR", bg='blue', fg='white',
                                                        command=lambda: [
                                                        voltage_dividerR1_result.destroy(),
                                                        voltage_dividerR2_result.destroy(),
                                                        voltage_dividerVout_result.destroy(),
                                                        R1_lab.grid_remove(), R1_input.grid_remove(),
                                                        R2_calculate.grid_remove(),
                                                        V_calculate.grid_remove(),
                                                        R1_calculate.grid(),
                                                        R2_lab.grid(), R2_input.grid(),
                                                        Vout_lab.grid(), Vout_input.grid(),
                                                        canvas_formulaR1.grid(row=0, rowspan=6, column=4, columnspan=10),
                                                        canvas_formulaR2.grid_remove(),
                                                        canvas_formulaVout.grid_remove()])
    Show_R1.grid(row=0, column=0)

    Show_R2 = Button(voltage_divider_window, text="R2 CALCULATOR", bg='blue', fg='white',
                                                        command=lambda: [
                                                        voltage_dividerR1_result.destroy(),
                                                        voltage_dividerR2_result.destroy(),
                                                        voltage_dividerVout_result.destroy(),
                                                        R2_lab.grid_remove(), R2_input.grid_remove(),
                                                        R1_calculate.grid_remove(),
                                                        V_calculate.grid_remove(),
                                                        R2_calculate.grid(),
                                                        R1_lab.grid(), R1_input.grid(),
                                                        Vout_lab.grid(), Vout_input.grid(),
                                                        canvas_formulaR2.grid(row=0, rowspan=6, column=4, columnspan=10),
                                                        canvas_formulaR1.grid_remove(),
                                                        canvas_formulaVout.grid_remove()])
    Show_R2.grid(row=1, column=0)

    Show_Vout = Button(voltage_divider_window, text="Vout CALCULATOR", bg='blue', fg='white',
                                                        command=lambda: [
                                                        voltage_dividerR1_result.destroy(),
                                                        voltage_dividerR2_result.destroy(),
                                                        voltage_dividerVout_result.destroy(),
                                                        Vout_lab.grid_remove(), Vout_input.grid_remove(),
                                                        R1_calculate.grid_remove(),
                                                        R2_calculate.grid_remove(),
                                                        V_calculate.grid(),
                                                        R1_lab.grid(), R1_input.grid(),
                                                        R2_lab.grid(), R2_input.grid(),
                                                        canvas_formulaVout.grid(row=0, rowspan=6, column=4, columnspan=10),
                                                        canvas_formulaR1.grid_remove(),
                                                        canvas_formulaR2.grid_remove()])
    Show_Vout.grid(row=2, column=0)



    # ---------------------------------------------------------#
    # Drawing elements
    # ---------------------------------------------------------#

    # Drawing Voltage Source
    canvas_voltage = Canvas(voltage_divider_window, width=130, height=50)
    canvas_voltage.create_line(50, 0, 50, 50)
    canvas_voltage.create_polygon(40, 15, 50, 0, 60, 15)
    canvas_voltage.grid(row=4, column=2)
    canvas_voltage.create_text(80, 25, fill="black", font="Times 12 italic bold", text="Vin")

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


    # Draw Formula R1
    canvas_formulaR1 = Canvas(voltage_divider_window, width=250, height=150)
    canvas_formulaR1.create_line(3, 3, 250, 3, fill="darkblue", width=5)
    canvas_formulaR1.create_line(250, 3, 250, 150, fill="darkblue", width=5)
    canvas_formulaR1.create_line(250, 150, 3, 150, fill="darkblue", width=5)
    canvas_formulaR1.create_line(3, 150, 3, 3, fill="darkblue", width=5)
    canvas_formulaR1.create_line(70, 70, 210, 70, fill="darkblue")
    canvas_formulaR1.create_text(50, 70, fill="darkblue", font="Times 14 italic bold", text="R1 = ")
    canvas_formulaR1.create_text(140, 55, fill="darkblue", font="Times 14 italic bold", text="(Vin - Vout)*R2")
    canvas_formulaR1.create_text(140, 80, fill="darkblue", font="Times 14 italic bold", text="Vout")
    #canvas_formulaR1.grid(row=4, rowspan=5, column=4)

    # Draw Formula R2
    canvas_formulaR2 = Canvas(voltage_divider_window, width=250, height=150)
    canvas_formulaR2.create_line(3, 3, 250, 3, fill="darkblue", width=5)
    canvas_formulaR2.create_line(250, 3, 250, 150, fill="darkblue", width=5)
    canvas_formulaR2.create_line(250, 150, 3, 150, fill="darkblue", width=5)
    canvas_formulaR2.create_line(3, 150, 3, 3, fill="darkblue", width=5)
    canvas_formulaR2.create_line(70, 70, 210, 70, fill="darkblue")
    canvas_formulaR2.create_text(50, 70, fill="darkblue", font="Times 14 italic bold", text="R2 = ")
    canvas_formulaR2.create_text(140, 55, fill="darkblue", font="Times 14 italic bold", text="Vout * R1")
    canvas_formulaR2.create_text(140, 80, fill="darkblue", font="Times 14 italic bold", text="Vin - Vout")
    # canvas_formulaR1.grid(row=4, rowspan=5, column=4)

    # Draw Formula Vout
    canvas_formulaVout = Canvas(voltage_divider_window, width=250, height=150)
    canvas_formulaVout.create_line(3, 3, 250, 3, fill="darkblue", width=5)
    canvas_formulaVout.create_line(250, 3, 250, 150, fill="darkblue", width=5)
    canvas_formulaVout.create_line(250, 150, 3, 150, fill="darkblue", width=5)
    canvas_formulaVout.create_line(3, 150, 3, 3, fill="darkblue", width=5)
    canvas_formulaVout.create_line(80, 70, 210, 70, fill="darkblue")
    canvas_formulaVout.create_text(50, 70, fill="darkblue", font="Times 14 italic bold", text="Vout = ")
    canvas_formulaVout.create_text(140, 55, fill="darkblue", font="Times 14 italic bold", text="R2 * Vout")
    canvas_formulaVout.create_text(140, 80, fill="darkblue", font="Times 14 italic bold", text="R1 + R2")
    # canvas_formulaR1.grid(row=4, rowspan=5, column=4)


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