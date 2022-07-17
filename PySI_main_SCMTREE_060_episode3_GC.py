# coding: utf-8
#
#
#            Copyright (C) 2020 Yasushi Ohsugi
#            Copyright (C) 2021 Yasushi Ohsugi
#            Copyright (C) 2022 Yasushi Ohsugi
#
#            license follows MIT license

import numpy as np
import matplotlib.pyplot as plt

#  # メモリ解放
#  import gc
#  del tmp_data
#  del bulk
#  gc.collect()

# ******************************
# PySI related module
# ******************************
from PySILib.PySI_library_V0R1_070 import *

from PySILib.PySI_env_V0R1_080 import *

from PySILib.PySI_PlanLot_SCMTREE_GC_060 import *

from PySILib.PySI_search_LEAF_in_SCMTREE import *



# ******************************
# profileとPSI計画データ読込み loading 
# class PlanSpaceとLotSpaceの初期設定
# ******************************

# ******************************
# node_file_nameは将来的に"scm_tree"で定義したnode_nameで順次読込む
# ******************************
#print('loading plan')
#
#node_name = "Wch00"
#
#i_PlanSpace,i_LotSpace = load_plan( node_name )





# ******************************
# LEAFの場合　PSI_data_file読み込み 
# ******************************
def set_leaf_PSI_data(node):

# nodeはSCM tree のchild_nodeを指定

    PSI_data_file_name = ".\\node_all\\" + node + "\\PySI_data_std_IO.csv" 
    #PSI_data_file_name = ".\\" + node + "\\PySI_data_std_IO.csv" 
    # PSI data IOファイル名を宣言

    #print('PSI_data_file_name@input@LEAF',PSI_data_file_name)

    PSI_data = [] #retuen用にリスト型を宣言
    PSI_data = read_PSI_data_csv( PSI_data_file_name )

    #print('PSI_data',PSI_data) # LEAFの時、Sが入ってくる

    return PSI_data



def read_common_plan_unit( file_name, node ):

    # **********************************
    # start of reading 'common_plan_unit.csv'
    # **********************************
    
    df = pd.read_csv('common_plan_unit.csv')
    #df = pd.read_csv('common_plan_unit.csv',encoding='shift-jis',sep=',')
    
    print(df)

    # 'Dpt_entity == @node '

    df_node = df.query( 'Dpt_entity == @node ' )

    print('df_node in CPU ', df_node,node)
    
    #df_USA = df.query('Dpt_entity == "USA" ')
    #print(df_USA)
    #
    #df_JPN = df.query('Dpt_entity == "JPN" ')
    #print(df_JPN)
    
    
    #df.groupby('Dpt_week').sum()

    # **************************
    # "step"は一ロット単位を表す要求元のシリアル番号
    # ここで加算するのは、ロットの個数なので、sum()ではなく、count()
    # **************************
    Dpt_S = df_node[['Dpt_week','Dpt_step']].groupby('Dpt_week').count()

    #Dpt_S = df_node[['Dpt_week','Dpt_step']].groupby('Dpt_week').sum()
    #Dpt_S = df_JPN[['Dpt_week','Dpt_step']].groupby('Dpt_week').sum()
    
    print('Dpt_S',Dpt_S)
    
    
    #Dpt_S_list = Dpt_S.values.tolist()
    #print(Dpt_S_list)
    
    common_plan_S = Dpt_S.reset_index().values.tolist()
    
    print(common_plan_S)
    
    # [[-7, 15], [-6, 28], [-5, 31], [-4, 1], [-3, 22], [-2, 6], [-1, 0], [2, 0], 
    # [3, 15], [4, 10], [6, 0], [8, 10], [9, 28], [10, 3], [11, 55], [12, 28], 
    # [13, 28], [14, 114], [15, 54], [16, 48], [18, 210], [19, 92], [20, 55], 
    # [21, 157], [22, 46], [23, 579], [24, 31], [25, 174], [26, 1], [27, 297], 
    # [28, 3], [29, 45], [30, 0], [31, 0], [32, 55], [33, 6], [34, 21], 
    # [36, 66], [37, 56], [38, 0], [40, 6], [41, 15], [42, 1], [44, 0], [45, 0]]
    
    
    
    # *********************
    #@220215 commomn_plan_Sの check and remake
    # *********************
    # 1. temporary solutionとしてW0以前のSは、W0にすべて集計する。
    # 2. 欠番の週がある場合には、0で追加する。
    
    common_plan_SX = []
    element_SX = [0,0]
    
    
    # ***********************************************
    
    i = 0
    
    for element_S in common_plan_S:
    
        if element_S[0] <= i :
    
            element_SX[1] += element_S[1]
    
        else:
    
            break
    
    common_plan_SX.append(element_SX)
    
    # ***********************************************
    
    for i in range( 1,54 ):
    
        element_SX = [0,0]
    
        for element_S in common_plan_S:
        
            if element_S[0] < i :
    
                continue
    
            elif element_S[0] == i :
    
                element_SX[0] =  i
                element_SX[1] += element_S[1]
    
                common_plan_SX.append(element_SX)
    
                break
    
            else:
    
                element_SX[0] =  i
                element_SX[1] += 0
    
                common_plan_SX.append(element_SX)
    
                break
    
    # ***********************************************
    
    print(common_plan_SX)
    
    # ***********************************************
    # range(0,54)の54に対応できるようにcommon_plan_SXの長さ=54に補正する。
    # ***********************************************
    
    check_len = len(common_plan_SX)
    
    print(check_len)
    
    element_SX = [0,0]
    
    if check_len < 54 :
    
        for i in range(check_len,54):
    
            #print(i)
    
            element_SX[0] = i
            element_SX[1] = 0
    
            #print('before SX',element_SX,common_plan_SX)
    
            common_plan_SX.append(element_SX)
    
            #print('after  SX',element_SX,common_plan_SX)
    
            element_SX = [0,0]  #ココで明示的に0クリアしないと最後の値=53が入る
    
    #print(common_plan_SX)


    PSI_data_S = []
    PSI_data_S = common_plan_SX

    return PSI_data_S
    # **********************************
    # end of reading 'common_plan_unit.csv'
    # **********************************


