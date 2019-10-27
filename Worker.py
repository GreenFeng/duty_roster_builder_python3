"""
@purpose: to enable the worker class
@author: green hui
@version:1.0
"""

class Worker(object):
  def __init__(self,name,worktime):
    self.name=name
    self.worktime=worktime
    self.state=True

  def set_work(self,day,period):
    self.worktime[day,period]=True

  def stop_work(self):
    self.state=False

  def couldwork(self):
    return self.state

  def could_setwork(self,day,period):
    return self.worktime[day,period]

  def __str__(self):
    return str(self.name)+str(self.worktime)