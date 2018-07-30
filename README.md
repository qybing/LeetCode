# LeetCode
def extract_cookies(cookie):
    """从浏览器或者request headers中拿到cookie字符串，提取为字典格式的cookies"""
    cookies = dict([l.split("=", 1) for l in cookie.split("; ")])
    return cookies

if __name__ == "__main__":
    cookie = "SINAGLOBAL=8579763841229.657.1524737226558; SSOLoginState=1532686386; _s_tentry=-; Apache=5424097773756.871.1532686388530; ULV=1532686388539:10:2:1:5424097773756.871.1532686388530:1530518563447; wvr=6; YF-Page-G0=35f114bf8cf2597e9ccbae650418772f; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWfYrSxRTZkwQ1-2RkMmYjW5JpX5KMhUgL.Foe0SKefSoMpSoB2dJLoI0YLxK.L1KzLBo2LxK-L12eL1h-LxK-LBKBLBo.LxK-LBo2L1hzLxKnL1KML12qLxKML1-BL1h5LxKBLB.2LB.2t; ALF=1564459165; SCF=Ajw4dwBpqmTxIyrvESOdzxryMS7nPsKwxBCyvBa0OB4Q8VZ9LNYlDuj1t1fhYxQ4XAt1pqsn2gerySDEkv36pTo.; SUB=_2A252Wv1ODeRhGeVN7lEU9inNzTiIHXVVLmmGrDV8PUNbmtBeLRLCkW9NTJ-_OES9Ym9U_ssrFDS3EWPaIYe-AX7P; SUHB=0A0Jw36ZcjmrmU; wb_view_log_3353567164=1280*7201.5; UOR=www.cocoachina.com,widget.weibo.com,login.sina.com.cn; cross_origin_proto=SSL"
    cookies = extract_cookies(cookie)
    print(cookies)
