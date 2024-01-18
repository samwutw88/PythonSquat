# minio設定
## 安裝後設定
## 新增access key
(後續會需要)
![111](https://hackmd.io/_uploads/ry9V-EYu6.png)
  
## 設定region  
![333](https://hackmd.io/_uploads/Bk5LbEtdp.png)


 --------------------    
 
# 設定AWS相關資訊 
## 設定config及credentials
在cmd下指令 aws configure，產生檔案
    ![image](https://hackmd.io/_uploads/HJ-aJzt_6.png)

## 將access key的內容，複製到asw的credentials檔內
 ![222](https://hackmd.io/_uploads/rJ-8Z4Y_T.png)
 
## 設定bucket及region
![image](https://hackmd.io/_uploads/SJsmO7K_a.png)
  
  
# 測試 
## A
### 執行程式
 - run as > maven install  
   (產生quarkus-run.jar檔, 放置Target 目錄)
 - 開新cmd，至Target 目錄，輸入 java -jar quarkus-run.jar
 - 

## 開Browser
 - http://localhost:8080  (顯示上傳畫面)

## B
 - 指令1: cd C:\20240103_quarkus-upload-file\learning-quarkus\upload-image

 - 指令2: quarkus dev
 - 指令3: w
![image](https://hackmd.io/_uploads/SJVo9QFup.png)  
 
 
## 上傳測試畫面   
![image](https://hackmd.io/_uploads/B1iX_ZFOp.png)

## MINIO確認
![image](https://hackmd.io/_uploads/BJvZOWtO6.png)  







  
    
     
       
       
----------參考資訊-------------
Eclipse got Quarkused !
https://quarkus.io/blog/eclipse-got-quarkused/

BUILDING A NATIVE EXECUTABLE
https://quarkus.io/guides/building-native-image

Upload File to Object Storage (MinIO)
   https://ithelp.ithome.com.tw/m/articles/10306493
   
Day-30-Quarkus 介紹
  https://ithelp.ithome.com.tw/articles/10336848



INSTALL GRVEELM
INSTALL AWS CLI
  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html  
  
INSTALL minio

INSTALL
 MinIO JavaScript Library for Amazon S3 Compatible Cloud Storage
https://github.com/minio/minio-js


------------------------
Day-30-Quarkus 介紹
https://ithelp.ithome.com.tw/articles/10336848


因為我們使用 Typescript 進行開發，要另外安裝 Type 定義檔：
npm i -D @types/minio


INSTALL npm
https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
   https://github.com/coreybutler/nvm-windows?tab=readme-ov-file
   
   https://nodejs.org/en/download/
  
  
  
 



