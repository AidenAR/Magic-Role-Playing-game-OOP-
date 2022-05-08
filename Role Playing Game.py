
import check
import math

##Constants:
increase_factor = 0.1
punch_factor_st = 2


class Character:
  ''' 
  Fields: 
     name(Str) 
     st(Nat)
     hp(Nat)
     max_hp(Nat)
     mp(Nat)
     max_mp(Nat)
     level(Nat)
     
  Requires:  
     st, max_hp are both strictly greater than 0.
  '''
  def __init__(self, new_name, strength, 
               maximumHP, maximumMP):
    '''
    Initializes a Character object self with 
    name new_name, st strength,
    hp and max_hp of maximumHP, and
    mp and max_mp of maximumMP, and
    level should start at 1.
    
    Effects: Mutates self
    
    __init__: Character Str Nat Nat Nat -> None
    Requires
      0 < strength, maximumHP, level
      maximumHP > hp
      maximumMP > mp
    '''
    self.name = new_name
    self.st = strength
    self.hp = maximumHP
    self.max_hp = maximumHP
    self.mp = maximumMP
    self.max_mp = maximumMP
    self.level = 1

    
  def __eq__(self, other):
    '''
    Returns True if self and other are equal and False otherwise
    
    __eq__: Character Any -> Bool
    '''
    return isinstance(other, Character) and \
        self.name == other.name and \
        self.st == other.st and \
        self.hp == other.hp and \
        self.max_hp == other.max_hp and \
        self.mp == other.mp and \
        self.max_mp == other.max_mp and \
        self.level == other.level

  
  def __repr__(self):
    '''
    Returns a string representation of self
    
    __repr__: Character -> Str
    '''
    game_string = ("{0.name}"
                   "\nLevel: {0.level}"
                   "\nStrength: {0.st}"
                   "\nHP: {0.hp}/{0.max_hp}"
                   "\nMP: {0.mp}/{0.max_mp}")
    return game_string.format(self)

  
  def cast_spell(self, cost, damage, enemy):
    '''
    Casts a spell if self is able that requires cost mp to cast and
    deals damage to enemy. A message is printed if the enemy is 
    defeated or there was not enough mp to cast the spell.
    
    Effects: 
       Prints to screen
       Mutates self
       Mutates enemy
    
    cast_spell: Character Nat Nat Character -> None
    
    Examples:
       c = Character("Test", 1, 4, 5)
       e = Character("Test", 1, 4, 5)
       c.cast_spell(3, 10, e) => None
       and e.hp is mutated to 0
       and c.mp is mutated to 2
       and "Enemy defeated" is printed (no quotes).
       
       c = Character("Test", 1, 4, 5)
       e = Character("Test", 1, 4, 5)
       c.cast_spell(13, 10, e) => None
       and "Not enough MP" is printed (no quotes).
       
       c = Character("Test", 1, 4, 5)
       e = Character("Test", 1, 4, 5)
       c.cast_spell(3, 2, e) => None
       and e.hp is mutated to 2
       and c.mp is mutated to 2
    '''
    error_msg = "Not enough MP"
    defeated_msg = "Enemy defeated"
    if self.mp < cost:
      print(error_msg)
    if enemy.hp <= 0:
      print(defeated_msg)
    if (self.mp >= cost) and (enemy.hp > 0):
      self.mp = self.mp - cost
      enemy.hp = enemy.hp - damage
      if enemy.hp <= 0:
        enemy.hp = 0
        print(defeated_msg)


  def level_up(self):
    '''
    Performs a level-up for self. Increase stats 10% plus 1
    via mutation of self.
    
    Effects: Mutates self
    
    level_up: Character -> None
    
    Examples:
       c = Character("Test", 1, 4, 5)
       c.level_up() => None
       and c.level is mutated to 2
       and c.st is mutated to 2
       and c.hp is mutated to 5
       and c.max_hp is mutated to 5
       and c.mp is mutated to 6
       and c.max_mp is mutated to 6
    '''
    self.level = self.level + 1
    st_increase = math.floor(increase_factor * self.st) + 1
    self.st = self.st + st_increase
    hp_increase = math.floor(increase_factor * self.max_hp) + 1
    self.max_hp = self.max_hp + hp_increase
    self.hp = self.hp + hp_increase
    mp_increase = math.floor(increase_factor * self.max_mp) + 1
    self.max_mp = self.max_mp + mp_increase
    self.mp = self.mp + mp_increase


