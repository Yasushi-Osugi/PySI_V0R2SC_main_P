#
# PySI_set_Leaf_Node_week_S2PSI.py
#

#
# 2022 Yasushi Ohsugi
#
#
import os
import csv
import calendar
import pandas as pd

#from datetime import date



# *****************************************
# read_csv_plan_month 
# *****************************************

def read_csv_Leaf_Node_week_S( file_path ):

    week_row_list = []

    with open(file_path, encoding='utf8', newline='') as f:
    #with open(file_path, encoding='shift-jis', newline='') as f:

        csvreader = csv.reader(f)

        header = next(csvreader) # タイトル行を飛ばす


# *********************************
# header image "PLAN S week 2023 Contry node.csv"
# *********************************
# 0 Product id
# 1 Country name
# 2 P node id
# 3 C node id
# 4 C node name
# 5 year
# 6 W0 W1 W2 W3 W4 W5 W6 W7     W52 W53
# *********************************

        for row in csvreader:

            #@220627

            #Prod_ID         = row[0]
            #Country_name    = row[1]
            #Parent_node     = row[2]
            #Child_node      = row[3]

            #Child_node_name  = row[4]
            #year             = row[5]

            S_w_list_str  = row[6:]

            S_w_list = [int(s) for s in S_w_list_str]


            week_row = row[:6] + S_w_list

            week_row_list.append(week_row)


    return week_row_list


# ******************************
# read_PSI_data_csv
# ******************************

def read_PSI_data_csv( node ): 

    dir_name  = 'node_all\\' + node + '\\PySI_data_std_IO.csv' ### node_allの下

    #dir_name  = node + '\\PySI_data_std_IO.csv'         ### nodeの下
    #file_path = ' .\\' + node+ '\\PySI_data_std_IO.csv' ### nodeの下


# *****************************************
#import os
#
#    print('getcwd:      ', os.getcwd()) # カレントpath
#    print('__file__:    ', __file__)    # python実行中のpath
#
#    print('file_path:    ', file_path)  # 指定したいpath
#    print('dir_name:    ', dir_name)    # 指定したいpath
#
#    print('[set target path]')
#
# *****************************************

    target_path = os.path.join(os.path.dirname(__file__), dir_name)

# *****************************************
#
#    print('target_path: ', target_path)
#
# *****************************************


    PSI_data = [] #リスト型を宣言

# ******************************
# Headerがcsv fileに含まれている場合の記述
# ******************************
# prod_name	scm_id	node_from	node_to	SIP	W00	W01	W02	W03	W04	W05	W06	W07	W08	W09	W10	W11	W12	W13	W14	W15	W16	W17	W18	W19	W20	W21	W22	W23	W24	W25	W26	W27	W28	W29	W30	W31	W32	W33	W34	W35	W36	W37	W38	W39	W40	W41	W42	W43	W44	W45	W46	W47	W48	W49	W50	W51	W52	W53

    with open(target_path, encoding='shift-jis', newline='') as f1:
    #with open(file_path, encoding='utf8', newline='') as f1:

        csvreader = csv.reader(f1)

        #header = next(csvreader) # STOPタイトル行を飛ばさない

        for r in csvreader:

            PSI_data.append( r )

#    df = pd.read_csv( file_path , header=0  )
#    #df = pd.read_csv( file_path , header=0 , encoding='shift-jis' )
#    #df = pd.read_csv( file_path , encoding='shift-jis' , sep=',' )
#
#    PSI_data = df.values.tolist()
#    #PSI_data = df.to_numpy().tolist() #どっちが自然か?
#
#    #for l in PSI_data:
#    #    #print(l)
#    #    print(l[3])
#    #    print(l[4])
#    #    print(l[5:])

    return PSI_data



# ******************************
# write_PSI_data2csv
# ******************************

def write_S2PSI( node, PSI_data, Prod_ID, Parent_node, S_w ):

    dir_name  = 'node_all\\' + node + '\\PySI_data_std_IO.csv' ### nodeの下
    #dir_name  = node + '\\PySI_data_std_IO.csv' ### nodeの下

    target_path = os.path.join(os.path.dirname(__file__), dir_name)

    print('target_path: ', target_path)

    l       = []

#    X_row = []
#
#    0 product_name
#    1 SC_tree_id
#    2 node_from
#    3 node_to
#    4 S-CO-I-P-IP
#    5 W0,W1,W2,,,,,W52,W53

