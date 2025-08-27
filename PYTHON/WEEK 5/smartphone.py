# smartphone.py

# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


# Child class: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, os, battery=100):
        super().__init__(brand, model)
        self.os = os
        self.battery = battery

    def call(self, contact):
        if self.battery > 0:
            print(f"📞 Calling {contact}... Battery: {self.battery}%")
            self.battery -= 5
        else:
            print("❌ Battery too low to make a call!")

    def install_app(self, app):
        print(f"📲 Installing {app} on {self.brand} {self.model}.")

    def charge(self):
        self.battery = 100
        print("⚡ Phone fully charged!")

    def check_battery(self):
        print(f"🔋 Battery: {self.battery}%")


# Interactive test mode
def main():
    phone = Smartphone("Samsung", "Galaxy S25", "Android", 50)

    print("Welcome to Smartphone Simulator!")
    print(f"Your device: {phone.info()} ({phone.os})")
    print("Type: call <name>, install <app>, charge, battery, quit")

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command.startswith("call "):
            name = command.split(" ", 1)[1]
            phone.call(name)

        elif command.startswith("install "):
            app = command.split(" ", 1)[1]
            phone.install_app(app)

        elif command == "charge":
            phone.charge()

        elif command == "battery":
            phone.check_battery()

        elif command == "quit":
            print("👋 Exiting Smartphone Simulator. Goodbye!")
            break

        else:
            print("❓ Unknown command. Try again.")


if __name__ == "__main__":
    main()

