# Imports
try:
    import time
    from plyer import notification
    import pyowm
    import time
    import pyfiglet
    import sys
    import pip
    #from pyowm.exceptions import api_response_error
    
except Exception:
    # Installing additional modules
    answer = input("\nYou not install some dependencies. You want to install it? (y/n): ")

    while True:
        answer = answer.strip().lower()
        if answer in ('y', 'yes'):
            pip.main(['install', "pyowm"])
            pip.main(['install', "pyfiglet"])
            pip.main(['install', "plyer"])
            break

        if answer in ('n', 'no'):
            print("\nAborting.")
            input("\nPress any key to exit. ")
            sys.exit()

# City selection
result = pyfiglet.figlet_format("WeatherNotify")
print(result)

city = input("Enter the location for monitoring. Like 'New York': ")

# PyOWM initialization
try:
    owm = pyowm.OWM('bc12083e70d2d22298c2df1cec7101d9')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    temp = w.temperature("celsius")["temp"]
    temp = round(temp)
    temp = str(temp)

except Exception:
    print("\nPyOWM Error, Aborting.")
    input("\nPress any key to exit. ")
    sys.exit()

# Weather now
print("\nNow in the " + city + " " + temp + "°C degrees.")
print("\nWe informate you when weather changes in the Windows notification and here.")

# Notify when weather changes
def WarnMessage():
    if globalVal < oldglobalVal:
        print('\nWeather got colder! \nNew weather: ' + globalVal + "°C degrees.")
        try:
            notification.notify(
                title = 'Weather',
                message = 'Weather got colder! \nNew weather: ' + globalVal + "°C degrees.",
                app_icon = None,
                timeout = 10,
            )
        except Exception:
            pass
    else:
        print('\nWeather got warmer! \nNew weather: ' + globalVal + "°C degrees.")
        try:
            notification.notify(
                title = 'Weather',
                message = 'Weather got warmer! \nNew weather: ' + globalVal + "°C degrees.",
                app_icon = None,
                timeout = 10,
            )
        except Exception:
            pass

# Check if new weather != old weather
def setValue(val):
    global globalVal
    global oldglobalVal

    oldglobalVal = globalVal 
    valueChanged = globalVal != val

    globalVal = val

    if valueChanged:
        WarnMessage()

globalVal = temp

# Main weather check loop
while True:
    try:
        time.sleep(10)
        temp = w.temperature("celsius")["temp"]
        temp = round(temp)
        temp = str(temp)
        setValue(temp)
    except Exception:
        print("\nPyOWM Error, Aborting.")
        input("\nPress any key to exit. ")
        sys.exit()


