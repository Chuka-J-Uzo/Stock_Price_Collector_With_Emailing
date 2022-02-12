import smtplib
import email
import sys, csv
from email.mime.multipart import MIMEMultipart
#from email.MIMEText import MIMEText
from email.headerregistry import Address
from email.message import EmailMessage
import email.encoders
import email.mime.text
import email.mime.base
from email.mime.text import MIMEText
import ast
import re
import os
import subprocess
import io
#import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


#BAE Systems, Gen Dynamics, Raytheon, Lockheed, Airbus, Boeing, Northrop Grumman, ROLLS Royce
my_urls1  = ('https://markets.ft.com/data/equities/tearsheet/summary?s=BA.:LSE')
my_urls2 = ('https://markets.ft.com/data/equities/tearsheet/summary?s=0IUC:LSE')
my_urls3 = ('https://markets.ft.com/data/equities/tearsheet/summary?s=0KU4:LSE')
my_urls4 = ('https://markets.ft.com/data/equities/tearsheet/summary?s=0R3E:LSE')
my_urls5 = ('https://markets.ft.com/data/equities/tearsheet/summary?s=0KVV:LSE')
my_urls6 = ('https://markets.ft.com/data/equities/tearsheet/summary?s=BOE:LSE')
my_urls7 = ('https://markets.ft.com/data/equities/tearsheet/summary?s=0K92:LSE')
my_urls8 = ('https://markets.ft.com/data/equities/tearsheet/summary?s=RR.:LSE')


# opening up connection, grabbing the page ###1
uClient = uReq(my_urls1)
page_html_1 = uClient.read()
uClient.close()

# opening up connection, grabbing the page ###2
uClient = uReq(my_urls2)
page_html_2 = uClient.read()
uClient.close()

# opening up connection, grabbing the page ###3
uClient = uReq(my_urls3)
page_html_3 = uClient.read()
uClient.close()

# opening up connection, grabbing the page ###4
uClient = uReq(my_urls4)
page_html_4 = uClient.read()
uClient.close()

# opening up connection, grabbing the page ###5
uClient = uReq(my_urls5)
page_html_5 = uClient.read()
uClient.close()

# opening up connection, grabbing the page ###6
uClient = uReq(my_urls6)
page_html_6 = uClient.read()
uClient.close()

# opening up connection, grabbing the page ###7
uClient = uReq(my_urls7)
page_html_7 = uClient.read()
uClient.close()

# opening up connection, grabbing the page ###8
uClient = uReq(my_urls8)
page_html_8 = uClient.read()
uClient.close()



#html parsing html
page_soup_1 = soup(page_html_1, "html.parser")
page_soup_2 = soup(page_html_2, "html.parser")
page_soup_3 = soup(page_html_3, "html.parser")
page_soup_4 = soup(page_html_4, "html.parser")
page_soup_5 = soup(page_html_5, "html.parser")
page_soup_6 = soup(page_html_6, "html.parser")
page_soup_7 = soup(page_html_7, "html.parser")
page_soup_8 = soup(page_html_8, "html.parser")


#Grabs all item containers on a page

#BAE Shares ONLY 1
containers = page_soup_1.findAll("div", {"class":"mod-tearsheet-overview__quote"})

for container in containers:  
    price1 = container.findAll("span", {"class":"mod-ui-data-list__label"})
    price_label = price1[0].text

    price2 = container.findAll("span", {"class":"mod-ui-data-list__value"})
    price_value = price2[0].text


containers2 = page_soup_1.findAll("div", {"class":"mod-tearsheet-overview__header"})
for container in containers2:
    company_name = container.findAll("h1", {"class":"mod-tearsheet-overview__header__name mod-tearsheet-overview__header__name--large"})
    company1 = company_name[0].text


#GENERAL Dynamics Shares ONLY 2
containers3 = page_soup_2.findAll("div", {"class":"mod-tearsheet-overview__quote"})

for container in containers3:  
    price1_3 = container.findAll("span", {"class":"mod-ui-data-list__label"})
    price_label3 = price1_3[0].text

    price2_3 = container.findAll("span", {"class":"mod-ui-data-list__value"})
    price_value_3 = price2_3[0].text


containers2_3 = page_soup_2.findAll("div", {"class":"mod-tearsheet-overview__header"})
for container in containers2_3:
    company_name_3 = container.findAll("h1", {"class":"mod-tearsheet-overview__header__name mod-tearsheet-overview__header__name--large"})
    company1_3 = company_name_3[0].text


#RAYTHEON Shares ONLY 3
RAYTHEON_1 = page_soup_3.findAll("div", {"class":"mod-tearsheet-overview__quote"})

for container in RAYTHEON_1:  
    RAYTH_price = container.findAll("span", {"class":"mod-ui-data-list__label"})
    RAY_price_label = RAYTH_price[0].text

    RAYTH_val = container.findAll("span", {"class":"mod-ui-data-list__value"})
    RAY_value = RAYTH_val[0].text


