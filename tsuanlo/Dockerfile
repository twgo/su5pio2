FROM twgo/su5pio2

RUN pip3 install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/archive/master.zip
RUN pip3 install --upgrade https://github.com/Taiwanese-Corpus/hue7jip8/archive/master.zip
RUN python3 manage.py 匯入台文語料庫trs
RUN python3 manage.py icorpus臺華平行新聞語料庫
RUN python3 manage.py TGB通訊
RUN python3 manage.py 台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計 --錯誤印部份就好
RUN python3 manage.py 台語文數位典藏資料庫 --錯誤印部份就好
RUN python3 manage.py 教育部臺灣閩南語字詞頻調查工作
RUN python3 manage.py 白話字文獻館 --錯誤印部份就好
# RUN python3 manage.py 台灣植物名彙
RUN python3 manage.py 台灣白話基礎語句

COPY lautsuanlo.py .
RUN echo import lautsuanlo | python3 manage.py shell

COPY thongke.py .
RUN echo import thongke | python3 manage.py shell

