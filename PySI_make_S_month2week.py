# make_S_month2week
#
# 2022 Yasushi Ohsugi
#
#
import csv
import calendar

from datetime import date


# 日付からISO週

# 2021年1月3日（日）は2020年第53週として扱われます
#
#print(date(2021, 1, 3).isocalendar())
#
#(2020, 53, 7)

# 2021年1月4日（月）は2021年第1週として扱われます
#
#print(date(2021, 1, 4).isocalendar())
#
#(2021, 1, 1)


# 週番号から日付

#date.fromisocalendar(2021, 1, 1)
#
#datetime.date(2021, 1, 4)


# YYYY年1月～12月の需要Sが月別に与えられている時、ISO WEEKのSをセットする。
# S = [YYYY, nnn1, nnn2, nnn3, nn4, nn5, nn6, nn7, nn8, nn9, nn10, nn11, nn12 ]

def make_S_M2W(year,S_m_list,S_w_init):
#def make_S_month2week(prod_name,year,S_m_list,S_w_init):

    S_m = S_m_list
    S_w = S_w_init

    for i in range(54):

        print( 'week =' , i )

        if i == 0:

            print('i==0 skipped',i)

            continue

        if i == 1:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)

            month = r.month
            day   = r.day

# month=12, day=29,30,31の時の計算

            if month == 12:

                if day >= 25 :

                    N = 31-day+1

                    S_w[i] = int( S_m[0] * N / 31 + S_m[1]*(7-N)/31 )

                    continue

            elif month == 1 :

# もし、ISO-week=1, day=1がmonth=1の時
# month=1, day=1,2,3,4の時の計算

                N =7

                S_w[i] = int( S_m[1] * N / 31 )

                continue

            else:

                continue



        if i in ( 2, 3, 4 ):
        #if i == 2 or 3 or 4:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)


            S_w[i] = int(S_m[ r.month ] * 7/31 )

            continue


        if i == 5:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day

# ******************
# うるう年の確認
# ******************
            if calendar.isleap(year) == True:
                feb_e = 29
            else:
                feb_e = 28


# もし、ISO-week=5, day=1がmonth=1の時

            if month == 1:

                if day >= 25 :

                    N = 31-day+1

                    S_w[i] = int( S_m[month]*N/31 + S_m[ month+1 ]*(7-N)/feb_e)

                    continue

            elif month == 2 :

# もし、ISO-week=5, day=1がmonth=2の時

                N =7

                S_w[i] = int( S_m[month+1] * N / feb_e )

                continue

            else:

                pass


        if i in ( 6, 7, 8 ):
        #if i == 6 or 7 or 8:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)

            month = r.month
            day   = r.day

# ******************
# うるう年の確認
# ******************
            if calendar.isleap(year) == True:
                feb_e = 29
            else:
                feb_e = 28

            S_w[i] = int(S_m[ r.month ] * 7/ feb_e )

            continue


        if i == 9:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day

# ******************
# うるう年の確認
# ******************
            if calendar.isleap(year) == True:
                feb_e = 29
            else:
                feb_e = 28


# もし、ISO-week=9, day=1がmonth=2の時
# month=2, day=23,24,25,26,27,28の時の計算 

            if month == 2:

                if day >= 23 :

                    N = feb_e - day + 1  # うるう年

                    S_w[i] = int( S_m[month]*N/feb_e + S_m[month+1]*(7-N)/31 )

                    continue

            elif month == 3 :

# もし、ISO-week=10,11,12 day=1がmonth=3の時

                N = 7

                S_w[i] = int( S_m[month] * N / 31 )

                continue

            else:

                pass


        if i in ( 10, 11, 12 ):
        #if i == 10 or 11 or 12:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)

            month = r.month
            day   = r.day

            N = 7

            S_w[i] = int(S_m[ r.month ] * N / 31 )

            continue


        if i == 13:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day

