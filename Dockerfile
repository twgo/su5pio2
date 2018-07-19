FROM i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7:latest as ki1tshoo2
MAINTAINER i3thuan5

RUN pip3 install tai5-uan5_gian5-gi2_hok8-bu7 hue7jip8 tw01 twisas

WORKDIR /usr/local/
RUN git clone https://github.com/i3thuan5/hok8-bu7.git

WORKDIR /usr/local/hok8-bu7
RUN pip3 install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_hok8-bu7/archive/master.zip
RUN pip3 install --upgrade https://github.com/Taiwanese-Corpus/hue7jip8/archive/master.zip

RUN python3 manage.py migrate

RUN python3 manage.py 教典例句
RUN python3 manage.py icorpus臺華平行新聞語料庫
RUN python3 manage.py TGB通訊
RUN python3 manage.py 詞彙分級

COPY twisas2.json .
COPY twisas-HL.json .

RUN echo 0717-1732
RUN pip3 install --upgrade https://github.com/twgo/twisas/archive/master.zip
RUN python3 manage.py 匯入台文語料庫2版文本 twisas2.json
RUN python3 manage.py 匯入台文語料庫trs

RUN pip3 install --upgrade https://github.com/Taiwanese-Corpus/hue7jip8/archive/itaigi.zip
RUN python3 manage.py itaigi

COPY docker轉詞表 .
RUN python3 docker轉詞表
