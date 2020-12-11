infile = "test_input.txt"

with open(infile, "r") as f:
    model = [list(line.strip()) for line in f.readlines()]


def is_floor(model, x, y):
    return True if model[x][y] == "." else False


class Seat:
    def __init__(self, model, x, y):
        self.x = x
        self.y = y
        self.state = model[x][y]
        self.neighbors = self._set_neighbors()
        self.empty_n = self.neighbors.count("L")
        self.occupied_n = self.neighbors.count("#")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"<Seat:{self.state}:{self.x},{self.y}>"

    def next_state(self):
        if self.state == "L" and self.occupied_n == 0:
            self.state = "#"
        if self.state == "#" and self.occupied_n >= 4:
            self.state = "L"

    def _set_neighbors(self):
        neighbors = []
        for x in range(self.x - 1, self.x + 2):
            for y in range(self.y - 1, self.y + 2):
                # print(f"processing coord: {x},{y}")
                if x == self.x and y == self.y:
                    # print("thats me, skipping")
                    continue
                if not x >= 0 or not y >= 0:
                    # print("one coord under 0, skipping")
                    continue
                try:
                    if not is_floor(model, x, y):
                        # print(f"not a floor, adding: {model[x][y]}")
                        neighbors.append(model[x][y])
                except IndexError:
                    continue
        print(neighbors)
        return neighbors


seats = []
for x, row in enumerate(model):
    for y, elem in enumerate(model):
        if not is_floor(model, x, y):
            seat = Seat(model, x, y)
            seats.append(seat)
            print(seat)

print(seats)
