import random
from math import pi
import math

EARTH_REDIUS = 6378.137         #地球半径

def rad(d):
    return d * pi / 180.0

def getDistance(lat1, lng1, lat2, lng2):        #计算两个点的距离
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(
        math.sin(b / 2), 2)))
    s = s * EARTH_REDIUS                    #两个点之间的距离
    if s<5:
        c = (lat1, lng1, lat2, lng2)        #随机产生一个距离小于5km的纬度,经度
        result = (lat2, lng2)
        print('已知坐标：{}'.format((lat1, lng1)))
        print('另一个点的坐标：{}'.format(result))
    else:
        get_random()

def get_random():
    lat1 = 34.6426                  #已知纬度
    lng1 = 112.5872                 #已知经度
    lat1_ = math.floor(lat1)            #向下取整
    lng1_ = math.floor(lng1)
    lat2 = lat1_ + round(random.random(), 4)            #随机产生一个4位数
    lng2 = lng1_ + round(random.random(), 4)
    getDistance(lat1, lng1, lat2, lng2)


if __name__ == '__main__':
    get_random()