from 臺灣言語服務.models import 訓練過渡格式
import re
list(訓練過渡格式.objects.values_list('來源').distinct())
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.音標系統.台語 import 新白話字


def tsuliau():
    for tsua in (
        訓練過渡格式.objects
        .exclude(來源__in=[
            'TGB通訊',
            'twisas-trs',
            '台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計-HL',
        ])
        .filter(文本__isnull=False).order_by('id')
    ):
        句物件 = 拆文分析器.分詞句物件(tsua.文本)
        for 字物件 in 句物件.篩出字物件():
            if 字物件.音 != 無音:
                字物件.型 = 字物件.音
                字物件.音 = 無音
        lo = 句物件.轉音(新白話字).看分詞()
        if not re.search('[a-z]', lo):
            print(tsua.來源, tsua.文本)
        yield lo


def ku():
    tsuanpooku = []
    for 句物件 in tsuliau():
        tsuanpooku.append(句物件)
    with open('tsuanpooku.txt', 'w') as tong:
        print('\n'.join(tsuanpooku), file=tong)


ku()
