import csv
import re


def main():
    hanji = set(thak('kautianimtsiat/tsuanpooji.txt'))
    lo = set(thak('tsuanlo/tsuanpooji.txt'))
    bun = sorted(set(thak('tsuanlo/tsuanpooku.txt')))

    with open('imtsiat.csv', 'wt', encoding='utf-8') as 檔:
        詞表 = csv.writer(檔)
        詞表.writerow(
            ['音節', '教育部漢字辭典', '全羅', '人工判斷'] +
            ['例{}'.format(soo+1) for soo in range(10)]
        )
        for su in sorted(hanji | lo):
            print(su)
            h = su in hanji
            if not h:
                h = ''
            l = su in lo
            if not l:
                l = ''
            tshue = re.compile('[^a-zA-z0-9]{}\d'.format(su))
            si7 = []
            if h != l:
                for ku in bun:
                    if tshue.search(ku):
                        si7.append(ku)
            詞表.writerow([su, h, l, ''] + si7[:10])


def thak(mia):
    with open(mia) as tong:
        for su in tong.readlines():
            yield su.strip()


main()
