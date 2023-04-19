import math
import time

class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.next = None
    
class CityDatabase:
    def __init__(self):
        self.head = None
    
    def insert(self, name, x, y):
        new_city = City(name, x, y)
        new_city.next = self.head
        self.head = new_city
    
    def delete_by_name(self, name):
        if self.head is None:
            return
        if self.head.name == name:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next is not None:
            if curr.next.name == name:
                curr.next = curr.next.next
                return
            curr = curr.next
    
    def delete_by_coordinate(self, x, y):
        if self.head is None:
            return
        if self.head.x == x and self.head.y == y:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next is not None:
            if curr.next.x == x and curr.next.y == y:
                curr.next = curr.next.next
                return
            curr = curr.next
    
    def search_by_name(self, name):
        curr = self.head
        while curr is not None:
            if curr.name == name:
                return curr
            curr = curr.next
        return None
    
    def search_by_coordinate(self, x, y):
        curr = self.head
        while curr is not None:
            if curr.x == x and curr.y == y:
                return curr
            curr = curr.next
        return None
    
    def points_within_distance(self, x, y, distance):
        results = []
        curr = self.head
        while curr is not None:
            if math.sqrt((curr.x - x) ** 2 + (curr.y - y) ** 2) <= distance:
                results.append(curr)
            curr = curr.next
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

