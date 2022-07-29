import datetime
import json
import re
import pymongo
import requests
from scrapy.http import HtmlResponse

con = pymongo.MongoClient('mongodb://localhost:27017')
db = con['Ticket_master_New']
conn = db['test']


def tickt_scraper(url, main_event_url):
    url = url
    main_event_url = main_event_url

    payload = {}
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        # need to change Cookies
        'cookie': '_gcl_au=1.1.1036941650.1643268412; mt.v=2.2096440774.1643268413669; __qca=P0-1181147536-1643268483442; _fbp=fb.1.1643268848443.1738513254; ku1-vid=949a9517-acbd-8e9c-a91a-201c65676375; _pxvid=05e8d7db-7f47-11ec-8e76-6149496d6974; TKM_USR=%7B%22id%22%3A%229d8bdc46d42950d6ab2831d317eeff0e3e67abc934d8b8d381be18b71c8b8ffa%22%2C%22email%22%3A%22akashpython710%40gmail.com%22%2C%22firstName%22%3A%22akash%22%2C%22lastName%22%3A%22gohil%22%2C%22__typename%22%3A%22User%22%2C%22ids%22%3A%7B%22hmacId%22%3A%229d8bdc46d42950d6ab2831d317eeff0e3e67abc934d8b8d381be18b71c8b8ffa%22%2C%22tmUserId%22%3A%229d8bdc46d42950d6ab2831d317eeff0e3e67abc934d8b8d381be18b71c8b8ffa%22%7D%7D; _scid=c46edffc-05b7-43ad-b7b1-69f4c1e8931d; AMCV_8DDE41805409FD450A4C98A5%40AdobeOrg=-1124106680%7CMCIDTS%7C19058%7CMCMID%7C29631354213312173443167805287330831762%7CMCAAMLH-1647160489%7C12%7CMCAAMB-1647160489%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1646562889s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; _gcl_dc=GCL.1646555886.CjgKEAiA1JGRBhClu5-Q8f_40mgSJADPPD1lo2tOkPUAGjNCScCietpDTfWPRCSqh6I_pcQArhD7PvD_BwE; _rdt_uuid=1646555901494.7a9d6d15-6100-4f7f-b291-f200b98b63c6; discovery_location=%7B%22description%22%3A%22Washington%2C%20DC%22%2C%22name%22%3A%2220001%22%2C%22dmaId%22%3A409%2C%22marketId%22%3A47%2C%22marketName%22%3A%22Washington%2C%20DC%20and%20Maryland%22%2C%22fromHeaders%22%3Afalse%2C%22fromUser%22%3Atrue%2C%22geoHash%22%3A%22dqcj%22%2C%22unit%22%3A%22miles%22%7D; AMCV_248F210755B762187F000101%40AdobeOrg=-637568504%7CMCIDTS%7C19058%7CMCMID%7C29621737301555082453166774389095003207%7CMCAAMLH-1647160904%7C12%7CMCAAMB-1647160904%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1646563304s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.1.1; s_fid=0E9E57DE9A544818-137074289611C51E; AAMC_nba_0=REGION%7C12; aam_uuid=29602356716339394983169895869793700472; __gads=ID=c752f8f53ea3cb34:T=1643268480:S=ALNI_Mb8VH4kd9rUMHSxphYZYLshS6KIAw; _pin_unauth=dWlkPU1tUTRNakV4WmpJdE0yRXhPUzAwWVdabUxUbGpNbUV0TldOa09EVTRPR1EwWTJSbQ; _mkto_trk=id:227-QUG-057&token:_mch-ticketmaster.com-1647089212026-50637; _sctr=1|1647158400000; LANGUAGE=en-us; mt.pc=2.1; mt.g.2f013145=2.2096440774.1643268413669; _gid=GA1.2.1495103768.1647447760; TM_PIXEL={"_dvs":"0:l0truzi7:YlKJi8vPlx7k81MmQSPxGHcxT5Pf1ol9","_dvp":"0:kywnmj7c:hsuCq~NrMIpZKUZIk_b4df1OfJYsjbvB"}; SID=Gho_Cu5JROnldnjDvIpFn0QZQhxsWJv9HaNfFn7xWbJPJSOyNlBB2vXn612tqpNyCojYBm0oUSdWlXBm; ku1-sid=YNUTdFqAgEDJ1n4zWU2ms; TMSPON=48b26025-4941-413b-9803-9ea6aa7035a7; com.silverpop.iMAWebCookie=11c0ab2b-9889-1ad0-6068-8ada195c3973; TMUO=west_lG6dNQbc7MadOfIfInROuKIanQLcu48xbt9LSKHBO+0=; _ga=GA1.2.1934171473.1646544622; _uetsid=68848000a54511ecb350df129c620c22; _uetvid=8498a0709d0e11ecac568dc4b70ee6d0; reese84=3:3fdby75YxNQzsXOQadn85w==:a8nb5sZGgROdwh0Mub+5FLGBbfkWrajUW7++VfYp02S6W/wbDBClc3WBuY+GI8d+DsWRQHUrm1HLX/dfnZWYGIQJaQJb7Vl9n/HmcFGhp/FoAVp4Oxq4JFIelfXUYbVYdbNPqCLIWeBcNOTiXF6vlymlqpWUhvuvlb29D/afFp9r/qxh79b004/S6KTC8KLzs0/jxtcnj21xkVTTXutUVAsmrWXYC8hQJbWsTGx2047c7XkdZLQb5ZhvtarOmwz81Tq3W10ZIGXlttIxFrC5qWWsfxNCm/IG8wYLH7sBZnf977sRdcn88ZEirHAyNIrAWFvwfgJ49XosmvLkUq/BlTV4VYCtse+34T7ZQ/Z2udr64rosNQUV8xibIZgh6lTl5KXXTBE2chW9yf4wLytjuHMQUwlOIaAshne31fn7FKBprsq73N8e9ZI5ylCCgV3p26VGEsFWNZAsAJtBYiKqQI6eAEvDPzZKetVdP83ugOI=:PDeSblmMGFwUYokveX60blIXNH6yTNCPKSRKvh9Zec4=; BID=Vs2YJkKGYGnsnX_GX8iSyMPYfaSM5t0XcDqUB7npaiw9RGlIoGPhwwpbia-0qLxGFc0YBLMVHvn8ovvY; _ga_Y9KJECPJMY=GS1.1.1647451570.11.1.1647452059.60; eps_sid=9a58941eb82e4440bf1365d8f79725eb',
        'if-modified-since': 'Sat, 12 Mar 2022 12:47:38 GMT',
        'if-none-match': 'W/"04abe16920a6b9734c2d779aecfd306dd"',
        'origin': 'https://www.ticketmaster.com',
        'ot-tracer-sampled': 'true',
        'ot-tracer-spanid': '6ac1461d572370e6',
        'ot-tracer-traceid': '2ab1000a4e686104',
        'referer': 'https://www.ticketmaster.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'tmps-correlation-id': '936d020b-6f11-4cbf-9fe9-ad01327c8c5d',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }

    response1 = requests.request("GET", url, headers=headers, data=payload)
    response = HtmlResponse(url=url, body=response1.text, encoding='utf-8')
    body = json.loads(response.text)

    lisst1 = body['picks']
    for i in range(0, len(lisst1)):
        offersid_list = body['_embedded']['offer']
        for sub in range(0, len(offersid_list)):
            item = {}

            item['Edit'] = 'Y'

            res1 = requests.request('GET', main_event_url, headers=headers)
            res23 = HtmlResponse(url=main_event_url, body=res1.text, encoding='utf-8')

            try:
                temps = res23.xpath('//*[@data-bdd="eventSchema"]//text()').extract_first(default='')
            except:
                temps = {}
            event_name_json = json.loads(temps)
            try:
                item['Event'] = event_name_json['name']
            except Exception as e:
                print(e)
                item['Event'] = ''
            try:
                item['Venue'] = event_name_json['location']['name']
            except:
                item['Venue'] = ''

            try:
                try:
                    from datetime import datetime
                    evet_date = str(event_name_json['startDate'])
                    Event_Date = str((f'{evet_date.split("T")[0]}'.replace('-', '/')))
                    Event_Time1 = str(evet_date.split('T')[1])
                    Event_Time = datetime.strptime(f"{Event_Time1}", "%H:%M").strftime("%I:%M %p")
                    print(Event_Time + "  ---  " + Event_Date)
                except:
                    pass
                    Event_Date = ''
                    Event_Time = ''
                item['EventDate'] = Event_Date
                item['EventTime'] = Event_Time
            except:
                item['EventDate'] = ''
                item['EventTime'] = ''

            # ----------------

            try:
                item['Quantity'] = body['picks'][i]['maxQuantity']
            except:
                item['Quantity'] = ''
            try:
                item['Section'] = body['picks'][i]['section']
            except:
                item['Section'] = ''
            try:
                item['Row'] = body['picks'][i]['row']
            except:
                item['Row'] = ''
            try:
                item['SeatFrom'] = ''
            except:
                item['SeatFrom'] = ''
            try:
                item['SeatThru'] = ''
            except:
                item['SeatThru'] = ''

            item['Notes'] = 'xfer'
            item['TicketID'] = ''
            item['EDelivery'] = 'Y'
            item['InHandDate'] = '07/29/2022'  # event ni date mathi 1 day minus karvano
            item['Instant'] = 'N'
            item['SplitType'] = 'CUSTOM'
            item['SplitValue'] = '1:2:3:4'
            try:
                item['StockType'] = 'mobile transfer'
            except:
                item['StockType'] = ''
            item['Electronic Transfer'] = 'N'
            item['Hide_seat'] = 'Y'
            item['Broadcast'] = 'Y'
            item['Public_Notes'] = ''
            item['Event_URL'] = main_event_url

            try:
                offers_id_for_match = str(body['picks'][i]['offerGroups'][0]['offers'][0]).strip()
            except Exception as e:
                print(e)
                offers_id_for_match = ''

            # Matching Data
            if offersid_list[sub]['offerId'].strip() == offers_id_for_match:
                print('Offer ID Match')

                offer_dict = offersid_list[sub]
                item = {**item, **offer_dict}
                print(item)
                item.pop('meta', None)
                item.pop('schema', None)
                item.pop('sellableQuantities', None)
                item.pop('_links', None)
                item.pop('protected', None)
                item.pop('rollup', None)
                item.pop('inventoryType', None)
                item.pop('alternateIds', None)
                item.pop('auditPriceLevel', None)
                item.pop('priceLevelId', None)
                item.pop('priceLevelSecname', None)
                item.pop('totalPrice', None)
                item.pop('online', None)
                item.pop('rank', None)
                item.pop('name', None)
                item.pop('description', None)
                item.pop('currency', None)
                item.pop('faceValue', None)
                item.pop('noChargesPrice', None)
                item.pop('charges', None)
                item.pop('offerId', None)
                item.pop('offerType', None)
                v = item['ticketTypeId']
                del item['ticketTypeId']
                item['TicketID'] = v

                # conn.insert_one(item)
                print('Data Inserted..')


            else:
                print('Offer ID Not Match')
                pass
    try:
        url = body['_links']['next']
        url = url[0]
        url = url['href']
        if url:
            main_event_url = main_event_url
            offset = str(re.findall('offset=(.*?)&', url)[0])
            url = f'https://offeradapter.ticketmaster.com/api/ismds/event/{event_id}/quickpicks?show=places+maxQuantity+sections&mode=primary:ppsectionrow+resale:ga_areas+platinum:all&qty=2&q=not(%27accessible%27)&includeStandard=true&includeResale=true&includePlatinumInventoryType=false&ticketTypes=000000000001%2C002260800007%2C0003E0020002%2C000400040002%2C000420050002%2C000440060002&embed=area&embed=offer&embed=description&apikey=b462oi7fic6pehcdkzony5bxhe&apisecret=pquzpfrfz7zd2ylvtz3w5dtyse&resaleChannelId=internal.ecommerce.consumer.desktop.web.browser.ticketmaster.us&limit=40&offset={offset}&sort=listprice'
            tickt_scraper(url, main_event_url)
    except:
        pass


if __name__ == '__main__':
    main_event_url = 'https://www.ticketmaster.com/the-weeknd-after-hours-til-dawn-east-rutherford-new-jersey-07-16-2022/event/00005C57C7735367'
    event_id = main_event_url.split('/event/')[1]

    url = f"https://offeradapter.ticketmaster.com/api/ismds/event/{event_id}/quickpicks?show=places+maxQuantity+sections&mode=primary:ppsectionrow+resale:ga_areas+platinum:all&qty=2&q=not(%27accessible%27)&includeStandard=true&includeResale=true&includePlatinumInventoryType=false&ticketTypes=000000000001%2C002260800007%2C0003E0020002%2C000400040002%2C000420050002%2C000440060002&embed=area&embed=offer&embed=description&apikey=b462oi7fic6pehcdkzony5bxhe&apisecret=pquzpfrfz7zd2ylvtz3w5dtyse&resaleChannelId=internal.ecommerce.consumer.desktop.web.browser.ticketmaster.us&limit=40&offset=0&sort=listprice"
    tickt_scraper(url, main_event_url)
