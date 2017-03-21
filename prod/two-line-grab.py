import pyquery,sys
sys.exit(",".join([pyquery.PyQuery(url="http://m.ghin.com/HLR.aspx?ghinno="+ghin)("#ctl00_cphContent_lblHI").text() for ghin in sys.argv[1].split(",")]))
