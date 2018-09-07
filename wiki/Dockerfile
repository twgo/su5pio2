FROM i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7:latest

COPY wiki.txt .
COPY wiki.py .

RUN python3 wiki.py < wiki.txt > tl.txt

CMD cat tl.txt

