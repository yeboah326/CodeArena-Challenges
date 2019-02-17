#Diwali Lights
nl = list(map(lambda x: int(x),input().split(" ")))
n, r, g, b = nl[0], [], [], []
colors = [r,g,b]
for col in colors:
    for i in range(n):
        col.append(0)
#print(colors)

r_time, g_time, b_time = nl[1], nl[2], nl[3]

#Assigning 1's for on and zero for off
for o in range(1,12,2):
    for e in range(2,12,2):
        colors[0][(r_time * o) : (r_time * e) - 1] = [1,1]
        colors[1][(g_time * o) : (g_time * e) - 1] = [1,1,1]
        colors[2][(b_time * o) : (g_time * e) - 1] = [1,1,1,1,1]
        break
colors[0], colors[1], colors[2] = colors[0][:n], colors[1][:n], colors[2][:n]
#print(colors)

#Colors
red,green,blue,yellow,cyan,magenta,white,black = 0,0,0,0,0,0,0,0
#Checking for color combination
for i in range(n):
        if [colors[0][i],colors[1][i],colors[2][i]] == [1,0,0]:
                red = red + 1
                
        if [colors[0][i],colors[1][i],colors[2][i]] == [0,1,0]:
                green = green + 1
                
        if [colors[0][i],colors[1][i],colors[2][i]] == [0,0,1]:
                blue = blue + 1
                
        if [colors[0][i],colors[1][i],colors[2][i]] == [1,1,0]:
                yellow = yellow + 1
                
        if [colors[0][i],colors[1][i],colors[2][i]] == [0,1,1]:
                cyan = cyan + 1
                
        if [colors[0][i],colors[1][i],colors[2][i]] == [1,0,1]:
                magenta = magenta + 1
                
        if [colors[0][i],colors[1][i],colors[2][i]] == [1,1,1]:
                white = white + 1
                
        if [colors[0][i],colors[1][i],colors[2][i]] == [0,0,0]:
                black = black + 1

print(red,green,blue,yellow,cyan,magenta,white,black)