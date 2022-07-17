# make_SCMTREE2postorder.py
#
# Yasushi Ohsugi 2022
#

import copy
import csv


# ************************************************************
# read SCMTREE file
# ************************************************************

filename = 'SCMTREE_profile010.csv'
#filename = 'SCMTREE_profile010_test.csv'

supplier_buyer_list     = []
profile_list            = []

node_name_list      = []

bfs_pos_list_noleaf     = []


with open(filename, encoding='utf8', newline='') as f:
#with open(filename, encoding='shift-jis', newline='') as f:

    csvreader = csv.reader(f)

    header = next(csvreader) # タイトル行を飛ばす

    for row in csvreader:

        supplier_buyer_pair = row[:2]  # 0:supplier_node 1:buyer_node
        profile_row = row

        # *************************************
        # supplier nodeに"root"を指定 そのbuyer nodeがマザープラント
        # *************************************
        if supplier_buyer_pair[0] == "root":

        # *************************************
        # scm_tree listの初期設定
        # *************************************

            scm_tree  = [ supplier_buyer_pair[1] ,[]]
            #scm_tree = [ 'JPN'      ,[]]

            bfs_tree  = []

            seq_list  = [ supplier_buyer_pair[1] ]
            #seq_list = [ 'JPN'      ]

            # 親ノードの初期設定
            node_name_list  = [ supplier_buyer_pair[1] ]
            #node_name_list = [ 'JPN' ]


# 需給関係のペアリストをリストにした二次元配列
# supplier_buyer_list = [['JPN', 'YTO'], ['JPN', 'NYC'], ['JPN', 'LAX'], ,,,]

        supplier_buyer_list.append(supplier_buyer_pair)


# 各nodeのPSI計画profileリスト
        profile_list.append(profile_row)


#print('supplier_buyer_list =',supplier_buyer_list)
# supplier_buyer_list = [['root', 'JPN'], ['JPN', 'YTO'], ['JPN', 'NYC'], ['JPN', 'LAX'], ['JPN', 'MEX'], ['JPN', 'SAO'], ['JPN', 'BUE'], ['JPN', 'KUL'], ['JPN', 'BKK'], ,,,,,,,,,  ['MAD', 'MADLEAF'], ['ZRH', 'ZRHLEAF']]

#print('len(supplier_buyer_list) =',len(supplier_buyer_list))  
#92


# "root"を指定して、ツリー構造を作成する。
def make_scm_tree( scm_tree, supplier_buyer_list ):

    w = [0]
    invest = [scm_tree]             # 調べるノードのリスト invest

    while not( len(invest)==0):     # investが空になるまで

        invest_node = invest.pop(0) # investの位置[0]要素を取り出し削除

        # すべてのsupplier_buyerのpairを調査
        for sup_buy in supplier_buyer_list: 

            # pair状態とtree状態の親 供給者[0]が一致したら、
            if sup_buy[0] == invest_node[0]: 

# *********************************************************************
                node_name_list.append( sup_buy[1] )
# *********************************************************************

                # 子 購買者[1]のツリーデータを作成して、
                x = [sup_buy[1],[]]

                # 調査対象のツリーの子ノードとして追加
                invest_node[1].append(x)

                # 子 購買者ノードを調査対象investに追加
                invest.append( x )

                # end of pair状態とtree状態の親 供給者[0]が一致

            # end of supplier_buyerのpairを調査

    return scm_tree, node_name_list

# ノード一覧
# node_name__list = ['JPN', 'YTO', 'NYC', 'LAX', 'MEX', 'SAO', 'BUE', 'KUL', 'BKK', 'SIN', 'SGN', 'IST', 'JKT', 'SEL', 'SYD', 'DEL', 'RUH', 'GOT', 'LON', 'PAR', 'HAM', 'MXP', 'JNB', 'SHA', 'CAN', 'LED', 'BRU', 'TYO', 'OSA', 'AMS', 'AKL', 'WAW', 'LIS', 'MAD', 'ZRH', 'YTOLEAF', 'NYC_N', 'NYC_D', 'NYC_I', 'LAX_N', 'LAX_D', 'LAX_I', 'SFOLEAF', 'MEXLEAF', 'SAOLEAF', 'BUELEAF', 'KULLEAF', 'BKKLEAF', 'SINLEAF', 'SGNLEAF', 'ISTLEAF', 'JKTLEAF', 'SELLEAF', 'SYDLEAF', 'DELLEAF', 'RUHLEAF', 'SWELEAF', 'NORLEAF', 'DENLEAF', 'HELLEAF', 'LONLEAF', 'PARLEAF', 'HAM_N', 'HAM_D', 'HAM_I', 'MUC', 'FRALEAF', 'MXPLEAF', 'JNBLEAF', 'SHA_N', 'SHA_D', 'SHA_I', 'BJS_N', 'BJS_D', 'BJS_I', 'HGH', 'CAN_N', 'CAN_D', 'CAN_I', 'LEDLEAF', 'BRULEAF', 'TYOLEAF', 'OSALEAF', 'AMSLEAF', 'AKLLEAF', 'WAWLEAF', 'LISLEAF', 'MADLEAF', 'ZRHLEAF', 'MUC_N', 'MUC_D', 'MUC_I', 'HGH-N', 'HGH-D', 'HGH-I']



