from urllib import request

google_url = "https://finance.yahoo.com/quote/GOOG/history?p=GOOG"


def download_csv(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')

    fx.close()
download_csv(google_url)
