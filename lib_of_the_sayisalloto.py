
#########################################################################
####                                                                 ####
####                    Loto Sonuçları Kütüphanesi                   ####
####                      Lottory Results Library                    ####
####                                                                 ####
####                 © The library has Created by HEG                ####
####                                                                 ####
####               feel free to use or change this doc               ####
####                                                                 ####
#########################################################################

"""
In this file, I have created a something like library.
Some functions could be impractical.
"""

import json
import numpy as np

def import_table(i = 1266, doc_name = 'tablearray.json'):
    """
    first return: list
    second return: length of the list
    """
    table_ = []
    with open(doc_name, 'r') as f:
        table__loaded = json.load(f)
    len_of_table_ = len(table__loaded)

    while i > -1:
        table_.append(table__loaded[i])
        i = i - 1
    return table_, len_of_table_

def week_get():

    (table_,len_of_table_) = import_table()
    week = []
    for i in range(len_of_table_):
        week.append(table_[i][0])
    week = np.array([week])
    week = np.ndarray.astype(week,dtype=float)

    return week

def date_get(table_,len_of_table_):

    date = []
    for i in range(len_of_table_):
        date.append(table_[i][1])

    return date

def ball_1_get(table_,len_of_table_):
    t1 = []
    for i in range(len_of_table_):
        t1.append(table_[i][2])
    return t1

def ball_2_get(table_,len_of_table_):
    t2 = []
    for i in range(len_of_table_):
        t2.append(table_[i][3])
    return t2

def ball_3_get(table_,len_of_table_):
    t3 = []
    for i in range(len_of_table_):
        t3.append(table_[i][4])
    return t3

def ball_4_get(table_,len_of_table_):
    t4 = []
    for i in range(len_of_table_):
        t4.append(table_[i][5])
    return t4

def ball_5_get(table_,len_of_table_):
    t5 = []
    for i in range(len_of_table_):
        t5.append(table_[i][6])
    return t5

def ball_6_get(table_,len_of_table_):
    t6 = []
    for i in range(len_of_table_):
        t6.append(table_[i][7])
    return t6

def turn_it_to_array():
    """
    it's convering list to array table like;

        __week :
        __date :
        __ball_1  :
        __ball_2  :
        __ball_3  :
        __ball_4  :
        __ball_5  :
        __ball_6  :

    """
    (list,leng) = import_table()
    (d, m, y) = seperate_date()
    week = week_get(list,leng)
    ball_1 = ball_1_get(list, leng)
    ball_2 = ball_2_get(list, leng)
    ball_3 = ball_3_get(list, leng)
    ball_4 = ball_4_get(list, leng)
    ball_5 = ball_5_get(list, leng)
    ball_6 = ball_6_get(list, leng)

    table_array = np.array((week,d,m,y,ball_1,ball_2,ball_3,ball_4,ball_5,ball_6))

    print(table_array)
    return table_array

def seperate_date():

    (list,leng) = import_table()
    date = date_get(list,leng)
    len2 = len(date)
    day = []
    month = []
    year = []

    for date_count in range(len2):
        date2 = date[date_count]
        day.append(int(date2[0:2]))
        month.append(int(date2[3:5]))
        year.append(int(date2[8:10]))

    day = np.array([day])
    month = np.array([month])
    year = np.array([year])

    return day,month,year

def seperated_array_for_train():
    (list, leng) = import_table()
    (d, m, y) = seperate_date()
    week = week_get(list, leng)
    ball_1 = ball_1_get(list, leng)
    ball_2 = ball_2_get(list, leng)
    ball_3 = ball_3_get(list, leng)
    ball_4 = ball_4_get(list, leng)
    ball_5 = ball_5_get(list, leng)
    ball_6 = ball_6_get(list, leng)

    x_array = np.array((week, d, m, y))
    y_array = np.array((ball_1, ball_2, ball_3, ball_4, ball_5, ball_6))

    return x_array, y_array

