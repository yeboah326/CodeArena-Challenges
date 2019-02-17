#Diwali Lights
n, r, g, b = 12, [], [], []
colors = [r,g,b]
for col in colors:
    for i in range(n):
        col.append(0)
print(colors)

r_time, g_time, b_time = 2, 3, 5

for o in range(1,12,2):
    for e in range(2,12,2):
        colors[0][(r_time * o) : (r_time * e) - 1] = [1,1]
        colors[1][(g_time * o) : (g_time * e) - 1] = [1,1,1]
        colors[2][(b_time * o) : (g_time * e) - 1] = [1,1,1,1,1]
        break
print(colors)
