import csv
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.羅馬字仕上げ import 羅馬字仕上げ


def _main(詞目總檔所在):
    詞 = set()
    with open(詞目總檔所在, 'rt', encoding='utf-8') as 檔:
        for tsua in 檔.readlines():
            for 詞分詞 in tsua.rstrip().split():
                詞.add(詞分詞)
    資料集合 = set()
    for 詞分詞 in sorted(詞):
        try:
            詞物件 = 拆文分析器.分詞詞物件(詞分詞).轉音(臺灣閩南語羅馬字拼音)
            漢字 = 詞物件.看型()
            羅馬字 = 羅馬字仕上げ.輕聲佮外來語(詞物件.轉音(臺灣閩南語羅馬字拼音, '轉調符').看音())
            資料集合.add((漢字, 羅馬字, 詞物件.看音()))
        except Exception as 錯誤:
            print('詞分詞', 詞分詞, 錯誤)

    with open('su5pio2.txt.csv', 'wt', encoding='utf-8') as 詞表檔:
        詞表 = csv.writer(詞表檔)
        詞表.writerow(['漢字', '羅馬字', '來源', '會用得無', ])
        for 資料 in sorted(資料集合):
            詞表.writerow((資料[0], 資料[1], '', '', 資料[2]))


if __name__ == '__main__':
    _main('語言模型.txt')
