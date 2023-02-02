from tkinter import *
from tkinter import messagebox as mb
import RUI_func
#from RUI_func import *




#---------------------------------------------------------------------------------------#
#--------------------------THE LED CALCULATOR THINGS------------------------------------#
#---------------------------------------------------------------------------------------#
def button_clear():
    global Vin_input
    global R1_input
    global R2_input
    global Vout_input
    Vin_input.delete(0, END)
    R1_input.delete(0, END)
    R2_input.delete(0, END)
    Vout_input.delete(0, END)



def led_calc():
    global led_window
    led_window = Tk()
    led_window.geometry("600x600")
    led_window.title("Led Resistor calculator basic")

    global counter
    global U_led_input
    global I_led_input
    global led_calc_result_lab
    global led_calc_discr_label
    global Uin_input

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

    led_calc_result_lab = Label(led_window)
    led_calc_discr_label = Label(led_window)

#Button to calculate resistor value
    R_calculate = Button(led_window, text="Press to calculate R value", command = RUI_func.led_resistor)
    R_calculate.grid(row=4, column=1)



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

# Draw Ground sumbol
    canvas_ground = Canvas(led_window, width=130, height=50)
    canvas_ground.create_line(50, 0, 50, 25)
    canvas_ground.create_line(30, 25, 70, 25)
    canvas_ground.create_line(35, 30, 65, 30)
    canvas_ground.create_line(40, 35, 60, 35)
    canvas_ground.create_line(45, 40, 55, 40)
    canvas_ground.create_line(48, 45, 52, 45)
    canvas_ground.grid(row=3, column=2)

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

    R1_calculate = Button(voltage_divider_window, text="Press to calculate R1 value", command=RUI_func.voltage_divider_calc_R1)
    R1_calculate.grid(row=8, column=1)

    R2_calculate = Button(voltage_divider_window, text="Press to calculate R2 value", command=RUI_func.voltage_divider_calc_R2)
    R2_calculate.grid(row=9, column=1)

    V_calculate = Button(voltage_divider_window, text="Press to calculate Vout value", command=RUI_func.voltage_divider_calc_Vout)
    V_calculate.grid(row=10, column=1)


    Clear_button = Button(voltage_divider_window, text="Press to clear", command=button_clear)

    Clear_button.grid(row=8, column=2)

    # Buttons to choose calculator

    Show_R1 = Button(voltage_divider_window, text="R1 CALCULATOR", bg='blue', fg='white',
                                                        command=lambda: [
                                                        R1_lab.grid_remove(), R1_input.grid_remove(),
                                                        R2_calculate.grid_remove(),
                                                        V_calculate.grid_remove(),
                                                        button_Show_R1(),
                                                        #RUI_func.voltage_dividerR2_result.grid_remove(),
                                                        R1_calculate.grid(),
                                                        R2_lab.grid(), R2_input.grid(),
                                                        Vout_lab.grid(), Vout_input.grid(),
                                                        canvas_formulaR1.grid(row=0, rowspan=6, column=4, columnspan=10),
                                                        canvas_formulaR2.grid_remove(),
                                                        canvas_formulaVout.grid_remove()])
    Show_R1.grid(row=0, column=0)



    Show_R1.grid(row=0, column=0)

    Show_R2 = Button(voltage_divider_window, text="R2 CALCULATOR", bg='blue', fg='white',
                                                        command=lambda: [
                                                        R2_lab.grid_remove(), R2_input.grid_remove(),
                                                        R1_calculate.grid_remove(),
                                                        V_calculate.grid_remove(),
                                                        button_Show_R2(),
                                                        #RUI_func.voltage_dividerR1_result.grid_remove(),
                                                        R2_calculate.grid(),
                                                        R1_lab.grid(), R1_input.grid(),
                                                        Vout_lab.grid(), Vout_input.grid(),
                                                        canvas_formulaR2.grid(row=0, rowspan=6, column=4, columnspan=10),
                                                        canvas_formulaR1.grid_remove(),
                                                        canvas_formulaVout.grid_remove()])
    Show_R2.grid(row=1, column=0)

    Show_Vout = Button(voltage_divider_window, text="Vout CALCULATOR", bg='blue', fg='white',
                                                        command=lambda: [
                                                        Vout_lab.grid_remove(), Vout_input.grid_remove(),
                                                        R1_calculate.grid_remove(),
                                                        R2_calculate.grid_remove(),
                                                        button_Show_Vout(),
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
    canvas_voltage.create_text(80, 25, fill="black", font="Times 12 italic bold", text="Vin")
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
    canvas_formulaR1.grid(row=4, rowspan=5, column=4)

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
    canvas_formulaR2.grid(row=4, rowspan=5, column=4)

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
    canvas_formulaVout.grid(row=4, rowspan=5, column=4)

def button_Show_R1():

    if (RUI_func.voltage_dividerR1_result):
        RUI_func.voltage_dividerR1_result.grid_remove()
    if (RUI_func.voltage_dividerR2_result):
        RUI_func.voltage_dividerR2_result.grid_remove()
    if (RUI_func.voltage_dividerVout_result):
        RUI_func.voltage_dividerVout_result.grid_remove()

def button_Show_R2():
    if (RUI_func.voltage_dividerR1_result):
        RUI_func.voltage_dividerR1_result.grid_remove()
    if (RUI_func.voltage_dividerR2_result):
        RUI_func.voltage_dividerR2_result.grid_remove()
    if (RUI_func.voltage_dividerVout_result):
        RUI_func.voltage_dividerVout_result.grid_remove()

def button_Show_Vout():
    if (RUI_func.voltage_dividerR1_result):
        RUI_func.voltage_dividerR1_result.grid_remove()
    if (RUI_func.voltage_dividerR2_result):
        RUI_func.voltage_dividerR2_result.grid_remove()
    if (RUI_func.voltage_dividerVout_result):
        RUI_func.voltage_dividerVout_result.grid_remove()

#---------------------------------------------------------------------------------------#
#------------------------------THE MAX CURRENT THROW WIRE CALCULATOR--------------------#
#---------------------------------------------------------------------------------------#

def wire_calc():
    global wire_window
    global D_input
    global I_input
    global D_Voltage_drop_input
    global l_Voltage_drop_input
    global wire_input_label
    global l_input
    global V_input

    wire_window = Tk()
    wire_window.geometry("600x600")
    wire_window.title("Max currunt throw wire calculator")

#---------------------------------------START PAGE---------------------------------------#

    canvas_wire_calc_start_page = Canvas(wire_window, width=350, height=150)
    canvas_wire_calc_start_page.create_text(220, 100, fill="black", font="Times 15 italic bold", text="Please, choose the calculator")
    canvas_wire_calc_start_page.grid(row=6, column=1)

#------------------------------THE SHOW CURRENT BUTTON COMPONENTS------------------------#

    canvas_wire = Canvas(wire_window, width=350, height=150)
    canvas_wire.create_line(200, 150, 200, 50)
    canvas_wire.create_line(100, 150, 200, 150)
    canvas_wire.create_line(100, 50, 200, 50)
    canvas_wire.create_line(200, 50, 210, 70)
    canvas_wire.create_line(200, 50, 190, 70)
    canvas_wire.create_line(200, 150, 210, 130)
    canvas_wire.create_line(200, 150, 190, 130)
    canvas_wire.create_oval(50, 150, 150, 50)
    canvas_wire.create_text(220, 100, fill="black", font="Times 12 italic bold", text="D = ")
    canvas_wire.create_text(100, 70, fill="black", font="Times 12 italic bold", text="COPPER")
    canvas_wire.create_text(270, 100, fill="black", font="Times 12 italic bold", text="mm")
    #canvas_wire.grid(row=6, column=1)

    D_input = Entry(wire_window, width=5)
    D_input_window = canvas_wire.create_window(240, 100, window=D_input)

#------------------------------THE SHOW DIAMETER BUTTON COMPONENTS------------------------#

    canvas_wire_current = Canvas(wire_window, width=350, height=150)
    canvas_wire_current.create_line(40, 50, 300, 50)
    canvas_wire_current.create_line(40, 100, 300, 100)
    canvas_wire_current.create_arc(30, 50, 55, 100, start=90, extent=180, style=ARC)
    canvas_wire_current.create_arc(30, 50, 55, 100, start=270, extent=180, style=ARC)
    canvas_wire_current.create_arc(285, 50, 310, 100, start=270, extent=180, style=ARC)
    canvas_wire_current.create_line(110, 90, 210, 90)
    canvas_wire_current.create_line(210, 90, 200, 85)
    canvas_wire_current.create_line(210, 90, 200, 95)
    canvas_wire_current.create_text(130, 70, text="I =", fill="black", font=('Times 15'))
    canvas_wire_current.create_text(220, 70, text="Amperes", fill="black", font=('Times 15'))
    canvas_wire_current.create_line(40, 30, 300, 30)
    canvas_wire_current.create_line(40, 30, 45, 25)
    canvas_wire_current.create_line(40, 30, 45, 35)
    canvas_wire_current.create_line(300, 30, 295, 25)
    canvas_wire_current.create_line(300, 30, 295, 35)
    canvas_wire_current.create_text(130, 20, text="l =", fill="black", font=('Times 15'))
    canvas_wire_current.create_text(210, 20, text="mm", fill="black", font=('Times 15'))
    #canvas_wire_current.grid(row=6, column=1)

    I_input = Entry(wire_window, width=5)

    I_input_window = canvas_wire_current.create_window(160, 70, window=I_input)

    l_input = Entry(wire_window, width=5)

    l_input_window = canvas_wire_current.create_window(165, 20, window=l_input)

#---------------------------------THE VOLTAGE DROP BUTTON COMPONENTS------------------------#

    canvas_voltage_drop = Canvas(wire_window, width=350, height=150)
    canvas_voltage_drop.create_line(40, 50, 300, 50)
    canvas_voltage_drop.create_line(40, 100, 300, 100)
    canvas_voltage_drop.create_arc(30, 50, 55, 100, start=90, extent=180, style=ARC)
    canvas_voltage_drop.create_arc(30, 50, 55, 100, start=270, extent=180, style=ARC)
    canvas_voltage_drop.create_arc(285, 50, 310, 100, start=270, extent=180, style=ARC)
    canvas_voltage_drop.create_line(100, 50, 100, 100)
    canvas_voltage_drop.create_line(100, 50, 95, 55)
    canvas_voltage_drop.create_line(100, 50, 105, 55)
    canvas_voltage_drop.create_line(100, 100, 105, 95)
    canvas_voltage_drop.create_line(100, 100, 95, 95)
    canvas_voltage_drop.create_line(40, 30, 300, 30)
    canvas_voltage_drop.create_line(40, 30, 45, 25)
    canvas_voltage_drop.create_line(40, 30, 45, 35)
    canvas_voltage_drop.create_line(300, 30, 295, 25)
    canvas_voltage_drop.create_line(300, 30, 295, 35)
    canvas_voltage_drop.create_text(130, 20, text="l =", fill="black", font=('Times 15'))
    canvas_voltage_drop.create_text(210, 20, text="mm", fill="black", font=('Times 15'))
    canvas_voltage_drop.create_text(130, 80, text="D =", fill="black", font=('Times 15'))
    canvas_voltage_drop.create_text(210, 80, text="mm", fill="black", font=('Times 15'))
    #canvas_voltage_drop.grid(row=6, column=1)

    l_Voltage_drop_input = Entry(wire_window, width=5)
    D_Voltage_drop_input = Entry(wire_window, width=5)

    l_input_window = canvas_voltage_drop.create_window(165, 20, window=l_Voltage_drop_input)
    d_input_window = canvas_voltage_drop.create_window(165, 80, window=D_Voltage_drop_input)



    var = IntVar()
    var.set(0)
    #alum = Radiobutton(wire_window, text="Aluminium", variable=var, value=0)
    copper = Radiobutton(wire_window, text="Copper", variable=var, value=1)
    #alum.grid(row=4, column=0, sticky="w")
    #copper.grid(row=5, column=0, sticky="w")



#-----------------------------------------------BUTTONS TO CALCULATE---------------------------------------

    I_calculate = Button(wire_window, text="Press to calculate max current through wire", command = RUI_func.wire_current_I)

    D_calculate = Button(wire_window, text="Press to calculate max diameter of the wire", command = RUI_func.wire_current_D)

    V_calculate = Button(wire_window, text="Press to calculate voltage drop", command = RUI_func.wire_current_V)


    #BUTTONS TO CHOOSE THE CALCULATOR

    Show_current = Button(wire_window, text="Max current", bg='blue', fg='white', command=lambda: [
                                                                                    canvas_wire_calc_start_page.grid_remove(),
                                                                                    canvas_wire.grid_remove(),
                                                                                    canvas_wire.grid(row=6, column=1),
                                                                                    canvas_wire_current.grid_remove(),
                                                                                    canvas_voltage_drop.grid_remove(),
                                                                                    D_calculate.grid_remove(),
                                                                                    I_calculate.grid(row=7, column=1),
                                                                                    V_calculate.grid_remove()])
    Show_current.grid(row=1, column=0, sticky="w")

    Show_voltage_drop = Button(wire_window, text="Voltage drop", bg='blue', fg='white', command=lambda: [
                                                                                    canvas_wire_calc_start_page.grid_remove(),
                                                                                    canvas_wire.grid_remove(),
                                                                                    canvas_wire_current.grid_remove(),
                                                                                    canvas_voltage_drop.grid(row=6, column=1),
                                                                                    D_calculate.grid_remove(),
                                                                                    I_calculate.grid_remove(),
                                                                                    V_calculate.grid(row=7, column=1)])
    Show_voltage_drop.grid(row=2, column=0, sticky="w")

    Show_diameter = Button(wire_window, text="Min. diameter", bg='blue', fg='white', command=lambda: [
                                                                                    canvas_wire_calc_start_page.grid_remove(),
                                                                                    button_show_diameter(),
                                                                                    canvas_wire_current.grid(row=6, column=1),
                                                                                    canvas_wire.grid_remove(),
                                                                                    canvas_voltage_drop.grid_remove(),
                                                                                    D_calculate.grid(row=7, column=1),
                                                                                    I_calculate.grid_remove(),
                                                                                    V_calculate.grid_remove()])

    Show_diameter.grid(row=0, column=0, sticky="w")


def button_show_current():
    if (canvas_wire):
        canvas_wire.grid_remove()
    if (canvas_wire_current):
        canvas_wire_current.grid_remove()
    if (RUI_func.voltage_dividerVout_result):
        RUI_func.voltage_dividerVout_result.grid_remove()
        


def button_show_voltage_drop():
    if (RUI_func.voltage_dividerR1_result):
        RUI_func.voltage_dividerR1_result.grid_remove()
    if (RUI_func.voltage_dividerR2_result):
        RUI_func.voltage_dividerR2_result.grid_remove()
    if (RUI_func.voltage_dividerVout_result):
        RUI_func.voltage_dividerVout_result.grid_remove()

def button_show_diameter():
    if (RUI_func.voltage_dividerR1_result):
        RUI_func.voltage_dividerR1_result.grid_remove()
    if (RUI_func.voltage_dividerR2_result):
        RUI_func.voltage_dividerR2_result.grid_remove()
    if (RUI_func.voltage_dividerVout_result):
        RUI_func.voltage_dividerVout_result.grid_remove()