# もし、ISO-week=13, day=1がmonth=3の時
# month=3, day=23,24の時

            if month == 3:

                if day <  25:

                    N = 7 # 23, 24は月をマタがない

                    S_w[i] = int( S_m[ month ] * N / 31 )

                else:

# month=3, day=25,26,27,28,29,30,31の時の計算
# N = 31-day+1
# S_m3 * N / 31 + S_m4*(7-N)/30
# ここで、ISO-week=13, day=1がmonth=4は発生しない

                    N = 31-day+1

                    S_w[i] = int( S_m[month]*N/31 + S_m[month+1]*(7-N)/30 )


                continue

            continue


        if i == 14:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day

#もし、ISO-week=14, day=1がmonth=3の時
#month=3, day=29,30,31の時の計算
# N = 31-day+1

# S_m3 * N / 31 + S_m4*(7-N)/30

            if month == 3:

                if day >= 25 :

                    N = 31-day+1

                    S_w[i] = int( S_m[month]*N/31 + S_m[ month+1 ]*(7-N)/30)

                    continue

#もし、ISO-week=14, day=1がmonth=4の時
# int(S_m4 * 7 / 30)

            elif month == 4 :

                N =7

                S_w[i] = int( S_m[ month ] * N / 30 )

                continue

            else:

                pass


# もし、ISO-week=15,16 day=1がmonth=4の時

        if i in ( 15, 16 ):
        #if i == 15 or 16:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day


            if month == 4:

                N = 7

                S_w[i] = int( S_m[month] * N / 30 )

                continue

            continue




        if i == 17:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day

# もし、ISO-week=17, day=1がmonth=4の時
# N = 30-day+1 > 7     day < 24 = 30-7+1  N=7
# month=4, day=20,21,22,23の時の計算
# S_m4 * N / 30

            if month == 4:

                if day <  24:

                    N = 7 

                    S_w[i] = int( S_m[ month ] * N / 30 )

                else:

# month=4, day=24,25,26の時の計算
# N = 30-day+1
# S_m4 * N / 30 + S_m5*(7-N)/31
# ここで、ISO-week=17, day=1がmonth=5は発生しない

                    N = 30-day+1

                    S_w[i] = int( S_m[month]*N/30 + S_m[month+1]*(7-N)/31 )

                continue

            continue




        if i == 18:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day

# もし、ISO-week=18, day=1がmonth=4の時
# month=4, day=27,28,29,30の時の計算
# N = 30-day+1
# S_m4 * N / 30 + S_m5*(7-N)/31

            if month == 4:

                if day >= 27 :

                    N = 30-day+1

                    S_w[i] = int( S_m[month]*N/30 + S_m[ month+1 ]*(7-N)/31)

                    continue

# もし、ISO-week=18, day=1がmonth=5の時
# int(S_m5 * 7 / 31)

            elif month == 5 :

                N =7

                S_w[i] = int( S_m[ month ] * N / 31 )

                continue

            else:

                pass



        if i in ( 19, 20, 21 ):
        #if i == 19 or 20 or 21:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)


            S_w[i] = int(S_m[ r.month ] * 7 / 31 )

            continue




        if i == 22:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day

# もし、ISO-week=22, day=1がmonth=5の時

            if month == 5:

                if day <  24:

                    continue

                else:

# month=5, day=25,26,27,28,29,30,31の時の計算
# N = 31-day+1 
# S_m5 * N / 31 + S_m6*(7-N)/30
# ここで、ISO-week=22, day=1がmonth=6は発生しない

                    N = 31-day+1

                    S_w[i] = int( S_m[month]*N/31 + S_m[month+1]*(7-N)/30 )

                continue

            continue




        if i == 23:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day

# もし、ISO-week=23, day=1がmonth=5の時
# month=5, day=31の時の計算
# N = 31-day+1
# S_m5 * N / 31 + S_m6*(7-N)/30

            if month == 5:

                if day >= 31 :

                    N = 31-day+1

                    S_w[i] = int( S_m[ month ]*N/31 + S_m[ month+1 ]*(7-N)/30)

                    continue

