# Import libraries
from lxml import html
import requests

# Base data
base_url = "http://m.ghin.com/HLR.aspx?ghinno="
ghin_nums = ['2064561','2259440','0878514']
result = {}

# Request pages and parse specified elements
for ghin in ghin_nums:
    page = requests.get(base_url + ghin)
    tree = html.fromstring(page.content)
    name = tree.xpath('//*[@id="ctl00_cphContent_lblName"]/text()')
    handicap = tree.xpath('//*[@id="ctl00_cphContent_lblHI"]/text()')
    club = tree.xpath('//*[@id="ctl00_cphContent_lblClub"]/text()')
    result[ghin] = {
        'name': name,
        'handicap': handicap,
        'club': club
    }

# Print results to command line
# for k in result.keys():
#     print "GHIN: %s\n%r\n" % (k, result[k])