# ******************************
# NOLEAFの場合　PSI_data_file読み込み 
# ******************************
def set_no_leaf_PSI_data(node):

# nodeはSCM tree のchild_nodeを指定

    PSI_data = [] #retuen用にリスト型を宣言

# nodeはSCM tree のchild_nodeを指定


# ******************************
# NOLEAFの時も、まずは、PSI_data_file読んでPSI_dataのリストを作っておく。
# ******************************
    PSI_data_file_name = ".\\node_all\\" + node + "\\PySI_data_std_IO.csv" 

    PSI_data_current = [] #retuen用にリスト型を宣言

    PSI_data_current = read_PSI_data_csv( PSI_data_file_name )

    #print('PSI_data@NOLEAF',PSI_data_current) 


# ******************************
# 次に、'common_plan_unit.csv'を読んでPSI_dataの'S'作る
# ******************************

#
# 共通計画単位common_plan_unit.csvは、nodeの上のディレクトリにある
#
    file_name = "common_plan_unit.csv" 

    PSI_data_S = [] #retuen用にリスト型を宣言

    PSI_data_S = read_common_plan_unit( file_name, node )

    #print('NOLEAF PSI_data_S@220630',PSI_data_S) 


# ******************************
# PSI_data_current[0][5:]    PSI_dataの'1S' のW0-W53に
# common_plan_unitのS        PSI_data_SのW0-W53     をセットする
# ******************************

    #print('PSI_data_S',PSI_data_S)

# image #
# PSI_data_S [[0, 20], [1, 6], [2, 6], [3, 3], [4, 1], [5, 1], [6, 1], [7, 3], [8, 3], [9, 3], [10, 1], [11, 1], [12, 10], [13, 6], [14, 6], [15, 6], [16, 0], [17, 21], [18, 21], [19, 15], [20, 10], [21, 10], [22, 10], [23, 6], [24, 6], [25, 28], [26, 28], [27, 28], [28, 28], [29, 55], [30, 0], [31, 55], [32, 55], [33, 10], [34, 10], [35, 6], [36, 6], [37, 6], [38, 28], [39, 28], [40, 28], [41, 21], [42, 0], [43, 0], [44, 0], [45, 0], [46, 0], [47, 0], [48, 0], [49, 0], [50, 0], [51, 0], [52, 0], [53, 0]]

    S_cpu_year = []

    for s in PSI_data_S :

        S_cpu_year.append( s[1] )
    
    PSI_data_current[0][5:] = S_cpu_year   #### W0,W1,W2,,,,W52,W53

    return PSI_data_current

