from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer

def main():
    car = ParkedCar("Toyota", "Tundra", "Gray", "123-123", 60)
    meter = ParkingMeter(60)
    officer = PoliceOfficer("Sgt. Guy", "12345")
    ticket = officer.inspection(car, meter)

    if ticket:
        print("Ticket Served!\n")
        print(ticket.ticket())
    else:
        print("No ticket given, validated parking.")

if __name__ == "__main__":
    main()
