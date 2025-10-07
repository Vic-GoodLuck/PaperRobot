import os
import json
import requests
from datetime import datetime

# 参考 https://platform.caiyunapp.com/api/manage
def translate(source, direction = "en2zh"):
    caiyun_api = os.environ.get("CAIYUN_TOKEN")
    caiyun_url = "http://api.interpreter.caiyunai.com/v1/translator"
    payload = {
            "source": source,
            "trans_type": direction,
            "request_id": "demo",
            "detect": True,
        }
    headers = {
        "content-type": "application/json",
        "x-authorization": "token " + caiyun_api,
    }
    try:
        response = requests.post(caiyun_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        result = json.loads(response.text)["target"]
        return result
    except Exception as e:
        print(e)
        return None


# 参考 https://zhuanlan.zhihu.com/p/425670267
# ti	Title
# au	Author
# abs	Abstract
# co	Comment
# jr	Journal Reference
# cat	Subject Category
# rn	Report Number
# id	Id (use id_list instead)
# all	All of the above
def arxiv_search(domain = None, author = None, keyword = None, frm = 0, pagesize = 10):
    arxiv_url = 'http://export.arxiv.org/api/query?search_query='

    conditions = []
    if domain:
        conditions.append(f'cat:{domain}')
    if author:
        conditions.append(f'au:{author}')
    if keyword:
        conditions.append(f'all:{keyword}')

    url = arxiv_url + '&'.join(conditions) + \
        f'&start={frm}&&max_results={pagesize}' + \
        f'&sortBy=submittedDate&sortOrder=descending'

    papers = requests.get(url).text.split('<entry>')[1:]

    search_results = []
    for paper in papers:
        title = paper.split('<title>')[1].split('</title>')[0].strip()
        abstract = paper.split('<summary>')[1].split('</summary>')[0].strip().replace('\n', ' ').replace('\r', '')
        url = paper.split('<id>')[1].split('</id>')[0].strip()
        pub_date = paper.split('<published>')[1].split('</published>')[0]
        pub_date = datetime.strptime(pub_date, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")

        search_results.append({
            'title': title,
            'abstract': abstract,
            'url': url,
            'pub_date': pub_date,
            'translated_abstract': translate(abstract),
        })

    return search_results

# 参考 https://github.com/Doragd/Algorithm-Practice-in-Industry/tree/main
def send_feishu_message(message_title, message_content):
    feishu_url = os.environ.get("FEISHU_URL")
    card_data = {
        "config": {
            "wide_screen_mode": True
        },
        "header": {
            "template": "green",
            "title": {
            "tag": "plain_text",
            "content": message_title
            }
        },
        "elements": [
            {
                "tag": "markdown",
                "content": message_content
            }
        ]
    }
    card = json.dumps(card_data)
    body =json.dumps({"msg_type": "interactive","card":card})
    headers = {"Content-Type":"application/json"}
    requests.post(url=feishu_url, data=body, headers=headers)