def find_supplier( node, supplier_buyer_list ):

    for sb_pair in supplier_buyer_list:

        if sb_pair[1] == node:

            return sb_pair[0]  # supplier(親)は一人



def is_leaf(node):

    for sb_pair in supplier_buyer_list:

        if sb_pair[0] == node:

            return False  # 自分がsupplier(親)になる時がある

        else:

            pass

    return True #  最後まで自分がsupplier(親)にならなかった


bfs_pos_list         = []
bfs_pos_list_noleaf  = []
pos_list             = []

# ******************************
# 親子ペアリストで同じ親を探して「bfsの葉ノードなし位置リスト」を生成
# ******************************
def node_name2pos( node_name_list, supplier_buyer_list ):

    l = node_name_list

    mother = l[0]

    work_pos = []


    for node in l :

        supplier = find_supplier( node, supplier_buyer_list )  
        # 自分の親、supplierを見つける

        if supplier == 'root':

            continue

        elif supplier == mother:

            work_pos.append(l.index(node)) # node_name_listの位置をappend

        else:
        # 自分の親、supplierが切り替わった時点で、work_posにあるbuyerをappend
            pos_list.append(work_pos)


            work_pos = []
            work_pos.append(l.index(node)) # node_name_list位置をappend

            mother = supplier

    # ******* loop end process ***********

    pos_list.append(work_pos)

    # ******* loop end process ***********


    return pos_list



# ツリー構造を表示
def tree_str(node,indent=""):

    s = indent+str(node[0])+"\n"

    # 子ノードでループ
    for c in node[1]:              

        s += tree_str(c,indent+"+-")

    return s



# ********************************************************************
# RUN
# ********************************************************************


#scm_tree = ['JPN',[]]


scm_tree, node_name_list = make_scm_tree( scm_tree, supplier_buyer_list )


print('')
print('scm_tree =',scm_tree)


print('')
print('node_name_list =',node_name_list)

str = tree_str(scm_tree)

print('')
print(str)


#scm_tree = ['JPN', [['YTO', [['YTOLEAF', []]]], ['NYC', [['NYC_N', []], ['NYC_D', []], ['NYC_I', []]]], ['LAX', [['LAX_N', []], ['LAX_D', []], ['LAX_I', []], ['SFOLEAF', []]]', 

#node_name_list = ['JPN', 'YTO', 'NYC', 'LAX', 'MEX', 'SAO', 'BUE', 'KUL', 'BKK', 'SIN', 'SGN', 'IST', 'JKT', 'SEL', 'SYD', 'DEL', 'RUH', 'GOT', 'LON', 'PAR',,,,,, 'MUC_N', 'MUC_D', 'MUC_I', 'HGH-N', 'HGH-D', 'HGH-I']

# JPN
# +-YTO
# +-+-YTOLEAF
# +-NYC
# +-+-NYC_N
# +-+-NYC_D
# +-+-NYC_I
# +-LAX
# +-+-LAX_N


# ******************************
# 親子ペアリストで同じ親を探して「bfsの葉ノード=[]なし位置リスト」を生成
# ******************************
bfs_pos_list_noleaf = node_name2pos( node_name_list , supplier_buyer_list)

print('bfs_pos_list_noleaf',bfs_pos_list_noleaf)

#bfs_pos_list_noleaf [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [35], [36, 37, 38], [39, 40, 41, 42], [43], [44], [45], [46], [47], [48], [49], [50], [51], [52], [53], [54], [55], [56, 57, 58, 59], [60], [61], [62, 63, 64, 65, 66], [67], [68], [69, 70, 71, 72, 73, 74, 75], [76, 77, 78], [79], [80], [81], [82], [83], [84], [85], [86], [87], [88], [89, 90, 91], [92, 93, 94]]


