# -*- coding: utf-8 -*-
import time


def compare_time(time1, time2):
    """
    :param time1:要比较的时间1，是"YYYYMMDD"8位数字格式
    :param time2:要比较的时间2，是"YYYYMMDD"8位数字格式
    :return:前后时间相同 = 0；前面的时间比后面的时间晚 > 0的结果；前面的时间比后面的时间早 < 0的结果
    """
    s_time = time.mktime(time.strptime(time1, '%Y%m%d'))
    e_time = time.mktime(time.strptime(time2, '%Y%m%d'))
    return int(s_time) - int(e_time)


def get_all_payday(first, stage):  # 输入第一个还款日与期数，输出一个由所有还款日期组成的数组
    all_payday = [first]
    first_time = time.strptime(first, '%Y%m%d')
    for i in range(1, stage):
        next_time_tm_mon = first_time.tm_mon + 1
        next_time_tm_year = first_time.tm_year
        if next_time_tm_mon == 13:
            next_time_tm_mon = 1
            next_time_tm_year = next_time_tm_year + 1
        next_time = str(next_time_tm_year) + str(next_time_tm_mon).zfill(2) + str(first_time.tm_mday)
        first_time = time.strptime(next_time, '%Y%m%d')
        all_payday.append(next_time)
    return all_payday


def getpastday(time1, time2):
    """
    :param time1:
    :param time2:
    :return: 返回两个以"YYYYMMDD"为格式的日期之间的天数差，返回值的类型为数值
    """
    time1 = time.strptime(time1,"%Y%m%d")
    time2 = time.strptime(time2,"%Y%m%d")
    time3 = abs(time.mktime(time2) - time.mktime(time1))
    day = time3/(60*60*24)
    return day
