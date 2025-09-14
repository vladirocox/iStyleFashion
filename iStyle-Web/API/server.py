from argparse import _MutuallyExclusiveGroup
from flask import Flask, request, jsonify
import requests, random
from typing import List
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from werkzeug.datastructures.structures import MultiDict

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
user_agents = user_agent_rotator.get_user_agents()
user_agent = user_agent_rotator.get_random_user_agent()

app = Flask(__name__)


class arcadeData:
    url = "https://istyle.ro/appleservices/endpoint/ajaxcall/"
    headers = {
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Prefer": "safe",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "null",
        "Connection": "keep-alive",
        "Cookie": "_gcl_au=1.1.933259587.1703366025; _ga_E4N1EX0BPG=GS1.1.1703366025.1.0.1703366025.0.0.0; _ga=GA1.2.1719511963.1703366025; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; _gid=GA1.2.360085304.1703366025; _fbp=fb.1.1703366025470.1060841994; mage-translation-storage=%7B%7D; mage-translation-file-version=%7B%7D; _hjSessionUser_973988=eyJpZCI6ImU1ZGQwOTAyLWIwMWYtNTMyNC1hMGFhLTZiYTAyZDdlNjA5MSIsImNyZWF0ZWQiOjE3MDMzNjYwMjU1MzgsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_973988=0; _hjSession_973988=eyJpZCI6IjZkMzg3M2RhLTgxODAtNDlmNi05NWFiLTQxZmQzMWZiNTBhMSIsImMiOjE3MDMzNjYwMjU1MzgsInMiOjAsInIiOjAsInNiIjoxfQ==; _hjAbsoluteSessionInProgress=0; CookieConsent={stamp:%276ppWJxkvc5ufoHelCAQoXUHzTrb5LPLr3vT97XevrlPaxPFI7sy0yA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1703366026153%2Cregion:%27ro%27}; form_key=2dVli8RCg2XFl9pa; mage-messages=; section_data_ids=%7B%22cart%22%3A1703366439%2C%22customer%22%3A1703366439%2C%22compare-products%22%3A1703366439%2C%22customweb_external_checkout_widgets%22%3A1703366439%2C%22last-ordered-items%22%3A1703366439%2C%22directory-data%22%3A1703366439%2C%22review%22%3A1703366439%2C%22wishlist%22%3A1703366439%2C%22wp_ga4%22%3A1703366439%2C%22paypal-billing-agreement%22%3A1703366439%7D; PHPSESSID=k9t0uiufmdu9v43ooh6k8ug1m6; wp_ga4_customerGroup=NOT+LOGGED+IN; private_content_version=470d7dc16df20b8b2e978ca73644160e; X-Magento-Vary=f25c03e27a6e1b3fd288b9c3c2d49a7668693c08",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "TE": "trailers"
    }
    data = {

            "captcha": "03AFcWeA5VuHvLwD4RAbif1hYdchE3E1j45IO4xm-HgjJMhSlIcc4orjrijfEAFtwe-GIvPrHZu_2TfHUnq-nsUCYxSpCO_sEZTahFjJl6FFaAUm035IgDadtLUhkQTCjbaHWBAGkS6waGYC_lcVhNAKLsSwlvnN2hf_-3qvMwg1G5EmO-kedKqYrYxdYenjNxDf51h67UlBZp4JcgUXSFE7p4cuL7PkWi5BneocFWkk-It86lzGLG4wxiInFnE1SRNkn2kBrVuoaI0nimVYoKcBO_9_iKAPkHnrxidh5WUYT3n_aGSMifsfE2iTKx2f-qhKtTWBb9MrMN-FMhP3ojZ8NHjl76ufCzOz5iPAHGt6Mlsw88b2XUbdH4qjESKnY57hUNzuThVvomWbBbdNKIGuSHSDI5j0-SaMfDd1UB_2otVxnm4jJYrS6tV6InHXoK1LDGlsznYS1rZqQBbh3kxtGmAgM2WqV2pSEYzRlOYg-5xMFvKxMj2gT_DgZ81GYl5X-Smh3PIVpBtlfpPJXq-sPAPgzYsUCudkvcSNHgIBBCLzLUDqL1nqpor7mcJqgjrOYxFSsAS3GwcIb6-PJ3ixoGjSjwUvt-ug",
            "unique_id": "9bc6f768-a87f-41f0-84cc-d2e8f5c3dbbb",
            "api_endpoint": "https://codemanager.apple.com/jwt/api/v1/campaigns/9bc6f768-a87f-41f0-84cc-d2e8f5c3dbbb/codes/vend",
            "secret_key": "8de71eedb4225c2db87d42edffc46dfd0fd126f51b8ad740f602998cafd4a01a68f7e9cfcfbb52b63ae1a10558e96ff2acc961f200595698e1a18f2b07bd4aff",
            "referral_token": "online"
            }

