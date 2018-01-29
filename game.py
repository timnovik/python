from tkinter import Tk, Canvas, mainloop, NW
from PIL import Image, ImageTk

# размер карты в пикселях
window_width = 600
window_height = 600

# карта
game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# размеры блока
block_width = window_width // 12
block_height = window_height // 12

# создаем холст
tk = Tk()
c = Canvas(tk, width=window_width, height=window_height, bg='white')
c.pack()

# картинки со стеной и травой
brick = ImageTk.PhotoImage((Image.open("images/grass.jpg").resize((block_width, block_height))))
grass = ImageTk.PhotoImage((Image.open("images/grass.jpg").resize((block_width, block_height))))

# рисуем карту
for i in range(12):
    for j in range(12):
        if game_map[i][j] == 0:
            c.create_image(i * block_width, j * block_height, image=grass, anchor=NW)
        if game_map[i][j] == 1:
            c.create_image(i * block_width, j * block_height, image=brick, anchor=NW)


# картинка с игроком
player_image_w = ImageTk.PhotoImage((Image.open("images/tank_a.gif").convert('RGBA').resize((block_width, block_height))))
player_image_d = ImageTk.PhotoImage((Image.open("images/tank_a.gif").convert('RGBA').resize((block_width, block_height)).rotate(270)))
player_image_s = ImageTk.PhotoImage((Image.open("images/tank_a.gif").convert('RGBA').resize((block_width, block_height)).rotate(180)))
player_image_a = ImageTk.PhotoImage((Image.open("images/tank_a.gif").convert('RGBA').resize((block_width, block_height)).rotate(90)))

# координаты игрока
x = 6
y = 6

# создаем игрока
player_w = c.create_image(x * block_width, y * block_height, image=player_image_w, anchor=NW)
player_d = c.create_image(x * block_width, y * block_height, image=player_image_d, anchor=NW)
player_s = c.create_image(x * block_width, y * block_height, image=player_image_s, anchor=NW)
player_a = c.create_image(x * block_width, y * block_height, image=player_image_a, anchor=NW)

# проверка доступности клетки
def is_available(i, j):
    if i < 0 or i >= 12 or j < 0 or j >= 12:
        return False
    if game_map[i][j] == 1:
        return False
    return True

# нажатие клавиши
def keyDown(key):
    global x, y, player_w, player_a, player_s, player_d, derskaya_pulya
    c.itemconfig(player_w, state='hidden')
    c.itemconfig(player_d, state='hidden')
    c.itemconfig(player_s, state='hidden')
    c.itemconfig(player_a, state='hidden')
    if key.char == 'a':
        c.itemconfig(player_a, state='normal')
        if is_available(x - 1, y):
            x -= 1
    if key.char == 'd':
        c.itemconfig(player_d, state='normal')
        if is_available(x + 1, y):
            x += 1
    if key.char == 'w':
        c.itemconfig(player_w, state='normal')
        if is_available(x, y - 1):
            y -= 1
    if key.char == 's':
        c.itemconfig(player_s, state='normal')
        if is_available(x, y + 1):
            y += 1
    c.coords(player_a, x * block_width, y * block_height)
    c.coords(player_d, x * block_width, y * block_height)
    c.coords(player_s, x * block_width, y * block_height)
    c.coords(player_w, x * block_width, y * block_height)

# при нажатии любой клавишы вызываем keyDown
tk.bind("<KeyPress>", keyDown)

mainloop()
