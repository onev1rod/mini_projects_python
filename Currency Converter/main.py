def main():
    price = float(input("Enter amount: "))
    price_convert = round(convert(price),2)
    print(f"{price} {from_unit} --> {price_convert} {to_unit}")

options = """
1. Dollars to VND
2. VND to Dollars
Select the option you want to convert: (enter 0 if you wantna quit)
"""
while True:
    try:
        option = int(input(f'{options}'))
        if option == 0:
            break
        elif option == 1:
            from_unit = "USD"
            to_unit = "VND"
            convert = lambda price: price * 25457
            main()
            break
        elif option == 2:
            from_unit = "VND"
            to_unit = "USD"
            convert = lambda price: price * 0.000039
            main()
            break
        else:
            print("Invalid input, please choose in the list option!!")
    except ValueError:
        print("Invalid input, please enter a number!")