class musicData:
    url = "https://istyle.ro/appleservices/endpoint/ajaxcall/"
    headers = {
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Prefer": "safe",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "null",
        "Connection": "keep-alive",
        "Cookie": "_gcl_au=1.1.933259587.1703366025; _ga_E4N1EX0BPG=GS1.1.1703366025.1.0.1703366025.0.0.0; _ga=GA1.2.1719511963.1703366025; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; _gid=GA1.2.360085304.1703366025; _fbp=fb.1.1703366025470.1060841994; mage-translation-storage=%7B%7D; mage-translation-file-version=%7B%7D; _hjSessionUser_973988=eyJpZCI6ImU1ZGQwOTAyLWIwMWYtNTMyNC1hMGFhLTZiYTAyZDdlNjA5MSIsImNyZWF0ZWQiOjE3MDMzNjYwMjU1MzgsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_973988=0; _hjSession_973988=eyJpZCI6IjZkMzg3M2RhLTgxODAtNDlmNi05NWFiLTQxZmQzMWZiNTBhMSIsImMiOjE3MDMzNjYwMjU1MzgsInMiOjAsInIiOjAsInNiIjoxfQ==; _hjAbsoluteSessionInProgress=0; CookieConsent={stamp:%276ppWJxkvc5ufoHelCAQoXUHzTrb5LPLr3vT97XevrlPaxPFI7sy0yA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1703366026153%2Cregion:%27ro%27}; form_key=2dVli8RCg2XFl9pa; mage-messages=; section_data_ids=%7B%22cart%22%3A1703366439%2C%22customer%22%3A1703366439%2C%22compare-products%22%3A1703366439%2C%22customweb_external_checkout_widgets%22%3A1703366439%2C%22last-ordered-items%22%3A1703366439%2C%22directory-data%22%3A1703366439%2C%22review%22%3A1703366439%2C%22wishlist%22%3A1703366439%2C%22wp_ga4%22%3A1703366439%2C%22paypal-billing-agreement%22%3A1703366439%7D; PHPSESSID=k9t0uiufmdu9v43ooh6k8ug1m6; wp_ga4_customerGroup=NOT+LOGGED+IN; private_content_version=470d7dc16df20b8b2e978ca73644160e; X-Magento-Vary=f25c03e27a6e1b3fd288b9c3c2d49a7668693c08",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "TE": "trailers"
    }
    data = {
        "captcha": "03AFcWeA5TaFHqCtY9q3lhntei7Mo1ICgYEzjsYEIZB96Zp4nr7OfMt1vL3AO4cWHBC14WpCCvHA476CN1y_xkjvcjdJ-iDe7N-bdZWGP93h3KMzi36vC45U-MPcCEp7KHYsHaI-iUed5gkgM5TeuHy_dzmGSCTeBU2WqgqERi1Uoz65tlQeoRkHxybTSP0vR-aaDhCOAUFgJaXqnUOZ6x9f_a6DwUA3Lcff9N_j2_IRXVYlBO37SerzOdqxIyfZapyP9WR2CbCuG6OrnXUa0sSmM5uTyzHMY-AzGV3Uy9KcbG8oGe0ZTLpdOulguH1BWcB7KaNwizMGw69DTGwhqq6-mab3g70DIeOq99EUxlWHB63tUfflwm_jxnQPwZs2D6iNE1DnIdvPbrHS56U9Yj77dNbALbnzuicIExxxFxOMeRkAQ7Mrjw6P9RvHp3rVrp238DpZETIn-pPnaDZFybcoDjzdUSaS2v-r37vTVDZie67wBBlZNCmbt8bQFmPpoF_ksI_0ekQOiquDTOcCg--ZjYuN0TBW3-y8cFJOyNFA3V7N0MOE5VC_b4rSJjkn54XwLubSEvksCa",
        "unique_id": "3d79d4e0-4344-49f3-9d8a-83e3ea6c5f58",
        "api_endpoint": "https://codemanager.apple.com/jwt/api/v1/campaigns/3d79d4e0-4344-49f3-9d8a-83e3ea6c5f58/codes/vend",
        "secret_key": "8de71eedb4225c2db87d42edffc46dfd0fd126f51b8ad740f602998cafd4a01a68f7e9cfcfbb52b63ae1a10558e96ff2acc961f200595698e1a18f2b07bd4aff",
        "referral_token": "online"
    }

