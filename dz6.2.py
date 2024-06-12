input_seconds = int(input("Enter the number of seconds: "))
if input_seconds < 0 or input_seconds >= 8640000:
    print("Invalid value. Please enter a number greater than or equal to 0 and less than 8640000.")

else:
    seconds_in_day = 24 * 60 * 60
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60
    days = input_seconds // seconds_in_day
    remaining_seconds = input_seconds % seconds_in_day
    hours = remaining_seconds // seconds_in_hour
    remaining_seconds = remaining_seconds % seconds_in_hour
    minutes = remaining_seconds // seconds_in_minute
    seconds = remaining_seconds % seconds_in_minute
    if days == 1:
        days_word = "день"
    elif 2 <= days <= 4:
            days_word = "дні"
    else:
            days_word = "днів"
    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)
    result = f"{days} {days_word}, {hours_str}:{minutes_str}:{seconds_str}"

    print(result)