# ************************************
# PSI_data image
# ************************************
#PSI_data [
#['TEST-PROD010', 'OD010', 'YTO', 'YTOLEAF', '1S', 0, 213, 213, 213, 213, 229, 236, 236, 236, 219, 213, 213, 213, 215, 220, 220, 220, 220, 213, 213, 213, 213, 217, 220, 220, 220, 218, 213, 213, 213, 213, 213, 213, 213, 213, 216, 220, 220, 220, 219, 213, 213, 213, 213, 218, 220, 220, 220, 217, 213, 213, 213, 213, 0], 
#['TEST-PROD010', 'OD010', 'YTO', 'YTOLEAF', '2CO', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ['TEST-PROD010', 'OD010', 'YTO', 'YTOLEAF', '3I', 0, 0, 237, 624, 771, 678, 779, 723, 847, 701, 752, 1079, 1046, 863, 678, 788, 808, 888, 698, 485, 692, 809, 686, 829, 939, 1049, 889, 701, 758, 755, 782, 569, 746, 533, 770, 557, 641, 781, 741, 521, 362, 1469, 1856, 2033, 1970, 1782, 1562, 1342, 1122, 905, 692, 509, 296, 83],
# ['TEST-PROD010', 'OD010', 'YTO', 'YTOLEAF', '4P', 0, 450, 600, 360, 120, 330, 180, 360, 90, 270, 540, 180, 30, 30, 330, 240, 300, 30, 0, 420, 330, 90, 360, 330, 330, 60, 30, 270, 210, 240, 0, 390, 0, 450, 0, 300, 360, 180, 0, 60, 1320, 600, 390, 150, 30, 0, 0, 0, 0, 0, 30, 0, 0, 0],
# ['TEST-PROD010', 'OD010', 'YTO', 'YTOLEAF', '5IP', 0, 0, 237, 624, 771, 678, 779, 723, 847, 701, 752, 1079, 1046, 863, 678, 788, 808, 888, 698, 485, 692, 809, 686, 829, 939, 1049, 889, 701, 758, 755, 782, 569, 746, 533, 770, 557, 641, 781, 741, 521, 362, 1469, 1856, 2033, 1970, 1782, 1562, 1342, 1122, 905, 692, 509, 296, 83]]




def input(node,isleaf):

    #print('monitor node is leaf',node,isleaf)

# ******************************
# profile読込み  
# ******************************
# reading "PySI_Profile_std.csv"
# setting planning parameters
#
# Plan_engine = "ML" or "FS" , cost marameters, planning one and so on
# ML:Machine Learning  FS:Fixed Sequence/Normal PSI

    profile_name = ".\\node_all\\"+node+"\\PySI_Profile_std.csv" 
    #プロファイル名を宣言

#    #file_path = ' .\\' + node+ '\\PySI_Profile_std.csv' ### nodeの下
#
#    dir_name  = node + '\\PySI_Profile_std.csv' ### nodeの下
#    file_path = os.path.join(os.path.dirname(__file__), dir_name)
#
#print('profile_name',profile_name)

    plan_prof = {} #辞書型を宣言

    plan_prof = read_plan_prof_csv( profile_name )


    # ******************************
    # PSI_data_file読み込み LEAF判定
    # ******************************

    PSI_data = [] #retuen用にリスト型を宣言

    if isleaf == "LEAF":

        PSI_data = set_leaf_PSI_data( node )

    elif isleaf == "NOLEAF":

        PSI_data = set_no_leaf_PSI_data( node )

    else:

        print('isleaf flag error: LEAF or NOLEAF should be defined')


# *******************************
# instanciate class PlanSpace 初期設定
# *******************************

    i_PlanSpace = PlanSpace( plan_prof, PSI_data )


# ******************************
# instanciate class LotSpace 初期設定
# ******************************

    i_LotSpace = LotSpace( 54 )


# ******************************
# instanciate class PlanEnv 初期設定
# ******************************

    plan_env = PlanEnv()


    return i_PlanSpace, i_LotSpace, plan_env






# ******************************
# Q_learning modules
# ******************************

def observe(next_action,  i_PlanSpace,i_LotSpace,plan_env,  month_no, calendar_act_weeks,episode):

    week_pos     = next_action
    week_no      = week_pos + 1
    week_no_year = month2year_week( month_no, week_no )

    calendar_inact_weeks = act_inact_convert( calendar_act_weeks )

    #### calendar_inact_weeks == i_PlanSpace.act_week_poss

    week4_month_list = [1,2,4,5,7,8,10,11]

