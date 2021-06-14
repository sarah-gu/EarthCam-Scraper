import os
import sys
import re
import requests
import json 
import yaml 




city_name = "littleitaly_hd"
counter = 3000 #if scraping gets cut off in the middle, restart by changing counter to #imgs already scraped
url = "https://www.earthcam.com/cams/common/gethofitems.php?hofsource=com&tm=ecn&camera=" + city_name + "&start=" + str(counter) + "&length=21&ec_favorite=0&cdn=0&callback=onjsonpload"
result = re.search('\[(.*?)\]',"[some_tmp_start]" )
while(result.group() != ""):
    r = requests.get(url)
    toParse = str(r.content)
    #print(toParse)
    result = re.search('\[(.*?)\]', toParse)
    toIter = result.group(1)[:-1]
    #pattern = r'doesn\'t'
    clean_string = toIter.replace('\\\'', '')
    toIter = clean_string.split('},')
    for img in toIter: 
        img += '}'
        img = img.replace('\\\"', '')
        img = img.replace("\\", "")
        #print(eval(img))
        #print(img[219:])
        img_dict = yaml.load(img)
        image_url = img_dict["image_source"]
        image_url = image_url.replace('\\','')
        r = requests.get(image_url)
        with open(city_name + '_photos/'+image_url[-20:],'wb+') as outfile:
            outfile.write(r.content)
        image_date = img_dict["date_added_plain"]
        with open(city_name + '_metadata/'+ image_url[-20:-3]+"txt" , 'w+') as metaoutfile: 
            metaoutfile.write(image_date)
        #print(image_url)
        print(image_date)
    counter += 21
    print(counter, " images have been saved")
    url = "https://www.earthcam.com/cams/common/gethofitems.php?hofsource=com&tm=ecn&camera=" + city_name + "&start=" + str(counter) + "&length=21&ec_favorite=0&cdn=0&callback=onjsonpload"
