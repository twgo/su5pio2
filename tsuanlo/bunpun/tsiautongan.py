from 臺灣言語服務.models import 訓練過渡格式
from os.path import join
import re
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.公用變數 import 無音
from 臺灣言語工具.音標系統.台語 import 新白話字
from os import makedirs


def tsuliau():
    makedirs('tsiau')
    for laiguan in (
        訓練過渡格式.objects.values_list('來源', flat=True).distinct()
    ):
        with open(join('tsiau', laiguan), 'w') as tong:
            for tsua in (
                訓練過渡格式.objects
                .filter(來源=laiguan, 文本__isnull=False).order_by('id')
            ):
                句物件 = 拆文分析器.分詞句物件(tsua.文本)
                for 字物件 in 句物件.篩出字物件():
                    if 字物件.音 != 無音:
                        字物件.型 = 字物件.音
                        字物件.音 = 無音
                lo = 句物件.轉音(新白話字).看分詞()
                if not re.search('[a-z]', lo):
                    if lo:
                        print(tsua.來源, tsua.文本)
                else:
                    print(lo, file=tong)


tsuliau()
