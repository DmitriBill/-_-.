from tkinter import *
from math import sqrt
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


x_list = []  # Полученные корни
values_list = [] # Вводимые значения


# Решение квадратного уравнения

def solution(a,b,c):
    values_list.append(a)
    values_list.append(b)
    values_list.append(c)

    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "Дискриминант равен: %s \nX1 is: %s \nX2 is: %s \n" % (D, x1, x2)     
        x_list.append(x1)
        x_list.append(x2)
    
    # Второй вариант с одной переменной (Но график не строится)

    #elif D == 0:
        #x = -b / (2*a)
        #text = "Дискриминант равен: 0.0""\nx = %.2f" % x
        
    else:
        text = "Дискриминант равен: %s \nДанное уравнение не имеет корней" % D 

    return text


# Вставляет вводимый аргумент

def set(introduced):
    output.delete("0.0","end")
    output.insert("0.0",introduced)    


# Очищает поле ввода

def clear(event):
    caller = event.widget
    caller.delete("0", "end")


# Сообщение о результате ввода

def enter():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        set(solution(a_val, b_val, c_val))
    except ValueError:
        set("Вы точно ввели 3 значения?")


# Окно

root = Tk()
root.title("Калькулятор квадратных уравнений")
root.minsize(400,300)
root.resizable(width=False, height=False)


frame = Frame(root)
frame.grid()

a = Entry(frame, width=4)
a.grid(row=1,column=1,padx=(10,0))
a.bind("<FocusIn>", clear)
a_lab = Label(frame, text="x**2+").grid(row=1,column=2)

b = Entry(frame, width=4)
b.bind("<FocusIn>", clear)
b.grid(row=1,column=3)
b_lab = Label(frame, text="x+").grid(row=1, column=4)

c = Entry(frame, width=4)
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)
c_lab = Label(frame, text="= 0").grid(row=1, column=6)

but = Button(frame, text="Решение", command=enter).grid(row=1, column=8, padx=(7,0))

output = Text(frame, bg="orange", font="Arial 13", width=50, height=18)
output.grid(row=2, columnspan=10)

root.mainloop()



# График

k1, k2, k3 = values_list[0], values_list[1], values_list[2]
 
y0 = 0, 0
 

points = x_list[0], x_list[1]
  
frequency = 100  # частота непрерывной функции

xi = np.linspace(x_list[0], x_list[1], frequency)
y = [k1 * t * t + k2 * t + k3 for t in xi]       # квадратичная функция

plt.scatter(points, y0, color='red')
plt.plot(xi, y)

plt.title("График квадратичной функции", fontsize=18, fontweight="bold") # заголовок
plt.xlabel("Значения Х1, Х2 - точки пересечения оси Х", fontsize=15, fontweight="bold") # метка оси
plt.ylabel("Ось Y", fontsize=15, fontweight="bold") # метка оси



plt.tick_params(axis='both', labelsize=15) # шрифт делений на осях
plt.grid(True)


# axis - суммирование по оси
ax = plt.gca()

# plot X - axis    
ax.axhline(y=0, color='r')

# plot Y - axis    
ax.axvline(x=0, color='r')

plt.savefig('sqrt.png')
plt.show()

print(x_list)
print(values_list) 