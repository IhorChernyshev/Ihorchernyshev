def difference(*args):
    if not args:
        return 0
    max_val = max(args)
    min_val = min(args)
    return round(max_val - min_val, 2)
assert difference(1, 2, 3) == 2
assert difference(5, -5) == 10
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4
assert difference() == 0

print('OK')