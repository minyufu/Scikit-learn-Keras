# -*- coding: utf-8 -*-
import time
import numpy as np
import matplotlib.pyplot as plt

def line(A):#直線方程式
    return (-A*w[0]+threshold)/w[1]

#初始化 w1,w2,threshold,learning_rate,xr,Y,E
w = []
for i in range(2): 
    w.append(float(input('請輸入w{}的值:'.format(i+1))))
threshold=float(input("請輸入 threshould 的值:"))
learning_rate=float(input('請輸入learning_rate 學習效率 參數:'))
learning_or_and=int(input('請輸入學習的邏輯: 1.AND 2.OR: '))

#選擇要學習 and | or
if learning_or_and == 1:
    andYd=[0,0,0,1]
    Yd = andYd
    and_or='AND'
    # print('執行 {} 運算 Yd陣列:{}'.format(and_or,andYd))
else:
    orYd=[0,1,1,1]
    Yd = orYd
    and_or='OR'
    # print('執行 {} 運算 Yd陣列:{}'.format(and_or,orYd))

#誤差值,初始設定為0
E=0
#邏輯
xr = [[0,0],[0,1],[1,0],[1,1]]

#輸出值 Ya ans n 設定初始值
Ya=[1,1,1,1]
ans=[0.0,0.0]
n=0
start = time.time()
while True:
    for i in range(4):
        for j in range(2):
            ans[j] = (xr[i][j] * w[j])
            # print(ans[j])
            
        if ans[0]+ans[1] >= threshold:
            Y=1
            Ya[i]=Y
            # print(Y)
        else:
            Y=0
            Ya[i] = Y
            # print(Y)
        # 計算誤差值 Yd - Ya   
        E = Yd[i] - Ya[i]
        # print(E)
        
        for k in range(2):
            if E >= 1:
                num = w[k] + learning_rate
                w[k] = num
                # print(w[j] + learning_rate)
            elif E <= -1:
                num = w[k] - learning_rate
                w[k] = num
                # print(w[j]-learning_rate)
            else:
                pass
            
    n += 1
    if Ya == Yd:
        print('Ya:{} == Yd:{} w1={} w2={}'.format(Ya,Yd,w[0],w[1]))
        print('第{}次 {} 已經完成學習'.format(n,and_or))
        break
    else:
        print('Ya:{} != Yd:{} w1={} w2={}'.format(Ya,Yd,w[0],w[1]))
        print('第{}次 {} 沒有完成再繼續一次學習'.format(n,and_or))
end = time.time()
print('執行時間 : %f 秒'%(end - start))
#畫 AND | OR 圖
x = np.arange(0, 3, 0.01)
y = line(x)
plt.plot(x,y) 

# 這段邏輯錯誤
# xpt=[w[0],0]
# ypt=[0,w[1]]
# plt.xlim(0, 1)
# plt.ylim(1, 0)
# plt.plot(xpt,ypt) 
    
plt.plot(0,0,'ro')
plt.text(0, 0, r'P1(0,0)')
plt.plot(0,1,'ro')
plt.text(0, 1, r'P2(0,1)')
plt.plot(1,1,'ro')
plt.text(1, 1, r'P3(1,1)')
plt.plot(1,0,'ro')
plt.text(1, 0, r'P4(1,0)')
# plt.savefig('learing_{}.png'.format(and_or))
plt.show()
