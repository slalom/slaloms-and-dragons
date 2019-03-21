class ability ():
  def __init__(self, ID, name, description):
    self.ID = ID
    self.name = name
    self.description = description
    
  def GetName(self):
    return self.name
  
  def GetDescription(self):
    return self.description

  