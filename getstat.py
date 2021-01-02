import urllib.request
import pandas as pd
from datetime import datetime
import os

url = "https://rpi-imager-stats.raspberrypi.org"
prefix = datetime.today().strftime('%Y%m%d')

os.system("git pull")

fp = urllib.request.urlretrieve(url, "stats.html")
html = pd.read_html("stats.html")

tbl1 = html[0]
tbl2 = html[1]
tbl3 = html[2]
tbl4 = html[3]
tbl5 = html[4]
tbl6 = html[5]

#print(tbl1)
#print(tbl2)
#print(tbl3)
#print(tbl4)
#print(tbl5)
#print(tbl6)

ostoday = prefix + "_os_today.csv"
osweek = prefix + "_os_week.csv"
osmonth = prefix + "_os_month.csv"
imagetoday = prefix + "_image_today.csv"
imageweek = prefix + "_image_week.csv"
imagemonth = prefix + "_image_month.csv"

tbl1.to_csv(ostoday, index=False)
tbl2.to_csv(osweek, index=False)
tbl3.to_csv(osmonth, index=False)
tbl4.to_csv(imagetoday, index=False)
tbl5.to_csv(imageweek, index=False)
tbl6.to_csv(imagemonth, index=False)

os.system("git add stats.html")
os.system("git add " + ostoday + " " + osweek + " " + osmonth)
os.system("git add " + imagetoday + " " + imageweek + " " + imagemonth)
os.system("git commit -m 'Today stats'")
os.system("git push")