# もし、ISO-week=23, day=1がmonth=6の時
# N=7
# S_m6*N/30

            elif month == 6 :

                N =7

                S_w[i] = int( S_m[ month ] * N / 30 )

                continue

            else:

                pass



        if i in ( 24, 25 ):
        #if i == 24 or 25:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)

# S_m6*N/30

            S_w[i] = int(S_m[ r.month ] * 7 / 30 )

            continue




        if i == 26:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day

# もし、ISO-week=26, day=1がmonth=6の時
# N = 30-day+1 > 7    day < 25 = 30-7+1  N=7
# month=6, day=21,22,23,24の時の計算
# S_m6 * N / 30

            if month == 6:

                if day <  25:

                    N = 7 

                    S_w[i] = int( S_m[ month ] * N / 30 )

                else:

# month=6, day=25,26,27,28の時の計算
# N = 30-day+1
# S_m6 * N / 30 + S_m7*(7-N)/31
# ここで、ISO-week=26, day=1がmonth=7は発生しない

                    N = 30-day+1

                    S_w[i] = int( S_m[month]*N/30 + S_m[month+1]*(7-N)/31 )

                continue

            continue




        if i == 27:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day

# もし、ISO-week=27, day=1がmonth=6の時
# month=6, day=28,29,30の時の計算
# N = 30-day+1
# S_m6 * N / 30 + S_m7*(7-N)/31

            if month == 6:

                if day >= 28 :

                    N = 30-day+1

                    S_w[i] = int( S_m[ month ]*N/30 + S_m[ month+1 ]*(7-N)/31)

                    continue

# もし、ISO-week=27, day=1がmonth=7の時
# N=7 
# S_m7 * N / 31

            elif month == 7 :

                N =7

                S_w[i] = int( S_m[ month ] * N / 31 )

                continue

            else:

                pass



        if i in ( 28, 29 ):
        #if i == 28 or 29:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)

# S_m7*N/31

            S_w[i] = int(S_m[ r.month ] * 7 / 31 )

            continue


        if i == 30:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day

# もし、ISO-week=30, day=1がmonth=7の時
# N = 31-day+1 > 7   day < 25  N=7
# month=7, day=19,20,21,22,23,24の時の計算
#  S_m7 * N / 31

            if month == 7:

                if day <  25:

                    N = 7 

                    S_w[i] = int( S_m[ month ] * N / 31 )

                else:

# month=7, day=25,26の時の計算
# N = 31-day+1
# S_m7 * N / 31 + S_m8*(7-N)/31
# ここで、ISO-week=30, day=1がmonth=8は発生しない

                    N = 31-day+1

                    S_w[i] = int( S_m[month]*N/31 + S_m[month+1]*(7-N)/31 )

                continue

            continue




        if i == 31:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day




# もし、ISO-week=31, day=1がmonth=7の時
# month=7, day=26,27,28,29,30,31の時の計算
# N = 31-day+1
# S_m7 * N / 31 + S_m8*(7-N)/31

            if month == 7:

                if day >= 26 :

                    N = 31-day+1

                    S_w[i] = int( S_m[ month ]*N/31 + S_m[ month+1 ]*(7-N)/31)

                    continue

# もし、ISO-week=31, day=1がmonth=8の時
# N=7 
# S_m8 * N / 31

            elif month == 8 :

                N =7

                S_w[i] = int( S_m[ month ] * N / 31 )

                continue

            else:

                pass


        if i in ( 32, 33, 34 ):
        #if i == 32 or 33 or 34:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)

# S_m8*N/31

            S_w[i] = int(S_m[ r.month ] * 7 / 31 )

            continue


        if i == 35:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day


# もし、ISO-week=35, day=1がmonth=8の時
# N = 31-day+1 > 7   day < 25 
# month=8, day=24の時の計算
# N=7 
# S_m8 * N / 31

            if month == 8:

                if day <  25:

                    N = 7 

                    S_w[i] = int( S_m[ month ] * N / 31 )

                else:

