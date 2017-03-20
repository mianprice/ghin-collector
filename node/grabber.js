var request = require('request');
var cheerio = require('cheerio');
var fs = require('fs');
var result = {};
var ghin_nums = ['2064561','2259440','0878514'];

ghin_nums.forEach(function(ghin_num) {
  request('http://m.ghin.com/HLR.aspx?ghinno=' + ghin_num, function(error, response, body) {
    console.log("Error: ", error);
    console.log("StatusCode: ", response && response.statusCode);
    // console.log("Body: ", body);
    // fs.writeFile('page.html', body, 'utf8');
    $ = cheerio.load(body);
    var h = $("#ctl00_cphContent_lblHI").text();
    h = parseFloat(h);
    var n = $("#ctl00_cphContent_lblName").text();
    var c = $("#ctl00_cphContent_lblClub").text();
    result[ghin_num] = {name: n, handicap: h, club: c};
    console.log(result);
  });
});
