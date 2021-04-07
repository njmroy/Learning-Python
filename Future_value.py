# future_value function definition
# Parameter variables present, interest, months must be numbers

def future_value(present, interest, months):
    # Calculate future value and store in formatted string
    text="Future value is $%.2f" % (present * ( pow(( 1 +interest ),months)))

    # Display result to user
    print(text)
    return

def main():
    #Get values from user
    present = float(input("Enter present value: "))
    interest = float(input("Enter interest rate: "))
    months = float(input("Enter number of months: "))

    #Call future_value function on user input
    future_value(present, interest, months)

# Main function call
main()
