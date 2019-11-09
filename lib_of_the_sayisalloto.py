
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

def test_array_creator_and_saver():

    import numpy as np
    import random as rand

    """---------------------------------------------------------------"""
    """               We are loading our lotodataset.npz              """
    """---------------------------------------------------------------"""

    (d, m, y) = seperate_date()
    w = week_get()
    (tablo, length) = import_table()

    ball1_test = []
    ball2_test = []
    ball3_test = []
    ball4_test = []
    ball5_test = []
    ball6_test = []

    ball1 = ball_1_get(tablo, length)
    ball2 = ball_2_get(tablo, length)
    ball3 = ball_3_get(tablo, length)
    ball4 = ball_4_get(tablo, length)
    ball5 = ball_5_get(tablo, length)
    ball6 = ball_6_get(tablo, length)

    """---------------------------------------------------------------"""
    """              Create Test File Randomly                        """
    """---------------------------------------------------------------"""

    test_file_size = 100
    lenn = len(d[0])

    for i in range(test_file_size):
        lenn = len(d)
        random = rand.randint(0, lenn)
        if i == 0:
            x_test = np.array([[[w[0][random], d[0][random]], [m[0][random], y[0][random]]]], dtype=float)
            w = np.delete(w[0], random)
            d = np.delete(d[0], random)
            m = np.delete(m[0], random)
            y = np.delete(y[0], random)
            ball1_test.append(ball1[random])
            ball2_test.append(ball2[random])
            ball3_test.append(ball3[random])
            ball4_test.append(ball4[random])
            ball5_test.append(ball5[random])
            ball6_test.append(ball6[random])
            del ball1[random], ball2[random], ball3[random], ball4[random], ball5[random], ball6[random]
        else:
            random_pick_ba = np.array([[[w[random], d[random]], [m[random], y[random]]]], dtype=float)
            x_test = np.vstack((x_test, random_pick_ba))
            w = np.delete(w, random)
            d = np.delete(d, random)
            m = np.delete(m, random)
            y = np.delete(y, random)
            ball1_test.append(ball1[random])
            ball2_test.append(ball2[random])
            ball3_test.append(ball3[random])
            ball4_test.append(ball4[random])
            ball5_test.append(ball5[random])
            ball6_test.append(ball6[random])
            del ball1[random], ball2[random], ball3[random], ball4[random], ball5[random], ball6[random]

    for i in range(len(d)):
        if i == 0:
            x_train = np.array([[[w[i], d[i]], [m[i], y[i]]]], dtype=float)
        else:
            new_block = np.array([[[w[i], d[i]], [m[i], y[i]]]], dtype=float)
            x_train = np.vstack((x_train, new_block))

    ball1_train = np.transpose(np.array([ball1], dtype=float))
    ball2_train = np.transpose(np.array([ball2], dtype=float))
    ball3_train = np.transpose(np.array([ball3], dtype=float))
    ball4_train = np.transpose(np.array([ball4], dtype=float))
    ball5_train = np.transpose(np.array([ball5], dtype=float))
    ball6_train = np.transpose(np.array([ball6], dtype=float))

    ball1_test_array = np.transpose(np.array([ball1_test], dtype=float))
    ball2_test_array = np.transpose(np.array([ball2_test], dtype=float))
    ball3_test_array = np.transpose(np.array([ball3_test], dtype=float))
    ball4_test_array = np.transpose(np.array([ball4_test], dtype=float))
    ball5_test_array = np.transpose(np.array([ball5_test], dtype=float))
    ball6_test_array = np.transpose(np.array([ball6_test], dtype=float))

    np.savez(
        'lotodataset3.npz', InputsTrain=x_train, InputsTest=x_test,
        y1_train=ball1_train, y2_train=ball2_train, y3_train=ball3_train,
        y4_train=ball4_train, y5_train=ball5_train, y6_train=ball6_train,
        y1_test=ball1_test_array, y2_test=ball2_test_array, y3_test=ball3_test_array,
        y4_test=ball4_test_array, y5_test=ball5_test_array, y6_test=ball6_test_array
    )
