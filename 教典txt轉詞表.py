from csv import DictReader
import csv
import io
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from txt轉詞表 import txt資料


def _main():
    with open('kautian_kah_giliau.csv', 'wt', encoding='utf-8') as 詞表檔:
        詞表 = csv.writer(詞表檔)
        詞表.writerow(['漢字', '羅馬字', '來源', '會用得無', ])
        for 資料 in sorted(_全部資料()):
            詞表.writerow(資料)


def _全部資料():
    教典 = set(_教典資料('../moedict-data-twblg/uni/詞目總檔.csv'))
    教典有收 = set()
    for 漢, 羅, *_ in 教典:
        for 羅it in 羅.split('/'):
            教典有收.add((漢, 羅it))
    for txt in txt資料('語言模型.txt'):
        漢, 羅, *_ = txt
        if (漢, 羅) not in 教典有收:
            教典.add(txt)
    return 教典


def _教典資料(詞目總檔所在):
    with open(詞目總檔所在, 'rt', encoding='utf-8') as 檔:
        with io.StringIO(檔.read()) as 資料:
            for row in DictReader(資料):
                主編碼 = int(row['主編碼'].strip())
                音讀 = row['音讀'].strip()
                漢字 = row['詞目'].strip()
                結果 = []
                for 一詞 in 音讀.split('/'):
                    一个唸法 = (
                        拆文分析器.建立句物件(一詞).轉音(臺灣閩南語羅馬字拼音)
                        .看型('-', ' ')
                    )
                    if '-1' not in 一个唸法:
                        結果.append(一个唸法)
                if 主編碼 < 60000:
                    yield (漢字, 音讀, '教典', '1', *結果)


if __name__ == '__main__':
    _main()