def all_punch(players, enemy):
  '''
  Returns None but simulates all the characters (players) 
  in the list of characters, players, punching an enemy 
  character. Each Character in players will hit the enemy
  mutating enemy, by dealing damage to them and thus,
  decreasing their hp by twice the, st, strength statistic
  of each individual Character in players, and if the
  enemy runs out of hp, their hp is set to 0, and each 
  character in players is mutated by levelling up. 
  
  Effects: Mutates players
           Mutates enemy
  
  all_punch: (listof Character) Character -> None
  Requires: enemy cannot be a member of the list of 
              characters, players. 
            for each player in the list and the enemy
              the following must hold:
               0 < strength, maximumHP, level
               maximumHP > hp
               maximumMP > mp
  
  Examples:
     d1 = Character("C1", 10, 10, 10)
     d2 = Character("C2", 1, 10, 10)
     d3 = Character("C3", 20, 20, 10)
     e2 = Character("E2", 20, 20, 10)
     L = [d1, d2, d3]
     all_punch(L, e2) => None
     and e.hp is mutated to 0
     and all of all of d1, d2, d3 have levelled up.
     
     all_punch([], e2) => None
     and no mutation occurs
  '''
  for character in players:
    player_st = (character.st * punch_factor_st)
    enemy.hp = enemy.hp - player_st
  if enemy.hp <= 0:
    enemy.hp = 0
    for character in players:
      character.level_up()


##The following are defined for testing purposes.
c1 = Character("Fay", 12, 10, 11)
c2 = Character("Jay", 11, 99, 97)
d1 = Character("C1", 10, 10, 10)
d2 = Character("C2", 1, 10, 10)
d3 = Character("C3", 20, 20, 10)
d4 = Character("C4", 1, 12, 13)
d5 = Character("C5", 1, 20, 15)
d6 = Character("C6", 1, 15, 17)
d7 = Character("C7", 3, 13, 15)
d8 = Character("C8", 10, 20, 15)
d9 = Character("C4", 1, 12, 13)

e1 = Character("E1", 2, 5, 10)
e2 = Character("E2", 20, 20, 10)
e3 = Character("E3", 20, 30, 10)
e4 = Character("E4", 20, 30, 20)
e5 = Character("E5", 20, 15, 20)
e6 = Character("E6", 100, 100, 20)
e7 = Character("E7", 100, 58, 20)
e8 = Character("E8", 100, 500, 20)
e9 = Character("E9", 100, 90, 20)
e10 = Character("E7", 100, 58, 20)

L = [d1, d2, d3]
A = [d4, d5]
B = [d6, d7, d8]
C = [d2, d3, d7]
D = [d2, d3, d4, d5, d7, d8]


##Examples:

##Sample Example for  __init__ :

check.expect("Example 1: __init__ e7 name", e7.name, "E7")
check.expect("Example 1: __init__ e7 strength", e7.st, 100)
check.expect("Example 1: __init__ e7 HP", e7.hp, 58)
check.expect("Example 1: __init__ e7 maximumHP", e7.max_hp, 58)
check.expect("Example 1: __init__ e7 maximumMP", e7.max_mp, 20)
check.expect("Example 1: __init__ e7 mp", e7.mp, 20)
check.expect("Example 1: __init__ e7 level", e7.level, 1)


##Sample Example for __eq__:

check.expect("Example 1: __eq__ True", e7 == e10, True)
check.expect("Example 2: ___eq__ False", e3 == e7, False)


##Sample Example for  __repr__:

check.set_print_exact(
  "E7",
  "Level: 1",
  "Strength: 100",
  "HP: 58/58",
  "MP: 20/20",)
check.expect("Example  __repr__", print(e7), None)
check.expect("Example  __repr__ Alternate", str(e7),
             ("E7\nLevel: 1\nStrength: 100"
              "\nHP: 58/58\nMP: 20/20"))


##Sample Examples for cast_spell:

c = Character("Test", 1, 4, 5)
e = Character("Test", 1, 4, 5)
check.set_print_exact("Enemy defeated")
check.expect("Example 1: cast_spell: Enemy Defeated",
             c.cast_spell(3, 10, e), None)
check.expect("Example 1: cast_spell: e mutation", e.hp, 0)
check.expect("Example 1: cast_spell: c mutation", c.mp, 2)

