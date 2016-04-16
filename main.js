function computeSunrise(e,t){var n=-9.135499;var r=38.707126;var i=90.83333333333333;var s=Math.PI/180;var o=180/Math.PI;var u=n/15;var a;if(t){a=e+(6-u)/24}else{a=e+($
function dayOfYear(){var e=Math.floor((new Date).setFullYear((new Date).getFullYear(),0,1)/864e5);var t=Math.ceil((new Date).getTime()/864e5);var n=t-e;return n}
Highcharts.setOptions({global:{useUTC:false}});options={chart:{renderTo:"content",type:"spline"},title:{text:"Temperatures"},subtitle:{text:""},xAxis:{type:"datetime",$
function GetUrlPath(){urlPath=window.location.pathname.split(".")[0].substring(1).split("/")[1];if(urlPath=="humidity"){return"humid"}else{return"temperature"}}
function GetUrlParameter(){idx=window.location.href.indexOf("?");if(idx<0)return"";return window.location.href.substring(idx+1)}
function GetChartXml(){switch(urlParameter){case"3h":case"48h":case"1w":case"1m":case"3m":case"1y":return""+urlPath+urlParameter+".xml"}return""+urlPath+"24h$
function GetBandsNumber(){switch(urlParameter){case"3h": return 0;case"48h": return 2;case"1w": return 8;case"1m": return 31;case"3m": return 0;case"1y": return 0}retu$
function GetChartTitle(){var e="Temperatures";if(urlPath=="humid"){e="Humidity"}switch(urlParameter){case"3h":return e+" of the last 3 hours";case"48h":return e+" of t$
urlPath="DS18B20";
urlParameter=GetUrlParameter();
