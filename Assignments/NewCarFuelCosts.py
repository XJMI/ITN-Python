def calculate_cost(miles_per_week, average_mpg, current_fuel_cost, car_type):
    if miles_per_week and average_mpg and current_fuel_cost and car_type:
        total_gallons_used = miles_per_week / average_mpg
        estimated_cost = total_gallons_used * current_fuel_cost
        return print(f"\n> The Weekly Estimated Gas Cost For a {car_type} is: ${estimated_cost:.2f}")

def main():
    print("<<| Welcome to The Gas Cost Estimator |>>")

    try:
        car_type = str(input("\n> Please Enter the Car's Maker & Model: ").strip())
        average_mpg = int(input(f"> What is {car_type}'s Average MPG Rating: "))
        current_fuel_cost = float(input("> What is The Current Cost of A Gallon: "))
        miles_per_week = int(input("> How Many Miles do You Drive Per-Week: "))
    except ValueError:
        print("Error: Incorrect Input, Please Try Again!")
        return

    calculate_cost(miles_per_week, average_mpg, current_fuel_cost, car_type)

main()
