FROM i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7:latest as ki1tshoo2
MAINTAINER i3thuan5

RUN pip3 install tai5-uan5_gian5-gi2_hok8-bu7 hue7jip8 tw01 twisas

WORKDIR /usr/local/
RUN git clone https://github.com/i3thuan5/hok8-bu7.git

WORKDIR /usr/local/hok8-bu7
RUN pip3 install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_hok8-bu7/archive/master.zip
RUN pip3 install --upgrade https://github.com/Taiwanese-Corpus/hue7jip8/archive/master.zip

RUN python3 manage.py 教典例句
RUN python3 manage.py icorpus臺華平行新聞語料庫
RUN python3 manage.py TGB通訊
RUN python3 manage.py 詞彙分級

RUN pip3 install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_hok8-bu7/archive/台文斷詞.zip
RUN python3 manage.py 台文用語料斷詞 --欲參考 教典例句 詞彙分級 --欲斷詞 icorpus臺華平行新聞語料 TGB通訊
