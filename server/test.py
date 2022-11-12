from logic.locations_methods import get_locations, add_location, delete_location
from logic.classes import Location


if __name__ == "__main__":
    for i in get_locations():
        print(i)

    # l = Location(
    #     id=3,
    #     country="Singapore",
    #     city="Singapore",
    #     location_name="GBTB",
    #     location_address="1234"
    # )
    # add_location(l)
    # print(get_locations())

    # delete_location(2)
