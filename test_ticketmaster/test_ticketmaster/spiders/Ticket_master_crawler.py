import datetime
import json
import os
import random

import pandas as pd
import requests
import scrapy
from scrapy.cmdline import execute
from csv import reader
import cloudscraper
from scrapy.http import HtmlResponse


# Note : In Ticket-Master it's required proxy to full scraper


# Free Proxy using (get more ->> https://free-proxy-list.net/)
proxy_list = ['98.162.96.53']
proxy = random.choice(proxy_list)

proxies = {
    "http": proxy,
    "https": proxy,
}



def AllAvailableTickets(event_id):
    try:
        ticket_count_url = f'https://offeradapter.ticketmaster.ca/api/ismds/event/{event_id}/quickpicks?show=places+maxQuantity+sections&mode=primary:ppsectionrow+resale:ga_areas+platinum:all&qty=001029400007%3A2&q=not(%27accessible%27)&includeStandard=true&includeResale=true&includePlatinumInventoryType=false&ticketTypes=001029400007&embed=area&embed=offer&embed=description&apikey=b462oi7fic6pehcdkzony5bxhe&apisecret=pquzpfrfz7zd2ylvtz3w5dtyse&resaleChannelId=internal.ecommerce.consumer.desktop.web.browser.ticketmaster.ca&limit=40&offset=0&sort=totalprice'
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'LANGUAGE=en-ca; SID=A5HT8NAy5TcDKHgUpFWqn2koYHIIadDSBLPlRAu1i2sz0JVYYycPqUZtTXC7W0gco0MckyiIDjAqVmEm; _gcl_au=1.1.1829371104.1659077989; TMUO=east_XSbxj8zHW6JP4mnl6vHSbJOXbL8HEnw+bPPFKpZswvA=; mt.pc=2.2; mt.g.2f013145=2.302171200.1659076597645; mt.v=2.302171200.1659076597645; _pndbg=si; pushly.user_puuid=2qQKzO19ICyT3fysLJ2ndWEdLB6CYAUp; _pnvl=false; _pndnt=; TM_PIXEL={"_dvs":"0:l66479sd:0el4J_hvM9nHD5JpoB53RkFC5s1MlWSd","_dvp":"0:l66479sd:B2YL5H1ZaS29Y84VbRyzCovAiv9xJL8z"}; _gid=GA1.2.1218278432.1659077995; _fbp=fb.1.1659077995184.323348883; _scid=6f7a7ac6-84a2-4d6a-8a9b-9b8d71eb08f9; _sctr=1|1659033000000; __qca=P0-181267472-1659077995940; _pnlspid=18966; _pnss=dismissed; _pnpdm=true; _pndbgpr=updm; _sp_id.145e=1ae8d879-5f81-441d-a25f-6dbaea860a3e.1659077996.2.1659082230.1659079718.e1dca2a7-48d2-4cc8-ba30-1b6319b1ba46; reese84=3:qVbY/XvfvDjBqRsJu5pXNw==:I5osjWwcSQrMyq9eBYyPjJiJbOMnCW5b1Lb/kZbdpaj2VUkbBMiZVENwqs36QC82fZhLAle7yKt2m4Ks4o/8uwqd53OJb8iQW8opcXRW/9m+QS9gRt0Ji8Z78zXeKXA9kecdX1l2KIc+gAnp83mDL1Feb/fea7kAWfOTrw9+qUlOveVwSzLUOO7dBGmFRMJbVJ7ZixN34LbCzr7Kiv9T3IC4U0ZG1Zgt9DrhowKIcBYjbYrGNnyYpeBgfhKbs1+APssFiN7LuVrDMWs3WDUghFDim7nmNw4Ojow3ySFc3inzHKV/gFXHnPbfLaidkPwvObShbiEARBGM7p1NnNcmHD1vn9S+jDU1N4yLrhfmxciCtZ+QVjxUArE70fxZi73rjumDl971/PdRqH788Fj4BGyPtwOmIUO22jwWKNGDn5ZIBZGLn0nWqTv90LitR915yc8RdMUihbRywB70aU4XtPFz9XUjXB+u7yuLt3BW4M4=:WeibvHb0eyzPIrl3YAB6O933eAeJmW0g677cfQurx9o=; BID=52Ol4u7rwDe6OLHDm0BWmrWe85wLLL5_uW-JrneGsd-FIQz_HklxYnx9pZCZwPLBMqUzRlI6PdUb8l25; eps_sid=c9ca652c256e4f8bb77fa452c7b2c6ac; _ga_Y9KJECPJMY=GS1.1.1659085781.3.1.1659086153.56; _ga=GA1.2.1673507098.1659077995; _dc_gtm_UA-60025178-1=1; _uetsid=0d1962b00f0c11eda2c54f7fd0b54a55; _uetvid=0d19e5800f0c11edba648fadfefd9a34; _gat_tracker18531573=1',
            'origin': 'https://www.ticketmaster.com',
            'ot-tracer-sampled': 'true',
            'ot-tracer-spanid': '5ba0aab466985b7a',
            'ot-tracer-traceid': '7e7e03057fa67d27',
            'referer': 'https://www.ticketmaster.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'tmps-correlation-id': 'e1824258-caf0-4c2a-937b-7cbcb863a893',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }

        response1 = requests.request("GET", ticket_count_url, headers=headers)
        response = HtmlResponse(url=ticket_count_url, body=response1.text, encoding='utf-8')
        body = json.loads(response.text)
        if body:
            try:
                ticket_count = body['total']
            except:
                ticket_count = ''
    except Exception as e:
        print(e)

    ''':return value like --->> ticket count-->>  1501'''
    return ticket_count


