import csv
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def _main(詞目總檔所在):
    詞 = set()
    with open(詞目總檔所在, 'rt', encoding='utf-8') as 檔:
        for tsua in 檔.readlines():
            for 詞物件 in 拆文分析器.分詞句物件(tsua.rstrip()).轉音(臺灣閩南語羅馬字拼音).網出詞物件():
                詞.add(詞物件)

    with open('su5pio2.txt.csv', 'wt', encoding='utf-8') as 詞表檔:
        詞表 = csv.writer(詞表檔)
        for 詞物件 in sorted(詞):
            漢字 = 詞物件.看型()
            羅馬字 = 詞物件.轉音(臺灣閩南語羅馬字拼音, '轉調符').看音()
            詞表.writerow([漢字, 羅馬字, 詞物件.看音()])
            print(漢字, 羅馬字, 詞物件.看音())


if __name__ == '__main__':
    _main('語言模型.txt')
