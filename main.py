import os
import time
from utils import *

# os.environ['CAIYUN_TOKEN'] = ""
# os.environ['FEISHU_URL'] = ""

# os.environ['Target_Domain'] = ''
# os.environ['Target_Keyword'] = ''
# os.environ['Paper_Num'] = 

domain = os.environ.get("Target_Domain",None)
keyword = os.environ.get("Target_Keyword",None)

translated_papers = arxiv_search(domain = domain, keyword = keyword, frm = 0, pagesize = 10)

for idx,paper in enumerate(translated_papers):
    message_title = f"{domain}-{keyword}-{idx}"
    message_content = f'''
    Title：[{paper["title"]}]({paper["url"]})
    
    Abstract：{paper["translated_abstract"]}

    ArXiv Url：{paper["url"]}

    Pub Date：{paper["pub_date"]}
    '''
    send_feishu_message(message_title, message_content)
    time.sleep(10)