from random import choice

def print_field() -> None:
    def to_matrix(f: list, a: int) -> list:
        res = []
        for i in range(0, a**2, a):
            res.append(f[i:i+a])
        
        return res

    a, n = int(input()), int(input())
    res = to_matrix(*gen(5, n))
    [print(*x) for x in res]

def gen(a: int, num_of_mines: int) -> (list, int):
    def set_n(f: list, m: set, a: int) -> (list, int):

        for i in m:
            if not(i % 5): # left
                ns = (
                    i + 1,
                    i + a, i + a + 1,
                    i - a, i - a + 1
                )
            elif not((i+1) % 5): # right
                ns = (
                    i - 1,
                    i + a, i + a - 1,
                    i - a, i - a - 1
                )
            else: # center
                ns = (
                    i + 1, i - 1,
                    i + a, i + a + 1, i + a - 1,
                    i - a, i - a + 1, i - a - 1
                )

            for n in ns:
                if n >= 0 and n < a**2 and f[n] != 'X': f[n] += 1        

        return f, a

    def set_m(a: int, n: int) -> (list, set, int):
        avi_m = set(range(a**2))
        field = [0] * a**2
        for _ in range(n):
            m = choice(list(avi_m))
            field[m] = 'X'
            avi_m.remove(m)
        mines = set(range(a**2)) - avi_m
        
        return field, mines, a

    return set_n(*set_m(a, num_of_mines))