c = Character("Test", 1, 4, 5)
e = Character("Test", 1, 4, 5)
check.set_print_exact("Not enough MP")
check.expect("Example 2: cast_spell: Not enough MP",
             c.cast_spell(13, 10, e), None)
check.expect("Example 2: cast_spell: No e mutation", e.hp, 4)
check.expect("Example 2: cast_spell: No c mutation", c.mp, 5)

c = Character("Test", 1, 4, 5)
e = Character("Test", 1, 4, 5)
check.expect("Example 3: cast_spell: Spell Cast but enemy hp not 0",
             c.cast_spell(3, 2, e), None)
check.expect("Example 3: cast_spell: e mutation", e.hp, 2)
check.expect("Example 3: cast_spell: c mutation", c.mp, 2)


##Sample Example for level_up:

c = Character("Test", 1, 4, 5)
check.expect("Example 1: level_up",  c.level_up(), None)
check.expect("Example 1 level_up: Mutation: c level", c.level, 2)
check.expect("Example 1 level_up: Mutation: c st", c.st, 2)
check.expect("Example 1 level_up: Mutation: c hp", c.hp, 5)
check.expect("Example 1 level_up: Mutation: c max_hp", c.max_hp, 5)
check.expect("Example 1 level_up: Mutation: c mp", c.mp, 6)
check.expect("Example 1 level_up: Mutation: c max_mp", c.max_mp, 6)

c0 = Character("Test", 0, 0, 0)
check.expect("Example 2: level_up c0", c0.level_up(), None)
check.expect("Example 2 level_up: Mutation: c0 level", c0.level, 2)
check.expect("Example 2 level_up: Mutation: c0 st", c0.st, 1)
check.expect("Example 2 level_up: Mutation: c0 hp", c0.hp, 1)
check.expect("Example 2 level_up: Mutation: c0 max_hp", c0.max_hp, 1)
check.expect("Example 2 level_up: Mutation: c0 mp", c0.mp, 1)
check.expect("Example 2 level_up: Mutation: c0 max_mp", c0.max_mp, 1)


##Examples for all_punch:

check.expect("Example 1: 0 hp on 1st hit", all_punch(L, e2), None)
check.expect("Example 1: Mutation: enemy", e2.hp, 0)

check.expect("Example 1: Mutation: d1 level", d1.level, 2)
check.expect("Example 1: Mutation: d1 st", d1.st, 12)
check.expect("Example 1: Mutation: d1 hp", d1.hp, 12)
check.expect("Example 1: Mutation: d1 max_hp", d1.max_hp, 12)
check.expect("Example 1: Mutation: d1 mp", d1.mp, 12)
check.expect("Example 1: Mutation: d1 max_mp", d1.max_mp, 12)

check.expect("Example 1: Mutation: d2 level", d2.level, 2)
check.expect("Example 1: Mutation: d2 st", d2.st, 2)
check.expect("Example 1: Mutation: d2 hp", d2.hp, 12)
check.expect("Example 1: Mutation: d2 max_hp", d2.max_hp, 12)
check.expect("Example 1: Mutation: d2 mp", d2.mp, 12)
check.expect("Example 1: Mutation: d2 max_mp", d2.max_mp, 12)

check.expect("Example 1: Mutation: d3 level", d3.level, 2)
check.expect("Example 1: Mutation: d3 st", d3.st, 23)
check.expect("Example 1: Mutation: d3 hp", d3.hp, 23)
check.expect("Example 1: Mutation: d3 max_hp", d3.max_hp, 23)
check.expect("Example 1: Mutation: d3 mp", d3.mp, 12)
check.expect("Example 1: Mutation: d3 max_mp", d3.max_mp, 12)


check.expect("Example 2: Empty players, No change in enemy hp",
             all_punch([], e3), None)
check.expect("Example 2: No Mutation: enemy", e3.hp, 30)


##Tests:

## Sample Test for  __init__ :
check.expect("Test 1: __init__ d4 name", d4.name, "C4")
check.expect("Test 1: __init__ d4 strength", d4.st, 1)
check.expect("Test 1: __init__ d4 HP", d4.hp, 12)
check.expect("Test 1: __init__ d4 maximumHP", d4.max_hp, 12)
check.expect("Test 1: __init__ d4 maximumMP", d4.max_mp, 13)
check.expect("Test 1: __init__ d4 mp", d4.mp, 13)
check.expect("Test 1: __init__ d4 level", d4.level, 1)


