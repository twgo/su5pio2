def a():
    import csv
    from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器

    def _main():
        with open('docker.csv',  encoding='utf-8') as 詞表檔:
            詞表 = set()
            for ho, 資料 in enumerate(csv.reader(詞表檔)):
                if ho != 0:
                    詞表.add((資料[0], 資料[1]))
            for han, lo in 詞表:
                for 字物件 in 拆文分析器.建立句物件(han, lo):
                    key = 字物件.看型(), 字物件.看音()
                    if key not in 詞表:
                        print(key)
    _main()


a()
