cache-from 的原理
Docker 在 v1.13 的版本中新增了 cache-from 的機制，而該機制就是先載入利用指定的 Docker Image 後，再透過比對本次 build 的 Dockerfile 內文找出相同的 Docker Layer，相同的 Docker Layer 在此次 build 時不會再重複執行，而是使用 cache，這樣的方式可以加速整體編譯的速度，把寶貴的時間省下來了！  

# 快取資訊儲存在本地端   
--無cache
![image](https://hackmd.io/_uploads/HyN1735vp.png)

下載image
docker pull sam168170/my-image-cache-from:v1.1.6 
![image](https://hackmd.io/_uploads/Hy6qEh9PT.png)   

![image](https://hackmd.io/_uploads/SyTpV35Dp.png)


執行:docker build --platform linux/amd64 . -t sam168170/my-image-cache-from:v2.2.2 -f Dockerfile --cache-from sam168170/my-image-cache-from:v1.1.6
![image](https://hackmd.io/_uploads/H1WvHhqva.png)   


清除cache,image
![image](https://hackmd.io/_uploads/By-0B2qPp.png)   

執行:docker build --platform linux/amd64 . -t sam168170/my-image-cache-from:v2.2.2 -f Dockerfile --cache-from sam168170/my-image-cache-from:v1.1.6  (沒有先pull image檔)
![image](https://hackmd.io/_uploads/HkB3I35D6.png)   


# 快取資訊儲存在遠端位置   
docker buildx build --platform linux/amd64 . -t  my-image-cache-from:v10.8.1 --push --cache-to type=registry,ref=sam168170/my-image-cache-from:v10.0.2 -mode=max --cache-from type=registry,ref=sam168170/my-image-cache-from:v10.0.2

part 1: 未設定cache 
第1次   
![image](https://hackmd.io/_uploads/SkifbS-u6.png)

  



part 2: 設定cache  
第1次  
![image](https://hackmd.io/_uploads/rJNBvXW_6.png)  

第2次  
![image](https://hackmd.io/_uploads/BkxHiwmZu6.png)


![image](https://hackmd.io/_uploads/SJaZ369vT.png)

docker hub
![image](https://hackmd.io/_uploads/HyBFoacPa.png)
 
 
local:
![image](https://hackmd.io/_uploads/SJvMjaqw6.png)

---  COPY --link    ---------------  
dockerfile  

第一次  
![image](https://hackmd.io/_uploads/ry85Kw-uT.png)
  
改dockerfile  
![image](https://hackmd.io/_uploads/Sy2zqDZ_p.png)  


第二次  
![image](https://hackmd.io/_uploads/BJt3KwWdp.png)








 

   
 
------------------


copy + --link:
 


 




--其他--

part 3: 完整  
 docker buildx build --platform linux/amd64 . -t sam168170/my-image-cache-from:v10.0.3 --push  --cache-to type=registry,ref=sam168170/my-image-cache-from:v1.1.6  --cache-from type=registry,ref=sam168170/my-image-cache-from:v1.1.6   -mode=max
 
 
未清cache, 仍有case作用在:
![image](https://hackmd.io/_uploads/Skcxeaqwp.png)
 ------------------

改動映像層:
![image](https://hackmd.io/_uploads/HyzDfp9Pa.png)   

時間變長:
![image](https://hackmd.io/_uploads/HyCVzT5Pa.png)

這是因為改動映像層 ( 我們把原先的 AUTHOR 這個變數換成您的英文名字 ) 進而造成 SHA 算出來的 ID 有異，使得映像檔找不到匹配的映像層而是重新建置新的映像層。   
   







