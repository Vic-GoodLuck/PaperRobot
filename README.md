


### Quick Start
    - 彩云小译获取API Key
    - 飞书群聊添加机器人，获取Webhook Url
    - Fork本项目，将CAIYUN_TOKEN、FEISHU_URL添加至 Settings -> Secrets and Variables -> Actions -> Repository secrets
    - 获取个人Github Token，添加至 Settings -> Secrets and Variables -> Actions -> Repository secrets（注意Key命名为GHB_TOKEN）
    - 参考.github/workflows中的yml文件，根据个人需求配置：
        - cron（执行时间）
        - Target_Domain（Paper领域，对齐ArXiv分类，可省略）
        - Target_Keyword（Paper关键词）
        - Paper_Num（单次抓取Paper数量）

### References

https://zhuanlan.zhihu.com/p/425670267
https://github.com/Vincentqyw/cv-arxiv-daily/tree/main
https://github.com/Doragd/Algorithm-Practice-in-Industry/tree/main