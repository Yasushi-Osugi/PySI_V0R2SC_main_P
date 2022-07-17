# initial setting PySI data and directory for SCM node tree
#" with windows commands test

import os
import subprocess

from make_SCMTREE2postorder010 import *
#from make_SCMTREE_profile010 import *


#postorder_node = ['TKO_L', 'TKO', 'OSA_L', 'OSA', 'BRU_L', 'BRU', 'HEL_L', 'HEL', 'AMS_L', 'AMS', 'AKL_L', 'AKL', 'WAW_L', 'WAW', 'LIS_L', 'LIS', 'MAD_L', 'MAD', 'ZRH_L', 'ZRH', 'YTOLEAF', 'YTO', 'NYC_N', 'NYC_D', 'NYC_I', 'NYC', 'LAX_N', 'LAX_D', 'LAX_I', 'SFOLEAF', 'LAX', 'MEXLEAF', 'MEX', 'SAOLEAF', 'SAO', 'BUELEAF', 'BUE', 'KULLEAF', 'KUL', 'BKKLEAF', 'BKK', 'SINLEAF', 'SIN', 'SGNLEAF', 'SGN', 'ISTLEAF', 'IST', 'JKTLEAF', 'JKT', 'SELLEAF', 'SEL', 'SYDLEAF', 'SYD', 'DELLEAF', 'DEL', 'RUHLEAF', 'RUH', 'SWELEAF', 'DENLEAF', 'NORLEAF', 'GOT', 'LONLEAF', 'LON', 'PARLEAF', 'PAR', 'HAM_L', 'FRALEAF', 'FRA', 'MUCLEAF', 'MUC', 'HAM', 'MXPLEAF', 'MXP', 'JNBLEAF', 'JNB', 'SHA_N', 'SHA_D', 'SHA_I', 'BJS_N', 'BJS_D', 'BJS_I', 'SHA', 'CAN_N', 'CAN_D', 'CAN_I', 'CAN', 'LEDLEAF', 'LED', 'JPN']


#postorder_node = ['test_1', 'test_2' ]

# *****************************************
# STOP make dir and copy files ファイル生成は停止
# *****************************************

#for node in postorder_node:
#
#    #cmd = "dir ."
#    #cmd = "md test"
#
#    cmd = "md " + node
#    print(cmd)
#    res = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="shift-jis")
#
#
#    node_dir = ' .\\' + node
#    print(node_dir)
#
#
#    cmd = "copy PySI_data_std_IO.csv  " + node_dir
#    print(cmd)
#    res = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="shift-jis")
#
#
#    cmd = "copy PySI_Profile_std.csv  " + node_dir
#    print(cmd)
#    res = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="shift-jis")
#
#    cmd = "copy PySI_monitor.xlsx  " + node_dir
#    print(cmd)
#    res = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="shift-jis")
#
#    #print(res)
#
#
#    cmd = "cd  " + node
#    print(cmd)
#    res = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="shift-jis")
#
#    node_dir = ' .\\' + node
#
#    cmd = "md " + node_dir + "\\data"
#    print(cmd)
#    res = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="shift-jis")
#
#
#print("end node list")



# ********************************************
# filename と profile_list は、
# importした　make_SCMTREE2postorder010で定義している 
# ********************************************

##filename = 'SCMTREE_profile010.csv'
#filename = 'SCMTREE_profile010_test.csv'

# ********************************************
# write profile 2 node with profile_list 
# ********************************************

print('**** ヘッダーのみ ****')


with open(filename, encoding='utf-8-sig', newline='') as f:
#with open(filename, encoding='utf8', newline='') as f:
#with open( filename, 'r') as f:

    reader = csv.reader(f)

    header = reader.__next__()  # ヘッダーの読み込み


    profile_header = header[3:]

print('profile_header',profile_header)

print('**** profile 本体 ****')

for r in profile_list:

    node = r[1]  #

    profile_row = r[3:]

# *****************************************
# nodeの下のfile_pathhの指定方法 2種類
# *****************************************

    #file_path = ' .\\' + node+ '\\PySI_Profile_std.csv' ### nodeの下

    node_dir = 'node_all\\' + node

    dir_name  = node_dir + '\\PySI_Profile_std.csv' ### nodeの下

    file_path = os.path.join(os.path.dirname(__file__), dir_name)

# profile_header = ['Parent node', 'Child node', 'Child node name', 
# 'attribute', 'BU_SC_node_profile', 'product_name', 'SC_tree_id', 'node_from', 'node_to', 'time_profile', 'plan_year', 'plan_engine', 'reward_sw', 'calendar_cycle_week', 'calendar_off_week', 'weeks_year', 'product_cost_profile', 'Price_a_planning_lot_size', 'AVE_PRICE_shipped_pack_lot', 'Cash_Intrest', 'PO_Mng_cost', 'Purchase_cost', 'REVENUE_RATIO', 'SGMC_ratio', 'WH_COST_RATIO', 'WH_COST_RATIO_aWeek', 'distribution_condition', 'LOT_SIZE', 'LT_boat', 'LT_air', 'LT_qourier', 'Indivisual_Packing', 'Packing_Lot', 'Transport_Lot', 'planning_lot_size', 'Distriburion_Cost', 'weeks_year', 'SS_days', 'TAX_currency_condition', 'HS_code', 'customs tariff rate', 'income_tax_from', 'income_tax_to', 'forex_rate_USD_from', 'forex_rate_USD_to', '']

# r[3:]

    prof_l = []

    for i, el in enumerate(profile_row):

        # *********************
        # *** write headder ***
        # *********************
        profile_r = [ profile_header[i] , el ] 

        prof_l.append( profile_r )


    with open( file_path , 'w'  , newline="") as f:

        writer = csv.writer(f)

        writer.writerows( prof_l )

print('end of write profile2node')
