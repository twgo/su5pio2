from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from builtins import set
import json
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def su():
    imchiat = 0
    su = 0
    tsuanpooji = set()
    tsuanpoojitiau = set()
    tsuanpoosu = set()
    for liong, 句物件 in enumerate(tsuliau()):
        imchiat += len(句物件.篩出字物件())
        su += len(句物件.網出詞物件())
        for 詞物件 in 句物件.網出詞物件():
            if not 詞物件.敢是標點符號():
                tshingkhi = True
                for 字物件 in 詞物件.篩出字物件():
                    if 臺灣閩南語羅馬字拼音(字物件.型).音標 is not None:
                        tsuanpooji.add(字物件.看分詞().strip('0123456789'))
                        tsuanpoojitiau.add(字物件.看分詞())
                    else:
                        tshingkhi = False
                if tshingkhi:
                    tsuanpoosu.add(詞物件.看分詞())
    with open('tsonghong.json', 'w') as tong:
        json.dump(
            {
                '總音節數（無算標點）': imchiat,
                '總詞數（無算標點）': su,
                '資料總數（詞、句、段）': liong,
                '詞種類（無算標點）': len(tsuanpoosu),
                '音節加調種類': len(tsuanpoojitiau),
                '音節無調種類': len(tsuanpooji),
            },
            tong, ensure_ascii=False, sort_keys=False, indent=2
        )
    with open('tsuanpoojitiau.txt', 'w') as tong:
        print('\n'.join(tsuanpoojitiau), file=tong)
    with open('tsuanpooji.txt', 'w') as tong:
        print('\n'.join(tsuanpooji), file=tong)
    with open('tsuanpoosu.txt', 'w') as tong:
        print('\n'.join(tsuanpoosu), file=tong)


def tsuliau():
    with open('tsuanpooku.txt') as tong:
        for tsua in tong.readlines():
            if tsua[-1] == '\n':
                tsua = tsua[:-1]
            yield 拆文分析器.分詞句物件(tsua)


su()
