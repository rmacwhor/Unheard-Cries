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
    scene front door #front door
    "Margaret approaches the door and is about to knock on it..."
    show marge
    ma "..."

    "...but there's a moment of hesitation."
    hide marge

    c"... Marge?"

    "She looks scared."
    show charles
    c "Margaret, what are you waiting for?"
    c "We don’t have all the time in the world here."
    hide charles

    show marge
    ma "I’m- I’m sorry, I..."

    "Marge sighs."

    ma "I don’t know what’s going to be waiting for us on the other side of that door."
    ma "What if they never find our kids, Charles?"
    ma "What would we do then?"
    ma "Just fly  home and pretend that the loves of our lives weren’t taken away from us?"
    ma "Or, what if they already found them, and..."
    ma "they’re..."
    ma "they’re not..."
    hide marge

    "The words get caught in Marge’s throat, as she starts choking up, tears welling in her eyes."

    menu:
        "Comfort her":
            "Charles rushes in to embrace her, causing her to break down into mournful sobs"
            "He pulls her in close, letting her cry into his shoulder"

            show charles
            c "It’s okay, Marge."
            c "I know you’re scared."
            c "I’m… I’m scared, too."
            c "During this trip I’ve realized that I… haven’t been spending enough time with Michael and Lisa."
            c "I was so focused on my work that I didn’t realize how much I’ve been neglecting them."
            c "I need to play trains with Michael and… give Lisa some guidance."
            c "That’s why we’re going to find them. No matter what."
            hide charles
            show marge
            ma "Can we trust him, though?"
            ma "Does he really care about our children, or does he only care about that ridiculous urban legend?"
            hide marge
            show charles
            c "We don’t have anyone else we can trust."
            c "His intentions may be..."
            c "uncertain"
            c "but he knows more about La Llorona than anyone else in this city."
            c "He’s our only chance at finding our kids again. It’s him or no one."
            hide charles
            show marge
            ma "Right… thank you."
            hide marge
            "Marge finally pulls away, wiping her face with her arm."

            "Marge, feeling better, finally knocks on the door."


        "Tell her to calm down":
            show charles
            c "Margaret, calm down."
            c "We need to talk with Francisco as soon as possible."
            c "We can’t do that if you’re acting hysterical in front of him."
            c "Pull yourself together!"
            hide charles

            "Marge sniffles, shaking her head."
            show marge
            ma "I- I’m really sorry."
            ma "I don’t know what got into me there."
            ma "I’m- I’m fine now."
            ma "It’s okay. We’ll be okay."
            hide marge

            "Marge, hiding her anxiety, finally knocks on the door."


    f "Pase."

    "Marge and Charles look at each other, confusedly."
    show marge
    ma "I… guess that means come in?"
    hide marge
    "Marge opens the door and walks into Francisco’s office, with Charles following close behind."

    scene office with fade_pov #change background to francisco's office
    "Francisco, holding a picture in his hand, places it aside on his desk and looks up at the two visitors."
    show francisco
    f "Hola, ¿cómo puedo ayuda- ah."
    f "Lo siento- sorry, I’m not used to tourists visiting my office."
    f "Mr. and Mrs..."
    hide francisco
    show charles
    c "Reed. I am Charles Reed."
    hide charles
    show marge
    ma "I'm Margaret Reed."
    hide marge
    show francisco
    f "...it’s good to see you two."
    f "Take a seat."
    hide francisco
    "Charles and Marge both sit down at the two chairs opposite Francisco, though Marge is far more reluctant to do so."
    show francisco
    f "To start off with, I want to offer my condolences."
    f "I heard from one of my acquaintances."
    f "I know that this is a very stressful situation for the both of you."
    f "This, unfortunately, isn’t the first time La Llorona has struck."
    f "But rest assured that I will do everything in my power to make this the last time."
    f "The good news is that there is something unique about your case that might help us."
    hide francisco
    show charles
    c "What do you mean?"
    hide charles
    show francisco
    f "La Llorona has haunted Mexico City for years now."
    f "But this is the first time that it has attacked turistas- tourists such as yourself."
    f "There has to be a reason for this."
    f "And once we determine what that reason is, we will find La Llorona."
    hide francisco
    show marge
    ma "Whatever you need from us, we will gladly provide."
    ma "It’s the least we can do."
    hide marge
    default explain = 0
    default repeat1 = 0
    default repeat2 = 0
    default repeat3 = 0
    #can be revised later to check for repeat choice or find a way to delete options
    label Michael:
    menu:
        "He loves trains":
            if repeat1 == 0:
                $ repeat1 += 1
                show charles
                c "Mikey always carries his favorite train everywhere."
                c "It was quite an issue when he threw a tantrum saying he left his train by Lake Nabor."
                hide charles
                $ explain += 1
                if explain != 3:
                    jump Michael
                jump end_micheal
            show francisco
            f "You've said that already"
            hide francisco
            jump Michael

        "He loves his mom":
            if repeat2 == 0:
                $ repeat2 += 1
                show charles
                c "Marge spends a lot of time with Mikey so he grew quite attached to her."
                hide charles
                $ explain += 1
                if explain != 3:
                    jump Michael
                jump end_micheal
            show francisco
            f "You've said that already"
            hide francisco
            jump Michael

        "He scares too easily":
            if repeat3 == 0:
                $ repeat3 += 1
                show charles
                c "Mikey is easily scared since there is a lot of things he doesn't know about."
                hide charles
                $ explain += 1
                if explain != 3:
                    jump Michael
                jump end_micheal
            show francisco
            f "You've said that already"
            hide francisco
            jump Michael

    label end_micheal:
    $ explain = 0
    $ repeat1 = 0
    $ repeat2 = 0
    $ repeat3 =0
    f "And your daughter... Lisa... how is she?"

    label lisa:
    menu:
        "A great caretaker":
            if repeat1 == 0:
                $ repeat1 += 1
                show charles
                c "She's always looking out for Mikey and takes great care for him when we aren't around."
                hide charles
                $ explain += 1
                if explain != 3:
                    jump lisa
                jump end_lisa
            show francisco
            f "You've said that already"
            hide francisco
            jump lisa
        "Going through a phase":
            if repeat2 == 0:
                $ repeat2 += 1
                show charles
                c "She's trying to show that she is independent but it comes off looking rebellious at times."
                hide charles
                $ explain += 1
                if explain != 3:
                    jump lisa
                jump end_lisa
            show francisco
            f "You've said that already"
            hide francisco
            jump lisa
        "Needs to be womanly":
            if repeat3 == 0:
                $ repeat3 += 1
                show charles
                c "She's kind off tom-boyish and doesn't really pay attention to appearance all that much."
                hide charles
                $ explain += 1
                if explain != 3:
                    jump lisa
                jump end_lisa
            show francisco
            f "You've said that already"
            hide francisco
            jump lisa

    label end_lisa:
    $ explain = 0
    $ explain = 0
    $ repeat1 = 0
    $ repeat2 = 0
    $ repeat3 =0
    show francisco
    f "Thank you for sharing all this."
    f "Give me a moment while I look over the evidence."
    f "If I combined with what you've told me and the previous cases..."
    hide francisco
    "Francisco lays out some papers on his desk and seems to go into a deep state of thought."

    #OPTIONAL MINIGAME OPTIONAL MINIGAME OPTIONAL MINIGAME
    "Let's find where they are."
    window hide
    call screen puzzle(puzzle_p)
    show francisco
    f "...that’s it. That’s it"
    hide francisco
    show marge
    ma "Did you find something, Francisco?"
    ma "Did you find our children?"
    hide marge
    show francisco
    f "Dime, did you visit Lake Nabor Carrillo?"
    hide francisco
    show charles
    c "Yes, yes we did."
    c "But what does that have to-"
    c "wait… a lake…"
    hide charles
    show francisco
    f "Exactly. And every victim to date has visited that lake."
    f "Which means… yes… haha… HAHAHAHAHAHA!"
    hide francisco
    "Francisco breaks into a fit of borderline maniacal laughter which seems to go on forever."
    "Charles and Marge look at each other with a mix of confusion and concern."
    show marge
    ma "Francisco, are you… are you all right?"
    hide marge
    show francisco
    f "Oh, believe me, I am feeling fantástico!"
    f "Finally, after so many years, I have figured it out!"
    hide francisco
    "Francisco finally calms himself down, taking a deep breath."
    "He stares at Charles and Marge, smirking."
    show francisco
    f "Mr. and Mrs. Reed. I have a plan."
    f "And when that plan succeeds I promise you that we will get back your children safe and sound."

    f "{i}La Llorona… demonia… morirás por lo que le hiciste a mi familia.{/i}"
    hide francisco
    scene black with fade_chp
    "END OF PART 4"
    scene night lake with fade_chp #CHAPTER 2.2 END and background for lake

    "{i}Michael and Lisa are under La Llorona's trance.{\i}"
    show mikey at left
    show lisa at right
    mi "..."

    l "..."
    hide lisa
    hide mikey
    #show them with eye lifeless in art
    show llorona
    "A loud shriek fills the air and slowly dies down to crying..."
    hide llorona
    scene office with fade_pov #switch back to office
    show francisco
    f "Ok muchachos, here's the plan."

    f "We know La Llorona is at Lake Nabor Carrillo."
    f "We will head there tonight."
    f "If your children are alive, they should be there."

    f "Charles, you will help me fight La Llorona."
    hide francisco
    show charles
    c "...fight?"
    c "Is that even possible."
    hide charles
    show francisco
    f "Wrong choice of words."
    f "I meant to say we'll distract her with this."
    hide francisco
    "Francisco passes notes and a crucifix to Charles."
    show francisco
    f "Those verses and crucifix could potentially harm the demon."
    f "Use this to divert its attention."
    hide francisco
    show charles
    c "How do you know this will be any effective against it?"
    hide charles
    show francisco
    f "Trial and error..."
    f "While La Llorona is distracted, Margaret will run to your children and try to wake them out of her spell."
    hide francisco
    show charles
    c "Okay"
    hide charles
    show marge
    ma "What happens if I can’t break the spell?"
    hide marge
    show francisco
    f "Then your kids will die."
    hide francisco
    show charles at left
    show marge at right
    c "..."

    ma "..."
    hide charles
    hide marge
    show francisco
    f "Go get ready. We leave now."
    hide francisco
    scene roadside with fade_chp
    #switch back to roadside background
    show francisco
    f "We are here. Get out of the car quietly"
    hide francisco
    "Charles leaves the car but sees Margaret having trouble calming down."
    "He grabs her hand and reassures that everything will be fine."
    "After a couple of seconds, Margaret catches her breathe and gets out."
    scene night lake with fade_chp
    "The group approaches the lake when suddenly..."

    play sound "cry.wav" volume 1.0
    pause 2
    "SHRIEEEEEEEK"
    show marge
    ma "Oh my god did you guys here that?"
    ma "Is that her?"
    hide marge
    show llorona
    #wipe the screen to show only the bg
    f "Mira. Look, there it is." #show llorona

    c "Where's Lisa and Mikey?"

    "Marge gasps"
    ma "Over there." #show mikey and lisa in the opposite side of screen from llorona
    show lisa at left
    show mikey at right
    f "Charles. Are you ready?"

    c "Yes. Let's do it."

    f "Ok."
    f "Tres."
    f "Dos."
    f "Uno."
    f "GO!"
    hide lisa
    hide mikey
    hide llorona

    scene black with fade_chp
    "END OF PART 5"
    scene night lake with fade_chp #reset the screen with only bg of lake

    #CHAPTER 3.2
    #CHAPTER 3.2

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

            "Unable to stop LLorona, Francisco and Michael can only watch the demon pull a screaming Margaret deeper in the lake.."
            "...the kids willingly following behind..."
            "The lake becomes still... but Michael's agonized scream can be heard through the night."
            "BAD END"
            jump end
    menu:
        "Wake Michael":
            show marge
            show mikey at right
            ma "Mikey wake up!! It’s me! Mommy is here! Wake up!!"
            "Michael remains unresponsive."
            hide marge
            hide mikey
            $ mistake += 1
            jump kid_choice

        "Wake Lisa":
            show marge
            show lisa at right
            ma "Lisa! Lisa dear please tell me you can hear me!!! Please..."
            "Lisa remains unresponsive..."
            hide marge
            hide lisa
            $ mistake = 0
    show lisa
    l "Mom...?"
    hide lisa
    show marge
    ma "Lisa! Wake up please!!!"
    hide marge
    "Suddenly her eyes return to life."
    show lisa
    l "MOM! What’s going on! Where’s the monster?" with hpunch
    hide lisa

    "Margaret hugs Lisa, relieved that she’s recovered from her trance."
    show marge
    ma "We don’t have time for questions. We need to wake up Mikey before it comes back"
    hide marge
    "Lisa quickly scans the situation and manages to put the pieces together."
    "Without asking anymore questions, she tries to help Margaret break Michael’s trance."
    "The two try to recall many of Michael’s fond memories to jerk a reaction."

    with fade_pov
    show charles
    c "{i}This is insane...{/i}"

    c "Isn’t there a better way to hold this thing off!?!?"
    hide charles
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

    show francisco
    f "There’s not much we can do! This spirit is powerful!"
    hide francisco
    "Francisco raises the cross and starts muttering something under his breath."

    "Reacting to Francisco's chants, Llorona screams again."

    "It rushes for Francisco but he manages to avoid her attack"
    show francisco
    f "Pull her off me Charles!"
    hide francisco
    "Charles begins to chant a verse."

    "The chant catches Llorona's attention and she rushes Charles."
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
                "Unable to stand, La Llorona grabs Charles and drags him towards the lake"
                "Despite Francisco's efforts, he cannot save Charles"
                show charles
                c "{i}...Margaret... kids... I'm... so-{/i}"
                scene underwater with drown
                #change background to under water during night
                "His thoughts are drowned by sudden water."
                "BAD END"
                jump end

            "...and with his family's safety in mind he manages to get up."
        "Duck Left":
            "Charles quickly ducks left to avoid the attack."
            "Luckily the swing goes over his head. Seeing this chance he jumps back to create distance"

    "Francisco chants again... louder this time..."

    "Charles expected to see La Llorona rage again... however the sight surprised him."

    "La Llorona seemed to be in pain. Every syllable from Francisco forces her to flinch."
    show francisco
    f "...it is possible..."
    hide francisco
    "Seeing this opportunity, Charles begins to chant louder as well."

    "Unable to handle the chanting, La Llorona approaches Charles to try and silence him."
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
                "Unable to stand, La Llorona grabs Charles and drags him towards the lake"
                "Despite Francisco's efforts, he cannot save Charles"
                show charles
                c "{i}...Margaret... kids... I'm... so-{/i}"
                scene underwater with drown
                #change background to under water during night
                "His thoughts are drowned by sudden water."
                "BAD END"
                jump end

            "...and with his family's safety in mind he manages to get up."
        "Jump to the side":
            "In just a nick of time, Charles manages to dodge out of La Llorona's charge."
            "As La Llorona recovers from her charge, Charles groups up with Francisco."

    $ mistake = 0
    "{i}I'm almost at my limit here... I hope Margaret got the kids to safety.{/i}"

    "Charles takes a quick glance at Francisco to see how he was doing..."

    "{i}...what...{/i}"

    "He was smiling..."

    "Charles and Francisco continue to lead the demon away from the children."

    "Suddenly La Llorona’s attacks stop entirely. She turns around, her attention now towards Margaret and the kids."

    "She begins to move towards them."

    menu:
        "Stop La Llorona":
            "Charles runs in front of the demon and raises the crucifix towards her."
            with hurt
            with hpunch
            "Angered by his actions, La Llorona knocks Charles to the side. "
        "Let her go":
            "With nothing stopping it, the ghost makes a mad dash towards Margaret."
            "Both Lisa and Margaret are left face to face with her."
            "Suddenly, the fear from Lisa and Margaret disappear and willingly follow La Llorona deeper into the lake."
            "Despite Charles’s best effort, he was not able to reach his family as they disappeared below the lake."
            "BAD END"
            jump end

    "Francisco manages to catch up with La Llorona and begins chanting verses, whilst keeping his crucifix raised towards Llorona."
    "La Llorona clutches her head and wails in pain, unable to move forward towards the kids."

    with fade_pov

    "La Llorona’s wail pierced through the night sky."
    "Both Margaret and Lisa cover their ears to try and block out her shriek."
    "As the shriek died down, Margaret hears someone whimpering,"
    show mikey
    mi "...Mom…"
    hide mikey
    "Suddenly Margaret feels someone hug her tightly around her waist, a small warmness could be felt on her stomach."
    show marge
    ma "...Mikey."
    hide marge
    "She says softly."

    "Michael was crying, hugging Margaret as hard as he could whilst saying “Mom” the entire time."

    "Then the shrieking started up again."

    "Margaret looks up and sees Francisco holding back La Llorona."
    "However, she sees that whatever was holding her back is suddenly waning in power."
    "...it inches ever closer to the detective."
    "Looking towards the lakeside she sees Charles, beaten and bleeding, signaling them to come over."
    show marge
    ma "...Let's go… I promise that I won’t lose track of you two again."
    hide marge
    "She grabs Lisa and Michael’s hands and makes her way towards Charles."
    "As soon as Margaret and the kids return to land, Charles comes up to the two and hugs them tightly."
    "He then carries Michael whose legs are shaking terribly."
    show charles
    c "Go on ahead first with the kids."
    hide charles
    "Margaret takes Michael from Charles and begins making her way back to the van."
    show lisa
    l "Dad… please come back..."
    hide lisa
    "Charles pats Lisa’s head to comfort her."
    show charles
    c "Don’t worry… I promise I’ll be back."
    hide charles
    "Lisa follows Margaret."

    with fade_pov

    "Suddenly Charles hears loud yelling from Francisco, as if he is trying to drown La Llorona’s shrieking."
    "In reaction to this, La Llorona begins to back away towards the lake."

    "Despite not understanding what he is saying, he can hear..."
    "ANGER"
    "PAIN"
    "SADNESS"
    "...in each of his words."
    "With the crucifix in hand, Charles hurries to Francisco-"
    show francisco
    f "LEAVE CHARLES."
    hide francisco
    show charles
    c  "We need to go!"
    hide charles
    show francisco
    f "No no no… I’m so close…. So close… look at it! LOOK AT IT! IT’S SCARED OF ME."
    hide francisco
    "Despite his claims, La Llorona manages to inch her way towards Francisco."
    "Seeing this, the detective screams his chants even louder."
    "With each chant, the ghost is forced to back away whilst Francisco continues to move towards La Llorona."
    show francisco
    f "no me queda nada..."
    f "¡ME TOMASTE TODO!" with hpunch
    hide francisco
    menu:
        "Convince Francisco":
            show charles
            c "We can’t be sure that this will make her disappear for good! This is too dangerous!"
            hide charles
            show francisco at left
            f "LOOK AT IT! IT’S SCARED! I’LL MAKE SURE IT DIES!" with hpunch
            "The detective takes another step towards the ghost..."
            "...not noticing that he is knee deep in water."
            hide francisco
        "Leave Francisco":
            jump leave_francisco
    menu:
        "Convince Francisco":
            "Charles notices a smile from La Llorona."
            show charles
            c "FRANCISCO YOU’RE FALLING FOR HER TRAP!"
            hide charles
            show francisco
            f "NO IT WILL DIE BEFORE I DO! I’LL MAKE SURE OF IT" with hpunch
            "The detective takes another step towards the ghost..."
            "...not noticing that he is waist deep in water."
            hide francisco
        "Leave Francisco":
            jump leave_francisco
    menu:
        "Convince Francisco":
            show charles
            c "WAKE UP FRANCISCO."
            hide charles
            show francisco at right
            f "I’M AWAKE CHARLES. THIS IS NO DREAM. I WILL AVENGE MY FAMILY." with hpunch
            "The detective takes another step towards the ghost..."
            "...not noticing that he is waist deep in water."
            hide francisco
        "Leave Francisco":
            jump leave_francisco

    "Now smiling widely, La Llorona lunges at Francisco."
    "She grabs the detective and pulls him under."
    "Despite wanting to help the detective, Charles is too frightened to enter the water."
    "The water continues to thrash around where the detective used to be."
    #bg should be just pic of water
    scene calm water
    "Suddenly the water comes to a still..."
    "...and Francisco's crucifix emerges..."
    "...floating along the water."
    "All was still and the night silent."
    "As if nothing happened."
    scene night lake with fade_chp
    menu:
        "Leave Francisco":
            show charles
            c "{i}Damn...{/i}"

    label leave_francisco:
    "{i}I should've known... he was a lost cause...{/i}"
    hide charles

    #CONCLUSIONS
    scene black with fade_chp
    "END PART 6"
    #background should be by roadside next to car/van
    scene roadside with fade_chp

    "Charles returns to Marge and the kids"
    show marge
    ma "Where’s Francisco?"
    hide marge
    "Charles shakes his head"
    show marge
    ma "Oh my god"
    hide marge
    show mikey
    mi "What’s wrong?"
    hide mikey
    show charles
    c "It's nothing, Mikey. Let’s go home."
    hide charles
    #background should be hotel with characters in the shot
    scene lr hotel with fade_pov
    "After the hellish encounter with la Llorona, the Reed family returns to the hotel, catching up with each other over the last few days of their vacation"

    scene black screen with fade_pov
    "On the last day before they are about to go to the airport"

    #background of interrogation room
    scene interro with fade_pov
    show police
    police "Mr.Reed could you explain again how you found your children?"
    hide police
    show charles
    c "I already told you guys everything..."
    c "We went and rescued them from La Llorona before she was able to drown them in the lake."
    hide charles
    show police
    "The policeman sighs"
    police "Sir, respectfully, La Llorona is just a myth parents tell their kids so that they don’t stay out late at night."
    hide police
    show charles
    c "Hey, I’m just telling the truth, whether you choose to believe it or not is not my problem."
    hide charles
    show police
    police "Ok, then can you tell us more about what happened to Francisco"
    hide police
    show charles
    c "After he was pulled into the water, we don’t know what happened to him."
    c "All we saw was his cross float to the surface of the water and nothing else."
    hide charles
    show police
    police "Charles, don’t lie to me."
    police "The delegación knows that Francisco most likely played a part in kidnapping your kids and had an ulterior motive."
    police "Stop protecting him and tell us where he is."
    hide police
    show charles
    c "For the last time, he drowned in Lake Nabor Carrillo!" with hpunch
    c "If that’s all you’re going to ask me, then I think this interview is finished"
    hide charles
    "Charles stands from his chair and walks to the door"
    show police
    police "Ok, well we’re all happy you got your children back."
    police "Stay safe and don’t let this happen again."
    hide police
    scene black with fade_pov
    "Charles leaves the room and is greeted by his family who are waiting for him"
    "After picking themselves up, they take a taxi to the airport"

    #background of airport
    scene leave airport with fade_pov#replace
    "At the airport"
    show marge
    ma "Michael, do you have your train? You didn’t forget it at the hotel right?"
    hide marge
    show mikey
    mi "Yes mom I have it right here"
    hide mikey
    "Michael shows the toy train to Margaret"
    show lisa
    l "I’m just happy we can finally go home."
    hide lisa
    show charles
    c "Surprisingly, being back home might be more relaxing than our vacation."
    hide charles
    show marge
    ma" You said it honey. This has to have been the most stressful vacation in history"
    hide marge
    "The Reeds continue to talk amongst themselves as they walk towards their gate."
    "Eventually the family boards the plane and are waiting for it to take off."
    "Happy to put this nightmare vacation behind them."

    scene black screen with fade_pov
    play sound "cry.wav" volume 1.0
    pause 3
    "END"

    label end:
    return