# ******************************
# ノード一覧で葉ノードを検査して、葉なしリストに、[]をinsertまたはappendする
# check leaf and insert or append [] in pos_list
# ******************************
def put_leaf_pos_list( bfs_pos_list_noleaf, node_name_list):

    l = node_name_list

    pos_list = bfs_pos_list_noleaf

    #print('l pos_list', l, pos_list)


    for node in l :

        if is_leaf(node):

            n = l.index(node)

            if n <= len(pos_list):

                pos_list.insert( n , [] )  

                #print('insert pos_list', n, pos_list)


            else:

                pos_list.append( [] )

                #print('append pos_list', n, pos_list)

            # n番目に[]を挿入する。

        else:

            pass

    return pos_list


bfs_pos_list = put_leaf_pos_list( bfs_pos_list_noleaf, node_name_list)

print('')
print('bfs_pos_list',bfs_pos_list)

#bfs_pos_list [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], [35], [36, 37, 38], [39, 40, 41, 42], [43], [44], [45], [46], [47], [48], [49], [50], [51], [52], [53], [54], [55], [56, 57, 58, 59], [60], [61], [62, 63, 64, 65, 66], [67], [68], [69, 70, 71, 72, 73, 74], [75, 76, 77], [78], [79], [80], [81], [82], [83], [84], [85], [86], [87], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [88, 89, 90], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]




# ***************************************
# 「幅優先の位置情報ツリー」から、「帰りがけ順」を生成する postorder_search
# ***************************************

postorder      = []
postorder_node = []

def postorder_search( pos, bfs_pos_list ):

    #子 購買者ノードを位置番号で調べる
    for i in bfs_pos_list[pos]:

        #再帰探索
        postorder_search(i, bfs_pos_list)

    #子ノードを調べた後に追加
    postorder.append(pos)

    return postorder


# 帰りがけ順の位置番号リスト
postorder_pos = postorder_search( 0, bfs_pos_list )


for pos in postorder_pos:

    # 帰りがけ順の要素リスト
    postorder_node.append( node_name_list[pos] )


print('')
print('postorder_pos', postorder_pos)

#postorder_pos [35, 1, 36, 37, 38, 2, 39, 40, 41, 42, 3, 43, 4, 44, 5, 45, 6, 46, 7, 47, 8, 48, 9, 49, 10, 50, 11, 51, 12, 52, 13, 53, 14, 54, 15, 55, 16, 56, 57, 58, 59, 17, 60, 18, 61, 19, 62, 63, 64, 88, 89, 90, 65, 66, 20, 67, 21, 68, 22, 69, 70, 71, 72, 73, 74, 23, 75, 76, 77, 24, 78, 25, 79, 26, 80, 27, 81, 28, 82, 29, 83, 30, 84, 31, 85, 32, 86, 33, 87, 34, 0]


print('')
print('postorder_node',postorder_node)

#postorder_node ['YTOLEAF', 'YTO', 'NYC_N', 'NYC_D', 'NYC_I', 'NYC', 'LAX_N', 'LAX_D', 'LAX_I', 'SFOLEAF', 'LAX', 'MEXLEAF', 'MEX', 'SAOLEAF', 'SAO', 'BUELEAF', 'BUE', 'KULLEAF', 'KUL', 'BKKLEAF', 'BKK', 'SINLEAF', 'SIN', 'SGNLEAF', 'SGN', 'ISTLEAF', 'IST', 'JKTLEAF', 'JKT', 'SELLEAF', 'SEL', 'SYDLEAF', 'SYD', 'DELLEAF', 'DEL', 'RUHLEAF', 'RUH', 'SWELEAF', 'NORLEAF', 'DENLEAF', 'HELLEAF', 'GOT', 'LONLEAF', 'LON', 'PARLEAF', 'PAR', 'HAM_N', 'HAM_D', 'HAM_I', 'MUC_N', 'MUC_D', 'MUC_I', 'MUC', 'FRALEAF', 'HAM', 'MXPLEAF', 'MXP', 'JNBLEAF', 'JNB', 'SHA_N', 'SHA_D', 'SHA_I', 'BJS_N', 'BJS_D', 'BJS_I', 'SHA', 'CAN_N', 'CAN_D', 'CAN_I', 'CAN', 'LEDLEAF', 'LED', 'BRULEAF', 'BRU', 'TYOLEAF', 'TYO', 'OSALEAF', 'OSA', 'AMSLEAF', 'AMS', 'AKLLEAF', 'AKL', 'WAWLEAF', 'WAW', 'LISLEAF', 'LIS', 'MADLEAF', 'MAD', 'ZRHLEAF', 'ZRH', 'JPN']


