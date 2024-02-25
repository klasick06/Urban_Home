import simple_draw as sd

sd.resolution = (1200, 600)
y = 500
x = 100

y2 = 450
x2 = 150

x3 = 300
y3 = 200

while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=50)
    y -= 10
    if y < 50:
        break
    x = x + 10

    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point2, length=50)
    y2 -= 10
    if y2 < 50:
        break
    x2 = x2 + 20

    point3 = sd.get_point(x3, y3)
    sd.snowflake(center=point3, length=50)
    y3 -= 10
    if y3 < 50:
        break
    x3 = x3 + 30

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()