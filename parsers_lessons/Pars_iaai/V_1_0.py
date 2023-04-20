from bs4 import BeautifulSoup
import requests
import json
cookies = {
    'X-Forwarded-For_IpAddress': '37.214.46.73%2C%20149.126.78.13%3A64218',
    'BrokerPopupIPAddress': '634793545-37.214.46.73-634793545',
    'BrokerPopupCountryCode': 'BY',
    'URI': 's4AVptX2B2oPa%252b3EeI63xkeSbO%252bH4hfzVWY0SkLJkKM%253d',
    'last_viewed_page': '%2Fsearch',
    'IAAITrackingCookie': 'ff1dce40-6559-498c-8e12-4fc1ec29c563',
    'visid_incap_2807936': '3rP7+u8QTLuoKmwSQXklLTUjQGQAAAAAQUIPAAAAAADzj+dzdyxE+JoCfOlf49ya',
    'nlbi_2807936': '8K+sX+vykXpQJ1R7xRLPjgAAAABd7Y52uZXlQYuYRA5AZF9m',
    'incap_ses_536_2807936': 'BtTldvHddUiUEpieAUJwBzUjQGQAAAAAwNSOR9PzCd1hc/f1nB6eDA==',
    '_gcl_au': '1.1.1318256949.1681924920',
    '_fbp': 'fb.1.1681924921142.530943085',
    '_evga_4ff5': '{%22uuid%22:%223a8ad49e4ae32ca4%22}',
    '_sfid_4446': '{%22anonymousId%22:%223a8ad49e4ae32ca4%22%2C%22consents%22:[]}',
    'ASP.NET_SessionId': 'yd3hboi1m3qzh5ecyngyu5fs',
    'BrokerPopupCountryCodeIP': '2508082701',
    'TimeZoneMapID': '120',
    'ln_or': 'eyIyMzg4ODk3IjoiZCJ9',
    '_clck': '1w1k0gm|1|faw|0',
    'mdLogger': 'false',
    'kampyle_userid': '4450-7285-8c3a-ec78-2782-5bc3-aa40-5c40',
    'OptanonAlertBoxClosed': '2023-04-19T17:22:09.930Z',
    'actualOptanonConsent': '%2CC0001%2CC0003%2CC0002%2CC0004%2C',
    '_gid': 'GA1.2.156194025.1681924931',
    'nlbi_2807936_2147483392': 'MeZcIOsPNkeTsfYXxRLPjgAAAADDvIV8BQ9f3RQEkN8BUJOV',
    '_ga_8J4GTR5B9Q': 'GS1.1.1681924919.1.1.1681925861.60.0.0',
    '_uetsid': 'b2797ce0ded611ed993c9944b8c0e3b6',
    '_uetvid': 'b27a9960ded611ed892921d7f644911b',
    '_ga': 'GA1.2.1058261839.1681924920',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Apr+19+2023+20%3A37%3A45+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.28.0&isIABGlobal=false&hosts=&consentId=82d06246-4293-45e6-94bc-edd1fd44e209&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=%3B&AwaitingReconsent=false',
    'kampyleUserSession': '1681925866756',
    'kampyleUserSessionsCount': '2',
    'kampyleSessionPageCounter': '1',
    'kampyleUserPercentile': '68.67605419222558',
    '_clsk': '1crz4m7|1681925867406|3|0|i.clarity.ms/collect',
}

