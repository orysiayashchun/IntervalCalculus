import functions

# пункт 1
# 1)
interval_1=[]
interval_2=[]
res_interval=[]
x=float(input("Введіть початок першого інтервалу a= "))
interval_1.append(x)
x=float(input("Введіть кінець першого інтервалу b= "))
interval_1.append(x)
x=float(input("Введіть початок другого інтервалу с= "))
interval_2.append(x)
x=float(input("Введіть кінець другого інтервалу d= "))
interval_2.append(x)
print("Введені інтервали [{}; {}] тa [{}; {}]".format(*interval_1,*interval_2))
res_interval=functions.sum_intervals(interval_1,interval_2)
print("Додавання інтевалів: ", res_interval)
res_interval=functions.diff_intervals(interval_1,interval_2)
print("Віднімання інтевалів: ", res_interval)
res_interval=functions.mult_intervals(interval_1,interval_2)
print("Множення інтевалів: ", res_interval)
if(res_interval[0]*res_interval[1]>0):
    res_interval=functions.div_intervals(interval_1,interval_2)
    print("Ділення інтевалів: ", res_interval)
else:
    print("Ділення неможливе {} містить 0".format(res_interval))
# 2)
my_interval=[17,17.07]
print("Заданий інтервал: ",my_interval)
functions.middle(my_interval)
functions.width(my_interval)
functions.radius(my_interval)
functions.absolute_value(my_interval)

# пункт 2

A=[[[1.0,4.0],[-1.0,2.0]],
   [[-1.0,3.0],[1.0,4.0]]]
B=[[[-1.0,1.0]],
   [[0.0,2.0]]]
print("Матриця A=")
functions.print_matrix(A)
print("Матриця B=")
functions.print_matrix(B)
det=functions.determinant(A)
print("Визначник матриці A= ", det)
functions.check_determinant(det)

# візьмемо А=[11,12]

A_2=[[[11.0,12.0],[-1.0,2.0]],
   [[-1.0,3.0],[1.0,4.0]]]
print("Матриця A=")
functions.print_matrix(A_2)
det_2=functions.determinant(A_2)
print("Визначник матриці A_2= ", det_2)
functions.check_determinant(det_2)
inverse_A_2=functions.inverse_matrix(A_2)
print("Обернена до матриці A= ")
functions.print_matrix(inverse_A_2)
X=functions.mult_matrixes(inverse_A_2,B)
print("Результат Х= ")
functions.print_matrix(X)
