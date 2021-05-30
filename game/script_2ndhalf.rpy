# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#add stuff later and change color if you want
define c = Character("Charles", color="#335eff")
define ma = Character("Margaret", color="#fbff33")
define l = Character("Lisa", color="#33ff66")
define mi = Character("Michael", color="#33fff6")
define f = Character("Francisco", color="#ff3333")
define police = Character("Police", color="#0000ff")

default mistake = 0
define drown = Fade(0.1, 0.0, 0.5, color ="0000ff")
define hurt = Fade(0.1, 0.0, 0.5, color = "ff0000")
define fade_chp = Fade(0.5, 1.0, 0.5)
define fade_pov = Fade(0.5, 0.0, 0.5) #will be used to fade to black for a second

# The game starts here.
#impementation for minigames#

init python:
    def get_image_size(d):
        d = renpy.easy.displayable(d)
        w, h = renpy.render(d, 0, 0, 0, 0).get_size()
        w, h = int(round(w)), int(round(h))
        return w, h
    class puzzle_piece:
        def __init__(self, cut, x, y, rotation, name):
            self.cut = cut
            self.x = x
            self.y = y
            self.rotation = rotation
            self.iname = name
            self.name = "0"
        def rotate(self):
            if self.rotation < 4:
                self.rotation += 1
            else:
                self.rotation = 1
        def dropped(self, drags, drop):
            if drop:
                self.name = drop.drag_name
                drags[0].snap(drop.x,drop.y)
            else:
                self.name = "0"
            renpy.restart_interaction()


    class puzzle_place:
        def __init__(self, x, y, name):
            self.x = x
            self.y = y
            self.name = name

    def pipe_reset(trans, st, at):
        if trans.rotate == 360:
            trans.rotate = 0
            return None

    class puzzle_handler:
        def __init__(self, img, size):
            self.img = img
            self.size = size
            self.map = []
            self.pieces = []
            self.framesize = None
        def init(self):
            self.map = []
            self.pieces = []
            w, h = get_image_size(self.img)
            rows = w/self.size
            columns = h/self.size
            self.framesize = ((rows*self.size)+40, (columns*self.size)+40)
            n = 0

            for c in range(columns):
                for r in range(rows):
                    n += 1
                    img = Crop((r*self.size, c*self.size, self.size, self.size), self.img)
                    p = puzzle_piece(img, r, c, 4, str(n))
                    p.rotation = renpy.random.randint(1, 4)
                    p.x = renpy.random.randint(-300, 300)
                    p.y = renpy.random.randint(-300, 300)
                    self.pieces.append(p)
                    yo = (c*self.size) - (self.size*columns)/2 + self.size/2
                    xo = (r*self.size) - (self.size*rows)/2 + self.size/2

                    self.map.append(puzzle_place(xo, yo, str(n)))
        def calc(self):
            for i in self.pieces:
                if not i.name == i.iname or not i.rotation == 4:
                    return False
            else:
                return True




screen puzzle(g):
    modal True

    on "show" action Function(g.init)
    if g.framesize:
        frame:
            align .5,.5 xysize g.framesize
            background "#222"
    draggroup:
        for i in g.map:
            drag:
                draggable False
                drag_name i.name
                align .5,.5 offset i.x, i.y
                frame:
                    xysize g.size,g.size background None padding 2,2
                    frame:
                        background "#333"
                    # text i.name

        for i in g.pieces:
            drag:
                align .5,.5 offset i.x, i.y
                droppable False
                clicked Function(i.rotate)
                dragged i.dropped
                fixed:
                    fit_first True
                    add i.cut at rotate(i.rotation*90) anchor (.5,.5) offset g.size/2,g.size/2
                    # vbox:
                    #     align .5,.5
                    #     text i.name
                    #     text i.iname
                    #     text str(i.rotation)

    if g.calc():
        frame:
            background "#333" yalign .923 padding 28,28 offset 10,-10
            text "You have solved it."


    hbox:
        spacing 10 offset 10,-10
        align 0.0,1.0
        #button:
        #    background "#333" padding 20,20
        #    text "Skip" size 24
        #    action Hide("puzzle"), Return()
        button:
            background "#333" padding 20,20
            text "Reset" size 24
            action Function(g.init)
        if g.calc():
            button:
                background "#333" padding 20,20
                text "Continue" size 24
                action Hide("puzzle"), Return()
