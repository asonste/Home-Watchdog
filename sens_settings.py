#!/usr/bin/python
"""
asonste 12/Nov.2016
For sefining variables for each sensor
Each sensor becomes a class.
Latest change: Disable stat, as it is not beeing used.
"""

from conf import *
class sens(object):
   def __init__(self,var):
      self.var = var
      self.name = config.get(var,'name')
#      self.stat = config.get(var,'stat')
      # Settings for High High alarm
      self.HH_lims = ""
      self.HH_enable = ""
      self.HH = ""# Alarm limit
#      self.HH_stat = ""

      self.H_lims = ""
      self.H_enable = ""
      self.H = ""
#      self.H_stat = ""

      self.L_lims = ""
      self.L_enable = ""
      self.L = ""
#      self.L_stat = ""

      self.LL_lims = ""
      self.LL_enable = ""
      self.LL = ""
#      self.LL_stat = ""

   def update(self):
      #print self.var
      self.HH_Lims = config.get(self.var,'HH')
      limslist = self.HH_Lims.split(',')
      self.HH_enable = int(limslist[0])
      self.HH = float(limslist[1])
#      self.HH_stat = limslist[2]

      self.H_Lims = config.get(self.var,'H')
      limslist = self.H_Lims.split(',')
      self.H_enable = int(limslist[0])
      self.H = float(limslist[1])
#      self.H_stat = limslist[2]

      self.L_Lims = config.get(self.var,'L')
      limslist = self.L_Lims.split(',')
      self.L_enable = int(limslist[0])
      self.L = float(limslist[1])
#      self.L_stat = limslist[2]

      self.LL_Lims = config.get(self.var,'LL')
      limslist = self.LL_Lims.split(',')
      self.LL_enable = int(limslist[0])
      self.LL = float(limslist[1])
#      self.LL_stat = limslist[2]

def print_sens(x):
   print x.var
   print x.HH_enable
   print x.HH
#   print x.HH_stat

if __name__ == "__main__":
   sens1 = sens('sens1')
   sens1.update()
   print_sens(sens1)
#print sens1.HH
