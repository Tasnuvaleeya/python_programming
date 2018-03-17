import tldextract
def domain_name(url):
    list = tldextract.extract(url)
    domain_name = list.domain + '.' + list.suffix
    return domain_name
print("http://www.github.com")
