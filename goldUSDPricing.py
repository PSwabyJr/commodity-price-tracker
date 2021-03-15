"""goldUSDPricing.py
By: Lorenzo Swaby pswabyjr@gmail.com
Date Created: 3/15/2021
Description:
Child class of Commodity that tracks the price of gold in USD.
"""
import commodity
from commodity import Commodity
#TODO: Add an import library for dealing with .json files saving the price of gold 

class GoldUSDPricing(Commodity):
  
  fileName= "gold_pricing.json"
  symbolTicker= "XAU"  
  
  #TODO: fill in the functions after developing json library for handing json files
