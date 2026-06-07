device_ststus = "active"
teamperature = 38

if device_ststus == "active":
    if teamperature > 35:
        print("Warn : High Temperature")
    else:
        print("Temperature Normal")
else:
    print("Device is Offline")
