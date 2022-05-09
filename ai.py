import pandas as pd
import matplotlib.pyplot as pPlot
import math
import numpy as np


def fx(x, a, b):
    return (a * x) + b
    
# least squares
def ls(x, y):
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
        
    return [fx(len(x), numerator, b), pX, pY, numerator]

# bias
def bias(w, x, y):
    return y - w * x

# regression    
#def regression():
    
    
# 데이터셋 불러오기
df = pd.read_excel('C:\\Users\\\dltmd\\\Desktop\\\SchoolTeamProject-main\\코로나바이러스감염증-19_확진환자_발생현황_220503.xlsx')

x = []
y = []
count = 1

# 데이터 가공
for i in df['Unnamed: 2'][5:]:
    if i == '-':
        continue
    x.append(count)
    y.append(i)
    count += 1

# 데이터 가공후 결과물 확인

data = ls(x,y)
weight = data[3]
bias = bias(weight, data[1], data[1])

yy = weight * np.asarray(x) + bias

print("weight : "+str(weight))
print("bias : "+str(bias))
print("yy : "+str(yy))
print("Next predicted number of infected people : "+ str(data[0]))



# 데이터 시각화
pPlot.plot(x, yy, color='b', label='independent variable')
pPlot.scatter(x, y, color='r', label='dependent variable')
pPlot.legend(fontsize=20)
pPlot.show()
