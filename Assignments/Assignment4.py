import my_programs as mp

while True:
    print("\n------ BASIC FUNCTION MENU ------")
    print("1. Print Numbers 1 to 5")
    print("2. Check Even Number")
    print("3. Check Odd Number")
    print("4. Sum of Two Integers")
    print("5. Print Alphabet")
    print("6. Print Star Pattern")
    print("7. Convert Uppercase")
    print("8. Convert Lowercase")
    print("9. Check Greater Number")
    print("10. Print Day Message")
    print("11. Add Three Numbers")
    print("12. Find Average")
    print("13. Perimeter of Square")
    print("14. Perimeter of Rectangle")
    print("15. Print Simple Message")
    print("0. Exit")
    print("-------------------------------")

    choice = input("Enter your choice: ")

    if choice == "1": mp.print_numbers()
    elif choice == "2": mp.check_even()
    elif choice == "3": mp.check_odd()
    elif choice == "4": mp.sum_two()
    elif choice == "5": mp.print_alphabet()
    elif choice == "6": mp.star_pattern()
    elif choice == "7": mp.uppercase()
    elif choice == "8": mp.lowercase()
    elif choice == "9": mp.greater_number()
    elif choice == "10": mp.day_message()
    elif choice == "11": mp.add_three()
    elif choice == "12": mp.average()
    elif choice == "13": mp.perimeter_square()
    elif choice == "14": mp.perimeter_rectangle()
    elif choice == "15": mp.simple_message()
    elif choice == "0":
        print("Exit Successful 👋")
        break
    else:
        print("Invalid choice")
