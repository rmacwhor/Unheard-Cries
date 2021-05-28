# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#add stuff later and change color if you want
define c = Character("Charles", color="#335eff")
define ma = Character("Margaret", color="#fbff33")
define l = Character("Lisa", color="#33ff66")
define mi = Character("Michael", color="#33fff6")
define f = Character("Francisco", color="#ff3333")

default mistake = 0
define drown = Fade(0.1, 0.0, 0.5, color ="0000ff")
define hurt = Fade(0.1, 0.0, 0.5, color = "ff0000")
define fade_chp = Fade(0.5, 1.0, 0.5)
define fade_pov = Fade(0.5, 0.0, 0.5) #will be used to fade to black for a second

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    with fade_chp
    scene bg room
    #background should be by the lakeside at night time
    #possible to just keep the background for this entire chapter
    #just fade to black between character POV transitions
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

    label end:
    with fade_chp
    return
