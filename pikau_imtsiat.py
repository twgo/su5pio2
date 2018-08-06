import csv


def main():
    hanji = set(thak('kautianimtsiat/tsuanpooji.txt'))
    lo = set(thak('tsuanlo/tsuanpooji.txt'))
    with open('imtsiat.csv', 'wt', encoding='utf-8') as 檔:
        詞表 = csv.writer(檔)
        詞表.writerow(['音節', '教育部漢字辭典', '全羅', '人工判斷'])
        for su in sorted(hanji | lo):
            print(su)
            h = su in hanji
            if not h:
                h = ''
            l = su in lo
            if not l:
                l = ''
            詞表.writerow([su, h, l])


def thak(mia):
    with open(mia) as tong:
        for su in tong.readlines():
            yield su.strip()


main()
