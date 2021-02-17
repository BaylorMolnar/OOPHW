import HW2


def main():

    car_make = input("Enter the car make: ")
    car_year = input("Enter the car year: ")
    # car_speed = 0
    car = HW2.Car(car_year, car_make)

    for iteration in range(5):
        car.accelerate()
        print("Accelerating... Your current speed is:", car.get_speed())
    for iteration in range(5):
        car.brake()
        print("Braking... Your current speed is:", car.get_speed())


main()