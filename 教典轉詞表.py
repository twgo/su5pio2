from csv import DictReader
import csv
import io
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def _main(詞目總檔所在):
    with open('su5pio2.csv', 'wt', encoding='utf-8') as 詞表檔:
        詞表 = csv.writer(詞表檔)
        with open(詞目總檔所在, 'rt', encoding='utf-8') as 檔:
            with io.StringIO(檔.read()) as 資料:
                for row in DictReader(資料):
                    主編碼 = int(row['主編碼'].strip())
                    音讀 = row['音讀'].strip()
                    漢字 = row['詞目'].strip()
                    結果 = []
                    for 一詞 in 音讀.split('/'):
                        結果.append(
                            拆文分析器.建立句物件(一詞).轉音(臺灣閩南語羅馬字拼音)
                            .看型('-', ' ')
                        )
                    if 主編碼 < 60000:
                        詞表.writerow([漢字, 音讀, *結果])
                        print(漢字, 音讀, *結果)


if __name__ == '__main__':
    _main('/Users/fafoy/git/moedict-data-twblg/uni/詞目總檔.csv')
