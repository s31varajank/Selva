# Run this cell and provide a list of planets

new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet or done if done : ')

for dis_planet in planets:
    print(dis_planet)
    