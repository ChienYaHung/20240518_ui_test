# python ui介面練習  
使用模組:PySide6  

## 功能
1. 寫入表格
2. 輸出至CSV(pandas)
3. 圖表繪製(matplotlib)

## 說明  
### firstMainWinRun.py:   
邏輯檔案，設定程式功能，讀取介面檔案(**.py**)並實例化
### main_read_UI_direct.py:   
邏輯檔案，設定程式功能，讀取介面檔案(**.ui**)並實例化  
直接讀取UI檔會無法使用鍵盤快捷鍵(尚未清楚原因)，暫不使用
### gui-1.ui:  
直接使用QT designer做出的介面檔  
### mainUI.py:  
將gui-1.ui轉換成py檔
