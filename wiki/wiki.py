from http import client
import http
import json
import ssl
from sys import stdin
from urllib.parse import quote


ssl.match_hostname = lambda cert, hostname: True


def _main():
    for tsua in stdin.readlines():
        while True:
            try:
                conn = client.HTTPSConnection(
                    "xn--lhrz38b.xn--v0qr21b.xn--kpry57d"
                )
                conn.request(
                    "GET",
                    "/{}?{}={}".format(
                        quote('羅馬字轉換'),
                        quote('查詢語句'),
                        quote(tsua),
                    )
                )
            except ConnectionResetError:
                time.sleep(0.3)
            else:
                break
        r1 = conn.getresponse()
        if r1.status != 200:
            print(r1.status, r1.reason)
            raise RuntimeError()
        print(
            json.loads(r1.read().decode('utf-8'))['臺羅']
        )


if __name__ == '__main__':
    _main()
