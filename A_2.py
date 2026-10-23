print("Welcome to Campus Cafe")

while True:
    name = input("Enter customer name: ")

    name = name.replace(" ", "")

    if name[0].isupper() and name.isalpha():
        print(
            "\nManu:\n 1. Tea RS. 100\n", "2. Sandwich RS. 250\n", "3. Burger RS. 450\n"
        )

        total_bill = 0
        discount = 0

        while True:
            choice = input("Enter (1/2/3) or enter (done) to finish order: ")

            if choice == "done":
                break
            elif choice == "1" or choice == "2" or choice == "3":
                q = input("Enter quantity: ")

                if q.isdigit() and int(q) > 0:
                    q = int(q)
                    if choice == "1":
                        total_bill += 100 * q
                    elif choice == "2":
                        total_bill += 250 * q
                    elif choice == "3":
                        total_bill += 450 * q
                    else:
                        print("Invalid choice of manu")
                        break
                else:
                    print("Invalid quatity")
                    break
            else:
                print("Invalid choice of manu")
                break

        if total_bill >= 1000:
            discount = 0.1 * total_bill

        final_bill = total_bill - discount

        print("--------------------------------")
        print("Campus Cafe")
        print("Customer Name:", name)
        print("Total bill: RS.", total_bill)
        print("Discount: RS.", discount)
        print("Final bill: RS.", final_bill)
        print("Thank you for order")
        print("--------------------------------")
        break
    else:
        print("First character of name must be capital")
