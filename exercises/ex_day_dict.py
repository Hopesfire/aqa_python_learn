days = {
    1: "Monday", 2: "Tuesday", 3: "Wednesday",4: "Thursday",
    5: "Friday", 6: "Saturday", 7: "Sunday"
}

def number_to_day(number):
    return days.get(number)
        
print(number_to_day(4))