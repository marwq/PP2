# Getting value of the key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.get("model")) # dict.get()

# Changing value of the key
car["year"] = 2020

# Adding a new pair to the dict
car["color"] = "red"

# Removing key from the dict
car.pop("model")

# Clearing a whole dict
car.clear()

