def sum_intervals(interval_1,interval_2):
    res_interval=[]
    res_interval.append(interval_1[0]+interval_2[0])
    res_interval.append(interval_1[1]+interval_2[1])
    return res_interval

def diff_intervals(interval_1,interval_2):
    res_interval=[]
    res_interval.append(interval_1[0]-interval_2[1])
    res_interval.append(interval_1[1]-interval_2[0])
    return res_interval

def mult_intervals(interval_1,interval_2):
    res_interval=[]
    min_mult=interval_1[0]*interval_2[0]
    max_mult=interval_1[0]*interval_2[0]
    for i in range(len(interval_1)):
        for j in range(len(interval_2)):
            if(interval_1[i]*interval_2[j]<min_mult):
                min_mult=interval_1[i]*interval_2[j]
            if(interval_1[i]*interval_2[j]>max_mult):
                max_mult=interval_1[i]*interval_2[j]
    res_interval.append(min_mult)
    res_interval.append(max_mult)
    return res_interval

def div_intervals(interval_1,interval_2):
    converse_interval_2=list(map(lambda x: 1/x,interval_2))
    return mult_intervals(interval_1,converse_interval_2)


def middle(interval):
    print("Середина даного інтервалу {}: {}".format(interval,(interval[0]+interval[1])/2))

def width(interval):
     print("Ширина даного інтервалу {}: {}".format(interval,round(interval[1]-interval[0],3)))

def radius(interval):
    print("Радіус даного інтервалу {}: {}".format(interval,round((interval[1]-interval[0])/2,3)))

def absolute_value(interval):
    if abs(interval[0])>abs(interval[1]):
        print("Абсолютне значення даного інтервалу {}: {}".format(interval,abs(interval[0])))
    else:
        print("Абсолютне значення даного інтервалу {}: {}".format(interval,abs(interval[1])))

def determinant(A):
    res_interval=[]
    res_interval=diff_intervals(mult_intervals(A[0][0],A[1][1]),mult_intervals(A[1][0],A[0][1]))
    return res_interval

def determinant_2(A):
    res_interval=[]
    res_interval=diff_intervals(mult_intervals(A[1][0],A[0][1]),mult_intervals(A[0][0],A[1][1]))
    return res_interval

def check_interval(interval):
    if interval[0]*interval[1]>0:
        return True
    else:
        return False
def check_determinant(det):
    if(det[0]*det[1]>0):
        print("Матриця А невироджена")
    else:
       print("Матриця А вироджена")
def mult_by_const(k,interval):
    if k>=0:
        return [k*interval[0],k*interval[1]]
    else:
        return [k*interval[1],k*interval[0]]

def div_const_by_interval(k,interval):
    if k<=0:
        return [k/interval[0],k/interval[1]]
    else:
        return [k/interval[1],k/interval[0]]

def inverse_matrix(A):
    new_A=[[[0.0,0.0],[0.0,0.0]],[[0.0,0.0],[0.0,0.0]]]
    if check_interval(A[1][1]):
        new_A[0][0][0]=1/((diff_intervals(A[0][0],div_intervals(mult_intervals(A[0][1],A[1][0]),A[1][1])))[0])
        new_A[0][0][1]=1/((diff_intervals(A[0][0],div_intervals(mult_intervals(A[0][1],A[1][0]),A[1][1])))[1])
    else:
        new_A[0][0][0]=(div_intervals(A[1][1],diff_intervals(mult_by_const(A[0][0][1],A[1][1]),
                                                             mult_intervals(A[0][1],A[1][0]))))[0]
        new_A[0][0][1]=(div_intervals(A[1][1],diff_intervals(mult_by_const(A[0][0][0],A[1][1])
                                                             ,mult_intervals(A[0][1],A[1][0]))))[1]
    if check_interval(A[0][0]):
        new_A[1][1][0]=1/((diff_intervals(A[1][1],div_intervals(mult_intervals(A[0][1],A[1][0]),A[0][0])))[0])
        new_A[1][1][1]=1/((diff_intervals(A[1][1],div_intervals(mult_intervals(A[0][1],A[1][0]),A[0][0])))[1])
    else:
        new_A[1][1][0]=(div_intervals(A[0][0],diff_intervals(mult_by_const(A[1][1][1],A[0][0]),
                                             mult_intervals(A[0][1],A[1][0]))))[1]
        new_A[0][0][1]=(div_intervals(A[0][0],diff_intervals(mult_by_const(A[1][1][0],A[0][0]),
                                            mult_intervals(A[0][1],A[1][0]))))[0]
    if check_interval(A[0][1]):
        new_A[0][1][1]=1/((diff_intervals(A[1][0],div_intervals(mult_intervals(A[0][0],A[1][1]),A[0][1])))[0])
        new_A[0][1][0]=1/((diff_intervals(A[1][0],div_intervals(mult_intervals(A[0][0],A[1][1]),A[0][1])))[1])
    else:
        new_A[0][1][0]=(div_const_by_interval(A[0][1][1],diff_intervals(mult_by_const(A[0][1][1],A[1][0]),
                                                   mult_intervals(A[0][0],A[1][1]))))[0]
        new_A[0][1][1]=(div_const_by_interval(A[0][1][0],diff_intervals(mult_by_const(A[0][1][0],A[1][0]),
                                                  mult_intervals(A[0][0],A[1][1]))))[1]

    if check_interval(A[1][0]):
        new_A[1][1][1]=1/((diff_intervals(A[0][1],div_intervals(mult_intervals(A[0][0],A[1][1]),A[1][0])))[0])
        new_A[1][1][0]=1/((diff_intervals(A[0][1],div_intervals(mult_intervals(A[0][0],A[1][1]),A[1][0])))[1])
    else:
        new_A[1][0][0]=(div_const_by_interval(A[1][0][1],diff_intervals(mult_by_const(A[1][0][1],A[0][1]),
                                             mult_intervals(A[0][0],A[1][1]))))[0]
        new_A[1][0][1]=(div_const_by_interval(A[1][0][0],diff_intervals(mult_by_const(A[1][0][0],A[0][1]),
                                             mult_intervals(A[0][0],A[1][1]))))[1]

    return new_A

def mult_matrixes(inverse_A,B):
    X=[[[0.0,0.0]],[[0.0,0.0]]]
    for i in range(len(inverse_A)):
        for j in range(len(B[0])):
            for k in range(len(inverse_A[i])):
                X[i][j]=sum_intervals(X[i][j],mult_intervals(inverse_A[i][k],B[k][j]))
    return X

def print_matrix(A):
    for i in range(len(A)):
        print(A[i])


