FROM twgo/su5pio2

RUN pip3 install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/archive/Siu_lo-ma-ji_kuihuan.zip

COPY sng.py .
RUN echo import sng | python3 manage.py shell

CMD cat tsonghong.json

# cat tsuanpoojitiau.txt > tsuanpoojitiau.txt
# cat tsuanpooji.txt > tsuanpooji.txt