# *****************************
# actionできない環境制約の判定 < LotSpaceの世界において >
# *****************************
# LotSpaceの世界では、off_week_listでplace_lotの可否を判定する。
# 判定action可能かどうか
# 環境制約からaction不可能であれば、位置を保持してnegative rewardを返す

# ******************************
# 制約を判定
# 1) 小の月の第5週目
# 2) 長期休暇週
# 3) ユーザー指定の稼働・非稼働週指定　船便の有無など
# ******************************

# action可能かどうか判定
# 環境制約からaction不可能であれば、状態位置を保持してnegative rewardをセット

# ******************************
# 1) 小の月の第5週目の判定
# ******************************
    if week_pos == 4 : #### next_action=week_pos=4 week_no=第5週の月の判定

        if month_no in week4_month_list:

        #@memo month2year_week( month_no, week_no=5 )の4週月

        # ******************************
        # update act_week_poss = seletable_action_list 
        # ******************************
            if week_pos in i_PlanSpace.act_week_poss:

                #act_week_possから年週week_no_year=月週week_pos=next_action外し
                i_PlanSpace.act_week_poss.remove( week_pos )

                monthly_episode_end_flag = False
                reward = -1000000
                #reward = -1

                return next_action, reward , monthly_episode_end_flag, i_PlanSpace.act_week_poss

            else:
            ### 小の月のカレンダー制約の判定後に、再度next_actionが入って来た

                monthly_episode_end_flag = False

                reward = -1000000
                #reward = -1

            # 既にremove済み
            ## act_week_possから年週week_no_year=月週week_pos=next_actionを外す
            #i_PlanSpace.act_week_poss.remove( week_pos )

                return next_action, reward , monthly_episode_end_flag, i_PlanSpace.act_week_poss


# ******************************
# 2) 長期休暇週の判定
# ******************************
    if week_no_year in i_PlanSpace.off_week_no_year_list:
    #week_pos     = next_action
    #week_no      = week_pos + 1
    #week_no_year = month2year_week( month_no, week_no )

        # ******************************
        # update act_week_poss = seletable_action_list 
        # ******************************
        if week_pos in i_PlanSpace.act_week_poss:

            # act_week_possから年週week_no_year=月週week_pos=next_actionを外す
            i_PlanSpace.act_week_poss.remove( week_pos )

            monthly_episode_end_flag = False
            reward = -1000000
            #reward = -1

            return next_action, reward , monthly_episode_end_flag, i_PlanSpace.act_week_poss

        else:
        ### 長期休暇のカレンダー制約の判定後に、再度next_actionが入って来た

            monthly_episode_end_flag = False

            reward = -1000000
            #reward = -1

            # 既にremove済み
            ## act_week_possから年週week_no_year=月週week_pos=next_actionを外す
            #i_PlanSpace.act_week_poss.remove( week_pos )

            return next_action, reward , monthly_episode_end_flag, i_PlanSpace.act_week_poss


# ******************************
# 3) ユーザー指定の稼働・非稼働週指定　船便の有無など
# ******************************
    elif week_pos in calendar_inact_weeks:

    #### MEMO
    #week_pos     = next_action
    #week_no      = week_pos + 1
    #week_no_year = month2year_week( month_no, week_no )

        # ******************************
        # update act_week_poss = seletable_action_list 
        # ******************************
        if week_pos in i_PlanSpace.act_week_poss:

            # act_week_possから年週week_no_year=月週week_pos=next_actionを外す
            i_PlanSpace.act_week_poss.remove( week_pos )

            monthly_episode_end_flag = False
            reward = -1000000
            #reward = -1

            return next_action, reward , monthly_episode_end_flag, i_PlanSpace.act_week_poss

        else:
            ### 物流カレンダー制約の判定後に、再度next_actionが入って来た

            monthly_episode_end_flag = False

            reward = -1000000
            #reward = -1


            # 既にremove済み
            ## act_week_possから年週week_no_year=月週week_pos=next_actionを外す
            #i_PlanSpace.act_week_poss.remove( week_pos )

            return next_action, reward , monthly_episode_end_flag, i_PlanSpace.act_week_poss


# ******************************
# ACTION(=place_lot)  UPDATE(=calc_plan)  EVALUATION(=eval_plan)
# ******************************

    else:

# ******************************
# 新規ロット番号の付番
# ******************************
        i_PlanSpace.lot_no += 1  #@ 新規ロット番号の付番


