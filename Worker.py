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
