FROM i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7:latest

RUN pip3 install tai5-uan5_gian5-gi2_hok8-bu7 hue7jip8 tw01 twisas

WORKDIR /usr/local/
RUN git clone https://github.com/i3thuan5/hok8-bu7.git

WORKDIR /usr/local/hok8-bu7
RUN pip3 install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/archive/%E8%87%BA%E7%BE%85%E9%99%84%E9%8C%84%E5%A4%96%E4%BE%86%E8%AA%9E%E6%8B%86%E9%96%8B.zip
RUN pip3 install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_hok8-bu7/archive/master.zip
RUN pip3 install --upgrade https://github.com/Taiwanese-Corpus/hue7jip8/archive/master.zip

RUN python3 manage.py migrate

RUN python3 manage.py 教典詞條
RUN python3 manage.py 教典例句

COPY twisas2.json .
#COPY twisas-HL-kaldi.json .

RUN pip3 install --upgrade https://github.com/twgo/twisas/archive/master.zip
RUN python3 manage.py 匯入台文語料庫2版文本 train twisas2.json
# RUN python3 manage.py 匯入台文語料庫trs文本

# RUN python3 manage.py icorpus臺華平行新聞語料庫
# RUN python3 manage.py TGB通訊
RUN python3 manage.py 詞彙分級
RUN python3 manage.py itaigi

COPY docker轉詞表.py .
RUN echo import docker轉詞表 | python3 manage.py shell 

CMD cat docker.csv
