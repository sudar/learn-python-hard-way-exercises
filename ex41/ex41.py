from sys import exit
from random import randint

def death():
    quips = ["You died. You kinda suck at this.",
            "Your mom would be proud. If she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this."]

    print quips[randint(0, len(quips)-1)]
    exit(1)

def princess_lives_here():
    print "You see a beautiful Princess with a shiny crown."
    print "She offers you some cake."

    eat_it = raw_input("> ")

    if eat_it == "eat it":
        print "You explode like a pinata full of frogs."
        print "The Princess cackles and eats the frogs. Yum!"
        return 'death'

    elif eat_it == "do not eat it":
        print "She throws the cake at you and it cuts off your head."
        print "The last thing you see is her munching on your torso. Yum!"
        return 'death'

    elif eat_it == "make her eat it":
        print "The Princess screams as you cram the cake in her mouth."
        print "Then she smiles and cries and thanks you for saving her."
        print "She points to a tiny door and says, 'The Koi needs cake too.'"
        print "She gives you the very last bit of cake and shoves you in."
        return 'gold_koi_pond'

    else:
        print "The princess looks at you confused and just points at the cake."
        return 'princess_lives_here'

def gold_koi_pond():
    print "There is a garden with a koi pond in the center."
    print "You walk close and see a massive fin poke out."
    print "You peek in and a creepy looking huge Koi stares at you."
    print "It opens its mouth waiting for food."
    
    feed_it = raw_input("> ")

    if feed_it == "feed it":
        print "The Koi jumps up, and rather than eating the cake, eats your arm."
        print "You fall in and the Koi shrugs than eats you."
        print "You are then pooped out sometime later."
        return 'death'

    elif feed_it == "do not feed it":
        print "The Koi grimaces, then thrashes around for a second."
        print "It rushes to the other end of the pond, braces against the wall..."
        print "then it *lunges* out of the water, up in the air and over your"
        print "entire body, cake and all."
        print "You are then pooped out a week later."
        return 'death'

    elif feed_it == "throw it in":
        print "The Koi wiggles, then leaps into the air to eat the cake."
        print "You can see it's happy, it then grunts, thrashes..."
        print "and finally rolls over and poops a magic diamond into the air"
        print "at your feet."

        return 'bear_with_sword'

    else:
        print "The Koi gets annoyed and wiggles a bit."
        return 'gold_koi_pond'

def bear_with_sword():
    print "Puzzled, you are about to pick up the fish poop diamond when"
    print "a bear bearing a load bearing sword walks in."
    print '"Hey! That\' my diamond! Where\'d you get that!?"'
    print "It holds its paw out and looks at you."

    give_it = raw_input("> ")

    if give_it == "give it":
        print "The bear swipes at your hand to grab the diamond and"
        print "rips your hand off in the process. It then looks at"
        print 'your bloody stump and says, "Oh crap, sorry about that."'
        print "It tries to put your hand back on, but you collapse."
        print "The last thing you see is the bear shrug and eat you."

        return 'death'

    elif give_it == "say no":
        print "The bear looks shocked. Nobody ever told a bear"
        print "with a broadsword 'no'.  It asks, "
        print '"Is it because it\'s not  a katana? I could go get one!"'
        print "It then runs off and now  you notice a big iron gate."
        print '"Where the hell did that  come from?" You say.'
                    
        return 'big_iron_gate'
    else:
        print "The bear look puzzled as to why you'd do that."
        return "bear_with_sword"

def big_iron_gate():
    print "You walk up to the big iron gate and see there's a handle."

    open_it = raw_input("> ")

    if open_it == 'open it':
        print "You open it and you are free!"
        print "There are mountains. And berries! And..."
        print "Oh, but then the bear comes with his katana and stabs you."
        print '"Who\'s laughing now!? Love this katana."'

        return 'death'

    else:
        print "That doesn't seem sensible. I mean, the door's right there."
        return 'big_iron_gate'

ROOMS = {
                            'death': death,
                            'princess_lives_here': princess_lives_here,
                            'gold_koi_pond': gold_koi_pond,
                            'big_iron_gate': big_iron_gate,
                            'bear_with_sword': bear_with_sword
}

def runner(map, start):
    next = start

    while True:
        room = map[next]
        print "\n--------"
        next = room()
        
runner(ROOMS, 'princess_lives_here')
