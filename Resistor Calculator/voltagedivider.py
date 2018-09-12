
resistors = [1, 6.2, 10, 47, 68, 100, 470, 1000, 1500, 2200, 4700, 6800, 10000,
20000, 47000, 68000, 100000, 200000, 470000, 1000000, 10000000, 2.2, 2.7, 3.3,
3.9, 4.7, 5.6, 6.8, 8.2, 12, 15, 18, 22, 27,
33, 39, 47, 51, 56, 68,75, 82, 120, 150, 180, 220, 270, 330, 390, 510,
560, 680, 820, 1200, 1800, 2000, 2700, 3300, 3900, 5600, 22000, 8200, 27000]

resistorsh = [100, 470, 1000, 1500, 2200, 4700, 6800, 10000,
20000, 47000, 68000, 100000, 200000, 470000, 1000000, 10000000, 120, 150, 180, 220, 270, 330, 390, 510,
560, 680, 820, 1200, 1800, 2000, 2700, 3300, 3900, 5600, 22000, 8200, 27000]

r1 = resistors[0]
r2 = resistors[0]

option = raw_input("What do you want to calculate?\n"
                   "VD(voltage divider), VDH(voltage divider high),"
                   "OAA(op amp amplifier)\n").upper()
num = input("How many do you want to do? ")
vins = [0]
vouts = [0]
for i in range(1,num+1):
    vins.append(input("Vin" + str(i) + " "))
    vouts.append(input("Vout"+ str(i) + " "))

error = float(1000000)
best = float(0)

if option == "VD":
    for i in range(1, num+1):
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
        print("Vout"+str(i)+": "+str(best)+"R1: "+str(r1)+"R2: "+str(r2))
        error = float(10000000)
        best = float(0)

elif option == "VDH":
    for i in range(1, num+1):
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
        print("Vout"+str(i)+": "+str(best)+"R1: "+str(r1)+"R2: "+str(r2))
        error = float(10000000)
        best = float(0)

elif option == "OAA":

    for a in resistors:
        for b in resistors:
            test = float(start)*(1+(b/a))
            testerror = abs(test-target)
            if testerror < error:
                r1 = a
                r2 = b
                error = testerror
                best = test


