class Country:

    __slots__ = ["__name", "__environment", "__economy", "__culture", "__healthcare", "__education"]

    def __init__(self, name, environment, economy, culture, healthcare, education):
        self.__name = name
        self.__environment = self.validate_input(environment)
        self.__economy = self.validate_input(economy)
        self.__culture = self.validate_input(culture)
        self.__healthcare = self.validate_input(healthcare)
        self.__education = self.validate_input(education)


    def validate_input(self, value):
        try:
            value = int(value)
            if value < 0:
                return 0  #if the user enters a value less than 100, we will set it as 0 by default
            elif value > 100:
                return 100  #if the user enters a value more than 100, we will set it as 100 by default
            else:
                return value
        except ValueError:
            print("Invalid input. Using default value 0.")
            return 0  #if the user enters a non-integer value, we will set it as 100 by default


    def get_name(self):
        return self.__name

    def get_environment(self):
        return self.__environment

    def get_economy(self):
        return self.__economy

    def get_culture(self):
        return self.__culture

    def get_healthcare(self):
        return self.__healthcare

    def get_education(self):
        return self.__education


class HappinessMeter:
    def __init__(self):
        self.countries = []

    def adding_countries(self, country):
        self.countries.append(country)

    def measure_happiness(self, country):
        happiness_calculator = (
            country.get_environment()
            + country.get_economy()
            + country.get_culture()
            + country.get_healthcare()
            + country.get_education()
        )
        return happiness_calculator


def main():
    try:
        number_of_countries = int(input("Enter the number of countries you want to assess: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    countries = []
    for _ in range(number_of_countries):
        name = input("Enter the country's name: ")
        if not name:
            print("Country name is required. Skipping this entry.")
            continue

        environment = input("Enter environment factor (0-100): ")
        economy = input("Enter economy factor (0-100): ")
        culture = input("Enter culture factor (0-100): ")
        healthcare = input("Enter healthcare factor (0-100): ")
        education = input("Enter education factor (0-100): ")

        country = Country(name, environment, economy, culture, healthcare, education)
        countries.append(country)

        happiness_meter = HappinessMeter()
        happiness = happiness_meter.measure_happiness(country)

        print("\nHappiness Measurement:")
        print(name, "total happiness:", happiness)
        average = happiness / 5
        print(name, "average happiness:", average)
        print("\n")


if __name__ == "__main__":
    main()
