def convert_minutes_to_time(minutes):
    hours = (minutes // 60) % 12
    if hours == 0:
        hours = 12
    remaining_minutes = minutes % 60
    if minutes < 720:
        period = "AM"
    else:
        period = "PM"
    return f"{hours:02}:{remaining_minutes:02} {period}"


print(convert_minutes_to_time(135))