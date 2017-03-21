# Import libraries
from pyquery import PyQuery as pq
import sys

# Base data
base_url = "http://m.ghin.com/HLR.aspx?ghinno="
result = []

# Parse arguments
ghin_input = sys.argv[1]
ghin_nums = ghin_input.split(",")

# Request pages and parse specified data
for ghin in ghin_nums:
    d = pq(url = base_url + ghin)
    h = d("#ctl00_cphContent_lblHI").text();
    result.append(h)

# Send results back to PHP
output_string = ",".join(result)
sys.exit(output_string)
