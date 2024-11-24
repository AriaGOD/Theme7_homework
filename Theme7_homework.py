import time
from concurrent.futures import *

def formula1(x):
    return x ** 2 - x ** 2 + x ** 4 - x ** 5 + x + x

def formula2(x):
    return x + x

def formula3(result1, result2):
    return result1 + result2

def execute_iterations(formula1, formula2, iterations, executor_type):
    results = []

    with executor_type(max_workers=2) as executor:
        start_time = time.time()
        results1 = list(executor.map(formula1, range(iterations)))
        duration1 = time.time() - start_time

        start_time = time.time()
        results2 = list(executor.map(formula2, range(iterations)))
        duration2 = time.time() - start_time

        start_time = time.time()
        results3 = [formula3(r1, r2) for r1, r2 in zip(results1, results2)]
        duration3 = time.time() - start_time

        results.append((duration1, duration2, duration3))

    return results

def main():
    iterations = [10_000, 100_000]

    print("Задание 1")
    for iters in iterations:
        durations = execute_iterations(formula1, formula2, iters, ThreadPoolExecutor)
        print(f"Итерации: {iters}")
        print(f"Вычисления 1: {durations[0][0]:.5f} сек")
        print(f"Вычисления 2: {durations[0][1]:.5f} сек")
        print(f"Вычисления 3: {durations[0][2]:.5f} сек\n")

    print("Задание 2")
    for iters in iterations:
        durations = execute_iterations(formula1, formula2, iters, ProcessPoolExecutor)
        print(f"Итерации: {iters}")
        print(f"Вычисления 1: {durations[0][0]:.5f} сек")
        print(f"Вычисления 2: {durations[0][1]:.5f} сек")
        print(f"Вычисления 3: {durations[0][2]:.5f} сек\n")


if __name__ == "__main__":
    main()
