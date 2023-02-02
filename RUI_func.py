from tkinter import *
from tkinter import messagebox as mb
#from Calc_interface import *
import Calc_interface
import math
counter_vd = 11
counter = 5

voltage_dividerR1_result = None
voltage_dividerR2_result = None
voltage_dividerVout_result = None

#------------------------------------FUNCTIONS------------------------------------------#

        #-------------------LED RESISTOR CALCULATION-------------------#

def led_resistor():
    global led_window
    global led_calc_result_lab
    global led_calc_discr_label
    global counter

    try:
        float(Calc_interface.Uin_input.get())
        float(Calc_interface.U_led_input.get())
        float(Calc_interface.I_led_input.get())
        pass
    except ValueError:
        mb.showerror("Error", "Enter digits, boy!")
    Uin = float(Calc_interface.Uin_input.get())
    U_led = float(Calc_interface.U_led_input.get())
    I_led = float(Calc_interface.I_led_input.get())

    R = (Uin - U_led)/(I_led*0.001)
    R_result = R



    led_calc_result_lab = Label(Calc_interface.led_window, text="Take about " + str(int(R_result)) + " Ohm")
    led_calc_result_lab.grid(row=counter, column=2)
    led_calc_discr_label = Label(Calc_interface.led_window, text= "Vin = " + str(Uin) + "V" + " | U_led = "
                                                   + str(U_led)+ "V" + " | I_led = " + str(I_led)+ "mA")
    led_calc_discr_label.grid(row=counter, column=0, columnspan=2)
    if (counter == 20):
        counter = 3
    counter = counter + 1


            # -------------------Voltage divider CALCULATION-------------------#

def voltage_divider_calc_R1():
    global voltage_divider_window
    global counter_vd
    global R1_result_lab
    global voltage_dividerR1_result
    global voltage_dividerR2_result
    global voltage_dividerVout_result

    try:
        float(Calc_interface.R2_input.get())
        float(Calc_interface.Vout_input.get())
        float(Calc_interface.Vin_input.get())
        pass
    except ValueError:
        mb.showerror("Error", "Enter digits, boy!")

    R2 = float(Calc_interface.R2_input.get())
    Vout = float(Calc_interface.Vout_input.get())
    Vin = float(Calc_interface.Vin_input.get())

    R1 = ((Vin - Vout)*R2)/Vout
    R1_result = R1

    voltage_dividerR1_result_lab = Label(Calc_interface.voltage_divider_window, text="Take value of R1 about "
                                                                                     + str(int(R1_result)) + " Ohm",fg='darkblue')
    voltage_dividerR1_result_lab.grid(row=counter_vd, column=2, columnspan=2)
    voltage_dividerR1_discr_label = Label(Calc_interface.voltage_divider_window, text="Vin = " + str(Vin) + "V" + " | Vout = "
                                                  + str(Vout) + "V" + " | R2 = " + str(R2) + "Ohm")
    voltage_dividerR1_discr_label.grid(row=counter_vd, column=0, columnspan=2)
    voltage_dividerR1_result = Label(Calc_interface.voltage_divider_window, text=str(int(R1_result)) + " Ohm" ,fg='darkblue')
    voltage_dividerR1_result.grid(row=5, column=1, sticky="e")

    if ((((Vin**2)/R1) >= 0.0625) or (((Vin**2)/R2) >= 0.0625)):
        attention_message = Label(Calc_interface.voltage_divider_window, text="Attention! Take care of resistor's power!", fg='red')
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
        float(Calc_interface.R1_input.get())
        float(Calc_interface.Vout_input.get())
        float(Calc_interface.Vin_input.get())
        pass
    except ValueError:
        mb.showerror("Error", "Enter digits, boy!")

    R1 = float(Calc_interface.R1_input.get())
    Vout = float(Calc_interface.Vout_input.get())
    Vin = float(Calc_interface.Vin_input.get())

    R2 = (R1 * Vout)/(Vin - Vout)
    R2_result = R2

    voltage_dividerR2_result_lab = Label(Calc_interface.voltage_divider_window,
                                         text="Take value of R2 about " + str(int(R2_result)) + " Ohm", fg='darkblue')
    voltage_dividerR2_result_lab.grid(row=counter_vd, column=2, columnspan=2)
    voltage_dividerR2_discr_label = Label(Calc_interface.voltage_divider_window, text="Vin = " + str(Vin) + "V" + " | Vout = "
                                                                       + str(Vout) + "V" + " | R1 = " + str(R1) + "Ohm")
    voltage_dividerR2_discr_label.grid(row=counter_vd, column=0, columnspan=2)
    voltage_dividerR2_result = Label(Calc_interface.voltage_divider_window, text=str(int(R2_result)) + " Ohm", fg='darkblue')
    voltage_dividerR2_result.grid(row=6, column=1, sticky="e")  #Result of calculation.

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
        float(Calc_interface.R1_input.get())
        float(Calc_interface.R2_input.get())
        float(Calc_interface.Vin_input.get())
        pass
    except ValueError:
        mb.showerror("Error", "Enter digits, boy!")

    R1 = float(Calc_interface.R1_input.get())
    R2 = float(Calc_interface.R2_input.get())
    Vin = float(Calc_interface.Vin_input.get())

    Vout = (R2 * Vin) / (R1 + R2)
    Vout_result = Vout

    voltage_dividerVout_result_lab = Label(Calc_interface.voltage_divider_window,
                                         text="Vout = " + str(float(round((Vout_result),2))) + " Volts", fg='darkblue')
    voltage_dividerVout_result_lab.grid(row=counter_vd, column=2, columnspan=2)
    voltage_dividerVout_discr_label = Label(Calc_interface.voltage_divider_window, text="Output voltage result with entered values are:")
    voltage_dividerVout_discr_label.grid(row=counter_vd, column=0, columnspan=2)
    voltage_dividerVout_result = Label(Calc_interface.voltage_divider_window, text=str(int(Vout_result)) + " Volts", fg='darkblue')
    voltage_dividerVout_result.grid(row=6, column=4, sticky="w")

    if (counter_vd == 15):
        counter_vd = 11
    counter_vd = counter_vd + 1


        #-----------------MAX WIRE CURRENT CALCULATION-----------------#

