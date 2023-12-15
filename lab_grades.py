# activity 2: 
def terminate():
    quit = input("Are you sure? (y/n): ")
    if quit.lower() == "y":
        return True
    else: 
        return False

def student_lab_average(record):
    grade = 0
    i=2
    while i < 10: 
        if record[i] == "":
            grade += 0  
            i +=1
        else:
            grade += float(record[i])
            i+=1
    return (grade/8) 
    
def main():
    while True:
        try:
            print("\nYou could enter the following filenames:")
            print("\"data/grades_010.csv\"")
            print("\"data/grades_363.csv\"\n")
            filename = input(">> ")
            if filename == "quit":
                if terminate()== True:
                    print("Goodbye!")
                    break
                else:
                    continue
            elif filename == "":
                print("Enter a command or \"quit\" to quit:")
                continue
            else:
                with open(filename) as file:
                    print("\nLab Averages from:", filename)
                    print("—----------------------------------------------------------")
                    print("Student                                         Lab Average")
                    print("—----------------------------------------------------------")
                    count = 0
                    total_grade = 0
                    min = 100 #minimum lab average will be below 100
                    max = 0
                    for student in file:
                        try: 
                            student_report = student.strip()
                            record = student_report.split(",")
                            average = student_lab_average(record)
                            print(record[0],", ",record[1],"\t\t\t\t\t", average, sep="")
                            total_grade += average
                            count+=1
                            
                            if average < min:
                                min = average
                            elif average > max:
                                max = average
                            else: 
                                continue
                        except ValueError:
                            continue
                    average = (total_grade/count)
                    print("—----------------------------------------------------------")
                    print("Class Average                                   ", average)
                    print("Class Minimum                                   ", min)
                    print("Class Maximum                                   ", max)
                    print()      
        except FileNotFoundError:
                print("No such file:", filename)

main()