##Sample Test for __eq__:
check.expect("Test 1: __eq__ True", d4 == d9, True)
check.expect("Test 2: ___eq__ False", d4 == d2, False)


##Sample Tests for  __repr__:
check.set_print_exact(
  "C4",
  "Level: 1",
  "Strength: 1",
  "HP: 12/12",
  "MP: 13/13",)
check.expect("Test 1: __repr__", print(d4), None)
check.expect("Test 1:  __repr__ Alternate", str(d4),
             ("C4\nLevel: 1\nStrength: 1"
              "\nHP: 12/12\nMP: 13/13"))

check.set_print_exact(
  "Fay",
  "Level: 1",
  "Strength: 12",
  "HP: 10/10",
  "MP: 11/11",)
check.expect("Test 2: __repr__", print(c1), None)
check.expect("Test 2:  __repr__ Alternate", str(c1),
             ("Fay\nLevel: 1\nStrength: 12"
              "\nHP: 10/10\nMP: 11/11"))

check.set_print_exact(
  "E1",
  "Level: 1",
  "Strength: 2",
  "HP: 5/5",
  "MP: 10/10",)
check.expect("Test 3: __repr__", print(e1), None)
check.expect("Test 3:  __repr__ Alternate", str(e1),
             ("E1\nLevel: 1\nStrength: 2"
              "\nHP: 5/5\nMP: 10/10"))


##Sample Tests for cast_spell:

c = Character("Test", 1, 4, 5)
e = Character("Test", 1, 4, 5)
check.set_print_exact("Enemy defeated")
check.expect("Test 1: cast_spell: Enemy Defeated and self mp = 0",
             c.cast_spell(5, 5, e), None)
check.expect("Test 1: cast_spell: e mutation", e.hp, 0)
check.expect("Test 1: cast_spell: c mutation", c.mp, 0)

c = Character("Test", 1, 4, 0)
e = Character("Test", 1, 4, 5)
check.set_print_exact("Not enough MP")
check.expect("Test 2: cast_spell: Not enough MP and mp = 0",
             c.cast_spell(13, 10, e), None)
check.expect("Test 2: cast_spell: No e mutation", e.hp, 4)
check.expect("Test 2: cast_spell: No c mutation", c.mp, 0)

cc = Character("Test", 1, 4, 5)
ee = Character("Test", 1, 6, 6)
check.expect
("Test 3: cast_spell: Spell Cast but enemy hp not 0",
 cc.cast_spell(0, 1, ee), None)
check.expect("Test 3: cast_spell: ee mutation", ee.hp, 5)
check.expect("Test 3: cast_spell: cc mutation", cc.mp, 5)

cc = Character("Test", 1, 4, 0)
ee = Character("Test", 1, 6, 6)
check.expect
("Test 4: cast_spell: Spell Cast but mp and cost = 0",
 cc.cast_spell(0, 1, ee), None)
check.expect("Test 4: cast_spell: ee mutation", ee.hp, 5)
check.expect("Test 4: cast_spell: No cc mutation", cc.mp, 0)


##Sample Tests for  level_up:

check.expect("Test 1: level_up", c1.level_up(), None)
check.expect("Test 1 level_up: Mutation: c1 level", c1.level, 2)
check.expect("Test 1 level_up: Mutation: c1 st", c1.st, 14)
check.expect("Test 1 level_up: Mutation: c1 hp", c1.hp, 12)
check.expect("Test 1 level_up: Mutation: c1 max_hp", c1.max_hp, 12)
check.expect("Test 1 level_up: Mutation: c1 mp", c1.mp, 13)
check.expect("Test 1 level_up: Mutation: c1 max_mp", c1.max_mp, 13)

check.expect("Test 2: level_up c1 twice", c1.level_up(), None)
check.expect("Test 2 level_up: Mutation: c1 level", c1.level, 3)
check.expect("Test 2 level_up: Mutation: c1 st", c1.st, 16)
check.expect("Test 2 level_up: Mutation: c1 hp", c1.hp, 14)
check.expect("Test 2 level_up: Mutation: c1 max_hp", c1.max_hp, 14)
check.expect("Test 2 level_up: Mutation: c1 mp", c1.mp, 15)
check.expect("Test 2 level_up: Mutation: c1 max_mp", c1.max_mp, 15)

