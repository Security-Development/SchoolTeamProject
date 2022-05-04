import pandas as pd
import matplotlib.pyplot as pPlot

# 데이터셋 불러오기
df = pd.read_excel('C:\\Users\\hansei\\Desktop\\코로나바이러스감염증-19_확진환자_발생현황_220503.xlsx')

data = []

# 데이터 가공
for i in df['Unnamed: 2'][5:]:
    if i == '-':
        continue
    
    data.append(i)

# 데이터 가공후 결과물 확인
print(data)


# 데이터 시각화
pPlot.plot(data)
pPlot.show()

