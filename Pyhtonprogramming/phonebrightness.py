brightness = 50 # Initial brightness
time = 1 # Initial time in hours
battery_level = 100 # Initial battery level
while time <= 12:
    if time <6:
        brightness= 20
    elif time < 9:
        brightness = 50
    elif time < 12:
        brightness = 80
    else:
        brightness = 30

    



    print(f"At {time}AM, screen brightness: {brightness}%")
    time += 1
    battery_level -= 5 # Decrease battery level by 5% each hour
    print(f"Battery level: {battery_level}%")
    if battery_level < 0:
        print("Battery dead, stopping brightness adjustment.")
        break