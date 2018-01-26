import requests
import json
import collections
from API_APPLOVIN import *
from API_VUNGLE import *

'''
    API APPLOVIN REQUEST

    -- ADVERTISER --
    
    day - date of reporting data
    impressions - number of impressions
    clicks - number of clicks
    ctr - number of clicks / number of impressions
    conversions - number of conversions (installs)
    conversion_rate - number of conversions / number of clicks
    average_cpa - average cost per conversion
    average_cpc - average cost per click
    ad - ad name
    country - two letter country code
    campaign - campaign name
    app_id_external - hashed application id (commonly referred to as 'site id')
    traffic_source - 'AppLovin', or the name of the exchange
    ad_type - GRAPHIC, VIDEO, or PLAY
    cost - advertiser spend
    sales - count of attributed sales events (requires setting up revenue postbacks)
    size - ad size (INTER, BANNER, MREC, LEADER, or NATIVE)
    device_type - phone, tablet, or other
    platform - android, ios, fireos, or tvos
    campaign_package_name - Package name or Bundle ID of the app being promoted
    campaign_id_external - Unique reference to a campaign, doesn't change when the campaign is renamed. Same value as {CAMPAIGN_ID} click macro
    campaign_ad_type - Returns 'ua' for user acquisition and 'rt' for Retargeting

     -- PUBLISHER --

    day - date of reporting data
    hour - hour of reporting data (only available for past 30 days)
    impressions - number of impressions
    clicks - number of clicks
    ctr - number of clicks / number of impressions
    revenue - money earned
    ecpm - money earned per 1000 impressions
    country - two letter country code
    ad_type - GRAPHIC, PLAY, VIDEO, REWARD, or MRAID
    size - ad size (INTER, BANNER, MREC, LEADER, or NATIVE)
    device_type - phone, tablet, or other
    platform - android, ios, fireos, or tvos
    application - app name
    package_name - apps package name or bundle ID
    placement - placement name 
    application_is_hidden - is the app hidden in the dashboard
    zone - Zone name, if available to your account
    zone_id - Zone ID, if available to your account. Please contact your account manager if you are interested in using Zones


    ADD Option for Python

    print - display request json call on server [true/false]

'''


# initiale ALL API
'''
API_A = API_APPLOVIN()
API_A.api_key = "YOUR_API_KEY"
'''

API_B = API_VUNGLE(api_key="YOUR_API_KEY", 
                   result="application/json", 
                   version="1")

'''
# set parametre for APPLOVIN
columns = ['day',
           'campaign', 
           'impressions', 
           'clicks', 
           'ctr', 
           'conversions', 
           'conversion_rate', 
           'app_id_external', 
           'cost', 
           'sales']

# request for send server APPLOVIN
result_1 = API_A.get(start="2018-01-17",
          end="now",
          columns=columns,
          format="json",
          report_type="advertiser",
          _print=True)
'''

# set parametre for VUNGLE
data = ['country', 'platform']
data2 = ['revenue']

'''
# all possibility country
all_country = ['CM','DE', 'AW', 'CN',
               'IN', 'KH', 'YE', 'BY',
               'PH', 'TJ', 'MP', 'FM',
               'SB', 'AZ', 'MZ', 'FO',
               'MM', 'JE', 'SX', 'MS',
               'JM', 'CD', 'GF', 'GE',
               'WF', 'HK', 'KR', 'GB',
               'GL', 'NZ', 'NL', 'BT',
               'MW', 'UA', 'YT', 'MT',
               'CH', 'IR', 'BZ', 'PS',
               'BL', 'WS', 'PY', 'LI',
               'AF', 'SO', 'GM', 'JP',
               'BO', 'MF', 'GD', 'ID',
               'ME', 'NP', 'NC', 'ZM',
               'CX', 'VE', 'GN', 'LT',
               'KY', 'CW', 'AL', 'CR',
               'BD', 'CG', 'NE', 'ZA',
               'DJ', 'ET', 'LA', 'MK',
               'LK', 'PK', 'LS', 'DK',
               'IE', 'SA', 'PF', 'KW',
               'GI', 'CF', 'AO', 'BH',
               'CL', 'BG', 'BR', 'TZ',
               'UY', 'PW', 'MA', 'SR',
               'VN', 'GT', 'LR', 'MR',
               'AM', 'MC', 'VG', 'US',
               'IL', 'IM', 'LB', 'VI',
               'RU', 'BW', 'PE', 'PA',
               'IT', 'MX', 'KN', 'TG',
               'IS', 'RE', 'EE', 'TH',
               'AS', 'BI', 'BF', 'MY',
               'AE', 'SG', 'PG', 'ZW',
               'FJ', 'CV', 'SN', 'MG',
               'AG', 'QA', 'GY', 'GG',
               'TL', 'CY', 'LC', 'BS',
               'MH', 'MO', 'CZ', 'GH',
               'OM', 'UZ', 'CK', 'SK',
               'BQ', 'KG', 'MU', 'SC',
               'IQ', 'AT', 'FI', 'AX',
               'SL', 'NG', 'PL', 'TN',
               'BJ', 'KM', 'BN', 'RS',
               'EG', 'BB', 'VU', 'BE',
               'AU', 'KZ', 'TT', 'RW',
               'TD', 'MD', 'CA', 'HU',
               'EC', 'DO', 'NA', 'ML',
               'GP', 'HT', 'TO', 'AD',
               'GA', 'KE', 'TW', 'GR',
               'PM', 'VC', 'JO', 'AI',
               'PR', 'HN', 'LU', 'TC',
               'BM', 'CO', 'GU', 'RO',
               'MV', 'AR', 'MQ', 'BA',
               'UG', 'SE', 'GS', 'HR',
               'MN', 'FR', 'TR', 'CI',
               'NI', '', 'SZ', 'LV',
               'SV', 'SI', 'DZ', 'LY',
               'PT', 'ES', 'SM', 'NO',
               'KI', 'ST', 'SY']
'''

country = ["FR", "EN", "ES",
           "RU", "GP", "NO",
           "NA", 'CY', "YT",
           "IT", "DK", "GR",
           "PL"]

# request for send server VUNGLE
result_2 = API_B.get(dimensions=data,
                     aggregates=data2,
                     start="2018-01-17",
                     end="2018-01-17",
                     country=country,
                     _print=False)

# parse data ...
json = json.loads(result_2)

# parse json to dict python
all_value = {}
for i, data in enumerate(json):
    all_value[i] = [data['country'], data['revenue'], data['platform']]

all_value = collections.OrderedDict(sorted(all_value.items()))

# get output result
# all_revenue for pays and device
platform = {}
platformT = {}
platform_revenu = {}
platform_revenu_total = {}


platform_revenu["android"] = API_B.find_object(all_value, "android")
platform_revenu["iOS"] = API_B.find_object(all_value, "iOS")
platform_revenu_total["Total"] = API_B.calcule_table(platform_revenu["android"], platform_revenu["iOS"])
platform['android'] = platform_revenu["android"]
platform["iOS"] = platform_revenu["iOS"]
platformT["Total"] = API_B.calcule_table(platform_revenu["android"], platform_revenu["iOS"])
platform_revenu = collections.OrderedDict(sorted(platform_revenu.items()))

# create the html output
html = API_B.generate_html(platform, platformT, platform_revenu, platform_revenu_total, country)

# save in file name 'index.html'
API_B.save("index.html", html)
