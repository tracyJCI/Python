#KJC4 4CREDITS
def main():
    hourly_rate,no_of_hours= eval(input("please input your hourly rate, the number of hours you worked for the week:"))
    if no_of_hours > 40 :
        overtime_hours = no_of_hours - 40
        overtime_hourly_rate = 1.5 * hourly_rate
        overtime_wages = overtime_hours * overtime_hourly_rate
        total_wages = (hourly_rate * 40) + overtime_wages
        print("your total wages for the week are :" , total_wages)
    else :
        total_wages = no_of_hours * hourly_rate
        print("your total wages for the week are:", total_wages)
main()