# month=8, day=25,26,27,28,29,30の時の計算
# N = 31-day+1
# S_m8 * N / 31 + S_m9*(7-N)/30
# ここで、ISO-week=35, day=1がmonth=9は発生しない

                    N = 31-day+1

                    S_w[i] = int( S_m[month]*N/31 + S_m[month+1]*(7-N)/30 )

                continue

            continue




        if i == 36:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day


# もし、ISO-week=36, day=1がmonth=8の時
# month=8, day=30,31の時の計算
# N = 31-day+1
# S_m8 * N / 31 + S_m9*(7-N)/30


            if month == 8:

                if day >= 26 :  # day >= 30 :

                    N = 31-day+1

                    S_w[i] = int( S_m[ month ]*N/31 + S_m[ month+1 ]*(7-N)/30)

                    continue


# もし、ISO-week=36, day=1がmonth=9の時
# N=7 
# S_m9 * N / 30


            elif month == 9 :

                N =7

                S_w[i] = int( S_m[ month ] * N / 30 )

                continue

            else:

                pass


        if i in ( 37, 38 ):
        #if i == 37 or 38 :

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)

# S_m9 * N / 30

            S_w[i] = int(S_m[ r.month ] * 7 / 30 )

            continue




        if i == 39:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day


# もし、ISO-week=39, day=1がmonth=9の時
# N = 30-day+1 > 7   day < 24 
# month=9, day=20,21,22,23の時の計算
# N=7 
# S_m9 * N / 30


            if month == 9:

                if day <  24:

                    N = 7 

                    S_w[i] = int( S_m[ month ] * N / 30 )

                else:


# month=9, day=24,25,26,27の時の計算
# N = 30-day+1
# S_m9 * N / 30 + S_m10*(7-N)/31
# ここで、ISO-week=39, day=1がmonth=10は発生しない


                    N = 30 - day + 1

                    S_w[i] = int( S_m[month]*N/30 + S_m[month+1]*(7-N)/31 )

                continue

            continue



# もし、ISO-week=40, day=1がmonth=10の時
# N=7 
# S_m10 * N / 31


        if i == 40:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day


# もし、ISO-week=40, day=1がmonth=9の時
# month=9, day=27,28,29,30の時の計算
# N = 30-day+1
# S_m9 * N / 30 + S_m10*(7-N)/31


            if month == 9:

                if day >= 27 :  # day >= 30 :

                    N = 30-day+1

                    S_w[i] = int( S_m[ month ]*N/30 + S_m[ month+1 ]*(7-N)/31)

                    continue


# もし、ISO-week=40, day=1がmonth=10の時
# N=7 
# S_m10 * N / 31


            elif month == 10 :

                N =7

                S_w[i] = int( S_m[ month ] * N / 31 )

                continue

            else:

                pass


        if i in ( 41, 42 ):
        #if i == 41 or 42 :

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)

# S_m10 * N / 31

            S_w[i] = int(S_m[ r.month ] * 7 / 31 )

            continue




        if i == 43:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day


# もし、ISO-week=43, day=1がmonth=10の時
# N = 31-day+1 > 7   day < 25 
# month=9, day=18,19,,,,23,24の時の計算
# N=7 
# S_m10 * N / 31


            if month == 10:

                if day <  25:

                    N = 7 

                    S_w[i] = int( S_m[ month ] * N / 31 )

                else:


# month=10, day=25の時の計算
# N = 31-day+1
# S_m10 * N / 31 + S_m11*(7-N)/30
# ここで、ISO-week=43, day=1がmonth=11は発生しない


                    N = 31 - day + 1

                    S_w[i] = int( S_m[month]*N/31 + S_m[month+1]*(7-N)/30 )

                continue

            continue




        if i == 44:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day


