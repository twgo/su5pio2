from 臺灣言語服務.models import 訓練過渡格式
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.公用變數 import 無音


def main():
    for tsua in (
        訓練過渡格式.objects.filter(文本__isnull=False).order_by('id')
    ):
        句物件 = 拆文分析器.分詞句物件(tsua.文本)
        for 字物件 in 句物件.篩出字物件():
            if 字物件.音 != 無音:
                字物件.型 = 字物件.音
                字物件.音 = 無音
        tsua.文本 = 句物件.看分詞()
        tsua.save()


main()
