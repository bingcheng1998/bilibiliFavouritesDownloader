# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # favorate list 默认 p1
    # GET https://api.bilibili.com/x/v3/fav/resource/list

    try:
        response = requests.get(
            url="https://api.bilibili.com/x/v3/fav/resource/list",
            params={
                "media_id": "1030308760",
                "pn": "1",
                "ps": "20",
                "keyword": "",
                "order": "mtime",
                "type": "0",
                "tid": "0",
                "jsonp": "jsonp",
            },
            headers={
                "pragma": "no-cache",
                "accept": "application/json, text/plain, */*",
                "sec-fetch-site": "same-site",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
                "cache-control": "no-cache",
                "sec-fetch-mode": "cors",
                "origin": "https://space.bilibili.com",
                "referer": "https://space.bilibili.com/57626460/favlist?fid=57789760&ftype=create",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
                "dnt": "1",
                "cookie": "_uuid=ED0DC1CA-2C3E-2AB3-0AA1-B8441D7E26C848309infoc; buvid3=EAFB10D0-1ED2-4DD3-A441-288FCA409C1D155809infoc; CURRENT_FNVAL=16; rpdid=|(u|JmummR~|0J'ulmkJ||l)l; DedeUserID=57626460; DedeUserID__ckMd5=076a9e6fd71ec253; PVID=1; sid=6eswdz6c; SESSDATA=d02c2e43,1614337110,deb29*81; bili_jct=6529028b8066b8fbafe2652cb4b57bb6; LIVE_BUVID=AUTO8715987851121453; blackside_state=1; bfe_id=1e33d9ad1cb29251013800c68af42315; bp_video_offset_57626460=430430004520694656; bp_t_offset_57626460=430431018138226185",
                "sec-fetch-dest": "empty",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