check.expect("Test 3: level_up odd stats ", c2.level_up(), None)
check.expect("Test 3 level_up: Mutation: c2 level", c2.level, 2)
check.expect("Test 3 level_up: Mutation: c2 st", c2.st, 13)
check.expect("Test 3 level_up: Mutation: c2 hp", c2.hp, 109)
check.expect("Test 3 level_up: Mutation: c2 max_hp", c2.max_hp, 109)
check.expect("Test 3 level_up: Mutation: c2 mp", c2.mp, 107)
check.expect("Test 3 level_up: Mutation: c2 max_mp", c2.max_mp, 107)


##Tests for all_punch:

check.expect("Test 1: Enemy hp not 0 after all hits",
             all_punch(A, e4), None)
check.expect("Test 1 Mutation: enemy", e4.hp, 26)

check.expect("Test 1: No Mutation: d4 level", d4.level, 1)
check.expect("Test 1: No Mutation: d4 st", d4.st, 1)
check.expect("Test 1: No Mutation: d4 hp", d4.hp, 12)
check.expect("Test 1: No Mutation: d4 max_hp", d4.max_hp, 12)
check.expect("Test 1: No Mutation: d4 mp", d4.mp, 13)
check.expect("Test 1: No Mutation: d4 max_mp", d4.max_mp, 13)

check.expect("Test 1: No Mutation: d5 level", d5.level, 1)
check.expect("Test 1: No Mutation: d5 st", d5.st, 1)
check.expect("Test 1: No Mutation: d5 hp", d5.hp, 20)
check.expect("Test 1: No Mutation: d5 max_hp", d5.max_hp, 20)
check.expect("Test 1: No Mutation: d5 mp", d5.mp, 15)
check.expect("Test 1: No Mutation: d5 max_mp", d5.max_mp, 15)


check.expect("Test 2: 0 hp on last hit, with some odd stats",
             all_punch(B, e5), None)
check.expect("Test 2: Mutation: enemy", e5.hp, 0)

check.expect("Test 2: Mutation: d6 level", d6.level, 2)
check.expect("Test 2: Mutation: d6 st", d6.st, 2)
check.expect("Test 2: Mutation: d6 hp", d6.hp, 17)
check.expect("Test 2: Mutation: d6 max_hp", d6.max_hp, 17)
check.expect("Test 2: Mutation: d6 mp", d6.mp, 19)
check.expect("Test 2: Mutation: d6 max_mp", d6.max_mp, 19)

check.expect("Test 2: Mutation: d7 level", d7.level, 2)
check.expect("Test 2: Mutation: d7 st", d7.st, 4)
check.expect("Test 2: Mutation: d7 hp", d7.hp, 15)
check.expect("Test 2: Mutation: d7 max_hp", d7.max_hp, 15)
check.expect("Test 2: Mutation: d7 mp", d7.mp, 17)
check.expect("Test 2: Mutation: d7 max_mp", d7.max_mp, 17)

check.expect("Test 2: Mutation: d8 level", d8.level, 2)
check.expect("Test 2: Mutation: d8 st", d8.st, 12)
check.expect("Test 2: Mutation: d8 hp", d8.hp, 23)
check.expect("Test 2: Mutation: d8 max_hp", d8.max_hp, 23)
check.expect("Test 2: Mutation: d8 mp", d8.mp, 17)
check.expect("Test 2: Mutation: d8 max_mp", d8.max_mp, 17)


check.expect
("Test 3: ALready mutated different levels, but no further mutation",
 all_punch(C, e6), None)
check.expect("Test 3: Mutation: enemy", e6.hp, 42)

check.expect("Test 3: No Mutation: d2 level", d2.level, 2)
check.expect("Test 3: No Mutation: d2 level: d2 st", d2.st, 2)
check.expect("Test 3: No Mutation: d2 hp", d2.hp, 12)
check.expect("Test 3: No Mutation: d2 max_hp", d2.max_hp, 12)
check.expect("Test 3: No Mutation: d2 mp", d2.mp, 12)
check.expect("Test 3: No Mutation: d2 max_mp", d2.max_mp, 12)