def wire_current_I():
    global D_input
    global MaxI_result
    global counter_vd

    try:
        float(Calc_interface.D_input.get())
        pass
    except ValueError:
        mb.showerror("Error", "Enter digits, boy!")
    D = float(Calc_interface.D_input.get())
    S = (3.14*(D*D))/4
    MaxI_result = 6 * S

    #Add COPPER/ALUMINIUM characteristics

    MaxI_result_string = Label(Calc_interface.wire_window, text="Max current of " + str(int(D))
                                                                + " mm diameter wire is " + str(int(MaxI_result))
                                                                + " Amperes", fg='darkblue')
    MaxI_result_string.grid(row=counter_vd, column=1)

    if (counter_vd == 15):
        counter_vd = 11
    counter_vd = counter_vd + 1

def wire_current_D():
    global I_input
    global l_input
    global V_input
    global MaxD_result
    global MaxS_result
    global counter_vd

    try:
        float(Calc_interface.I_input.get())
        float(Calc_interface.l_input.get())
        pass
    except ValueError:
        mb.showerror("Error", "Enter digits, boy!")
    I = float(Calc_interface.I_input.get())
    l = float(Calc_interface.l_input.get())
    MaxD_result = 2 * (math.sqrt(0.0172 * (l/((0.6/(I))*3.14))))
    MaxS_result = (3.14 * (MaxD_result * MaxD_result))/4

    MaxD_result_string = Label(Calc_interface.wire_window, text="Min diameter of wire for current of "
                                                                + str(float(I)) + " Amperes is "
                                                                + str(float(round((MaxD_result), 2))) + " mm "
                                                                + "   Max S = " + str(float(round((MaxS_result), 3)))
                                                                + " mm^2", fg='darkblue')
    MaxD_result_string.grid(row=counter_vd, column=0, columnspan=3)

    if (counter_vd == 15):
        counter_vd = 11
    counter_vd = counter_vd + 1

def wire_current_V():
    global D_Voltage_drop_input
    global l_Voltage_drop_input
    global MaxV_result
    global counter_vd
    #TO ADD COPPER/ALUMINIUM etc.
    try:
        float(Calc_interface.D_Voltage_drop_input.get()) or float(Calc_interface.l_Voltage_drop_input.get())
        pass
    except ValueError:
        mb.showerror("Error", "Enter digits, boy!")
    D = float(Calc_interface.D_Voltage_drop_input.get())
    l = float(Calc_interface.l_Voltage_drop_input.get())
    MaxV_result = D*l

    MaxV_result_string = Label(Calc_interface.wire_window, text="Approximate Voltage drop of " + str(int(l)) + " mm wire length with "
                                                                + str(int(D)) + " mm diameter is " + str(int(MaxV_result))
                                                                + " Volts", fg='darkblue')
    MaxV_result_string.grid(row=counter_vd, column=0, columnspan=3)

    if (counter_vd == 15):
        counter_vd = 11
    counter_vd = counter_vd + 1


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
