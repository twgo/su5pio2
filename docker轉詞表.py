import csv
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.台語 import 新白話字
from 臺灣言語服務.models import 訓練過渡格式
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def _main():
    with open('docker.csv', 'wt', encoding='utf-8') as 詞表檔:
        詞表 = csv.writer(詞表檔)
        詞表.writerow(['漢字', '羅馬字', '來源', '會用得無', ])
        for 資料 in sorted(_全部資料()):
            詞表.writerow(資料)


def _全部資料():
    全部資料 = {}
    for tsua in (
        訓練過渡格式.objects.filter(文本__isnull=False).order_by('id')
    ):
        句物件 = 拆文分析器.分詞句物件(tsua.文本).轉音(新白話字)
        for su in 句物件.網出詞物件():
            if su.敢是標點符號():
                continue
            if not su.音標敢著(臺灣閩南語羅馬字拼音):
                continue
            ui = (su.看型(), su.看音())
            if su.看音() != '' and ui not in 全部資料:
                全部資料[ui] = tsua.來源, 句物件.看型(), 句物件.看音().lstrip('1')
    for (han, lo), (guan, lehan, lelo) in 全部資料.items():
        yield han, lo, guan, lehan, lelo


_main()
