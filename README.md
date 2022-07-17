# PySI_V0R2SC_main_P
PySi is , Inventory Planning and financial analyse for Global Supply Chain 

# ******************************
# インストール時の注意点
# ******************************
【インストール時の注意点】
1. 導入時には、ディレクトリnode_allのzipファイルを解凍してください。


# ******************************
# 各処理の詳細、入力・出力ファイルについて
# ******************************
各処理の詳細、入力・出力ファイルについては、
別資料「PySI 主要処理プロセス　一覧.pdf」を参照。


# ******************************
# パッケージ PySI_V0R2SC_ini_P　サプライチェーン用の初期環境の生成方法
# ******************************
【初期処理】

1. PySI_create_node_dir_copy_prof.pyを起動すると
   PySIのSCMTREE用の初期環境を生成する。

注)すべてのnodeディレクトリーを初期設定するので、要注意。
   稼働している環境ではなく、新しいディレクトリを作成して初期化するのが望ましい


   1-1. 各事業拠点のnode名のディレクトリをmkdirで作成する。

   1-2. PSIの3つのァイルをcopyする。
   ディレクトリ.\\data下の3入出力フファイルを\node_all下の各\node下にcopyする
   PySI_data_std_IO.csv
   PySI_Profile_std.csv
   PySI_monitor.xlsx

   1-3. 各事業拠点のnode毎に定義されたPSI計画パラメータprofileのサマリー表
        "SCMTREE_profile010.csv"を読み込んで、
        \node_allの下の各profileにcopyする
   


# ******************************
# パッケージ PySI_V0R2SC_main_P　最終消費地の需要データ生成とmainの起動方法
# ******************************
【最終需要地(=LEAF NODE)の需要Sを生成する】

1. PySI_make_S_month2week.pyを起動する
   最終需要地(=LEAF NODE)の月別需要S monthを週別需要S weekに変換する


2. PySI_set_Leaf_Node_week_S2PSI.pyを起動する
   最終需要地(=LEAF NODE)の週別需要S weekを
   各node下のPySI_data_std_IO.csvのSにcopyする

   注) PySI_data_std_IO.csvの中のnode_from とnode_toは、
       この処理中にprofileで定義されたnode名に更新される


【サプライチェーンのPSI計画連携】

1. PySI_main_SCMTREE_060_episode3_GC.pyを起動する
   サプライチェーンの最終需要からマザープラントまでPSI計画を連携する

   注) PySI_data_std_IO.csvの中のnode_from とnode_toは、
       この処理中にprofileで定義されたnode名に更新される

   \node_all下の各\node下の"PySI_data_std_IO.csv"がPSI計画として更新される。


【PSI計画のグラフ表示 excel】

1. \node_all下の各\node下の下記の3ファイルをexcelで開くと、
   PySI_monitor.xlsxにPSIグラフが表示される。

   PySI_data_std_IO.csv
   PySI_Profile_std.csv
   PySI_monitor.xlsx


【PSI計画パラメータの一括更新とPSI計画連携の起動方法】

1. PSI計画パラメータの一括更新用の一覧表"SCMTREE_profile010.csv"を使って、
   各nodeのPSI計画パラメータをセットする

2. PySI_update_node_all_profile010.pyを起動すると、
   各node下のPSI計画パラメータが一括更新される

3. PySI_main_SCMTREE_060_episode3_GC.pyを起動する
   サプライチェーンの最終需要からマザープラントまでPSI計画が連携処理される

以上、end of readme.txt

