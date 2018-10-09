from 臺灣言語服務.models import 訓練過渡格式
from os.path import join
import re
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.音標系統.台語 import 新白話字
from os import makedirs
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def tsuliau():
    makedirs('tsiau-bopiautiam')
    for laiguan in (
        訓練過渡格式.objects.values_list('來源', flat=True).distinct()
    ):
        with open(join('tsiau', laiguan), 'r') as tong:
            with open(join('tsiau-bopiautiam', laiguan), 'w') as bopiau:
                for tsua in (
                    tong.readlines()
                ):
                    句物件 = 拆文分析器.建立句物件(tsua.rstrip())
                    lau = []
                    for 詞物件 in 句物件.網出詞物件():
                        tioh = True
                        for 字物件 in 詞物件.篩出字物件():
                            if 臺灣閩南語羅馬字拼音(字物件.型).音標 is None:
                                tioh = False
                        if tioh:
                            lau.append(詞物件.看分詞())
                    print(' '.join(lau), file=bopiau)


tsuliau()