#header = ["prod_name" , "scm_id" , "node_from" , "node_to" , "SIP" , "W00" , "W01" , "W02" , "W03" , "W04" , "W05" , "W06" , "W07" , "W08" , "W09" , "W10" , "W11" , "W12" , "W13" , "W14" , "W15" , "W16" , "W17" , "W18" , "W19" , "W20" , "W21" , "W22" , "W23" , "W24" , "W25" , "W26" , "W27" , "W28" , "W29" , "W30" , "W31" , "W32" , "W33" , "W34" , "W35" , "W36" , "W37" , "W38" , "W39" , "W40" , "W41" , "W42" , "W43" , "W44" , "W45" , "W46" , "W47" , "W48" , "W49" , "W50" , "W51" , "W52" , "W53"]

    with open( target_path , 'w'  , newline="") as f2:
        writer = csv.writer(f2)

        # *********************
        # *** write headder ***
        # *********************

        writer.writerow( PSI_data[0] )
        #writer.writerow(header)

        # *********************
        # *** write S-CO-I-P-IP
        # *********************

        w_row = PSI_data[1]  # Sの行

        SCM_ID = Prod_ID[ len(Prod_ID)-5 : ] # 下5桁

        w_row[0] = Prod_ID     # product 
        w_row[1] = SCM_ID      # SCM_ID
        w_row[2] = Parent_node # Parent_node
        w_row[3] = node        # Child_node
        w_row[4] = "1S"        # PSI

        w_row[5:] = S_w

        l = w_row

        print('l',l)

        writer.writerow(l)



        # ************************
        w_row = PSI_data[2]  # COの行

        w_row[0] = Prod_ID     # product 
        w_row[1] = SCM_ID      # SCM_ID
        w_row[2] = Parent_node # Parent_node
        w_row[3] = node        # Child_node
        w_row[4] = "2CO"       # PSI

        l = w_row[:5] + w_row[5:]

        print('l',l)

        writer.writerow(l)



        # ************************
        w_row = PSI_data[3]  # Iの行

        w_row[0] = Prod_ID     # product 
        w_row[1] = SCM_ID      # SCM_ID
        w_row[2] = Parent_node # Parent_node
        w_row[3] = node        # Child_node
        w_row[4] = "3I"        # PSI

        l = w_row[:5] + w_row[5:]

        print('l',l)

        writer.writerow(l)



        # ************************
        w_row = PSI_data[4]  # Pの行

        w_row[0] = Prod_ID     # product 
        w_row[1] = SCM_ID      # SCM_ID
        w_row[2] = Parent_node # Parent_node
        w_row[3] = node        # Child_node
        w_row[4] = "4P"        # PSI

        print('l',l)

        l = w_row[:5] + w_row[5:]

        writer.writerow(l)


        # ************************
        w_row = PSI_data[5]  # IPの行 # 

        w_row[0] = Prod_ID     # product 
        w_row[1] = SCM_ID      # SCM_ID
        w_row[2] = Parent_node # Parent_node
        w_row[3] = node        # Child_node
        w_row[4] = "5IP"       # PSI

        l = w_row[:5] + w_row[5:]

        print('l',l)

        writer.writerow(l)


# *****************************************
# run 
# *****************************************

Leaf_Node_S_list = []

node_name = ""
S_w       = []

xlsx_csv_file_path = "PLAN S week 2023 Contry node.csv"

Leaf_Node_S_list = read_csv_Leaf_Node_week_S( xlsx_csv_file_path )


for leaf_node_S in Leaf_Node_S_list:

    Prod_ID          = leaf_node_S[0]
    Country_name     = leaf_node_S[1]
    Parent_node      = leaf_node_S[2]
    Child_node       = leaf_node_S[3]

    Child_node_name  = leaf_node_S[4]
    year             = leaf_node_S[5]

    S_w_list         = leaf_node_S[6:]


    node = Child_node
    S_w  = S_w_list

    print('node',node)
    print('S_w',S_w)

# ******************************
# read_write_PSI_data2csv 
# ******************************

    PSI_data = read_PSI_data_csv( node ) 

    print('PSI_data',PSI_data)

    write_S2PSI( node, PSI_data, Prod_ID, Parent_node, S_w )


print('end of set S2PSI')
