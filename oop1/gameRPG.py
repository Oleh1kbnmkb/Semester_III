from datetime import datetime, timedelta
class Human:
  def __init__(self, title, hp, stamina, level, attack, reload) -> None:
    self.title = title
    self.hp = hp
    self.stamina = stamina
    self.level = level
    self.attack = attack
    self.reload = reload
    self.last_atack = None

  def __str__(self) -> str:
    return f"Race: {self.title}"

  def check_atatack(self):
    if self.last_atack and datetime.now()-self.last_atack < timedelta(microseconds=self.reload):
      return False
    else:
      return True


  def attack_func(self):
    if self.check_atatack():
      self.last_atack = datetime.now()
      return self.attack
    else:
      print("PLs wait")
      return 0



class Archer(Human):
  def __init__(self, level) -> None:
    self.title = "Archer"
    super().__init__(self.title, 80 + level*20, 95 + level*5, level, 40 + level*5, 3)


class Warior(Human):
  def __init__(self, level) -> None:
    self.title = "Archer"
    super().__init__(self.title, 80 + level*50, 95 + level*5, level, 200 + level*5, 5)