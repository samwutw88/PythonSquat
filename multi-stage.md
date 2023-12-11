Sign Your Container Images with Cosign, GitHub Actions and GitHub Container Registry
https://dev.to/n3wt0n/sign-your-container-images-with-cosign-github-actions-and-github-container-registry-3mni

Install Cosign
https://docs.sigstore.dev/system_config/installation/#alpine-linux

 --> HomeBrew installation on Ubuntu 20.04 Linux
   https://linux.how2shout.com/how-to-install-brew-ubuntu-20-04-lts-linux/
     -->https://brew.sh/
     -->https://github.com/theupdateframework/go-tuf
     
     
參考:
 透過 Multiple Stage Builds 編譯出最小的 Docker Image
  https://jiepeng.me/2018/06/09/use-docker-multiple-stage-builds
 建立一個比較小的 golang Docker Image
  https://github.com/kevingo/Go-Small-Docker-Image
  
 Multi-Stage Docker Build: Streamlining Your Python App Deployment 
  https://medium.com/@pranaymate/multi-stage-docker-build-streamlining-your-python-app-deployment-a8185601666f
優化 Python Docker Image Size - 從 multi-stage builds 到 distroless  
 https://myapollo.com.tw/blog/python-multi-stage-builds-and-distroless/
 ![Docker multi-stage builds](https://hackmd.io/_uploads/B1icXIEIp.png)

 Distroless 容器鏡像的內部結構：深入了解
  https://iximiuz.com/en/posts/containers-distroless-images/
  
 我的image (在github 上) 
  ghcr.io/samwutw88/pythonsquat:main
 
  
 產生key
![cosign-gen-key](https://hackmd.io/_uploads/Byd8OWEUp.png)

![image](https://hackmd.io/_uploads/BkJetWVIp.png)

How to Create a Personal Access Token in GitHub
   -->https://www.youtube.com/watch?v=SzrETQdGzBM
   Token->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(重要)
   
為GitHub 生成 Cosign 密鑰對   
  export GITHUB_TOKEN=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
  export CONSIGN_PASSWORD=123
  cosign configure github --key cosign.pub
    
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   
  cosign verify -key cosign.pub ghcr.io/samwutw88/pythonsquat:main