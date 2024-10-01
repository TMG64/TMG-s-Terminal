import time

commands = "?help: helps you with commands \n ?help 2: 2nd part of help command \n ?print: Print almost any words you like to print \n ?Mprint: Mass print almost anything \n ?Add: Additions function \n --------Page 1/3-------- "
commands2 = "?Sub: Subtraction function \n ?Multi: Multiply function \n ?Div: Divisions \n ?multi: multiplication fonction \n ?wait: counts time, alternative: ?sleep \n --------Page 2/3--------"
LocalInput = ""
SecondLocalInput = 0
Activate = False
FirstStringMemory = 0
SecondStringMemory = 0
repeat_time = 0
timewait = 0
seconds = 0
minuts = 0
DEBUGMODE = False




while True:
        LocalInput = input("Welcome To TMG's Terminal, print ?help for help \n  :")

        if LocalInput in ["?help", "?Help", "?HELP"]:
            print(" :\n", commands)
            time.sleep(2)
            continue

        elif LocalInput == "?help 2":
            print(" :\n", commands2)
            time.sleep(2)
            continue

        elif LocalInput in ["?print", "?Print", "?PRINT"]:
            to_print = input("What would you like to print? (no custom chars) \n  :")
            time.sleep(0.5)
            print(to_print)
            continue

        elif LocalInput in ["?Mprint", "?mprint", "?MPrint", "MPRINT"]:
            to_print = input("What would you like to mass print? (no custom chars) \n  :")
            time.sleep(0.5)
            try:
                repeat_times = int(input("How many times? (only digits !!!) \n  :"))
                for _ in range(repeat_times):
                    print(to_print)
                    time.sleep(0.02)
            except ValueError:
                print("ERROR!!!")
            time.sleep(2)
            continue

        elif LocalInput in ["?Add", "?add", "?ADD", "?+"]:
            Activate = True
            try:
                FirstStringMemory = int(input("Which number will you choose to be added to (only digits !!!) \n   :"))
                SecondStringMemory = int(input(f"Which number will you add {FirstStringMemory} to \n   :"))
                
                if DEBUGMODE == True:
                    
                        FinalValue = FirstStringMemory + SecondStringMemory
                        print("Result is ", FinalValue)
                    
                elif DEBUGMODE == False:
                        print("Calculating...")
                        time.sleep(1)
                        print("Done!")
                        time.sleep(1)
                        FinalValue = FirstStringMemory + SecondStringMemory
                        print("Result is ", FinalValue)
            except ValueError:
                print("ERROR: Please enter valid digits.")
            time.sleep(3)
            continue

        elif LocalInput in ["?Sub", "?sub", "?SUB", "?-", "?substract", "?Substract", "?SUBSTRACT"]:
            Activate = True
            try:
                FirstStringMemory = int(input("Which number will you choose to be subtracted from (only digits !!!) \n   :"))
                SecondStringMemory = int(input(f"Which number will you subtract from {FirstStringMemory} \n   :"))
                if DEBUGMODE == True:
                    
                        FinalValue = FirstStringMemory - SecondStringMemory
                        print("Result is ", FinalValue)
                    
                elif DEBUGMODE == False:
                        print("Calculating...")
                        time.sleep(1)
                        print("Done!")
                        time.sleep(1)
                        FinalValue = FirstStringMemory - SecondStringMemory
                        print("Result is ", FinalValue)
            except ValueError:
                print("ERROR: Please enter valid digits.")
            time.sleep(3)
            continue

        elif LocalInput in ["?multi", "?Multi", "?MULTI", "?multiply", "?Multiply", "?MULTIPLY"]:
            Activate = True
            try:
                FirstStringMemory = int(input("Which number will you choose to multiply (only digits !!!) \n   :"))
                SecondStringMemory = int(input(f"Which number will you multiply {FirstStringMemory} by \n   :"))
                if DEBUGMODE == True:
                    
                        FinalValue = FirstStringMemory * SecondStringMemory
                        print("Result is ", FinalValue)
                    
                elif DEBUGMODE == False:
                        print("Calculating...")
                        time.sleep(1)
                        print("Done!")
                        time.sleep(1)
                        FinalValue = FirstStringMemory * SecondStringMemory
                        print("Result is ", FinalValue)
            except ValueError:
                print("ERROR: Please enter valid digits.")
            time.sleep(3)
            continue

        elif LocalInput in ["?div", "?Div", "?DIV", "?divide", "?Divide", "?DIVIDE"]:
            Activate = True
            try:
                FirstStringMemory = int(input("Which number will you choose to divide (only digits !!!) \n   :"))
                SecondStringMemory = int(input(f"Which number will you divide {FirstStringMemory} by \n   :"))
                if SecondStringMemory == 0:
                    while True:
                        repeat_time = repeat_time + 1
                        for _ in range(1 + repeat_time):
                            print("ERROR!! \n")

                if DEBUGMODE == True:
                    
                        FinalValue = FirstStringMemory / SecondStringMemory
                        print("Result is ", FinalValue)
                    
                elif DEBUGMODE == False:
                        print("Calculating...")
                        time.sleep(1)
                        print("Done!")
                        time.sleep(1)
                        FinalValue = FirstStringMemory / SecondStringMemory
                        print("Result is ", FinalValue)
            except ValueError:
                print("ERROR: Please enter valid digits.")
            time.sleep(3)
            continue
        
        elif LocalInput in ["?wait", "?Wait", "?WAIT", "?sleep", "?Sleep", "?SLEEP"]:
            seconds = 0
            minuts = 0
            while True:
                    
                    seconds = seconds + 1

                    time.sleep(1)
                
                    if seconds > 60:
                        minuts = minuts + 1
                        seconds = seconds - 60
                    
                    print(seconds, "second(s) ", minuts, "minut(s)")