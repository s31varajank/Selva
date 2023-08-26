planet = {
    'name': 'Mars',
    'moons': 2
}

print(planet['name'], "has", planet['moons'], "moons")
print(f'{planet["name"]} has {planet["moons"]} moon(s)')

planet['circumfrence (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(f'{planet["name"]} has a polar circumfrence of {planet["circumfrence (km)"]["polar"]}')