def start_crawling():
    ''' Starting point of crawling ....'''

    final_list = []
    with open('Ticketmaster_Input.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            print('Crawling this url ---->>> ', ''.join(row))
            url = ''.join(row)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': 'LANGUAGE=en-ca; SID=A5HT8NAy5TcDKHgUpFWqn2koYHIIadDSBLPlRAu1i2sz0JVYYycPqUZtTXC7W0gco0MckyiIDjAqVmEm; _gcl_au=1.1.1829371104.1659077989; TMUO=east_XSbxj8zHW6JP4mnl6vHSbJOXbL8HEnw+bPPFKpZswvA=; mt.pc=2.2; mt.g.2f013145=2.302171200.1659076597645; mt.v=2.302171200.1659076597645; _pndbg=si; pushly.user_puuid=2qQKzO19ICyT3fysLJ2ndWEdLB6CYAUp; _pnvl=false; _pndnt=; TM_PIXEL={"_dvs":"0:l66479sd:0el4J_hvM9nHD5JpoB53RkFC5s1MlWSd","_dvp":"0:l66479sd:B2YL5H1ZaS29Y84VbRyzCovAiv9xJL8z"}; _gid=GA1.2.1218278432.1659077995; _fbp=fb.1.1659077995184.323348883; _scid=6f7a7ac6-84a2-4d6a-8a9b-9b8d71eb08f9; _sctr=1|1659033000000; __qca=P0-181267472-1659077995940; _pnlspid=18966; _pnss=dismissed; _pnpdm=true; _pndbgpr=updm; BID=EqWU-lYdya3mn8A_ThXB1reXY5RHdKjrHTwIeCin1OsSPXbgsgv2Nif9VUruu5Yjmm8M3MeNtaMce0Tv; eps_sid=097cc4b6032844209b9f6ac6ea87df28; lightstep_guid%2Fedp.app=77cf2c3057868acf; lightstep_session_id=1fc6187e3ee6bced; lightstep_guid%2Fco2.sdk=702d1edb181562ee; _dvp=0:l66479sd:B2YL5H1ZaS29Y84VbRyzCovAiv9xJL8z; _ga_Y9KJECPJMY=GS1.1.1659082225.2.1.1659082229.56; _uetsid=0d1962b00f0c11eda2c54f7fd0b54a55; _uetvid=0d19e5800f0c11edba648fadfefd9a34; _ga=GA1.2.1673507098.1659077995; _sp_id.145e=1ae8d879-5f81-441d-a25f-6dbaea860a3e.1659077996.2.1659082230.1659079718.e1dca2a7-48d2-4cc8-ba30-1b6319b1ba46; seerid=2e7dcc93-13b6-49f7-b674-031507adaf4e; reese84=3:qVbY/XvfvDjBqRsJu5pXNw==:I5osjWwcSQrMyq9eBYyPjJiJbOMnCW5b1Lb/kZbdpaj2VUkbBMiZVENwqs36QC82fZhLAle7yKt2m4Ks4o/8uwqd53OJb8iQW8opcXRW/9m+QS9gRt0Ji8Z78zXeKXA9kecdX1l2KIc+gAnp83mDL1Feb/fea7kAWfOTrw9+qUlOveVwSzLUOO7dBGmFRMJbVJ7ZixN34LbCzr7Kiv9T3IC4U0ZG1Zgt9DrhowKIcBYjbYrGNnyYpeBgfhKbs1+APssFiN7LuVrDMWs3WDUghFDim7nmNw4Ojow3ySFc3inzHKV/gFXHnPbfLaidkPwvObShbiEARBGM7p1NnNcmHD1vn9S+jDU1N4yLrhfmxciCtZ+QVjxUArE70fxZi73rjumDl971/PdRqH788Fj4BGyPtwOmIUO22jwWKNGDn5ZIBZGLn0nWqTv90LitR915yc8RdMUihbRywB70aU4XtPFz9XUjXB+u7yuLt3BW4M4=:WeibvHb0eyzPIrl3YAB6O933eAeJmW0g677cfQurx9o=; _dc_gtm_UA-60025178-1=1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
            }

            resp = requests.request("GET", url, headers=headers)
            response = HtmlResponse(url, body=resp.content)

            # page save or SaveHTMLPages
            event_id = url.split("/event/")[1]

            try:
                html_path = f'{os.getcwd()}/{event_id}'
            except:
                # if any specific path then please put path here
                html_path = f'{event_id}'

            with open(f'{html_path}.html', 'w') as file:
                file.write(response.text)
                print('Page save Done...!!!')

            # print(response.text)
            if response.status == 200:
                try:
                    final_dict = {}
                    if response:
                        final_dict['EventUrl'] = url
                        try:
                            ''' EventName for sample ---->>> My Chemical Romance '''
                            final_dict['EventName'] = str(response.xpath('//span[@class="event-header__event-name-text"]//text()').extract_first(default='')).strip()
                        except Exception as e:
                            print(e)
                            final_dict['EventName'] = ''
                        try:
                            final_dict['EventDate'] = ''.join(response.xpath('//div[contains(@data-bdd,"event-header-date")]//span[1]//text()').extract()).strip().replace('•','')
                            if final_dict['EventDate']:
                                '''DateTime converting like that '05/09/1900'''
                                try:
                                    final_dict['EventDate'] = datetime.datetime.strptime(f'{final_dict["EventDate"]}', '%a %b %d %H:%M %p').strftime( '%d/%m/%Y')
                                except:
                                    final_dict['EventDate'] = final_dict['EventDate']

                        except Exception as e:
                            print(e)
                            final_dict['EventDate'] = ''
                        try:
                            '''EventVenue (for sample) --->>  Scotiabank Arena, Toronto, ON '''
                            final_dict['EventVenue'] = response.xpath('//*[@data-bdd="event-venue-info"]//span//text()').extract_first(default='')
                        except Exception as e:
                            print(e)
                            final_dict['EventVenue'] = ''

                        '''For AllAvailableTickets'''
                        try:
                            final_dict['AllAvailableTickets'] = AllAvailableTickets(event_id)
                        except:
                            final_dict['AllAvailableTickets'] = ''

                        final_list.append(final_dict)
                except Exception as e:
                    print('please check something went to wrong ...!!')
            else:
                print(f'Response issue please check this -->> {url}')

        # NOW MAKING CSV FILE
        df = pd.DataFrame(final_list)
        df.to_csv('Ticket-master.csv')


if __name__ == '__main__':
    start_crawling()