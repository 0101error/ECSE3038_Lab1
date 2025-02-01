def parallel(resistances):
    total = sum(1/r for r in resistances)
    results = 1/total
    print(f'"{results:.3f} ohms"')

parallel([330, 1000, 2200])

def potential_divider(voltage_supply, series_resistances):

    total_resistance = sum(series_resistances)
    for r in series_resistances:
        voltage_drop = (r / total_resistance) * voltage_supply
        print(f'"{voltage_drop:.2f}v"')

potential_divider(9, [3000, 1000])