# もし、ISO-week=44, day=1がmonth=10の時
# month=10, day=26,27,28,29,30,31の時の計算
# N = 31-day+1
# S_m10 * N / 31 + S_m11*(7-N)/30


            if month == 10:

                if day >= 26 :  # day >= 30 :

                    N = 31-day+1

                    S_w[i] = int( S_m[ month ]*N/31 + S_m[ month+1 ]*(7-N)/30)

                    continue


# もし、ISO-week=44, day=1がmonth=11の時
# N=7 
# S_m11 * N / 30


            elif month == 11 :

                N =7

                S_w[i] = int( S_m[ month ] * N / 30 )

                continue

            else:

                pass


        if i in ( 45, 46, 47 ):
        #if i == 45 or 46 or 47 :

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)

# S_m11 * N / 30

            S_w[i] = int(S_m[ r.month ] * 7 / 30 )

            continue






        if i == 48:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day


# もし、ISO-week=48, day=1がmonth=11の時
# N = 30-day+1 >= 7   day <= 24 
# month=11, day=23の時の計算
#  N=7 
#   S_m11 * N / 30


            if month == 11:

                if day <  24: 

                    N = 7 

                    S_w[i] = int( S_m[ month ] * N / 30 )

                else:


# month=11, day=24,25,26,27,28,29の時の計算
# N = 30-day+1
# S_m11 * N / 30 + S_m12*(7-N)/31
# ここで、ISO-week=48, day=1がmonth=12は発生しない


                    N = 30 - day + 1

                    S_w[i] = int( S_m[month]*N/30 + S_m[month+1]*(7-N)/31 )

                continue

            continue




        if i == 49:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day


# もし、ISO-week=49, day=1がmonth=11の時
# month=11, day=29,30の時の計算
# N = 30-day+1
# S_m11 * N / 30 + S_m12*(7-N)/31


            if month == 11:

                if day >= 29 :  # day >= 30 :

                    N = 30-day+1

                    S_w[i] = int( S_m[ month ]*N/30 + S_m[ month+1 ]*(7-N)/31)

                    continue


# もし、ISO-week=49, day=1がmonth=12の時
# N=7 
# S_m12 * N / 31


            elif month == 12 :

                N =7

                S_w[i] = int( S_m[ month ] * N / 31 )

                continue

            else:

                pass


        if i in ( 50, 51 ):
        #if i == 50 or 51 :

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)

# S_m12 * N / 31

            S_w[i] = int(S_m[ r.month ] * 7 / 31 )

            continue




        if i == 52:

            r = date.fromisocalendar( year , i , 1)
            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day


# もし、ISO-week=52, day=1がmonth=12の時
# N = 31-day+1 > 7   day < 25 
# month=12, day=20,21,22,23,24の時の計算
#  N=7 
#   S_m12 * N / 31


            if month == 12:

                if day <  25: 

                    N = 7 

                    S_w[i] = int( S_m[ month ] * N / 31 )

                else:


# month=12, day=25,26,27の時の計算
# N = 31-day+1
# S_m12 * N / 31 + S_m13*(7-N)/31
# ここで、ISO-week=52, day=1がmonth=13は発生しない


                    N = 31 - day + 1

                    S_w[i] = int( S_m[month]*N/31 + S_m[month+1]*(7-N)/31 )

                continue

            continue




        if i == 53:

            r = date.fromisocalendar( year+1 , 1 , 1)  # 53週は翌年の1週

            #### r = xxxxx( year , i , 1) 


            print(r)
            # 2023-01-02

            print(r.year)
            print(r.month)
            print(r.day)
        
            month = r.month
            day   = r.day


# もし、ISO-week=53(=1), day=1がmonth=12の時
# month=12, day=29,30,31の時の計算
# N = 31-day+1
# S_m12 * N / 31 + S_m13*(7-N)/31


            if month == 12:

                if day >= 29 :  # day >= 30 :

                    N = 31-day+1

                    #### month + 1 = 13は、翌年の1月
                    S_w[i] = int( S_m[ month ]*N/31 + S_m[ month+1 ]*(7-N)/31)

                    continue


