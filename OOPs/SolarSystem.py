class Planet:
    def __init__(self, name, order_from_sun, planet_type, distance_million_km, has_life):
        self.name = name
        self.order_from_sun = order_from_sun
        self.planet_type = planet_type
        self.distance_million_km = distance_million_km
        self.has_life = has_life

    def show_details(self):
        print("\n--- Planet Details ---")
        print(f"Name              : {self.name}")
        print(f"Order from Sun    : {self.order_from_sun}")
        print(f"Type              : {self.planet_type}")
        print(f"Distance from Sun : {self.distance_million_km} million km")
        print(f"Life Present      : {'Yes' if self.has_life else 'No'}")
        print("----------------------")


class SolarSystem:
    def __init__(self, name):
        self.name = name
        self.planets = []

    def add_planet(self, planet):
        self.planets.append(planet)

    def show_all_planets(self):
        print(f"\n=== {self.name} ===")
        for planet in self.planets:
            print(f"{planet.order_from_sun}. {planet.name}")

    def find_planet(self, planet_name):
        for planet in self.planets:
            if planet.name.lower() == planet_name.lower():
                return planet
        return None


def main():
    solar_system = SolarSystem("Solar System")

    # Creating planet objects
    solar_system.add_planet(Planet("Mercury", 1, "Terrestrial", 57.9, False))
    solar_system.add_planet(Planet("Venus", 2, "Terrestrial", 108.2, False))
    solar_system.add_planet(Planet("Earth", 3, "Terrestrial", 149.6, True))
    solar_system.add_planet(Planet("Mars", 4, "Terrestrial", 227.9, False))
    solar_system.add_planet(Planet("Jupiter", 5, "Gas Giant", 778.5, False))
    solar_system.add_planet(Planet("Saturn", 6, "Gas Giant", 1434, False))
    solar_system.add_planet(Planet("Uranus", 7, "Ice Giant", 2871, False))
    solar_system.add_planet(Planet("Neptune", 8, "Ice Giant", 4495, False))

    while True:
        print("\nChoose an option:")
        print("1. Show all planets")
        print("2. View planet details")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            solar_system.show_all_planets()

        elif choice == "2":
            name = input("Enter planet name: ")
            planet = solar_system.find_planet(name)
            if planet:
                planet.show_details()
            else:
                print("Planet not found.")

        elif choice == "3":
            print("Exiting Solar System Program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
