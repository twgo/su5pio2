from 臺灣言語服務.models import 訓練過渡格式
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.公用變數 import 無音
from builtins import set
import json
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.音標系統.台語 import 新白話字


def tsuliau():
    for tsua in (
        訓練過渡格式.objects.filter(文本__isnull=False).order_by('id')
    ):
        句物件 = 拆文分析器.分詞句物件(tsua.文本)
        for 字物件 in 句物件.篩出字物件():
            if 字物件.音 != 無音:
                字物件.型 = 字物件.音
                字物件.音 = 無音
        yield 句物件.轉音(新白話字)


def main():
    imchiat = 0
    su = 0
    tsuanpooji = set()
    tsuanpoojitiau = set()
    tsuanpoosu = set()
    tsuanpooku = []
    for 句物件 in tsuliau():
        imchiat += len(句物件.篩出字物件())
        su += len(句物件.網出詞物件())
        for 字物件 in 句物件.篩出字物件():
            if 臺灣閩南語羅馬字拼音(字物件.型).音標 is not None:
                tsuanpooji.add(字物件.看分詞())
                tsuanpoojitiau.add(字物件.看分詞())
        for 詞物件 in 句物件.網出詞物件():
            if not 詞物件.敢是標點符號():
                tsuanpoosu.add(詞物件.看分詞())
        tsuanpooku.append(句物件.看分詞())
    with open('tsonghong.json', 'w') as tong:
        json.dump(
            {
                '總音節數（無算標點）': imchiat,
                '總詞數（無算標點）': su,
                '總句數': len(tsuanpooku),
                '詞種類（無算標點）': imchiat,
                '音節加調種類': len(tsuanpoojitiau),
                '音節無調種類': len(tsuanpooji),
            },
            tong, ensure_ascii=False, sort_keys=False, indent=2
        )
    with open('tsuanpooku.txt', 'w') as tong:
        print('\n'.join(tsuanpooku), file=tong)
    with open('tsuanpoojitiau.txt', 'w') as tong:
        print('\n'.join(tsuanpoojitiau), file=tong)
    with open('tsuanpooji.txt', 'w') as tong:
        print('\n'.join(tsuanpooji), file=tong)


main()
