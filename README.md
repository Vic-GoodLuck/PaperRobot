
一个非常简单的小工具，可以利用每天的闲暇时间刷一刷感兴趣的最新论文（毕竟更新迭代太快了，以免自己想了很长时间才发现已经有人做过了，这是个悲伤的故事(T⌓T)）

依赖Github Workflows、ArXiv API、彩云小译、飞书机器人，实现每日推送ArXiv论文至飞书群聊，支持指定Paper领域、关键词

Github上有很多同类的小工具，因为个人比较习惯用飞书，就简单搭了一下飞书版，有其他需求也可以上手改，只有一百多行代码，改起来很方便~

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