RAYTHEON_2 = page_soup_3.findAll("div", {"class":"mod-tearsheet-overview__header"})
for container in RAYTHEON_2:
    RAY_comp_name = container.findAll("h1", {"class":"mod-tearsheet-overview__header__name mod-tearsheet-overview__header__name--large"})
    RAY_company = RAY_comp_name[0].text

    

#LOCKHEED Martin Shares ONLY 4
LOCKHEED_1 = page_soup_4.findAll("div", {"class":"mod-tearsheet-overview__quote"})

for container in LOCKHEED_1:  
    LOCKH_price = container.findAll("span", {"class":"mod-ui-data-list__label"})
    LOCKH_price_label = LOCKH_price[0].text

    LOCKH_val = container.findAll("span", {"class":"mod-ui-data-list__value"})
    LOCKH_value = LOCKH_val[0].text


LOCKHEED_2 = page_soup_4.findAll("div", {"class":"mod-tearsheet-overview__header"})
for container in LOCKHEED_2:
    LOCKH_comp_name = container.findAll("h1", {"class":"mod-tearsheet-overview__header__name mod-tearsheet-overview__header__name--large"})
    LOCKH_company = LOCKH_comp_name[0].text



#AIRBUS Shares ONLY 5 
AIRBUS_1 = page_soup_5.findAll("div", {"class":"mod-tearsheet-overview__quote"})

for container in AIRBUS_1:  
    AIRB_price = container.findAll("span", {"class":"mod-ui-data-list__label"})
    AIRB_price_label = AIRB_price[0].text

    AIRB_val = container.findAll("span", {"class":"mod-ui-data-list__value"})
    AIRB_value = AIRB_val[0].text


AIRBUS_2 = page_soup_5.findAll("div", {"class":"mod-tearsheet-overview__header"})
for container in AIRBUS_2:
    AIRB_comp_name = container.findAll("h1", {"class":"mod-tearsheet-overview__header__name mod-tearsheet-overview__header__name--large"})
    AIRB_company = AIRB_comp_name[0].text



#BOEING Shares ONLY 6 
BOEING_1 = page_soup_6.findAll("div", {"class":"mod-tearsheet-overview__quote"})

for container in BOEING_1:  
    BOE_price = container.findAll("span", {"class":"mod-ui-data-list__label"})
    BOE_price_label = BOE_price[0].text

    BOE_val = container.findAll("span", {"class":"mod-ui-data-list__value"})
    BOE_value = BOE_val[0].text


BOEING_2 = page_soup_6.findAll("div", {"class":"mod-tearsheet-overview__header"})
for container in BOEING_2:
    BOE_comp_name = container.findAll("h1", {"class":"mod-tearsheet-overview__header__name mod-tearsheet-overview__header__name--large"})
    BOEING_company = BOE_comp_name[0].text



#Northrop Grumman Shares ONLY 7
NORTHROP_GM_1 = page_soup_7.findAll("div", {"class":"mod-tearsheet-overview__quote"})

for container in NORTHROP_GM_1:  
    NORT_price = container.findAll("span", {"class":"mod-ui-data-list__label"})
    NORT_price_label = NORT_price[0].text

    NORT_val = container.findAll("span", {"class":"mod-ui-data-list__value"})
    NORT_value = NORT_val[0].text


NORTHROP_GM_2 = page_soup_7.findAll("div", {"class":"mod-tearsheet-overview__header"})
for container in NORTHROP_GM_2:
    NORT_comp_name = container.findAll("h1", {"class":"mod-tearsheet-overview__header__name mod-tearsheet-overview__header__name--large"})
    NORTHROP_company = NORT_comp_name[0].text



#ROLLS Royce Shares ONLY 8
ROLLSROYCE_1 = page_soup_8.findAll("div", {"class":"mod-tearsheet-overview__quote"})

for container in ROLLSROYCE_1:  
    ROLLS_price = container.findAll("span", {"class":"mod-ui-data-list__label"})
    ROLLS_price_label = ROLLS_price[0].text

    ROLLS_val = container.findAll("span", {"class":"mod-ui-data-list__value"})
    ROLLS_value = ROLLS_val[0].text


ROLLSROYCE_2 = page_soup_8.findAll("div", {"class":"mod-tearsheet-overview__header"})
for container in ROLLSROYCE_2:
    ROLLS_comp_name = container.findAll("h1", {"class":"mod-tearsheet-overview__header__name mod-tearsheet-overview__header__name--large"})
    ROLLSROYCE_company = ROLLS_comp_name[0].text


 ##########   
    

smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)


me =  'Data Bot <your full email>'
you = "recepient's full email"


# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Defense Stocks | Freshly Pressed"
msg['From'] = me
msg['To'] = you


