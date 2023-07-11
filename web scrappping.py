#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origins
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq


# In[2]:


pip install flask_cors


# In[7]:


from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq


# In[1]:


searchstring = "iphone13"


# In[2]:


flipkart_url = "https://www.flipkart.com/search?q=" + searchstring


# In[3]:


flipkart_url


# In[8]:


uclient = uReq(flipkart_url)


# In[9]:


uclient                                                #it'll click the flipkart url automatically for python


# In[10]:


flipkartpage = uclient.read()                                          #will recieve a html corpos


# In[ ]:





# In[11]:


flipkart_html = bs(flipkartpage, "html.parser")                                                    #beautify the html corpos


# In[12]:


flipkart_html


# In[13]:


'https://www.flipkart.com/apple-iphone-13-midnight-128-gb/p/itmca361aab1c5b0?pid=MOBG6VF5Q82T3XRS&lid=LSTMOBG6VF5Q82T3XRSOXJLM9&marketplace=FLIPKART&q=iphone+13&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=f19e3ff0-0960-415a-b7bb-b25bca75bfdb.MOBG6VF5Q82T3XRS.SEARCH&ppt=hp&ppn=homepage&ssid=jc27yb3j1c0000001688981578527&qH=c68a3b83214bb235'


# In[14]:


"https://www.flipkart.com/apple-iphone-13-pink-128-gb/p/itm6e30c6ee045d2?pid=MOBG6VF5GXVFTQ5Y&amp;lid=LSTMOBG6VF5GXVFTQ5YSGQY4O&amp;marketplace=FLIPKART&amp;q=iphone13&amp;store=tyy%2F4io&amp;srno=s_1_3&amp;otracker=search&amp;fm=organic&amp;iid=83f3b320-be83-458b-a6b4-58794d54931e.MOBG6VF5GXVFTQ5Y.SEARCH&amp;ppt=None&amp;ppn=None&amp;ssid=4o2yofxq4w0000001688981855513&amp;qH=7d4afaedfc628b80"


# In[15]:


bigboxes = flipkart_html.findAll("div", {'class':'_1AtVbE col-12-12'})


# In[16]:


len(bigboxes)


# In[17]:


box = bigboxes[5]


# In[18]:


box.div


# In[19]:


box.div.div


# In[20]:


box.div.div.div.a


# In[21]:


box.div.div.div.a['href']


# In[22]:


"https://www.flipkart.com"+box.div.div.div.a['href']


# In[23]:


productlink = "https://www.flipkart.com"+box.div.div.div.a['href']


# In[24]:


productreq = requests.get(productlink)


# In[25]:


productreq


# In[26]:


productreq.text


# In[27]:


bs(productreq.text,"html.parser")


# In[28]:


prod_html = bs(productreq.text,"html.parser")


# In[29]:


prod_html.find_all('div',{"class":"_16PBlm"})


# In[30]:


comment_box = prod_html.find_all('div',{"class":"_16PBlm"}) 


# In[31]:


len(comment_box)


# In[32]:


comment_box[1]


# In[33]:


comment_box[1].div.div.div.div.text


# In[34]:


for i in comment_box:
    print(i.div.div.div.div.text)                           # to findout the rating 


# In[35]:


comment_box[1].div.div.find_all("div" ,{"class" : ""})


# In[36]:


comment_box[1].div.div.find_all("div" ,{"class" : ""})[0].div.text


# In[37]:


for i in comment_box:
    print(i.div.div.find_all("div" ,{"class" : ""})[0].div.text)
    print("\n")                                                               #to find out the review


# In[38]:


comment_box[1].div.div.find_all("p" , {"class" :"_2sc7ZR _2V5EHH" })[0].text


# In[39]:


for i in comment_box:
    print(i.div.div.find_all("p" , {"class" :"_2sc7ZR _2V5EHH" })[0].text)


# In[ ]:




