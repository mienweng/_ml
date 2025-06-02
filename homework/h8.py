import torch

x = torch.tensor(0.0, requires_grad=True)
y = torch.tensor(0.0, requires_grad=True)
z = torch.tensor(0.0, requires_grad=True)

optimizer = torch.optim.SGD([x, y, z], lr=0.1)

for step in range(100):
    optimizer.zero_grad()

    f = x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8

    f.backward()
    optimizer.step()

    if step % 10 == 0:
        print(f"Step {step}: f = {f.item():.4f}, x = {x.item():.4f}, y = {y.item():.4f}, z = {z.item():.4f}")

print("\n最小點在：")
print(f"x = {x.item():.4f}, y = {y.item():.4f}, z = {z.item():.4f}")
print(f"最小值 f(x, y, z) = {f.item():.4f}")
