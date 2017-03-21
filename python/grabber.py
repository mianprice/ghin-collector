from pyquery import PyQuery as pq

base_url = "http://m.ghin.com/HLR.aspx?ghinno="
ghin_nums = ['2064561','2259440','0878514']
result = {}

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

for k in result.keys():
    print "GHIN: %s\n%r\n" % (k, result[k])
