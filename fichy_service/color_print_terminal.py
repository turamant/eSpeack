import colorsys

H = 0.2
S = 0.4
V = 0.6

RGB = colorsys.hsv_to_rgb(H, S, V)

print(RGB) 