# ******************************
# 実行actin place_lot / 状態の更新update_state calc_plan_PSI / 評価eval_plan
# ******************************
        next_state, reward, monthly_episode_end_flag = plan_env.act_state_eval(next_action, month_no, i_PlanSpace, i_LotSpace, episode)

        return next_state, reward, monthly_episode_end_flag, i_PlanSpace.act_week_poss


# ******************************
# get_action 5つの週から選択する week_pos=[0,1,2,3,4] +1 week_no=[1,2,3,4,5]
# ******************************
def get_action(state, Qtable, act_week_poss, episode,i_PlanSpace):
#def get_action(state, Qtable, act_week_poss, episode):

    # e-greedy
    epsilon  = 0.2 

    #epsilon  = 0.5
    #epsilon  = 0.5 * (0.99 ** episode)  ### cartpoleのepsilon例


    #@220626 デバッグ用にエンジンを固定　& episode=3
    i_PlanSpace.plan_engine == "FS"


# ******************************
# plan_eigine="ML"を実行 確率epsilonでargmaxする。
# ******************************
    if i_PlanSpace.plan_engine == "ML":

        if  epsilon <= np.random.uniform(0, 1):
            ### exploit ###
            next_action = np.argmax(Qtable[state])

        else:  
            ### explore ###
            next_action = np.random.choice(act_week_poss) 

            ### 前処理の制約確認で選択可能な行動がact_week_possに入っている

            ### next_action = np.random.choice([0, 1, 2, 3, 4])
            ### 制約がなければ、5つの週を選択できる行動がact_week_possに入る


# ******************************
# plan_eigine="FS"を実行
# ******************************
    elif i_PlanSpace.plan_engine == "FS":

### ロットシーケンスlot_noを月内のaction可能数で割った余りで固定シーケンス発生
#
#w_mod = i_PlanSpace.lot_no % len(active_week) 
#
#next_action = active_week[w_mod]

        # ******************************
        # [0,1,2,3,4]の中にconstraint週が[1,4]ならselectableは[0,2,3]
        # ******************************
        next_action_list    = []
        next_action_list    = Qtable[state]

        ### act_week_poss # list of next_action
        selectable_pos_list = i_PlanSpace.act_week_poss 

        w_mod = i_PlanSpace.lot_no % len(selectable_pos_list) 

        next_action = selectable_pos_list[w_mod]

    else:
# ******************************
# plan_eigineを追加する場合はココでelifする
# ******************************
        print('No plan_engine definition')

    return next_action


# ******************************
# Qtableの更新
# ******************************
def update_Qtable(state, Qtable, next_state, reward, next_action):

# ******************************
# 新しい状態を判定してQtableに新規追加
# ******************************
    if next_state not in Qtable: #Q_tableにない状態を追加セット

        Qtable[next_state] = np.repeat(0.0, 5) ### action 0-4 = w1-w5

    cur_state = state

    state = next_state

# ******************************
# Q_table update
# ******************************
    alpha = 0.1   
    #alpha = 0.2  
    #alpha = 0.5  

    gamma = 0.99

    Qtable[cur_state][next_action]=(1-alpha)*Qtable[cur_state][next_action]+\
              alpha * (reward + gamma * max(Qtable[next_state]))

    return state, Qtable


# ******************************
# main process
# ******************************
def main_process(i_PlanSpace, i_LotSpace, plan_env):