#specifiy the module location for import
sys.path.extend(["C:\folder\Webscrp_send_experiments"])
    

#####
text = "Values at your fingertips"
html = """\
<html>
<body>
  <h1>News Brew 2.0 <img src="https://cdn.pixabay.com/photo/2018/08/30/16/57/coffee-3642712_960_720.png" width=40 height=40></h1> 
  <p>What's in today's numbers?</p>
  
  <hr>
  
  <h3><font color="blue"> Global Stock Values of Defense Companies: </font></h3>
    <small><p>Here are <b>stock values </b> from top defence companies.<br></small>
  <hr>
  <br>
  <p><img src="http://www.carlogos.org/logo/Rolls-Royce-text-logo-640x127.jpg" width=130 height=25></P>  
  """ + ROLLSROYCE_company + " | " + ROLLS_price_label + ":" + " " + """ <font color="red"><b>""" + "£"+ ROLLS_value + """</b></font></p>
  <br>
  <br>
  <small> Rolls-Royce is a United Kingdom-based engineering company focused on power and propulsion systems.</small>
  <hr>

  <br>
  <p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/BAE_Systems_logo.svg/320px-BAE_Systems_logo.svg.png" width=130 height=25></P>  
  """ + company1 + " | " + price_label + " : " + "  " + """ <font color="red"><b>""" +"£"+ price_value + """</b></font></p>
  <br>
  <br>
  <small> BAE Systems plc is a British multinational defence, security, and aerospace company. Its headquarters are in London </small>
  <hr>

  <br>
  <p><img src="http://www.stickpng.com/assets/images/58ee8d113545163ec1942cd3.png" width=130 height=25></P>  
  """ + BOEING_company + " | " + BOE_price_label + " : " + "  " + """ <font color="red"><b>""" +"$"+ BOE_value + """</b></font></p>
  <br>
  <br>
  <small> Boeing is an American multinational corporation that designs, manufactures, and sells airplanes, rotorcraft, rockets, satellites, and missiles worldwide. </small>
  <hr>

  <br>
  <p><img src="https://purepng.com/public/uploads/large/purepng.com-lockheed-martin-logologobrand-logoiconslogos-251519939105mamef.png" width=130 height=25></P>  
  """ + LOCKH_company + " | " + LOCKH_price_label + " : " + "  " + """ <font color="red"><b>""" +"$"+ LOCKH_value + """</b></font></p>
  <br>
  <br>
  <small> Lockheed Martin is a security and aerospace company that operates through four segments. Aeronautics segment (research, design, development, manufacture, integration...)  </small>
  <hr>

  <br>
  <p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Northrop_Grumman.svg/2000px-Northrop_Grumman.svg.png" width=130 height=25></P>
  """ + NORTHROP_company + " | " + NORT_price_label + " : " + "  " + """ <font color="red"><b>""" +"$"+ NORT_value + """</b></font></p>
  <br>
  <br>
  <small> Northrop Grumman is a global security company, providing products, systems and solutions in; cyber; command, control, comms and computers, intel, surveillance & reco... </small>
  <hr>

  <br>
  <p><img src="https://idraintheswamp.com/wp-content/uploads/2017/02/pngpix-com-general-dynamics-logo-png-transparent.png" width=130 height=25></P>  
  """ + company1_3 + " | " + price_label3 + " : " + "  " + """ <font color="red"><b>""" +"$"+ price_value_3 + """</b></font></p>
  <br>
  <br>
  <small> General Dynamics is a global aerospace and defense company offering a portfolio of products and services in business aviation; combat vehicles, weapons systems and munitions; info technology (IT) </small>
  <hr>

  <br>
  <br>
  <small> Raytheon specializes in defense and other government markets. It develops integrated products, services and solutions in various markets, including sensing; effects; command.... </small>
  <hr>

  <br>
  <p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Logo_Airbus_2014.svg/799px-Logo_Airbus_2014.svg.png" width=130 height=25></P>  
  """ + AIRB_company + " | " + AIRB_price_label + " : " + "  " + """ <font color="red"><b>""" + "€" + AIRB_value + """</b></font></p>
  <br>
  <br>
  <small> Airbus SE, formerly Airbus Group SE, is a company based in the Netherlands that is active in the aerospace and defense industry.  Airbus Commercial Aircraft, Airbus Helicopters and Airbus Defense & Space</small>
  <hr>


  
  <br>
  <br>
  <br>
  <br>
 
<footer>
  <p>Brewed by: <b>Data Bot</b></p>
  <p>Contact information: <a href="mailto:databot@tester.com">databot@tester.com</a>.</p>
</footer>

<p><strong>Note:</strong> <kbd>Mail is optimized for quick viewing, but we cannot warrant full correctness of all content. Copyright 2018-2019 by Data Bot. All Rights Reserved..</kbd></p>

        
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#s.starttls()
s.login("your full email here", "password of email here")
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()
