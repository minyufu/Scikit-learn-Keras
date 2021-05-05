# Scikit-learn-Keras
*機器學習與深度學習*
* * *
## Perceptron.py
### 單一神經感知器
* 步驟說明:
  1. initialigation(初始化參數)
  2. Activeation(反應方程式)
  3. 計算誤差(E = Yd - Ya)
  4. WiP+1 = WiP + α * xi * E
  5. Loop 2-4 till correct

### 使用者自訂義參數
* w1、w2值(刺激訊號輸入)
* threshold(承受刺激的門檻值)
* learning_rate(學習效率)
* learning_or_and(學習or邏輯或是and邏輯)

### 反應方程式
    IF(x1w1 + x2w2) >= θ
    then Y = 1
    else Y = 0

### 結果:將學習次數的結果印出，並使用 matplotlib 繪製圖
* * *
