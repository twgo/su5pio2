from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


def a():
    import csv
    from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器

    def _main():
        bosiu = {}
        with open('docker.csv',  encoding='utf-8') as 詞表檔:
            詞表 = {}
            for ho, 資料 in enumerate(csv.reader(詞表檔)):
                if ho != 0 and 資料[2].startswith('教典'):
                    詞表[(資料[0], 資料[1])] = tuple(資料[2:])
        for (han, lo), tshun in 詞表.items():
            try:
                for 字物件 in 拆文分析器.建立句物件(han, lo).篩出字物件():
                    if not 字物件.敢是標點符號():
                        key = 字物件.看型(), 字物件.看音()
                        if key not in 詞表:
                            bosiu[key] = tshun
            except 解析錯誤:
                pass
        for bo, tshun in sorted(bosiu.items()):
            print(bo + tshun)
    _main()


a()
