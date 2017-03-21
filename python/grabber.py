# Import library
from pyquery import PyQuery as pq

# Base data
base_url = "http://m.ghin.com/HLR.aspx?ghinno="
ghin_nums = ['2064561','2259440','0878514']
result = {}

# Request pages and parse specified data
for ghin in ghin_nums:
    d = pq(url = base_url + ghin)
    h = d("#ctl00_cphContent_lblHI").text();
    n = d("#ctl00_cphContent_lblName").text();
    c = d("#ctl00_cphContent_lblClub").text();
    result[ghin] = {
        'name': n,
        'handicap': h,
        'club': c
    }

# Print results to command line
# for k in result.keys():
#     print "GHIN: %s\n%r\n" % (k, result[k])
