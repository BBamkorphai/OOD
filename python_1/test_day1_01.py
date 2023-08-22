print(" *** Wind classification ***")
v_wind = float(input("Enter wind speed (km/h) : "))
def check_the_wind(v_wind: float):
    if v_wind<0:
        print("!!!Wrong value can't classify.")
    elif 51.99 >= v_wind>= 0:
        print("Wind classification is Breeze.")
    elif 52.00 <= v_wind<= 55.99:
        print("Wind classification is Depression.")

    elif 56.00 <= v_wind<= 101.99:
        print("Wind classification is Tropical Storm.")

    elif 102.00 <= v_wind<=208.99:
        print("Wind classification is Typhoon.")
    else:
        print("Wind classification is Super Typhoon.")

check_the_wind(v_wind)