headers = {
    'authority': 'www.iaai.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'X-Forwarded-For_IpAddress=37.214.46.73%2C%20149.126.78.13%3A64218; BrokerPopupIPAddress=634793545-37.214.46.73-634793545; BrokerPopupCountryCode=BY; URI=s4AVptX2B2oPa%252b3EeI63xkeSbO%252bH4hfzVWY0SkLJkKM%253d; last_viewed_page=%2Fsearch; IAAITrackingCookie=ff1dce40-6559-498c-8e12-4fc1ec29c563; visid_incap_2807936=3rP7+u8QTLuoKmwSQXklLTUjQGQAAAAAQUIPAAAAAADzj+dzdyxE+JoCfOlf49ya; nlbi_2807936=8K+sX+vykXpQJ1R7xRLPjgAAAABd7Y52uZXlQYuYRA5AZF9m; incap_ses_536_2807936=BtTldvHddUiUEpieAUJwBzUjQGQAAAAAwNSOR9PzCd1hc/f1nB6eDA==; _gcl_au=1.1.1318256949.1681924920; _fbp=fb.1.1681924921142.530943085; _evga_4ff5={%22uuid%22:%223a8ad49e4ae32ca4%22}; _sfid_4446={%22anonymousId%22:%223a8ad49e4ae32ca4%22%2C%22consents%22:[]}; ASP.NET_SessionId=yd3hboi1m3qzh5ecyngyu5fs; BrokerPopupCountryCodeIP=2508082701; TimeZoneMapID=120; ln_or=eyIyMzg4ODk3IjoiZCJ9; _clck=1w1k0gm|1|faw|0; mdLogger=false; kampyle_userid=4450-7285-8c3a-ec78-2782-5bc3-aa40-5c40; OptanonAlertBoxClosed=2023-04-19T17:22:09.930Z; actualOptanonConsent=%2CC0001%2CC0003%2CC0002%2CC0004%2C; _gid=GA1.2.156194025.1681924931; nlbi_2807936_2147483392=MeZcIOsPNkeTsfYXxRLPjgAAAADDvIV8BQ9f3RQEkN8BUJOV; _ga_8J4GTR5B9Q=GS1.1.1681924919.1.1.1681925861.60.0.0; _uetsid=b2797ce0ded611ed993c9944b8c0e3b6; _uetvid=b27a9960ded611ed892921d7f644911b; _ga=GA1.2.1058261839.1681924920; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Apr+19+2023+20%3A37%3A45+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.28.0&isIABGlobal=false&hosts=&consentId=82d06246-4293-45e6-94bc-edd1fd44e209&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=%3B&AwaitingReconsent=false; kampyleUserSession=1681925866756; kampyleUserSessionsCount=2; kampyleSessionPageCounter=1; kampyleUserPercentile=68.67605419222558; _clsk=1crz4m7|1681925867406|3|0|i.clarity.ms/collect',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48',
}
# --------- Выгрузка HTML  ---------
url = ""
response = requests.get(url=url,
    cookies=cookies,
    headers=headers,
)
with open("index.html","w") as file:
        file.write(response.text)
# --------- Выгрузка товаров в JSON  ---------
# response = requests.get(
#     'https://www.iaai.com/Search?c=1681927203646',
#     cookies=cookies,
#     headers=headers,
# )
# with open("result.json","w") as file:
#         json.dump(response.json(),file,indent=4,ensure_ascii=False)

import urllib.parse

data = {
    "Searches": [{
        "Facets": [{
            "Group": "AuctionType",
            "Value": "Buy Now"
        }],
        "FullSearch": None,
        "LongRanges": None
    }],
    "ZipCode": "",
    "miles": 0,
    "PageSize": 100,
    "CurrentPage": 1,
    "Sort": [{
        "IsGeoSort": False,
        "SortField": "AuctionDateTime",
        "IsDescending": False
    }],
    "SaleStatus": 0,
    "BidStatus": 6
}

query_string = urllib.parse.urlencode({'data': json.dumps(data)})
url = 'https://www.iaai.com/Search?c=&{}'.format(query_string)
print(url)








# headers = {
#         "Accept": "*/*",
#         "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
# }
# cookies = {
#         'MUID': '3424C29AA4CF61C7399ED062A5636009'
#     }
# proxies={'https': 'http://r894QHkE:nivYKzJG@45.149.131.202:63182'}
# def get_page(url):
#     s= requests.Session()
#     response = s.get(url=url,headers=headers,proxies=proxies,cookies=cookies)
#
#     with open("index.html","w") as file:
#         file.write(response.text)
# def main():
#     get_page(url='https://www.iaai.com/Search')
# if __name__=="__main__":
#     main()
# with open("url.txt") as file:
#     lines = [line.strip() for line in file.readlines()]
