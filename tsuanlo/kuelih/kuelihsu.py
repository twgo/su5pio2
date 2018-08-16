
from pyexcel_ods import get_data
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


def main():
    data = get_data("音節比較表.ods")['imtsiat']

    aisiu = set()
    for tsua in data[1:]:
        try:
            if tsua[1] or tsua[3] == 'y':
                aisiu.add(tsua[0])
        except IndexError:
            pass

    with open('aisiu.txt', 'w') as ai:
        print('\n'.join(sorted(aisiu)), file=ai)

    with open('tsuanpoosu_aisiu.txt', 'w') as ai:
        with open('tsuanpoosu.txt') as f:
            for su in f.readlines():
                for ji in 拆文分析器.建立句物件(su.rstrip()).篩出字物件():
                    if ji.型.rstrip('0123456789') not in aisiu:
                        break
                else:
                    print(su.rstrip(), file=ai)


main()
