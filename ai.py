import pandas as pd
import matplotlib.pyplot as pPlot
import math
import numpy as np

gX = []
gY = []

def fx(x, a, b):
    return (a * x) + b

# 시그모이드
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# LSTM 수식
#def formula(x, y, z):
    #forget gate
    #return sigmoid(np.dot(xt, x) + np.dot(y, ht) + z)

# LSTM
#def lstm(x):
    #ft = formula(wf, uf, bf)
    #it = formula(wi, ui, bi)
    #ot = formula(wo, uo, bo)
    #ct =  ft * ct_1 + it * sigmoid(np.dot(wc,xt) + np.dot(uc, ht_1 + bc)
    #ht = ot * (np.sinh(ct) / np.cosh(ct))
    #print(1)
        
# 최소제곱법
def ls(x, y):
    global gY, gX
    pX = pY = numerator = denominator = 0
    if len(x) == len(y):
        
        for i in range(len(x)):
            pX += x[i]
            pY += y[i]

        pX /= len(x)
        pY /= len(y)

        for i in range(len(x)):
            numerator += (y[i] - pY) * (x[i] - pX)
            denominator += (x[i] - pX) ** 2

        numerator /= denominator
        b = pY - (numerator * pX)

        for i in range(len(x)):
            gX.append(len(x) + i)
            #print(f"{numerator} * {len(x) + i} + {b} = "+str(fx(len(x) + i, numerator, b)))
            gY.append(fx(x[i], numerator, b))

        
    return [fx(len(x), numerator, b), pX, pY, numerator]

# bias
def bias(w, x, y):
    return y - w * x   
      
# 데이터셋 불러오기
df = pd.read_excel('C:\\Users\\\dltmd\\\Desktop\\\SchoolTeamProject-main\\코로나바이러스감염증-19_확진환자_발생현황_220503.xlsx')

x = []
y = []
count = 1

# 데이터 가공
for i in df['Unnamed: 2'][5:]:
    if i == '-':
        x.append(count)
        y.append(0)
        count += 1
        continue
    x.append(count)
    y.append(i)
    count += 1

# 데이터 가공후 결과물 확인

data = ls(x,y)
weight = data[3]
bias = bias(weight, data[1], data[1])

yy = weight * np.asarray(x) + bias # regression coefficient 



print("\n"+"= "*100+"\n")
print("independent variable : "+ str(x))
print("\n"+"= "*100 +"\n")
print("dependent variable : "+str(y))
print("\n"+"= "*100+"\n")
print("weight : "+str(weight))
print("bias : "+str(bias))
print("regression coefficient : "+str(yy))
print("Next predicted number of infected people : "+ str(data[0]))




# 데이터 시각화
f, plot = pPlot.subplots(1, 2)
f.set_size_inches((20, 15))

sx = np.arange(-5.0, 5.0, 0.1)
sy = sigmoid(sx)

plot[0].scatter(sx, sy, color='g', label= 'sigmoid graph')
plot[0].legend(fontsize=20)
    
pPlot.plot(x, y, color='b', label='independent variable')
pPlot.plot(x, gY, color='r', label='regression y')
pPlot.legend(fontsize=20)
pPlot.show()
