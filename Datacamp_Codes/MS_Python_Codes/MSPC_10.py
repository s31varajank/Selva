planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
user_planet = input('Enter planet name : ')

planet_index = planets.index(user_planet)
print(planets.index(user_planet))

print('Planet closer than : ' + user_planet)
print(planets[0:planet_index])

print('Planet Farther than : ' + user_planet)
print(planets[planet_index + 1:])