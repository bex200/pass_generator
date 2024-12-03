import numpy as np
import pandas
import matplotlib
def numpy_example():
    print ("\n==NumPy: Быстрая работа с числами ===")
    print("\nПредставьте, что   у вас есть температуры(в С) 20, 22, 19 , 21,23 24, 20")
    temperatures = np.array([20,22, 19, 21, 23, 24, 20])
    print("Температуры на неделе:", temperatures)
    print("\n Мы можем найти среднюю температуру за неделю.")
    average_temp = np.mean(temperatures)
    print(f"Средняя температура:{average_temp:.2f} C")
    print("\n Что если через 10 лет температура увеличится на 5 C каждый день?")
    future_temperature = temperatures + 5
    print("Температуры через 10 лет:", future_temperature)
numpy_example()