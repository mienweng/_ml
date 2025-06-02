import random

citys = [
    (0,3),(0,0),
    (0,2),(0,1),
    (1,0),(1,3),
    (2,0),(2,3),
    (3,0),(3,3),
    (3,1),(3,2)
]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5

def path_length(path):
    dist = 0
    for i in range(len(path)):
        dist += distance(citys[path[i]], citys[path[(i+1) % len(path)]])
    return dist

def neighbor(path):
    new_path = path.copy()
    a, b = sorted(random.sample(range(len(path)), 2))
    new_path[a:b+1] = reversed(new_path[a:b+1])
    return new_path

def hill_climbing(x, path_length, neighbor, max_fail=10000):
    fail = 0
    best_path = x
    best_cost = path_length(x)
    print("Initial cost:", best_cost, x)

    while fail < max_fail:
        nx = neighbor(x)
        new_cost = path_length(nx)

        if new_cost < best_cost:
            x = nx
            best_cost = new_cost
            best_path = x
            fail = 0
            print("New best:", best_cost, x)
        else:
            fail += 1

    print("Final solution:", best_cost, best_path)
    return best_path

best_path = hill_climbing(list(range(len(citys))), path_length, neighbor)