#if __name__ == '__main__':




    # ******************************
    # episode_no for Machine Learning
    # ******************************
    
    #episode_no = 10 ####必ず10回以上回す output maxが10回目以降のmaxを拾う
    
    #@220626
    episode_no = 3
    #episode_no = 20
    
    #episode_no = 50
    
    #episode_no = 100
    
    
    # ******************************
    # ML initianise and Q_learning modules
    # ******************************
    
    state = 0      #stateは (x,y) = x + 54 * y の数値で座標を定義
    
    prev_state  = 0 
    work_state  = 0 
    
    # ******************************
    #
    # stateは計画状態
    # place_lot時に、計画状態と一対一のposition=(x,y)を生成
    # position=(x,y)=(week_no_year,lot_step_no)をstateとして取り扱う
    #
    # 3月の第5週は、年間の第13週目、pos=(13,0)
    # week_no_year   = 13
    # lot_step_no    = 0     # ロットを1つ積み上げた数
    
    # (x,y)座標は1つの数字に相互変換する
    #   x=week_no_year  y=lot_step
    #   num = x + 54 * y
    #
    # ******************************
    # x軸 : 0<=x<=54週 week_no_year 年週: 年間を通した週
    #
    #       年週と別に、月内の週week_no=[W1,W2,W3,W4,W5]がある
    #
    #       Qlearningでの取り扱いは、0スタートのweek_pos=[0,1,2,3,4]とする
    #
    #       get_actionは、week_pos=[0,1,2,3,4]から一つの行動を選択すること
    #
    #
    # ******************************
    #
    # actionはplace_lotすることで、get_actionした週にロットを積み上げる
    # get_actionでx軸を選択したら、actionしてy軸を生成して、pos(x,y)が決まる
    #
    # ******************************
    # y軸 : lot_step_no 選択したx軸週にロットを積み上げた数
    #
    # 内部の処理上はlist.append(a_lot)したリストの要素数len(list.append(a_lot))
    #
    # ******************************
    
    
    prev_reward = 0 
    prev_profit = 0 
    
    profit_accum_prev_week = 0
    profit_accum_curr_week = 0
    
    Qtable = {}
    Qtable[state] = np.repeat(0.0, 5)  # actions=0-4 week=1-5
    
    lot_space_Y_LOG    = {}
    lot_space_Y_LOG[0] = []
    
    



    plan_reward = []    # reward logging

    monthly_episode_end_flag = False  # エージェントがゴールしてるかどうか？


    for episode in range(episode_no):

        #print('START episode = ',episode)

        episode_reward = []   #  報酬log


# ******************************
# 次のepisodeスタート前にPSI_dataとlot_countsを0クリアする
# ******************************

        # 需要Sの入力データを保持する。需要はゼロクリアしない
        # i_PlanSpace.S_year

        i_PlanSpace.CO_year    = [ 0 for i in range(54)]
        i_PlanSpace.I_year     = [ 0 for i in range(54)]
        i_PlanSpace.P_year     = [ 0 for i in range(54)]
        i_PlanSpace.IP_year    = [ 0 for i in range(54)]

        i_PlanSpace.lot_counts = [ 0 for i in range(54)]


# ******************************
# Q学習は月次で12回の処理を実施する
# ******************************
        for month_no in range(1,13): #LOOP 12ヶ月分

            #print('episode_no and month_no = ', episode, month_no )

            WEEK_NO = 5

            i_LotSpace.init_lot_space_M( WEEK_NO )
            #i_LotSpace.init_lot_space_M( 5 )


# ******************************
#   月のS==0で、i_PlanSpace.S445_month[month_no] == 0の時、月の処理をスキップ
# ******************************

            if i_PlanSpace.S445_month[month_no] == 0 :

                continue

# lot_place処理のためのget_actionをend_flagまで繰り返す。
# もし、月内にactive_weekがなければ、end_flag=Trueを返す。

            #辞書型で、{month_no,[week_list,,,]}のデータを持たせる
            calendar_week_dic = {} # active_week_dicの辞書型の宣言

            calendar_week_list = i_PlanSpace.calendar_cycle_week_list

#calendar_week_list = [1,3,5,7,9,11,14,16,17,20,22,24,27,29,31,33,35,37,40,42,44,46,48,50]

            calendar_week_dic = make_active_week_dic(calendar_week_list)

#an image
#calendar_week_dic {1: [1, 2, 3, 4], 2: [1, 2, 3, 4], 3: [1, 2, 3, 4, 5], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4], 6: [1, 2, 3, 4, 5], 7: [1, 2, 3, 4], 8: [1, 2, 3, 4], 9: [1, 2, 3, 4, 5], 10: [1, 2, 3, 4], 11: [1, 2, 3, 4], 12: [1, 2, 3, 4, 5]}

            calendar_act_week = []
            calendar_act_week = calendar_week_dic[month_no]

# カレンダー制約、1)小の月、2)長期休暇off週制約、3)船便物流制約を見て、
# active_weekSを生成する

