def fuel_reports(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name} : {value}')

fuel_reports(main=50, external=100, emergency=60)