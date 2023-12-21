
# **Sign and Verify Container Images with Cosign, and Kyverno: A Complete Guide**
![0_cosign-kyverno-流程圖](https://hackmd.io/_uploads/HJvonzWPT.png)



     
    
# Cosign 
Cosign 是一个用于签署和验证软件工件的命令行工具。它由 Sigstore 项目开发,旨在使代码签名变得简单易用。
Cosign 可以用于多种类型的工件,包括容器映像、二进制文件和源代码。

Sigstore 是一个开源项目,旨在使软件供应链更安全。它通过提供一个可信赖的签名仓库和一组用于签署和验证
软件的工具来实现这一点。

为了确认软件的来源和构建方式,实现完整性保护,Linux 基金会联合 Red Hat、Google 和 Purdue 在
2021年3月推出了 Sigstore 代码签名项目,该项目致力于让开发人员签署发布时无感和让用户轻松验证。

Cosign 是 Sigstore 项目中的一项重要工具,它用于生成和验证软件工件的签名。

以下是 Cosign 在 Sigstore 项目中的作用的一些示例:
• 用于签署容器映像,以确保它们来自受信任的来源。
• 用于签署二进制文件,以确保它们没有被篡改。
• 用于签署源代码,以确保它是正确的版本。

Cosign
https://www.youtube.com/watch?v=HLb1Q086u6M

https://www.ithome.com.tw/news/152397
GitHub新開啟的RFC,建議使用Sigstore來加入對NPM套件進行端到端簽署,如此將會產生套件的生成地
點、時間和方式,以便之後對其進行驗證。
社群對這個RFC有諸多疑慮,第一,Sigstore尚未完成,目前仍處於實驗性,第二,RFC也將會導致供應商
化,Sigstore提案只能用於來自公共儲存庫,以及商業託管CI/CD供應商的公共NPM套件,因此套件將會相依
於GitHub、Google或微軟等第三方,且因為Sigstore證書預設包含電子郵件,也會損害作者的隱私。
再來,Sigstore使用自己的證書頒發機構Fulcio,而Fulcio目前僅完整支援GitHub Actions,使得GitHub
Actions成為驗證套件的唯一方式,也就是說無意間開發者會被綁定在特定生態系中,這項限制也使得不少套件
開發者卻步。


用於工件和容器的簽名和驗證，儲存在開放容器計劃 (OCI) 註冊表中，使簽名和 in-toto/SLSA 證明成為不可見的基礎設施。

Rekor  
Rekor 是一種僅附加、可稽核的透明日誌服務，將簽署的元資料記錄到可查詢但無法竄改的分類帳中。

Fulcio  
代碼簽署憑證授權機構，向經過驗證的身分頒發短期憑證並將其發佈到憑證透明度日誌。

# Kyverno
https://www.youtube.com/watch?v=5ihkMblumD0
https://www.youtube.com/watch?v=DREjzfTzNpA
rule: node port
pod
![kyverno_Structure](https://hackmd.io/_uploads/rktejHdL6.png)

-----------------------------------------------
Sign Your Container Images with Cosign, GitHub Actions and GitHub Container Registry
https://dev.to/n3wt0n/sign-your-container-images-with-cosign-github-actions-and-github-container-registry-3mni

Install Cosign
https://docs.sigstore.dev/system_config/installation/#alpine-linux

 --> HomeBrew installation on Ubuntu 20.04 Linux
   https://linux.how2shout.com/how-to-install-brew-ubuntu-20-04-lts-linux/
     -->https://brew.sh/
     -->https://github.com/theupdateframework/go-tuf
     

# COSIGN  
#  產生key
 cosign generate-key-pair  
 ![1-cosign-generate-key](https://hackmd.io/_uploads/ryNIOVgDT.png)

![cosign-gen-key](https://hackmd.io/_uploads/Byd8OWEUp.png)

![image](https://hackmd.io/_uploads/BkJetWVIp.png)


#  產生image 成功 (20231211)
  docker build -t sam168170/squat:v1.1.2 . -f dockerfile1
  
#  上傳image 成功 (20231211)
  docker image push sam168170/squat:v1.1.2
  
#  sign 成功 (20231211)
 cosign sign --key cosign.key docker.io/sam168170/squat:v1.1.2  
 
![2-cosign-sign-image](https://hackmd.io/_uploads/SJnIFVxPT.png)

  
  ![kyverno-sign-image](https://hackmd.io/_uploads/B1p73Qs8T.png)

  *This command will create a new tag SHAxxxxx.sig in our OCI registry. You can verify that the name of the tag contains the digest of the image uploaded with the tag signed*

#  sign 成功-docker hub 上的影響 (20231212)
![image](https://hackmd.io/_uploads/HyMZX4BUp.png)

![squat-v112](https://hackmd.io/_uploads/H1KowVB8T.png)

![squat-v112-sig](https://hackmd.io/_uploads/SJ23vNrIa.png)

#  驗證 Docker 映像檔的簽章(OK) (20231212)
![3-cosign-verify-image](https://hackmd.io/_uploads/rJQBiVeDT.png)

---------------------------------------------


# Kyverno
#  安裝 Kyverno using Helm (20231212)
![install_kyverno](https://hackmd.io/_uploads/B1HTpSSLT.png)

![install_kyverno_1](https://hackmd.io/_uploads/HkvcSIrI6.png)

# 設定 Kyverno Policy 
# NodePort 使用限制
![kyverno-node-port-policy](https://hackmd.io/_uploads/Bka0O7-P6.png)

# NodePort 範圍使用限制
![kyverno-node-port-policy-0](https://hackmd.io/_uploads/ry_iZ4WDT.png)


![kyverno-node-port-policy-1](https://hackmd.io/_uploads/rJC-ZNZPa.png)

![kyverno-node-port-policy-2](https://hackmd.io/_uploads/B1shbE-wT.png)


# resource limit
![kyverno-resource-limit-policy_yaml](https://hackmd.io/_uploads/HyCqwGuUa.png)

# cosign 
![kyverno-policy_yaml](https://hackmd.io/_uploads/By-SwOBIa.png)

![kyverno-policy_yaml_apply](https://hackmd.io/_uploads/BJu8_uBLp.png)

cosign 的public key OK沒錯, 但是, 使用kyverno測試, 出現錯誤.

cosign verify --key cosign.pub sam168170/squat:v1.1.2
![image](https://hackmd.io/_uploads/Syz6icYLp.png)

kyverno測試:  
kubectl run demo-test1 --image docker.io/sam168170/squat:v1.1.2 -n demo
![kyverno-with-cosign-error](https://hackmd.io/_uploads/H1HntYaUp.png)

增加設定(無作用)(https://kyverno.io/docs/introduction/)  
a cosign attest docker.io/sam168170/squat:v1.1.2 --key cosign.key --predicate predicate.json  --type https://example.com/CodeReview/v1
![kyverno-with-cosign-set-attest-predicate](https://hackmd.io/_uploads/HkG6kc6I6.png)


https://eng.d2iq.com/blog/digital-signature-with-cosign/


Verify Images:  
https://release-1-9-0.kyverno.io/docs/writing-policies/verify-images/


重要-錯誤相關:  
https://github.com/kyverno/kyverno/issues/7581
https://flxw.de/tuf-kyverno-and-custom-sigstore.html

A Guide to Running Sigstore Locally:  
https://blog.sigstore.dev/a-guide-to-running-sigstore-locally-f312dfac0682/

--------------------------------
https://flxw.de/tuf-kyverno-and-custom-sigstore.html

How cosign works inside of Kyverno
Kyverno runs inside of Kubernetes pods, and it uses the cosign Go libraries. Those are the same code routines as the command-line client. That means that cosign has to have a directory inside the kyverno container to create the local TUF repository and keep it up to date.

聯合簽名如何在 Kyverno 內部運作
Kyverno在 Kubernetes Pod 內部運行，並使用cosign Go 庫。這些是與命令列客戶端相同的程式碼例程。這意味著容器cosign內必須有一個目錄kyverno來建立本機 TUF 儲存庫並使其保持最新。

----------------20231214-------------------------------
# OIDC
# 瞭解 OpenID Connect 認證機制
(每當點選社群帳號登入，背後發生了什麼事？)
*OIDC 和 OAuth 2.0 兩者在目的上有很大的區別。OIDC 目的是認證（Authentication），OAuth 2.0 目的則是授權（Authorization）。然而兩者在機制上卻大致雷同，後面會講到，OIDC 正是建構在 OAuth 2.0 framework 的基礎上面。*
https://petertc.medium.com/openid-connect-a27e0a3cc2ae





 我的image (在github 上) 
  ghcr.io/samwutw88/pythonsquat:main
 

How to Create a Personal Access Token in GitHub
   -->https://www.youtube.com/watch?v=SzrETQdGzBM
   Token->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(重要)
   
為GitHub 生成 Cosign 密鑰對   
  export GITHUB_TOKEN=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
  export CONSIGN_PASSWORD=123
  cosign configure github --key cosign.pub
    
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   
  cosign verify -key cosign.pub ghcr.io/samwutw88/pythonsquat:main