class icloudData:
    url = "https://istyle.ro/appleservices/endpoint/ajaxcall/"
    headers = {
    "User-Agent": user_agent,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Prefer": "safe",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "null",
    "Connection": "keep-alive",
    "Cookie": "_gcl_au=1.1.933259587.1703366025; _ga_E4N1EX0BPG=GS1.1.1703366025.1.0.1703366025.0.0.0; _ga=GA1.2.1719511963.1703366025; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; _gid=GA1.2.360085304.1703366025; _fbp=fb.1.1703366025470.1060841994; mage-translation-storage=%7B%7D; mage-translation-file-version=%7B%7D; _hjSessionUser_973988=eyJpZCI6ImU1ZGQwOTAyLWIwMWYtNTMyNC1hMGFhLTZiYTAyZDdlNjA5MSIsImNyZWF0ZWQiOjE3MDMzNjYwMjU1MzgsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_973988=0; _hjSession_973988=eyJpZCI6IjZkMzg3M2RhLTgxODAtNDlmNi05NWFiLTQxZmQzMWZiNTBhMSIsImMiOjE3MDMzNjYwMjU1MzgsInMiOjAsInIiOjAsInNiIjoxfQ==; _hjAbsoluteSessionInProgress=0; CookieConsent={stamp:%276ppWJxkvc5ufoHelCAQoXUHzTrb5LPLr3vT97XevrlPaxPFI7sy0yA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1703366026153%2Cregion:%27ro%27}; form_key=2dVli8RCg2XFl9pa; mage-messages=; section_data_ids=%7B%22cart%22%3A1703366439%2C%22customer%22%3A1703366439%2C%22compare-products%22%3A1703366439%2C%22customweb_external_checkout_widgets%22%3A1703366439%2C%22last-ordered-items%22%3A1703366439%2C%22directory-data%22%3A1703366439%2C%22review%22%3A1703366439%2C%22wishlist%22%3A1703366439%2C%22wp_ga4%22%3A1703366439%2C%22paypal-billing-agreement%22%3A1703366439%7D; PHPSESSID=k9t0uiufmdu9v43ooh6k8ug1m6; wp_ga4_customerGroup=NOT+LOGGED+IN; private_content_version=470d7dc16df20b8b2e978ca73644160e; X-Magento-Vary=f25c03e27a6e1b3fd288b9c3c2d49a7668693c08",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
    }
    data = {
        "captcha": "03AFcWeA7mrUlBXRJHr1rBSH5Ezd9BPZRzznMiL5PUSJ6zpCV0Q__ABoSBdWq7xfaBqVdM4NUgdGkIT6ppqrhFi-zZN24yOp_TIQtYwQB7n1yD7sICpFDb6yRFae5tevjh_RkGWS5Rv2geY0OMTS7MTE5eiozLHzJxidws2yIuPiWIVjiTuyP1QaDal7nU7t_AG-EPC9pPQihsBBjmfkkTlJXwD8WG8tFSxD1oPQnSr9WTW1D-ZdF_IG1eD8IKUH4iYkQL0Bs33b8qAusDdP8skeQN0LYrzmfIoLgXafEKDB8neFMO2cpcpFQeucE5o5JZv7Dzm6X6FbyWJq6-L0KUgIfCDZ4DZRemkMO4E1X7LncLqAtrEe2mUn9ze0to7fjxcDsvc2I9T_yYud4iVvTn9-DrT06ipWa9rjdT2YHjfovapFq31ItE2CdN0QwrF51PygDQuZ8xT9BiTX3AAPLrEv85RksA-TnWd5wl_imQL4_lQd7JO9wfoqkGv1hxmuY0bjAw_ueME13LNlXYSK-vpNzGOxqnPWx6QM6kSfo4fuRgUrBB1IcXUT_TU0NmQwIkSVppk4ntcr1v",
        "unique_id": "b3213d56-28e9-494e-a8a7-1a96ce932bef",
        "api_endpoint": "https://codemanager.apple.com/jwt/api/v1/campaigns/b3213d56-28e9-494e-a8a7-1a96ce932bef/codes/vend",
        "secret_key": "8de71eedb4225c2db87d42edffc46dfd0fd126f51b8ad740f602998cafd4a01a68f7e9cfcfbb52b63ae1a10558e96ff2acc961f200595698e1a18f2b07bd4aff",
        "referral_token": "online"
    }

def fetch_proxies(url: str) -> List[str]:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            proxies = response.text.split('\n')
            proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
            return proxies
        else:
            print(f"Failed to fetch proxies. Status code: ", response.status_code)
            return []
    except Exception as e:
        print(f"An error occured: ", e)
        return []

@app.route('/getarcade', methods=['GET'])
def get_arcade_page():
        proxies = fetch_proxies("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt")
        try:
            response = requests.post(arcadeData.url, proxies={'http': random.choice(proxies)}, headers=arcadeData.headers, data=arcadeData.data, timeout=5)
            response_json = response.json()
            redemption_url = response_json["redemption_url"]
            code = response_json["code"]
            return jsonify({
                "redemption_url": redemption_url,
                "code": code
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route('/geticloudplus', methods=['GET'])
def get_icloudplus_page():
        proxies = fetch_proxies("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt")
        try:
            response = requests.post(icloudData.url, proxies={'http': random.choice(proxies)}, headers=icloudData.headers, data=icloudData.data, timeout=5)
            response_json = response.json()
            redemption_url = response_json["redemption_url"]
            code = response_json["code"]
            return jsonify({
                "redemption_url": redemption_url,
                "code": code
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route('/getmusic', methods=['GET'])
def get_music_page():
        proxies = fetch_proxies("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt")
        try:
            response = requests.post(musicData.url, proxies={'http': random.choice(proxies)}, headers=musicData.headers, data=musicData.data, timeout=5)
            response_json = response.json()
            redemption_url = response_json["redemption_url"]
            code = response_json["code"]
            return jsonify({
                "redemption_url": redemption_url,
                "code": code
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="192.168.0.177", port=25565)
