class weapon:
  def __init__(self, name, type, level=1):
    self.name=name
    self.type=type
    self.level=level
  def upgrade(self):
    self.level +=1
  def display(self):
    print(f"weapon:{self.name}, Type:{self.type},level:{self.level}")
def run():
  sword= weapon("excalibur", "sword")
  bow= weapon("longbow", "bow")
  sword.display()
  bow.display()
  sword.upgrade()
  sword.display()