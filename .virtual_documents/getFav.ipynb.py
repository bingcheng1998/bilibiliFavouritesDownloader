# get_ipython().run_line_magic("load_ext", " autoreload")
# get_ipython().run_line_magic("autoreload", " 2")


from user_info import user_info


import HeaderHelper as hh
# import xPathHelper as xh


import json


def getFavList(media_id):
    pn = 1
    bv_list = []
    page_list = []
    title_list = []
    while True:
        url, params, headers = hh.gen_fav_info(hh.FAVORATE_INFO, user_info['cookie'])
        params['media_id'] = media_id
        params['pn'] = pn
        pn += 1
        response = hh.send_request(url, headers, params)
        bili_json = json.loads(response.text)
        if bili_json['data']['medias'] is None:
            break
        for video in bili_json['data']['medias']:
            bv_list.append(video['bvid'])
            page_list.append(video['page'])
            title_list.append(video['title'])
    return bv_list, page_list, title_list


def showFavInfo(title_list):
    num = len(title_list)
    unfinished = sum([item == '已失效视频' for item in title_list])
    print(f'总共{num}个BV，已失效{unfinished}个')


if __name__ == '__main__':
    media_id = 57789760
    bv_list, page_list, title_list = getFavList(media_id)
    showFavInfo(title_list)


def getFavInfo(media_id):
    url, params, headers = hh.gen_fav_info(hh.FAVORATE_INFO, user_info['cookie'])
    params['media_id'] = media_id
    params['pn'] = 1
    response = hh.send_request(url, headers, params)
    bili_json = json.loads(response.text)
    fav_title = bili_json['data']['info']['title']
    fav_up = bili_json['data']['info']['upper']['name']
    fav_num = bili_json['data']['info']['media_count']
#     print(bili_json['data']['info'])
    return fav_title, fav_up, fav_num


if __name__ == '__main__':
    media_id = 57789760
    fav_title, fav_up, fav_num = getFavInfo(media_id)
    print(fav_title, fav_up, fav_num)



