def parallel(resistances):
    total = sum(1/r for r in resistances)
    results = 1/total
    print(f'"{results:.3f} ohms"')

parallel([330, 1000, 2200])