check.expect("Test 3: No Mutation: d3 level", d3.level, 2)
check.expect("Test 3: No Mutation: d3 st", d3.st, 23)
check.expect("Test 3: No Mutation: d3 hp", d3.hp, 23)
check.expect("Test 3: No Mutation: d3 max_hp", d3.max_hp, 23)
check.expect("Test 3: No Mutation: d3 mp", d3.mp, 12)
check.expect("Test 3: No Mutation: d3 max_mp", d3.max_mp, 12)

check.expect("Test 3: No Mutation: d7 level", d7.level, 2)
check.expect("Test 3: No Mutation: d7 st", d7.st, 4)
check.expect("Test 3: No Mutation: d7 hp", d7.hp, 15)
check.expect("Test 3: No Mutation: d7 max_hp", d7.max_hp, 15)
check.expect("Test 3: No Mutation: d7 mp", d7.mp, 17)
check.expect("Test 3: No Mutation: d7 max_mp", d7.max_mp, 17)


("Test 4: exact 0 hp and further mutation of players in list",
 all_punch(C, e7), None)
check.expect("Test 4: Mutation: enemy", e7.hp, 0)

check.expect("Test 4: Mutation: d2 level", d2.level, 3)
check.expect("Test 4: Mutation: d2 level: d2 st", d2.st, 3)
check.expect("Test 4: Mutation: d2 hp", d2.hp, 14)
check.expect("Test 4: Mutation: d2 max_hp", d2.max_hp, 14)
check.expect("Test 4: Mutation: d2 mp", d2.mp, 14)
check.expect("Test 4: Mutation: d2 max_mp", d2.max_mp, 14)

check.expect("Test 4: Mutation: d3 level", d3.level, 3)
check.expect("Test 4: Mutation: d3 st", d3.st, 26)
check.expect("Test 4: Mutation: d3 hp", d3.hp, 26)
check.expect("Test 4: Mutation: d3 max_hp", d3.max_hp, 26)
check.expect("Test 4: Mutation: d3 mp", d3.mp, 14)
check.expect("Test 4: Mutation: d3 max_mp", d3.max_mp, 14)

check.expect("Test 4: Mutation: d7 level", d7.level, 3)
check.expect("Test 4: Mutation: d7 st", d7.st, 5)
check.expect("Test 4: Mutation: d7 hp", d7.hp, 17)
check.expect("Test 4: Mutation: d7 max_hp", d7.max_hp, 17)
check.expect("Test 4: Mutation: d7 mp", d7.mp, 19)
check.expect("Test 4: Mutation: d7 max_mp", d7.max_mp, 19)


("Test 5: Long list and different levels: enemy hp not 0",
 all_punch(D, e8), None)
check.expect("Test 5: Mutation: enemy", e8.hp, 404)

check.expect("Test 5: No Mutation: d2 level", d2.level, 3)
check.expect("Test 5: No Mutation: d2 level: d2 st", d2.st, 3)
check.expect("Test 5: No Mutation: d2 hp", d2.hp, 14)
check.expect("Test 5: No Mutation: d2 max_hp", d2.max_hp, 14)
check.expect("Test 5: No Mutation: d2 mp", d2.mp, 14)
check.expect("Test 5: No Mutation: d2 max_mp", d2.max_mp, 14)

check.expect("Test 5: No Mutation: d3 level", d3.level, 3)
check.expect("Test 5: No Mutation: d3 st", d3.st, 26)
check.expect("Test 5: No Mutation: d3 hp", d3.hp, 26)
check.expect("Test 5: No Mutation: d3 max_hp", d3.max_hp, 26)
check.expect("Test 5: No Mutation: d3 mp", d3.mp, 14)
check.expect("Test 5: No Mutation: d3 max_mp", d3.max_mp, 14)

check.expect("Test 5: No Mutation: d4 level", d4.level, 1)
check.expect("Test 5: No Mutation: d4 st", d4.st, 1)
check.expect("Test 5: No Mutation: d4 hp", d4.hp, 12)
check.expect("Test 5: No Mutation: d4 max_hp", d4.max_hp, 12)
check.expect("Test 5: No Mutation: d4 mp", d4.mp, 13)
check.expect("Test 5: No Mutation: d4 max_mp", d4.max_mp, 13)

