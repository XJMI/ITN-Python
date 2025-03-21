import os, json, winsound

def clean_up():
    if os.path.exists("comrates.json"):
        os.remove("comrates.json")
    else:
        return print(f"Failed to clean up json file")

def main():
    print("Welcome to the Sales Commission Calculator!\n")
    winsound.Beep(600, 500)

    with open("comrates.json", "a") as file:
        json_data = """{"commission_rates": {"A": [[10000, 19999, 5],[20000, 39999, 7.5],[40000, "inf", 9]],"B": [[10000, 19999, 6],[20000, 39999, 8],[40000, "inf", 10]],"C": [[10000, 19999, 3],[20000, 39999, 4.5],[40000, "inf", 5.5]]}}"""
        file.write(json_data)
        file.close()

    with open("comrates.json", "r") as file:
        data = json.load(file)

    for keys, ranges in data["commission_rates"].items():
        for i in range(len(ranges)):
            if ranges[i][1] == "inf":
                ranges[i][1] = float("inf")

    commissions_datatable = data["commission_rates"]

    rate = ""
    commission = ""

    product = input("Enter the product type (A, B, or C): ").strip().upper()

    if product not in commissions_datatable:
        print(f"Invalid input! | {product} is not a valid product type.")
        clean_up()
        return

    try:
        sale_amount = float(input("Enter the sale amount: ").strip())
    except ValueError:
        print("Invalid input! | Please enter a number for the sale amount.")
        clean_up()
        return

    for lower, upper, rate in commissions_datatable[product]:
        if lower <= sale_amount <= upper:
            commission = (rate * 0.01) * sale_amount
            break

    print(f"\nProduct Type: {product};\nCommission Rate: {rate:.2f}%;\nCommission Earned: ${commission:,.2f}")
    clean_up()

if __name__ == '__main__':
    main()
