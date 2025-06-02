def hillClimbing3D(f, x, y, z, dx=0.01):
    while True:
        current = f(x, y, z)
        print('x={:.4f} y={:.4f} z={:.4f} f={:.4f}'.format(x, y, z, current))

        neighbors = [
            (x + dx, y, z),
            (x - dx, y, z),
            (x, y + dx, z),
            (x, y - dx, z),
            (x, y, z + dx),
            (x, y, z - dx)
        ]

        best = (x, y, z)
        best_val = current
        for nx, ny, nz in neighbors:
            val = f(nx, ny, nz)
            if val < best_val:
                best = (nx, ny, nz)
                best_val = val

        if best_val >= current:
            break
        else:
            x, y, z = best

    return x, y, z

def f(x, y, z):
    return x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8
hillClimbing3D(f, x=0, y=0, z=0)
