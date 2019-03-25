# -*- coding: utf-8 -*-
import time_sy
import float_sy


def calcu(prin, today, first, rate, stage):  # prin 本金 today 借款日期（必须要是8位格式为YYYYMMDD的数字） first 第一个还款日 rate 日利率 stage 期数
    """
    :param prin: 本金
    :param today: 借款日期
    :param first: 第一个还款日
    :param rate: 日利率
    :param stage: 期数
    :return: 包含{还款日期:金额}的数组
    """
    result = []
    total = prin
    payday = time_sy.get_all_payday(first, stage)
    for i in payday:
        pastday = time_sy.getpastday(i, today)
        interest = float_sy.get_two_float(pastday * rate * total)
        a = float_sy.get_two_float(float(prin)/stage)
        money = float_sy.get_two_float(interest + a)
        total = total - a
        dic = {'日期': i,
               '本金': a,
               '利息': interest,
               '总待还': '%.2f' % money}
        result.append(dic)
        today = i
    return result


def discounts(rate, debt):
    """
    给含有字典列表的debt打上折扣（除了首期）！
    :param rate: 折扣率
    :param debt:
    :return:还是返回这个debt给你
    """
    count = 1
    for i in debt:
        if count != 1:
            print "现在的利息是%.2f,应当减免的利息是%.2f" % (i['利息'], i['利息'] * rate)
            i['利息'] = float('%.2f' % (i['利息'] * (1 - rate)))
            print "减免后的利息是%.2f" % i['利息']
            i['总待还'] = '%.2f' % (i['本金'] + i['利息'])
        count = count + 1
    return debt