transform rotate(r):

    subpixel True
    rotate_pad False
    ease .2 rotate r
    function pipe_reset

default puzzle_p = puzzle_handler(

    "puzzle.png",  #if the img is in other format, change its type. Ex: "puzzle.png" for png type image#
    175,                # Size of the pieces [must be an even number]
)

##End of minigames

#
label chp2_2:
    #CHAPTER 2.2
    #THE SCENE STARTS FROM THE PERSPECTIVE OF CHARLES AND MARGARET STANDING AT THE FRONT DOOR OF FRANCIS
    scene bg room #front door
    "CHARLES POV"
    "Margaret approaches the door and is about to knock on it..."
    ma "..."

    "...but there's a moment of hesitation."

    c"... Marge?"

    "She looks scared."

    c "Margaret, what are you waiting for?"
    c "We don’t have all the time in the world here."

    ma "I’m- I’m sorry, I..."

    "Marge sighs."

    ma "I don’t know what’s going to be waiting for us on the other side of that door."
    ma "What if they never find our kids, Charles?"
    ma "What would we do then?"
    ma "Just fly  home and pretend that the loves of our lives weren’t taken away from us?"
    ma "Or, what if they already found them, and..."
    ma "they’re..."
    ma "they’re not..."

    "The words get caught in Marge’s throat, as she starts choking up, tears welling in her eyes."

    menu:
        "Comfort her":
            "Charles rushes in to embrace her, causing her to break down into mournful sobs"
            "He pulls her in close, letting her cry into his shoulder"

            c "It’s okay, Marge."
            c "I know you’re scared."
            c "I’m… I’m scared, too."
            c "During this trip I’ve realized that I… haven’t been spending enough time with Michael and Lisa."
            c "I was so focused on my work that I didn’t realize how much I’ve been neglecting them."
            c "I need to play trains with Michael and… give Lisa some guidance."
            c "That’s why we’re going to find them. No matter what."

            ma "Can we trust him, though?"
            ma "Does he really care about our children, or does he only care about that ridiculous urban legend?"

            c "We don’t have anyone else we can trust."
            c "His intentions may be..."
            c "uncertain"
            c "but he knows more about La Llorona than anyone else in this city."
            c "He’s our only chance at finding our kids again. It’s him or no one."

            ma "Right… thank you."

            "Marge finally pulls away, wiping her face with her arm."

            "Marge, feeling better, finally knocks on the door."


        "Tell her to calm down":
            c "Margaret, calm down."
            c "We need to talk with Francisco as soon as possible."
            c "We can’t do that if you’re acting hysterical in front of him."
            c "Pull yourself together!"

            "Marge sniffles, shaking her head."

            ma "I- I’m really sorry."
            ma "I don’t know what got into me there."
            ma "I’m- I’m fine now."
            ma "It’s okay. We’ll be okay."

            "Marge, hiding her anxiety, finally knocks on the door."


    f "Pase."

    "Marge and Charles look at each other, confusedly."

    ma "I… guess that means come in?"

    "Marge opens the door and walks into Francisco’s office, with Charles following close behind."

    scene bg room with fade_pov #change background to francisco's room
    "Francisco, holding a picture in his hand, places it aside on his desk and looks up at the two visitors."

    f "Hola, ¿cómo puedo ayuda- ah."
    f "Lo siento- sorry, I’m not used to tourists visiting my office."
    f "Mr. and Mrs. LAST NAME, it’s good to see you two."
    f "Take a seat."

    "Charles and Marge both sit down at the two chairs opposite Francisco, though Marge is far more reluctant to do so."

    f "To start off with, I want to offer my condolences."
    f "I know that this is a very stressful situation for the both of you."
    f "This, unfortunately, isn’t the first time La Llorona has struck."
    f "But rest assured that I will do everything in my power to make this the last time."
    f "The good news is that there is something unique about your case that might help us."

    c "What do you mean?"

    f "La Llorona has haunted Mexico City for years now."
    f "But this is the first time that it has attacked turistas- tourists such as yourself."
    f "There has to be a reason for this."
    f "And once we determine what that reason is, we will find La Llorona."

    ma "Whatever you need from us, we will gladly provide."
    ma "It’s the least we can do."

    default explain = 0
    #can be revised later to check for repeat choice or find a way to delete options
    label micheal:
    menu:
        "He loves trains":
            "ADD SOMETHING"
            $ explain += 1
            if explain != 3:
                jump micheal
        "He loves his mom":
            "ADD SOMETHING"
            $ explain += 1
            if explain != 3:
                jump micheal
        "He scares too easily":
            "ADD SOMETHING"
            $ explain += 1
            if explain != 3:
                jump micheal

    $ explain = 0
    f "And your daughter... Lisa... how is she?"

    label lisa:
    menu:
        "A great caretaker":
            "ADD SOMETHING"
            $ explain += 1
            if explain != 3:
                jump lisa
        "Going through a phase":
            "ADD SOMETHING"
            $ explain += 1
            if explain != 3:
                jump lisa
        "Needs to be womanly":
            "ADD SOMETHING"
            $ explain += 1
            if explain != 3:
                jump lisa

    $ explain = 0
    f "Thank you for sharing all this."
    f "Give me a moment while I look over the evidence."

    "Francisco lays out some papers on his desk and seems to go into a deep state of thought."

    #OPTIONAL MINIGAME OPTIONAL MINIGAME OPTIONAL MINIGAME
    "Let's find where they are."
    window hide
    call screen puzzle(puzzle_p)

    f "...that’s it. That’s it"

    ma "Did you find something, Francisco?"
    ma "Did you find our children?"

    f "Dime, did you visit Lake Nabor Carrillo?"

    c "Yes, yes we did."
    c "But what does that have to-"
    c "wait… a lake…"

    f "Exactly. And every victim to date has visited that lake."
    f "Which means… yes… haha… HAHAHAHAHAHA!"

    "Francisco breaks into a fit of borderline maniacal laughter which seems to go on forever."
    "Charles and Marge look at each other with a mix of confusion and concern."

    ma "Francisco, are you… are you all right?"


    f "Oh, believe me, I am feeling fantástico!"
    f "Finally, after so many years, I have figured it out!"

    "Francisco finally calms himself down, taking a deep breath."
    "He stares at Charles and Marge, smirking."

    f "Mr. and Mrs. LAST NAME. I have a plan."
    f "And when that plan succeeds I promise you that we will get back your children safe and sound."

    f "{i}La Llorona… demonia… morirás por lo que le hiciste a mi familia.{/i}"

    scene bg room with fade_chp  #CHAPTER 2.2 END and background for lake

    mi "..."

    l "..."

    #show them with eye lifeless in art

    "A loud shriek fills the air and slowly dies down to crying..."

    scene bg room with fade_pov #switch back to office
    "CHARLES POV"
    f "Ok muchachos, here's the plan."

    f "We know La Llorona is at Lake Nabor Carrillo."
    f "We will head there tonight."
    f "If your children are alive, they should be there."

    f "Charles, you will help me fight La Llorona."

    c "...fight?"
    c "Is that even possible."

    f "Wrong choice of words."
    f "I meant to say we'll distract her with this."

    "Francisco passes notes and a crucifix to Charles."

    f "Those verses and crucifix could potentially harm the demon."
    f "Use this to divert its attention."

    c "How do you know this will be any effective against it?"

    f "Trial and error..."
    f "While La Llorona is distracted, Margaret will run to your children and try to wake them out of her spell."

    c "Okay"

    ma "What happens if I can’t break the spell?"

    f "Then your kids will die."

    c "..."

    ma "..."

    f "Go get ready. We leave now."

    scene bg room with fade_chp
    #switch back to lake background

    f "We are here. Get out of the car quietly"

    "Charles leaves the car but sees Margaret having trouble calming down."
    "He grabs her hand and reassures that everything will be fine."
    "After a couple of seconds, Margaret catches her breathe and gets out."

    "SHRIEK"
    #could play that shriek/scream sound here too

    ma "Oh my god did you guys here that?"
    ma "Is that her?"
    #wipe the screen to show only the bg
    f "Mira. Look There is." #show llorona

    c "Where's Lisa and Mikey?"

    "Marge gasps"
    ma "Over there." #show mikey and lisa in the opposite side of screen from llorona

    f "Charles. Are you ready?"

    c "Yes. Let's do it."

    f "Ok."
    f "Tres."
    f "Dos."
    f "Uno."
    f "GO!"

    scene bg room with fade_chp #reset the screen with only bg of lake

    #CHAPTER 3.2
    #screen wipe with only the background
    #background should be by the lakeside at night time
    #possible to just keep the background for this entire chapter
    #just fade to black between character POV transition
    #CHAPTER 3.2
    "MARGARET POV"

    "Charles and Francisco bolt towards La Llorona."
    "She whips her head around. Her face twists into a pure rage and a loud shriek escapes her."
    "Llorona flies towards the running men and with a single sweep with her arm, she launches them back."
    "Francisco was the first to recover from the launch and brings out a crucifix and waves it towards the spirit."
    "Enraged by this, La Llorona chases Francisco farther away from the children."
    "Charles finally gets back onto his feet and rushes over to Francisco to assist him."

    "Finding an opportunity to sneak past, Margaret manages to get near the children. As she approaches the children she notices how lifeless the two look."

    label kid_choice:
        if mistake >= 3:
            "LLorona's attention returns back to the children"
            "Noticing Margaret shaking one of the children she flies back to them."

            "Unable to stop LLorona, Francisco and Micheal can only watch the demon pull a screaming Margaret deeper in the lake.."
            "...the kids willingly following behind..."
            "The lake becomes still... but Micheal's agonized scream can be through the night."
            "BAD END"
            jump end
    menu:
        "Wake Michael":
            ma "Mikey wake up!! It’s me! Mommy is here! Wake up!!"
            "Michael remains unresponsive."
            $ mistake += 1
            jump kid_choice

        "Wake Lisa":
            ma "Lisa! Lisa dear please tell me you can hear me!!! Please..."
            "Lisa remains unresponsive..."
            $ mistake = 0

    l "Mom...?"

    ma "Lisa! Wake up please!!!"

    "Suddenly her eyes return to life."

    l "MOM! What’s going on! Where’s the monster?"

    "Margaret hugs Lisa, relieved that she’s recovered from her trance."

    ma "We don’t have time for questions. We need to wake up Mikey before it comes back"

    "Lisa quickly scans the situation and manages to put the pieces together."
    "Without asking anymore questions, she tries to help Margaret break Michael’s trance."
    "The two try to recall many of Michael’s fond memories to jerk a reaction."

    with fade_pov
    "CHARLES POV"

    "{i}This is insane...{/i}"

    c "Isn’t there a better way to hold this thing off!?!?"
    "Charles screams towards Francisco"

    "Llorona swings her right arm towards Charles."
    menu:
        "Jump Left":
            "Charles tries to jump left to create distance from the attack."
            with hurt
            with hpunch
            "However he was too slow and is hit."
            "{i}DAMN IT{/i}"
            "Charles tries to stand..."
            $ mistake += 1

            "...and with his family's safety in mind he manages to get up."
        "Duck Right":
            "Charles quickly ducks right to avoid the attack."
            "Luckily the swing goes over his head. Seeing this chance he jumps back to create distance"

    f "There’s not much we can do! This spirit is powerful!"
    "Francisco raises the cross and starts muttering something under his breath."

    "Reacting to Francisco's chants, Llorona screams again."

    "It rushes for Francisco but he manages to avoid her attack"

    f "Pull her off me Charles!"

    "Charles begins to chant a verse."

    "The chant pulls Llorona's attention and she rushes Micheal."
    "Llorona swings her left arm towards Charles."
    menu:
        "Duck Right":
            "Charles tries to duck right to dodge the attack."
            "The swing was faster than he thought and he is forced to raise his arms to protect himself."
            with hurt
            with hpunch
            "Llorona slashes him, pain rushing through Charles's arms."
            "The hit also sends him back, creating distance away from Llorona."
            "Charles tries to stand..."
            $ mistake += 1
            if mistake >= 2:
                "The pain becomes too excrutiating for Charles."
                "Unable to stand, Llorona grabs Micheal and drags him towards the Lake"
                "Despite Francisco's efforts, he cannot save Micheal"
                "{i}...Margaret... kids... I'm... so-{/i}"
                with drown
                #change background to under water during night
                "His thoughts are drowned by sudden water."
                "BAD END"
                jump end

            "...and with his family's safety in mind he manages to get up."
        "Duck Left":
            "Charles quickly ducks left to avoid the attack."
            "Luckily the swing goes over his head. Seeing this chance he jumps back to create distance"

    "Francisco chants again... louder this time..."

    "Charles expected to see Llorona rage again... however the sight surprised him."

    "Llorona seemed to be in pain. Every syllable from Francisco forces her to flinch."

    f "...it is possible..."

    "Seeing this opportunity, Charles begins to chant louder as well."

    "Unable to handle the chanting, Llorona approaches Charles to try and silence him."
    "It lunges forward at Charles"
    menu:
        "Raise the crucifix":
            "Though the crucifix made the demon hesitate for a second..."
            "...she continued to attack despite of it."
            with hurt
            with hpunch
            "It sweeps at Charles, knocking him back."
            "Charles tries to stand..."
            $ mistake += 1
            if mistake >= 2:
                "The pain becomes too excrutiating for Charles."
                "Unable to stand, Llorona grabs Micheal and drags him towards the Lake"
                "Despite Francisco's efforts, he cannot save Micheal"
                "{i}...Margaret... kids... I'm... so-{/i}"
                with drown
                #change background to under water during night
                "His thoughts are drowned by sudden water."
                "BAD END"
                jump end

            "...and with his family's safety in mind he manages to get up."
        "Jump to the side":
            "In just a nick of time, Charles manages to dodge out of Llorona's charge."
            "As Llorona recovers from her charge, Charles groups up with Francisco."

    $ mistake = 0
    "{i}I'm almost at my limit here... I hope Margaret got the kids to safety.{/i}"

    "Charles takes a quick glance at Francisco to see how he was doing..."

    "{i}...what...{/i}"

    "He was smiling..."

    "Charles and Francisco continue to lead the demon away from the children."

    "Suddenly Llorona’s attacks stop entirely. She turns around, her attention now towards Margaret and the kids."

    "She begins to move towards them."

    menu:
        "Stop Llorona":
            "Charles runs in front of the demon and raises the crucifix towards her."
            with hpunch
            "Angered by his actions, Llorona knocks Charles to the side. "
        "Let her go":
            "With nothing stopping it, the ghost makes a mad dash towards Margaret."
            "Both Lisa and Margaret are left face to face with her."
            "Suddenly, the fear from Lisa and Margaret disappear and willingly follow Llorona deeper into the lake."
            "Despite Charles’s best effort, he was not able to reach his family as they disappeared below the lake."
            "BAD END"
            jump end

    "Francisco manages to catch up with Llorona and begins chanting verses, whilst keeping his crucifix raised towards Llorona."
    "Llorona clutches her head and wails in pain, unable to move forward towards the kids."

    with fade_pov
    "MARGARET POV"

    "Llorona’s wail pierced through the night sky."
    "Both Margaret and Lisa cover their ears to try and block out her shriek."
    "As the shriek died down, Margaret hears someone whimpering,"

    ma "...Mom…"

    "Suddenly Margaret feels someone hug her tightly around her waist, a small warmness could be felt on her stomach."

    ma "...Mikey."
    "She says softly."

    "Michael was crying, hugging Margaret as hard as he could whilst saying “Mom” the entire time."

    "Then the shrieking started up again."

    "Margaret looks up and sees Francisco holding back Llorona."
    "However, she sees that whatever was holding her back is suddenly waning in power."
    "...it inches ever closer to the detective."
    "Looking towards the lakeside she sees Charles, beaten and bleeding, signaling them to come over."

    ma "...Let's go… I promise that I won’t lose track of you two again."

    "She grabs Lisa and Michael’s hands and makes her way towards Charles."
    "As soon as Margaret and the kids return to land, Charles comes up to the two and hugs them tightly."
    "He then carries Michael whose legs are shaking terribly."

    c "Go on ahead first with the kids."

    "Margaret takes Michael from Charles and begins making her way back to the van."

    l "Dad… please come back..."

    "Charles pats Lisa’s head to comfort her."

    mi "Don’t worry… I promise I’ll be back."

    "Lisa follows Margaret."

    with fade_pov
    "CHARLES POV"

    "Suddenly Charles hears loud yelling from Francisco, as if he is trying to drown Llorona’s shrieking."
    "In reaction to this, Llorona begins to back away towards the lake."

    "Despite not understanding what he is saying, he can hear..."
    "ANGER"
    "PAIN"
    "SADNESS"
    "...in each of his words."
    "With the crucifix in hand, Charles hurries to Francisco-"

    f "LEAVE CHARLES."

    c  "We need to go!"

    f "No no no… I’m so close…. So close… look at it! LOOK AT IT! IT’S SCARED OF ME."

    "Despite his claims, Llorona manages to inch her way towards Francisco."
    "Seeing this, the detective screams his chants even louder."
    "With each chant, the ghost is forced to back away whilst Francisco continues to move towards Llorona."

    f "no me queda nada..."
    f "¡ME TOMASTE TODO!" with hpunch
    menu:
        "Convince Francisco":
            c "We can’t be sure that this will make her disappear for good! This is too dangerous!"

            f "LOOK AT IT! IT’S SCARED! I’LL MAKE SURE IT DIES!" with hpunch
            "The detective takes another step towards the ghost..."
            "...not noticing that he is knee deep in water."
        "Leave Francisco":
            jump leave_francisco
    menu:
        "Convince Francisco":
            "Charles notices a smile from Llorona."
            c "FRANCISCO YOU’RE FALLING FOR HER TRAP!"

            f "NO IT WILL DIE BEFORE I DO! I’LL MAKE SURE OF IT" with hpunch
            "The detective takes another step towards the ghost..."
            "...not noticing that he is waist deep in water."
        "Leave Francisco":
            jump leave_francisco
    menu:
        "Convince Francisco":
            c "WAKE UP FRANCISCO."

            f "I’M AWAKE CHARLES. THIS IS NO DREAM. I WILL AVENGE MY FAMILY." with hpunch
            "The detective takes another step towards the ghost..."
            "...not noticing that he is waist deep in water."
        "Leave Francisco":
            jump leave_francisco

    "Now smiling widely, Llorona lunges at Francisco."
    "She grabs the detective and pulls him under."
    "Despite wanting to help the detective, Michael is too frightened to enter the water."
    "The water continues to thrash around where the detective used to be."
    #bg should be just pic of water
    "Suddenly the water comes to a still..."
    #same image of water but with crucifix floating now
    "...and Francisco's crucifix emerges..."
    "...floating along the water."
    "All was still and the night silent."
    "As if nothing happened."
    #back to lake bg
    menu:
        "Leave Francisco":
            "{i}Fuck...{/i}"

    label leave_francisco:
    "{i}I should've known... he was a lost cause...{/i}"

    #CONCLUSIONS
    #background should be by roadside next to car/van
    scene bg room with fade_chp

    "Charles returns to Marge and the kids"

    ma "Where’s Francisco?"

    "Charles shakes his head"

    ma "Oh my god"

    mi "What’s wrong?"

    c "It's nothing, Mikey. Let’s go home."

    #background should  be hotel with characters in the shot
    scene bg room with fade_pov
    "After the hellish encounter with la Llorona, the Reed family returns to the hotel, catching up with each other over the last few days of their vacation"

    scene black with fade_pov
    "On the last day before they are about to go to the airport"

    #background of interogation room
    scene bg room with fade_pov
    police "Mr.Reed could you explain again how you found your children?"

    c "I already told you guys everything..."
    c "We went and rescued them from La Llorona before she was able to drown them in the lake."

    "The policeman sighs"
    police "Sir, respectfully, La Llorona is just a myth parents tell their kids so that they don’t stay out late at night."

    c "Hey, I’m just telling the truth, whether you choose to believe it or not is not my problem."

    police "Ok, then can you tell us more about what happened to Francisco"

    c "After he was pulled into the water, we don’t know what happened to him."
    c "All we saw was his cross float to the surface of the water and nothing else."

    police "Charles, don’t lie to me."
    police "The delegacion (precinct) knows that Francisco most likely played a part in kidnapping your kids and had an ulterior motive."
    police "Stop protecting him and tell us where he is."

    c "For the last time, he drowned in Lake Nabor Carrillo!" with hpunch
    c "If that’s all you’re going to ask me, then I think this interview is finished"

    "Charles stands from his chair and walks to the door"

    police "Ok, well we’re all happy you got your children back."
    police "Stay safe and don’t let this happen again."

    scene black with fade_pov
    "Charles leaves the room and is greeted by his family who are waiting for him"
    "After picking themselves up, they take a taxi to the airport"

    #background of airport
    scene bg room with fade_pov#replace
    "At the airport"

    ma "Michael, do you have your train? You didn’t forget it at the hotel right?"

    ma "Yes mom I have it right here"

    "Michael shows the toy train to Margaret"

    l "I’m just happy we can finally go home."

    c "Surprisingly, being back home might be more relaxing than our vacation."

    ma" You said it honey. This has to have been the most stressful vacation in history"

    "The Reeds continue to talk amongst themselves as they walk towards their gate."
    "Eventually the family boards the plane and are waiting for it to take off."
    "Happy to put this nightmare vacation behind them."

    scene black with fade_pov
    #play Llorona audio screech

    label end:
    return
