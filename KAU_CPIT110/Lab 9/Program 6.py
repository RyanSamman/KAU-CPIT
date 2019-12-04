def celsiusToFahrenheit(celsus):
    fahrenheit = (9/5) * celsus + 32
    return fahrenheit


def fahrenheitToCelsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius


def main():
    start_celsius, jump_celsus = 40, -1
    start_fahrenheit, jump_fahrenheit = 120, -10
    rows = 9

    print(format("Celsius", "<15s") + format("Fahrenheit", "<15s") + "|     " +
          format("Fahrenheit", "<15s") + format("Celsius", "<15s"))
    print("-"*58)

    for i in range(rows + 1):
        print(format(start_celsius, "<15d") + format(celsiusToFahrenheit(start_celsius), "<15.2f") + "|     " +
              format(start_fahrenheit, "<15d") + format(fahrenheitToCelsius(start_fahrenheit), "<15.2f"))

        start_celsius += jump_celsus
        start_fahrenheit += jump_fahrenheit


if __name__ == '__main__':
    main()
