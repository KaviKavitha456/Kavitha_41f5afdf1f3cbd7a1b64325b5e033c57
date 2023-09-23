class Player(object):
    def play(self):
        print ("The Player is Playing Cricket");
class Batsman(object):
    def play(self):
        print ("The Batsman is Batting");
class Bowler(Player, Batsman):
    def play(self):
        Player.play(self);
        Batsman.play(self);
        print ("The Bowler is Bowling");
Bowler.play(object);
    
        
         
  

