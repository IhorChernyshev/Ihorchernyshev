input_seconds = int(input("Enter the number of seconds: "))
if input_seconds < 0 or input_seconds >= 8640000:
    print("Invalid value. Please enter a number greater than or equal to 0 and less than 8640000.")

else:
    days = input_seconds // (24 * 60 * 60)
    hours = (input_seconds % (24 * 60 * 60)) // (60 * 60)
    minutes = (input_seconds % (60 * 60)) // 60
    seconds = input_seconds % 60

    time_str = f"{int(days)} {'день' if days == 1 else 'дні' if 2 <= days <= 4 else 'днів'}:{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    print(time_str)