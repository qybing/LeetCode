import math
import random

import pymysql
import time

db = pymysql.connect(host='xxxx', user='xxxx', passwd='xxxx', db='xxxxx',
                                  charset='utf8')
cursor = db.cursor()
def change_time(result):
    t = int(time.time())
    num = math.ceil(len(result) * 0.2)
    rs_nums = random.sample(result, num)
    for rs_num in rs_nums:
        if abs(t - rs_num[1]) > 1800:
            rs_time = t - random.randint(500, 1800)
            save_to_mysql(rs_num[0], rs_time)

def save_to_mysql(id,activity):
    sql = "update location set activity={} where id ={}".format(activity,id)
    try:
        cursor.execute(sql)
        db.commit()
        print('id为{}修改成功'.format(id))
    except Exception as e:
        print(e)
        print('修改失败')

def get_activity():
    sql = "select id,activity from location"
    cursor.execute(sql)
    rs = cursor.fetchall()
    result = []
    for row in rs:
        result.append((row[0],row[1]))
    return change_time(result)

if __name__ == '__main__':
    get_activity()