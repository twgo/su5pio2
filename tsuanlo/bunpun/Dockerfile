FROM twgo/su5pio2

RUN pip3 install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/archive/master.zip
RUN pip3 install --upgrade https://github.com/Taiwanese-Corpus/hue7jip8/archive/master.zip
RUN pip3 install --upgrade https://github.com/twgo/twisas/archive/master.zip # 0906-1523
RUN python3 manage.py TGB通訊
RUN python3 manage.py 台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計 --錯誤印部份就好

RUN  \
  /usr/bin/python3 manage.py 台文用語料斷詞 \
    --欲參考 \
      教典詞條 \
      教典例句 \
      twisas-語料庫系統 \
      詞彙分級 \
      itaigi \
    --欲斷詞 \
            TGB通訊 \
            台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計-HL 

RUN python3 manage.py icorpus臺華平行新聞語料庫
RUN python3 manage.py 台語文數位典藏資料庫 --錯誤印部份就好
RUN python3 manage.py 教育部臺灣閩南語字詞頻調查工作
RUN python3 manage.py 白話字文獻館 --錯誤印部份就好
# RUN python3 manage.py 台灣植物名彙
RUN python3 manage.py 台灣白話基礎語句
COPY twisas-HL-kaldi.json .
RUN python3 manage.py 匯入台文語料庫trs文本 train --trs聽拍json twisas-HL-kaldi.json
            
COPY lautsuanlo.py .
RUN echo import lautsuanlo | python3 manage.py shell

RUN pip3 install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/archive/Siu_lo-ma-ji_kuihuan.zip
COPY thongke.py .
RUN echo import thongke | python3 manage.py shell

COPY tsiautongan.py .
RUN echo import tsiautongan | python3 manage.py shell
COPY bopiautiam.py .
RUN echo import bopiautiam | python3 manage.py shell

CMD cat tsonghong.json
