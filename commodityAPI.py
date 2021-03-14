"""commodityAPI.py
By: Lorenzo Swaby pswabyjr@gmail.com
Date Created: 3/14/2021
Description:
Commodity API class structure to accommodate
using Price APIs for the child classes."""

class CommodityAPI:

  def __init__(self):
    self.apiUsed = "blank"
    self.API_KEY = "blank"
    self._initialSetup(self)
    
  def _initialSetup(self):
  
  def getPricing(self):
    pass
 
  def getErrorStatus(self):
    pass