check.expect("Test 5: No Mutation: d5 level", d5.level, 1)
check.expect("Test 5: No Mutation: d5 st", d5.st, 1)
check.expect("Test 5: No Mutation: d5 hp", d5.hp, 20)
check.expect("Test 5: No Mutation: d5 max_hp", d5.max_hp, 20)
check.expect("Test 5: No Mutation: d5 mp", d5.mp, 15)
check.expect("Test 5: No Mutation: d5 max_mp", d5.max_mp, 15)

check.expect("Test 5: No Mutation: d7 level", d7.level, 3)
check.expect("Test 5: No Mutation: d7 st", d7.st, 5)
check.expect("Test 5: No Mutation: d7 hp", d7.hp, 17)
check.expect("Test 5: No Mutation: d7 max_hp", d7.max_hp, 17)
check.expect("Test 5: No Mutation: d7 mp", d7.mp, 19)
check.expect("Test 5: No Mutation: d7 max_mp", d7.max_mp, 19)

check.expect("Test 5: No Mutation: d8 level", d8.level, 2)
check.expect("Test 5: No Mutation: d8 st", d8.st, 12)
check.expect("Test 5: No Mutation: d8 hp", d8.hp, 23)
check.expect("Test 5: No Mutation: d8 max_hp", d8.max_hp, 23)
check.expect("Test 5: No Mutation: d8 mp", d8.mp, 17)
check.expect("Test 5: No Mutation: d8 max_mp", d8.max_mp, 17)


("Test 6: Long list and different levels: enemy hp 0",
 all_punch(D, e9), None)
check.expect("Test 6: Mutation: enemy", e9.hp, 0)

check.expect("Test 6: Mutation: d2 level", d2.level, 4)
check.expect("Test 6: Mutation: d2 level: d2 st", d2.st, 4)
check.expect("Test 6: Mutation: d2 hp", d2.hp, 16)
check.expect("Test 6: Mutation: d2 max_hp", d2.max_hp, 16)
check.expect("Test 6: Mutation: d2 mp", d2.mp, 16)
check.expect("Test 6: Mutation: d2 max_mp", d2.max_mp, 16)

check.expect("Test 6: Mutation: d3 level", d3.level, 4)
check.expect("Test 6: Mutation: d3 st", d3.st, 29)
check.expect("Test 6: Mutation: d3 hp", d3.hp, 29)
check.expect("Test 6: Mutation: d3 max_hp", d3.max_hp, 29)
check.expect("Test 6: Mutation: d3 mp", d3.mp, 16)
check.expect("Test 6: Mutation: d3 max_mp", d3.max_mp, 16)

check.expect("Test 6: Mutation: d4 level", d4.level, 2)
check.expect("Test 6: Mutation: d4 st", d4.st, 2)
check.expect("Test 6: Mutation: d4 hp", d4.hp, 14)
check.expect("Test 6: Mutation: d4 max_hp", d4.max_hp, 14)
check.expect("Test 6: Mutation: d4 mp", d4.mp, 15)
check.expect("Test 6: Mutation: d4 max_mp", d4.max_mp, 15)

check.expect("Test 6: Mutation: d5 level", d5.level, 2)
check.expect("Test 6: Mutation: d5 st", d5.st, 2)
check.expect("Test 6: Mutation: d5 hp", d5.hp, 23)
check.expect("Test 6: Mutation: d5 max_hp", d5.max_hp, 23)
check.expect("Test 6: Mutation: d5 mp", d5.mp, 17)
check.expect("Test 6: Mutation: d5 max_mp", d5.max_mp, 17)

check.expect("Test 6: Mutation: d7 level", d7.level, 4)
check.expect("Test 6: Mutation: d7 st", d7.st, 6)
check.expect("Test 6: Mutation: d7 hp", d7.hp, 19)
check.expect("Test 6: Mutation: d7 max_hp", d7.max_hp, 19)
check.expect("Test 6: Mutation: d7 mp", d7.mp, 21)
check.expect("Test 6: Mutation: d7 max_mp", d7.max_mp, 21)

check.expect("Test 6: Mutation: d8 level", d8.level, 3)
check.expect("Test 6: Mutation: d8 st", d8.st, 14)
check.expect("Test 6: Mutation: d8 hp", d8.hp, 26)
check.expect("Test 6: Mutation: d8 max_hp", d8.max_hp, 26)
check.expect("Test 6: Mutation: d8 mp", d8.mp, 19)
check.expect("Test 6: Mutation: d8 max_mp", d8.max_mp, 19)
