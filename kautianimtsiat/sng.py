
import csv
import json
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.台語 import 新白話字
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音通行韻母表


def _main():
    tsuanpooji = set()
    tsuanpoojitiau = set()
    for 字物件 in csvtsuliau():
        tailo = 新白話字(字物件.型)
        if (
            tailo.音標 is not None and
            tailo.韻 in 臺灣閩南語羅馬字拼音通行韻母表
        ):
            tsuanpooji.add(字物件.看分詞().strip('0123456789'))
            tsuanpoojitiau.add(字物件.看分詞().lstrip('01'))
    with open('tsonghong.json', 'w') as tong:
        json.dump(
            {
                '音節加調種類': len(tsuanpoojitiau),
                '音節無調種類': len(tsuanpooji),
            },
            tong, ensure_ascii=False, sort_keys=False, indent=2
        )
    with open('tsuanpoojitiau.txt', 'w') as tong:
        print('\n'.join(sorted(tsuanpoojitiau)), file=tong)
    with open('tsuanpooji.txt', 'w') as tong:
        print('\n'.join(sorted(tsuanpooji)), file=tong)


def csvtsuliau():
    with open('docker.csv',  encoding='utf-8') as 詞表檔:
        for ho, 資料 in enumerate(csv.reader(詞表檔)):
            if ho != 0:
                yield from 拆文分析器.建立句物件(資料[1]).篩出字物件()


_main()
