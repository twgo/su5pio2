FROM twgo/su5pio2

RUN pip3 install pyexcel-ods

COPY 音節比較表.ods .
COPY tsuanpoosu.txt .
COPY kuelihsu.py .
RUN echo import kuelihsu | python3 manage.py shell

CMD cat aisiu.txt
