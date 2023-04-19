import math
import time

class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

class CityDatabase:
    def __init__(self):
        self.cities = []
    
    def insert(self, name, x, y):
        self.cities.append(City(name, x, y))
    
    def delete_by_name(self, name):
        for i in range(len(self.cities)):
            if self.cities[i].name == name:
                del self.cities[i]
                return
    
    def delete_by_coordinate(self, x, y):
        for i in range(len(self.cities)):
            if self.cities[i].x == x and self.cities[i].y == y:
                del self.cities[i]
                return
    
    def search_by_name(self, name):
        for city in self.cities:
            if city.name == name:
                return city
        return None
    
    def search_by_coordinate(self, x, y):
        for city in self.cities:
            if city.x == x and city.y == y:
                return city
        return None
    
    def points_within_distance(self, x, y, distance):
        results = []
        for city in self.cities:
            if math.sqrt((city.x - x) ** 2 + (city.y - y) ** 2) <= distance:
                results.append(city)
        return results

# Example usage
if __name__ == '__main__':
    db = CityDatabase()

    # Insert records
    start = time.time()
    db.insert("Los Angeles", 34, -118)
    db.insert("New York", 40, -74)
    db.insert("Chicago", 41, -87)
    db.insert("Houston", 29, -95)
    db.insert("Phoenix", 33, -112)
    end = time.time()
    print("Inserted records in", end - start, "seconds")

    # Search by name
    start = time.time()
    city = db.search_by_name("Chicago")
    end = time.time()
    if city is not None:
        print("Found", city.name, "at", city.x, ",", city.y, "in", end - start, "seconds")
    else:
        print("City not found")

    # Search by coordinate
    start = time.time()
    city = db.search_by_coordinate(40, -74)
    end = time.time()
    if city is not None:
        print("Found", city.name, "at", city.x, ",", city.y, "in", end - start, "seconds")
    else:
        print("City not found")

    # Points within distance
    start = time.time()
    cities = db.points_within_distance(40, -74, 500)
    end = time.time()
    if len(cities) > 0:
        print("Cities within distance:")
    for city in cities:
        print(f"{city.name} ({city.x}, {city.y})")
    else:
        print("No cities found within distance.")
    print(f"Time taken: {end - start} seconds.")
