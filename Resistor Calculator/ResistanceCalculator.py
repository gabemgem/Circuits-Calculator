#Most of the resistors available in the Circuits lab and AD Parts Kit
resistors = [1, 6.2, 10, 47, 68, 100, 470, 1000, 1500, 2200, 4700, 6800, 10000,
20000, 47000, 68000, 100000, 200000, 470000, 1000000, 10000000, 2.2, 2.7, 3.3,
3.9, 4.7, 5.6, 6.8, 8.2, 12, 15, 18, 22, 27,
33, 39, 47, 51, 56, 68,75, 82, 120, 150, 180, 220, 270, 330, 390, 510,
560, 680, 820, 1200, 1800, 2000, 2700, 3300, 3900, 5600, 22000, 8200, 27000]

#Same as above but only the higher resistors
resistorsh = [100, 470, 1000, 1500, 2200, 4700, 6800, 10000,
20000, 47000, 68000, 100000, 200000, 470000, 1000000, 10000000, 120, 150, 180, 220, 270, 330, 390, 510,
560, 680, 820, 1200, 1800, 2000, 2700, 3300, 3900, 5600, 22000, 8200, 27000]

#Function to compute voltage divider resistor values from all resistors
def voltage_divider(num, vins, vouts):
    error = float(1000000)
    best = float(0)
    
    for i in range(1, num+1):
        if vins[i]<vouts[i]:
            print("Invalid Vin and Vout: "+str(vins[i]) + " -> "+str(vouts[i]))
        else:
            target = vouts[i]
            start = vins[i]
            for a in resistors:
                for b in resistors:
                    test = float(start)*b/(a+b)
                    testerror = abs(test-target)
                    if testerror < error:
                        r1 = a
                        r2 = b
                        error = testerror
                        best = test
            print("Vout"+str(i)+": "+str(best)+"\tR1: "+str(r1)+"\tR2: "+str(r2))
            error = float(10000000)
            best = float(0)

#Same as above but uses only high resistors
def voltage_divider_high(num, vins, vouts):
    error = float(1000000)
    best = float(0)

    for i in range(1, num+1):
        if vins[i]<vouts[i]:
            print("Invalid Vin and Vout: "+str(vins[i]) + " -> "+str(vouts[i]))
        else:
            target = vouts[i]
            start = vins[i]
            for a in resistorsh:
                for b in resistorsh:
                    test = float(start)*b/(a+b)
                    testerror = abs(test-target)
                    if testerror < error:
                        r1 = a
                        r2 = b
                        error = testerror
                        best = test
            print("Vout"+str(i)+": "+str(best)+"\tR1: "+str(r1)+"\tR2: "+str(r2))
            error = float(10000000)
            best = float(0)

#Function to find resistor values for a non-inverting op amp amplifier circuit
#Only uses high resistors and may not work
#CHECK ANSWERS IF YOU ARE USING THIS FOR THE FIRST TIME
def op_amp_amplifier(num, vins, vouts):
    
    error = float(1000000)
    best = float(0)

    for i in range(1, num+1):
        if vins[i]>vouts[i]:
            print("Invalid Vin and Vout: "+str(vins[i]) + " -> "+str(vouts[i]))
        else:
            target = vouts[i]
            start = vins[i]
            for a in resistorsh:
                for b in resistorsh:
                    test = float(start)*(1+(b/a))
                    testerror = abs(test-target)
                    if testerror < error:
                        r1 = a
                        r2 = b
                        error = testerror
                        best = test
            print("Vout"+str(i)+": "+str(best)+"\tR1: "+str(r1)+"\tR2: "+str(r2))
            error = float(10000000)
            best = float(0)




option = raw_input("What do you want to calculate?\n"
                   "VD(voltage divider), VDH(voltage divider high),"
                   "OAA(op amp amplifier)\n").upper()
num = input("How many do you want to do? ")

vins = [0]
vouts = [0]
for i in range(1,num+1):
    vins.append(input("Vin" + str(i) + " "))
    vouts.append(input("Vout"+ str(i) + " "))


if option == "VD":
    voltage_divider(num, vins, vouts)

elif option == "VDH":
    voltage_divider_high(num, vins, vouts)

elif option == "OAA":
    op_amp_amplifier(num, vins, vouts)

#wait until user presses a button to quit program    
raw_input()


