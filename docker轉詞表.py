def a():
    import csv
    from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
    from 臺灣言語工具.音標系統.台語 import 新白話字
    from 臺灣言語服務.models import 訓練過渡格式

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
            for su in 拆文分析器.分詞句物件(tsua.文本).轉音(新白話字).網出詞物件():
                ui = (su.看型(), su.看音())
                if su.看音() != '' and ui not in 全部資料:
                    全部資料[ui] = tsua.來源
        for (han, lo), guan in 全部資料.items():
            yield han, lo, guan

    _main()


a()