# 制約共通のactive_weekS=[0,1,2,3,4]を定義する。
# 月内のplanningのconstraint checkでactive_weekS=[]となったらend_flag == True

            act_week_poss             = [0,1,2,3,4] ###初期化 local
            i_PlanSpace.act_week_poss = [0,1,2,3,4] ###初期化 i_PlanSpaceの中


            while not(monthly_episode_end_flag == True):    

            # 終了判定の基本は、 accume_P >= accume_Sで終了を判定する
            #
            # 変化形として、
            # 1) 安全在庫日数 safty_stock_daysを上乗せして終了判定するケース
            #
            #    accume_P >= accume_S + SS_days
            #
            # 2) accume_Profitが減少し始めた時に終了判定するケース
            #
            #    accume_Profit_current < accume_Profit_previous

                # ******************************
                # get_action
                # ******************************
                next_action = get_action(state, Qtable, act_week_poss, episode,i_PlanSpace) 
                #next_action= get_action(state, Qtable, act_week_poss, episode)
# memo
# 機能拡張の案 get_actionには事前にpre_observeして評価する案が考えられる
# 例えば、
# 1. place_back_lotして状態を戻す。
# 2. PlanSpaceのcopy退避で状態を戻す。
# 3. check_action_constraint後、lot_countsを仮更新してEvalPalnSIPする

                # ******************************
                # monitor before_observe
                # ******************************
                pac = sum(i_PlanSpace.Profit[1:])
                #profit_accum_curr = sum(i_PlanSpace.Profit[1:])


                # ******************************
                # observe    check_action_constraint/action/update_state/eval
                # ******************************
                next_state, reward, monthly_episode_end_flag, act_week_poss = observe(next_action,  i_PlanSpace,i_LotSpace,plan_env,  month_no, calendar_act_week,episode) 


                # ******************************
                # monitor after_observe
                # ******************************
                pap = sum(i_PlanSpace.Profit[1:])
                #profit_accum_prev = sum(i_PlanSpace.Profit[1:])


                # ******************************
                # "PROFIT"の終了判定
                # ******************************
                if i_PlanSpace.reward_sw == "PROFIT":

                    if month_no >= 4: # 立ち上がりの3か月はそのまま

                        profit_deviation = ( pac - pap ) / pap

                        #print('profit_deviation',profit_deviation)


                # ******************************
                # 利益累計の変化を見てend conditionを設定する点に注目
                # ******************************
                        if profit_deviation <= 0:  #利益の変化率が0%以下

                        #if profit_deviation <= - 0.01:  #利益の変化率が-1%以下
                        #if (pac - pap) / pap <= - 0.03: #利益の変化率が-3%以下

                            monthly_episode_end_flag = True


                # ******************************
                # Q学習の処理　stateとrewardの変化からQ-Tableを管理
                # ******************************
                state, Qtable = update_Qtable(state,Qtable,next_state,reward,next_action) 

                episode_reward.append(reward)

                # M month
                #show_lot_space_M(i_LotSpace.lot_space_M)

                # Y year
                #show_lot_space_Y(i_LotSpace.lot_space_Y)

                # 制約loopから抜ける
                # ******************************
                # Q学習後、すべての制約を通過した結果act_week_poss== []なら終了
                # ******************************
                if act_week_poss == []: # 選択できるactive week positionsがない

                    monthly_episode_end_flag = true

            # ******************************
            # 月次終了のこの位置で、月次の操作域lot_space_Mを初期化
            # ******************************

            i_LotSpace.lot_space_M = [[] for j in range(5)] 

            monthly_episode_end_flag = False

            i_PlanSpace.lot_no = 0  ### クラス中の変数とする


        # ******************************
        # 年次終了の前に show_lot_space_Yを見たい時に使用
        # ******************************
        # print('episode NO',episode)
        # show_lot_space_Y(i_LotSpace.lot_space_Y)


        # ******************************
        # 年次終了の前に episode_noとshow_lot_space_YのLOG
        # ******************************
        lot_space_Y_LOG[episode] = i_LotSpace.lot_space_Y


# ******************************
# 次のepisodeスタート前にlot_space_Yを0クリアする
# ******************************
        i_LotSpace.lot_space_Y = [[] for j in range(53)]

        #print('lot_space_Yを0クリア')
        #show_lot_space_Y(i_LotSpace.lot_space_Y)


        # ******************************
        # episode reward log
        # ******************************
        plan_reward.append(np.sum(episode_reward))


        #@220625 Qtableの重みは保持して、学習し続ける???
        # ******************************
        # 年次終了のこの位置で、Q学習の初期化 
        # ******************************
        state = plan_env.reset(i_LotSpace)           # init state

        state = 0             #stateは (x,y) = x + 54 * y の数値で座標を定義

        update_Qtable(state,Qtable,next_state,reward,next_action) 

        monthly_episode_end_flag = False


