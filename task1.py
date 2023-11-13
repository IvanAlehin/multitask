"""
Используя пакет multiprocessing, распараллельте на процессы процедуру
вычисления суммы элементов матрицы (параллелить вычисление суммы по столбцам или
строкам, итоговую сумму вычислять в общем потоке). Написанное приложение должно
быть консольным. Аргументы командной строки – размеры матрицы и ее значения. """

import multiprocessing
import numpy as np

def sum_row(row):
    return sum(row)

def main(matrix):
    pool = multiprocessing.Pool()

    results_row = pool.map(sum_row, matrix)
    pool.close()
    pool.join()
    print("sum rows:", results_row)

    total_sum = sum(results_row)
    print("total sum:", total_sum)

if __name__ == "__main__":

    n, m = map(int,input().split())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    print("matrix:\n", np.array(matrix))
    main(matrix)
