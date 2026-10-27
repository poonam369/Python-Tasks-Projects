
from abc import ABC, abstractmethod


class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare

    def display(self):
        print(self.code, "|", self.airline, "|",
              self.source, "to", self.destination,
              "| Seats:", self.seats,
              "| Fare: Rs.", self.fare)


class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def discount(self):
        pass


class RegularPassenger(Passenger):
    def discount(self):
        return 0


class StudentPassenger(Passenger):
    def discount(self):
        return 10


class Booking:
    def __init__(self, booking_id, flight, passenger, tickets,
                 subtotal, discount_amount, total):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets
        self.subtotal = subtotal
        self.discount_amount = discount_amount
        self.total = total

    def display(self):
        print("\n----- Booking Summary -----")
        print("Booking ID:", self.booking_id)
        print("Passenger Name:", self.passenger.name)
        print("Passenger Age:", self.passenger.age)

        if isinstance(self.passenger, StudentPassenger):
            print("Passenger Type: Student")
        else:
            print("Passenger Type: Regular")

        print("Flight Code:", self.flight.code)
        print("Airline:", self.flight.airline)
        print("Route:", self.flight.source, "to",
              self.flight.destination)
        print("Number of Tickets:", self.tickets)
        print("Base Fare per Ticket: Rs.", self.flight.fare)
        print("Subtotal: Rs.", self.subtotal)
        print("Discount: Rs.", self.discount_amount)
        print("Final Amount: Rs.", self.total)


class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Kiran Air", "Mumbai", "Bengaluru", 25, 3500),
            Flight("PN303", "Kiran Air", "Pune", "Hyderabad", 15, 3000)
        ]

        self.bookings = []
        self.booking_number = 1001

    def view_flights(self):
        print("\n----- Available Flights -----")

        for flight in self.flights:
            flight.display()

    def find_flight(self, code):
        for flight in self.flights:
            if flight.code == code:
                return flight

        return None

    def book_flight(self):
        code = input("Enter flight code: ").strip().upper()
        flight = self.find_flight(code)

        if flight is None:
            print("Invalid flight code.")
            return

        name = input("Enter passenger name: ").strip()

        if name == "":
            print("Passenger name cannot be blank.")
            return

        try:
            age = int(input("Enter passenger age: "))
            if age <= 0:
                print("Age must be greater than zero.")
                return

            kind = input("Passenger type (Regular/Student): ")
            kind = kind.strip().lower()

            if kind == "student":
                passenger = StudentPassenger(name, age)
            elif kind == "regular":
                passenger = RegularPassenger(name, age)
            else:
                print("Invalid passenger type.")
                return

            tickets = int(input("Enter number of tickets: "))

            if tickets <= 0:
                print("Number of tickets must be greater than zero.")
                return

        except ValueError:
            print("Please enter valid numbers.")
            return

        if tickets > flight.seats:
            print("Booking failed: Not enough seats available.")
            return

        subtotal = flight.fare * tickets
        discount_amount = subtotal * passenger.discount() / 100
        total = subtotal - discount_amount

        booking_id = "BK" + str(self.booking_number)

        booking = Booking(
            booking_id, flight, passenger, tickets,
            subtotal, discount_amount, total
        )

        flight.seats = flight.seats - tickets
        self.bookings.append(booking)
        self.booking_number += 1

        print("\nBooking confirmed!")
        booking.display()

    def view_booking(self):
        if len(self.bookings) == 0:
            print("No bookings available.")
        else:
            print("\n----- Confirmed Bookings -----")

            for booking in self.bookings:
                booking.display()

    def run(self):
        print("Welcome to Kiran Air Booking")

        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.view_flights()

            elif choice == "2":
                self.book_flight()

            elif choice == "3":
                self.view_booking()

            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break

            else:
                print("Invalid choice. Please select 1, 2, 3 or 4.")


app = FlightBookingSystem()
app.run()
