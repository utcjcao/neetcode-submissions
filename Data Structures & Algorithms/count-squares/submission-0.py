class CountSquares:

    def __init__(self):
        self.d = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.d[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        nx, ny = point
        for x, y in self.pts:
            if abs(nx-x) != abs(ny-y) or x == nx or y == ny:
                continue
            res += self.d[(x,ny)] * self.d[(nx, y)]
        return res
