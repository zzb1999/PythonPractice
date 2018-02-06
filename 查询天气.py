#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import json
import jsonpath

def searchWeather(city):
    """
    查询天气
    :param city: 城市名
    返回python形式的unicode字符串
    """
    city = urllib.urlencode({"city":city})
    url = "http://www.sojson.com/open/api/weather/json.shtml?" + city
    headers = {"User-Agent":"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0"}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    jsondata = response.read()
    return jsondata


def strHandle(jsondata):
    # 转换成python形式的unicode字符串
    unicodestr = json.loads(jsondata)
    # 查询状态码
    status = jsonpath.jsonpath(unicodestr, "$..status")
    # print status
    # 城市
    city = jsonpath.jsonpath(unicodestr, "$..city")[0]
    shidu = jsonpath.jsonpath(unicodestr, "$..shidu")[0]
    pm25 = jsonpath.jsonpath(unicodestr, "$..pm25")[0]
    pm10 = jsonpath.jsonpath(unicodestr, "$..pm10")[0]
    quality = jsonpath.jsonpath(unicodestr, "$..quality")[0]
    wendu = jsonpath.jsonpath(unicodestr, "$..wendu")[0]
    ganmao = jsonpath.jsonpath(unicodestr, "$..ganmao")[0]

    # 预测
    # date = jsonpath.jsonpath(unicodestr, "$..forecast[0].date")
    # print date
    data = {
        "status": status,
        "city": city.encode('utf-8'),
        "shidu": shidu.encode('utf-8'),
        "pm25": pm25,
        "pm10": pm10,
        "quality": quality.encode('utf-8'),
        "wendu": wendu,
        "ganmao": ganmao.encode('utf-8'),
    }
    return data




def main():
    city = raw_input("请输入要查询天气的城市:")
    jsondata = searchWeather(city)
    data = strHandle(jsondata)
    print "城市：%s" % data['city']
    print "湿度：%s" % data['shidu']
    print "pm2.5：%s" % data['pm25']
    print "pm1.0：%s" % data['pm10']
    print "空气质量：%s" % data['quality']
    print "感冒：%s" % data['ganmao']
    print "-"*30


if __name__ == "__main__":
    main()
