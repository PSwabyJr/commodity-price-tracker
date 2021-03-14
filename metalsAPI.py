"""metalsAPI.py
By: Lorenzo Swaby pswabyjr@gmail.com
Date Created: 3/14/2021
Description:
Using API from www.metals-API.com for tracking/recording
prices of precious metals silver and gold."""

import commodityAPI
import requests
import error
from commodityAPI import CommodityAPI

logging.basicConfig(filename= 'PriceTrackerLog.log',level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')


class MetalsAPI(CommodityAPI):
  
  def __init__(self):
    self.apiUsed= "www.metals-API.com" #site for
    self._API_KEY= "XXXX"   #fill in API_KEY
    self.resp= none
    self._initialSetup(self)
  
  def _initialSetup(self):
    self.base_currency= 'USD'
    self.symbol= 'XAU'+ ',' +'XAG'   #XAU = Gold, XAG = Silver
    self.endpoint= 'latest'
  
  def getPricing(self):
    self.resp = requests.get(
    'https://metals-api.com/api/'+self.endpoint+
      '?access_key='+self.API_KEY+
      '&base='+self.base_currency+
      '&symbols='+self.symbol)
    
    # if something went wrong
    if self.resp.status_code != 200:
      self.getErrorStatus(self, self.resp.status_code, self.resp.json())
    else:
      return self.resp.json()   #return dictionary
     
  def getErrorStatus(self, status_code, reponse):
    logging.error("Metal-API.com request call failed.")
    logging.error("Error Status Code: " + str(status_code))
    logging.error("Error Desciption: " + response['error']['info'])
    raise APIError('GET /'+self.endpoint+'/ {}'.format(status_code))
    