# ******************************
# pickup TOP reward plan    lot_space_Y[top_reward]
# ******************************

# ******************************
# episode毎にloggingした計画結果から、episode10回目以降でreward maxを取り出す
# ******************************

    max_value = max(plan_reward[1:]) ### episode2回目以降
    #max_value = max(plan_reward[9:]) ### episode10回目以降

    #print('plan_reward',plan_reward)
    #print('plan_reward[9:]',plan_reward[9:])
    #print('max_value',max_value)

    max_index = plan_reward.index(max_value)

    #print('max value and index',max_value,max_index)

    fin_lot_space_Y = lot_space_Y_LOG[max_index]

    #show_lot_space_Y(fin_lot_space_Y)

#@220625 SCMTREEのバッチ処理なのでepisodeの描画はSTOP
## ******************************
## episode & reward log plot
## ******************************
#
#    # 結果のプロット
#    plt.plot(np.arange(episode_no), plan_reward)
#    plt.xlabel("episode")
#    plt.ylabel("reward")
#    plt.savefig("plan_value.jpg")
#    plt.show()




    return fin_lot_space_Y


def output(node,  i_PlanSpace,i_LotSpace,  fin_lot_space_Y):

# ******************************
# write_PSI_data2csv 
# ******************************

    print('')
    print('node@output',node)
    print('node@output',node)
    print('node@output',node)
    print('')


    PSI_data_file_name = ".\\node_all\\" + node + "\\PySI_data_std_IO.csv" 

    #PSI_data_file_name = '.\\'+ node+ '\\'+ 'PySI_data_std_IO.csv'

    #file_name = 'PySI_data_std_IO.csv'         ### .\dataより開きやすい
    #file_name = '.\data\PySI_data_std_IO.csv' 

    print('PSI_data_file_name@output',PSI_data_file_name)
    print('PSI_data_file_name@output',PSI_data_file_name)
    print('PSI_data_file_name@output',PSI_data_file_name)


    write_PSI_data2csv( i_PlanSpace, PSI_data_file_name )


#766l[@@220625 ここの位置でOK
# *********909o1i*********************
# csv write common_plan_unit.csv 共通計画単位による入出力
# ******************************
# 将来的にSCM treeでサプライチェーン拠点間の需要を連携する時に使用する

    csv_write2common_plan_unit(i_LotSpace,i_PlanSpace, fin_lot_space_Y)



def PySI(node,isleaf):

    #print('isleaf node', isleaf, node)

    #LEAFの時、leaf_nodeを処理
    i_PlanSpace, i_LotSpace, plan_env = input(node,isleaf)

    fin_lot_space_Y = main_process(i_PlanSpace, i_LotSpace, plan_env)

    output(node,  i_PlanSpace,i_LotSpace,  fin_lot_space_Y)




# ********************************************************
# csv_write2common_plan_header 共通計画単位のヘッダー書き出し
# ********************************************************
def csv_write2common_plan_header(): 


    l = []
    r = []

    #seq_no, control_flag , priority_no, modal, LT , from_x , from_Wxx , step_xx , to_y , to_Wyy , step_yy 

    # ********* ヘッダーのみ先に書き出す 各PSI計画の出力の前に
    r = ['seq_no','control_flag','priority_no','modal','LT','Dpt_entity','Dpt_week','Dpt_step','Arv_entity','Arv_week','Arv_step']


    # lot_noで出力するcsv file nameを作成
    csv_file_name = "common_plan_unit.csv"

    l.append(r)



# ****************************************
# CSV ファイル書き出し
# ****************************************

    #print('l',l)

    with open( csv_file_name , 'w', newline="") as f:

        writer = csv.writer(f)
        writer.writerows(l)

#### csv_write2common_plan_header ####




if __name__ == '__main__':


# ******************************
# csv_write2common_plan_header　計画共通単位のヘッダー初期設定

# ******************************

    csv_write2common_plan_header()




# ***********************************
# is_leaf node
# ***********************************

    for node in node_name:  #### SCM tree nodes are postordering 

        if is_leaf(node):

            print('leaf node',node)
            print('leaf node',node)
            print('leaf node',node)

            PySI(node, 'LEAF')

        else:              #### root node処理が必要な場合はelif is_root分岐

            print('mid or root node',node)
            print('mid or root node',node)
            print('mid or root node',node)

            PySI(node, 'NOLEAF')



    print('end of process')


# ******************************
# end of main process
# ******************************
