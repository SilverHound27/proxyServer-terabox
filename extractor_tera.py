import requests
from random import choice

def get_identity():
    data = [ {
         "cookies" : {
            'FCNEC': '[[\"AKsRol-GrWeFnY4ppOyjp1580hiBhXNP27ndr23GRnoZxUxaHIB43_Aqko5MW8HBy-dX1DAJTSvETsHaYEsRWrhxSoIyvwveb9o7JszX_a6g-s0ce3CsiMNrC7HhJs2Rp81MRGwK2aSDhaP3lRANewW21foW1m-8HQ==\"]]',
            '__eoi': 'ID=ba0d8d55a6684ce8:T=1716814082:RT=1716814082:S=AA-AfjarpNXgeu51nQVUkX3yi0Gv',
            '__gads': 'ID=217166d5cc082115:T=1716814082:RT=1716814082:S=ALNI_MbQTSsf3HoI45OkQ7CesHx8jn-Ssw',
            '__gpi': 'UID=00000e3054e81cc6:T=1716814082:RT=1716814082:S=ALNI_MaaVGGViQO6Poq8qKTxk94AcaFKoQ',
            'cf_clearance': 'S3Sd1MyAYxhnZKJyJm1AnFV.ArqaBSUcSiBRexfliEE-1716814081-1.0.1.1-NzgwtH0XR8HFbHIfEoFSFTV_voz5HwT9PTB.tHIsDUSXxxcM6HRpXrY2LoTX6EakJfu_HEqhsSghV2Wc.n2fPQ'
            },
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15'
    },
        {
         "cookies" : {
            'ext_name':'ojplmecpdpgccookcobabopnaifgidhf',
            'f_clearance':'2LJE71BZ3x61P48ByyRa6vUjYb.xTv5fcpqEj9Qicuc-1716655745-1.0.1.1-KJ3AShK4.AGU0gLf68KTLHbYz4BdU_AKzCJ1.kCU_X21kMR1l_AHIrxaZhAU2eHVAdzA_R8sgoTeJ4M5NKUWjA'
            },
         "user-agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
                    
        }
        
  

    ]
    # return data[0]
    return choice(data)


def make_connection(url):
    try:
        req_url = "https://ytshorts.savetube.me/api/v1/terabox-downloader"

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://ytshorts.savetube.me',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
        }

        payload = {
            "url": url
        }

        identity = get_identity()
        cookies = identity['cookies']
        user_agent = identity['user-agent']
        headers['user-agent'] = user_agent


        response = requests.post(req_url, headers=headers, json=payload, cookies=cookies)
        print(f'Response of POST request: {response.status_code}')
        response_json = response.json()
        
        return response_json, response.status_code
    except Exception as e:
            return f'error : Unknown Error \n {e}', 400
    