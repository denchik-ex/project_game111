# Начальная расстановка:
# (позиция X, тип препятствия)
BASE_OBSTACLES = [
    (900, "spike"),
    (1400, "double_spike"),
    (1900, "block"),
    (2400, "spike"),
    (2900, "double_spike"),
    (3400, "block"),
    (3900, "spike"),
    (4400, "double_spike"),
    (4900, "block"),
    (5400, "spike"),
]

SECTION_OFFSET = 5000

LEVEL_OBSTACLES = BASE_OBSTACLES + [
    (x + SECTION_OFFSET, kind)
    for x, kind in BASE_OBSTACLES
]

# Дополнительные препятствия перед финишем
LEVEL_OBSTACLES += [
    (10900, "block"),
    (11400, "double_spike"),
    (11900, "spike"),
]