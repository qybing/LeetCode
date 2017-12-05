import random
from math import pi
import math

import pymysql

db = pymysql.connect(host='xxxx', user='xxxx', passwd='xxxx', db='xxxx',
                         charset='utf8')
cursor = db.cursor()
EARTH_REDIUS = 6378.137

def rad(d):
    return d * pi /180.0

def getDistance(lat1, lng1, lat2, lng2,id):        #计算两个点的距离
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(
        math.sin(b / 2), 2)))
    s = s * EARTH_REDIUS                    #两个点之间的距离
    if s<5:
        print('两个点的距离为{}'.format(s))
        update_to_mysql(lat2, lng2,id)
        # print('两个点的距离为{}'.format(s))

def update_to_mysql(lat2, lng2,id):
    sql = "update location set lng ={},lat={} where id={} ".format(lng2,lat2,id)
    try:
        cursor.execute(sql)
        db.commit()
        print('插入成功')
    except Exception as e:
        print(e)
        print('插入失败')

def get_x_and_y():
    r = 446                         #圆半径
    x = random.randint(0,r)
    rs = int(math.sqrt((r*r-x*x)))
    y = (random.randint(0,rs))/10000
    # print(x/10000,y)
    return x/10000,y

def get_center_coordinate():
    sql = "select central_lng,central_lat,id from location where central_lng!=0"
    cursor.execute(sql)
    rs = cursor.fetchall()
    for row in rs:
        print(row[0],row[1],row[2])
        get_random(row[0],row[1],row[2])


def get_random(lng,lat,id):
    lat1 = float(round(lat,4))
    lng1 = float(round(lng,4))
    lat2,lng2 = get_x_and_y()       #随机获取坐标增量
    operators = ['+','-']
    operator = random.choice(operators)
    lat2 = round(eval(str(lat1) + operator + str(lat2)),4)
    lng2 = round(eval(str(lng1) + operator + str(lng2)),4)
    print('已知坐标{}'.format((lat1,lng1)))
    print('目标坐标{}'.format((lat2,lng2)))
    getDistance(lat1,lng1,lat2,lng2,id)

if __name__ == '__main__':
    get_center_coordinate()