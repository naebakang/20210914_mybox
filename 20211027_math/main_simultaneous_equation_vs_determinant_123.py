# File encoding: utf8

import numpy
import matplotlib.pyplot as plt

data_x = [0.5, 0.55, 0.64, 0.66, 0.85]
data_y = [60*60*24*10, 60*60*24*3, 60*60*3, 60*60*14, 60*60*24*6]
# data_x = [0.65, 0.7, 0.8, 0.9, 1.01]
# data_y = [60*60*3, 60*60*2, 60*60*1, 60*45, 60*30]

# simultaneous equation ############################################################################################
# 5*c1 + c2*sum(error2) = sum(error1)
square = []
multiplication = []
for i in range(len(data_x)):
    square.append(data_y[i]**2)
    multiplication.append(data_y[i]*data_x[i])

# c1*sum(error2) + c2*sum(error2)**2 = sum(multiplication)
# ((sum(x)-c2*sum(y))/5)*sum(y) + c2*sum(error2)**2 = sum(multiplication)
# sum(x)/5*sum(y) - c2*sum(y)/5*sum(y) + c2*sum(error2)**2 = sum(multiplication)
# c2*sum(error2)**2 - c2*sum(y)/5*sum(y) = sum(multiplication) - sum(x)/5*sum(y)
# c2(sum(error2)**2 - sum(y)/5*sum(y)) = sum(multiplication) - sum(x)/5*sum(y)
# c2 = (sum(multiplication) - sum(x)/5*sum(y)) / (sum(error2)**2 - sum(y)/5*sum(y))
c2 = (sum(multiplication) - sum(data_x)/len(data_x)*sum(data_y))/(sum(data_y)**2 - sum(data_y)/len(data_x)*sum(data_y))
c1 = (sum(data_x) - c2*sum(data_y)) / len(data_x)


# determinant #######################################################################################################
x = numpy.array(
    [
        [data_y[0], 1],
        [data_y[1], 1],
        [data_y[2], 1],
        [data_y[3], 1],
        [data_y[4], 1],
    ]
)

y = numpy.array(
    [
        [data_x[0]],
        [data_x[1]],
        [data_x[2]],
        [data_x[3]],
        [data_x[4]],
    ]
)

# 1. numpy.linalg.inv
square_matrix = numpy.dot(x.T, x)
square_matrix_inv = numpy.linalg.inv(square_matrix)
pseudo_x = numpy.dot(square_matrix_inv, x.T)
ab = numpy.dot(pseudo_x, y)

compare_1 = c2 - ab[0][0]
compare_2 = c1 - ab[1][0]

print('\n1. numpy.linalg.inv')
print(compare_1)
print(compare_2)

# 2. numpy.linalg.lstsq
# numpy - least square method
a, resid, rank, s = numpy.linalg.lstsq(x, y, rcond=None)

compare_1 = c2 - a[0][0]
compare_2 = c1 - a[1][0]

print('\n2. numpy.linalg.lstsq')
print(compare_1)
print(compare_2)

# 3. numpy.polyfit
y_data = numpy.array(data_x)
x_data = numpy.array(data_y)
# polyfit(x_데이터, y_데이터, 다항식의 차수)
# 차수 1는 y = ax + b 형태를 의미하며, 해는 [a, b] 순서로 반환됩니다.
coefficients = numpy.polyfit(x_data, y_data, 1)

compare_1 = c2 - coefficients[0]
compare_2 = c1 - coefficients[1]

print('\n3. numpy.polyfit')
print(compare_1)
print(compare_2)

# 계수 할당
a, b = coefficients

print("--- 최소제곱법으로 구한 2차 방정식의 계수 ---")
print(f"a (x 계수):   {a:.4f}")
print(f"b (상수항):   {b:.4f}")
print("\n=> 최적의 2차 방정식: y = {:.4f}x + {:.4f}".format(a, b))

# --- 3. 결과 시각화 (선택 사항) ---

# 적합된 곡선을 그리기 위한 부드러운 x 값 생성
x_fit = numpy.linspace(min(x_data), max(x_data), 100)

# poly1d를 사용하여 계수로부터 다항식 함수 생성
p = numpy.poly1d(coefficients)
y_fit = p(x_fit)  # 적합된 2차 함수 값 계산

plt.figure(figsize=(8, 5))
# 원본 데이터 점
plt.scatter(x_data, y_data, color='red', label='Original Data Points (4 points)')
# 최소제곱법으로 구한 최적의 2차 곡선
plt.plot(x_fit, y_fit, color='blue', label='Best-Fit Parabola (y = ax^2 + bx + c)')

plt.title('Least Squares Quadratic Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
