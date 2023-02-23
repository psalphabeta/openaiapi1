#import os
#clear = lambda: os.system('cls')
#clear()
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
st.title('Uber pickups in NYC')
#@title **Provide Complete Path Of The API Key Here**

API_Path = "Pipal.json" #@param {type:"string"}

from oauth2client.service_account import ServiceAccountCredentials
import httplib2
#@st.cache
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
#print('*'*50);print("Scopes & Endpoint Configured...");print('*'*50);print("Adding Key...");print('*'*50);
# service_account_file.json is the private key that you created for your service account.
JSON_KEY_FILE = API_Path
#print("Key Added Successfully!");print('*'*50);
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())
#print("Credentials Successfully Authorized!");print('*'*50);

#@title **Replace Your Post/Page URL and Run the Code**
#@markdown Site URL will the exact URL you want to update or delete from the Google Search Index. **Also, please make a note that you have to provide URL only for the ownership verfied website. For any other URLs, it will not work.**
#st.stop()
#form = st.form(key='my_form',clear_on_submit=True)
with st.form('Form1',clear_on_submit=True):
     siteURL = st.text_input("Your URL here ") #@param {type:"string"}
     forupdate = "URL_UPDATED"
     fordelete = "URL_DELETED"
     option = st.selectbox( 'Choose the operation :', ("URL_UPDATED", "URL_DELETED")) 
     submit_button = st.form_submit_button(label='Submit')
requestType = option
#requestType = "URL_UPDATED" #@param ["URL_UPDATED", "URL_DELETED"]
content = str({'url':siteURL,'type':requestType})
#print("RESULT:");print('*'*50);print("URL and Update Request Type Configured!");print('*'*50);
response, content = http.request(ENDPOINT, method="POST", body=content)
#output = st.write(response['status'])
#if output == '200':
if submit_button:
  if response['status'] == '200':
     st.write("Status",response['status'],"Successfully Done!");  
     #st.write("Successfully Done!");print('*'*50);
     #st.write(response);
     st.write("You Submitted: ",siteURL,"  for ", option);
  else:
      st.write("Error Code: ", response['status'])
      #st.write(response['status']);#.format(output));print('*'*50);
      #st.write(response);
      st.write("Can't Submit: ",siteURL,"  for ", option);
      st.write("Visit here for more details: https://developers.google.com/search/apis/indexing-api/v3/core-errors#api-errors");
  #print('*'*50);

else:
     st.write("Note: Submit complete URL with https://, www, etc");
#clear = lambda: os.system('cls')
#clear()