# もし、ISO-week=53(=1), day=1がmonth=1(=13)の時
# N=7 
# S_m13 * N / 31


            elif month == 1 :
            #elif month == 13 : は発生しないので、翌年のmonth==1とする

                N =7

                #### month = 13は、翌年の1月 month+12 = 13としてM_s[13]を検索
                S_w[i] = int( S_m[ month+12 ] * N / 31 )

                continue

            else:

                pass


    return S_w


# *****************************************
# read_csv_plan_month 
# *****************************************

def read_convert_csv_plan_M2W( filename ):

#def read_csv_plan_month( "PLAN S month 2023 Contry node.csv" ):
#filename = "PLAN S month 2023 Contry node.csv"

    week_row_list = []

    with open(filename, encoding='utf8', newline='') as f:

        csvreader = csv.reader(f)

        header = next(csvreader)

# *********************************
# header image "PLAN S month 2023 Contry node.csv"
# *********************************
# 0 Product id
# 1 Country name
# 2 P node id
# 3 C node id
# 4 C node name
# 5 year
# 6 M0 M1 M2 M3 M4 M5 M6 M7 M8 M9 M10 M11 M12 M13
# *********************************

        for row in csvreader:

            year          = int( row[5] )

            S_m_list_str  = row[6:]

            print('S_m_list_str',S_m_list_str)

            S_m_list = [int(s) for s in S_m_list_str]



            S_w_init  = [0] * 54 


            S_w = make_S_M2W( year, S_m_list, S_w_init )


            week_row = row[:6] + S_w

            week_row_list.append(week_row)

    return week_row_list


# *****************************************
# write_csv_plan_week 
# *****************************************

def write_csv_plan_week( csv_file_name , week_row_list ):

    l = []


    r0 = [ 'Product id', 'Country name', 'P node id', 'C node id', 'C node name', 'year' ]

    r1 = [ 'W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10', 'W11', 'W12', 'W13' ]    

    r2 = [ 'W14', 'W15', 'W16', 'W17', 'W18', 'W19', 'W20', 'W21', 'W22', 'W23', 'W24', 'W25', 'W26' ]

    r3 = [ 'W27', 'W28', 'W29', 'W30', 'W31', 'W32', 'W33', 'W34', 'W35', 'W36', 'W37', 'W38', 'W39' ]

    r4 = [ 'W40', 'W41', 'W42', 'W43', 'W44', 'W45', 'W46', 'W47', 'W48', 'W49', 'W50', 'W51', 'W52', 'W53' ]

    r = r0 + r1 + r2 + r3 + r4


    l.append(r) # 二次元リストの初期設定 setting header

    for r in week_row_list:

        l.append(r)

# ****************************************
# CSV ファイル書き出し
# ****************************************

    with open( csv_file_name, 'w', encoding='utf8',  newline="") as f1:
    #with open( csv_file_name , 'w', newline="") as f1:
        writer = csv.writer(f1)
        writer.writerows(l)


# *****************************************
# get_S_month 
# *****************************************

# *****************************************
# run 
# *****************************************
week_row_list = []

csv_file_name = "PLAN S month 2023 Contry node.csv"

week_row_list = read_convert_csv_plan_M2W( csv_file_name )


#for r in csv_plan_M:
#
#    S_m_list = get_S_month(r)
###
###S_m_list = [M0, M1, M2, M3, M4, M5, M6, M7, M8, M9,M10,M11,M12,M13 ]
###
##S_m_list  = [10, 20, 20, 30, 30, 40, 50, 60, 70, 80, 40, 20, 10, 10 ]
#
#    S_w_init  = [0] * 54 
#
##S_w_r = []
#
#    S_w = make_S_M2W( 2023, S_m_list, S_w_init )
#
#    print('S_week =',S_w)

csv_file_name = "PLAN S week 2023 Contry node.csv"

write_csv_plan_week( csv_file_name , week_row_list )

print('end of M2W conversion')
