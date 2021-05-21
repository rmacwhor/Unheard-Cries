# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define Charles = Character("Charles")
define Marge = Character("Margaret")
define Lisa = Character("Lisa", image = "eileen")
define Mikey = Character("Michael")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room #replace later
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy #lisa's room

    # These display lines of dialogue.
    "{i}Music Playing{/i}"

    Marge "Lisa, dinner’s ready! Put the radio down and come eat dinner"

    "{i}Lisa replies with an annoyance in her tone{/i}"

    Lisa "Coming"

    "{i}Lisa puts her radio away and heads out into the hall where
    she can see her younger brother playing with a toy train set{/i}"

    Lisa "{i}Michael really loves that train set I got him last christmas.{/i}"

    Lisa "Let’s go eat, Mikey"

    show eileen happy #MIkey
    Mikey "Mmmkay!!"

    "{i}Michael rushes towards Lisa’s side, clutching his toy train.{/i}"

    scene bg room #dining room
    with fade

    show eileen happy #Marge
    Marge "Kids! We’ve got some exciting news! Your father’s been given 3 weeks of paid leave."

    show eileen happy #Charles
    Charles "Since I haven’t been able to spend some quality time with you guys… We were planning on doing something fun"

    show eileen happy #Mikey
    Mikey "OH OH… ARE WE GOING TO RIDE ON A TRAIN?"

    show eileen happy #Lisa
    Lisa "Tickets to see The Beatles next week?!?"

    show eileen happy #Charles
    Charles "We can do all that and more because your mother and I have been planning a trip to Mexico for the Olympics"

    show eileen happy #Lisa
    Lisa "REALLY?!?!"

    "{i}Lisa nearly jumps out of her chair in excitement{/i}"

    show eileen happy #Marge
    Marge "And we get to ride the train while we’re there!"

    show eileen happy#Mikey
    Mikey "YAY!"

    show eileen happy #Charles
    Charles "My vacation starts next Monday.  The plane leaves on Sunday night.  Kids, after dinner start packing what you want to bring on the trip with you."

    show eileen happy #Lisa
    Lisa "Alright"

    show eileen happy #Mikey
    Mikey "OK Dad!"

    scene bg room #leaving the airport
    with fade

    "{i}Some time later... {/i}"
    "{i}The Reed family can be seen leaving airport in Mexico City{/i}"

    "Lisa (holding her radio)" "Mikey, I told you to leave that toy train at home, it’s embarrassing to have you next to me in public"

    Mikey "NO MR. TRAIN WOULD MISS ME"

    Marge "It’s alright, Lisa. If Mr. Train wants to go on a trip with Mikey then let him. The more the merrier!"

    Charles "I see that we’re all tired after a long flight. Let’s check into our hotel, drop off our bags there, and explore the city."

    "Lisa and Micheal" "Fineee"

    scene bg room #Montage 1
    with fade

    scene bg room #back at the hotel at the end of montage
    with fade

    "faint crying can be heard"
    "Marge sits up from the bed"

    Marge "Was that Mikey?"

    Charles "Huh?"

    Marge "I heard something crying just now… is Mikey awake?"

    "{i}The two stay silent, listening for any noise from the children’s room but they don’t hear anything.{/i}"

    Charles "It’s probably Mikey having a bad dream. With Lisa there she’ll take care of him"

    Marge "Yeah you’re probably right. Let’s go to bed"

    "The pair goes back to sleep"

    scene bg room #Montage 2
    with fade

    scene bg room #back at the hotel at the end of montage
    with fade

    "{i}faint crying can be heard but louder than the previous night{/i}"

    "Charles (to Margaret quietly)" "Marge, Marge. Did you hear that? Was that the crying noise you heard last night?"

    Charles "Does Mikey usually have this many nightmares?"

    "{i}Charles sits up on the bed and turns on the bedside lamp, clearly annoyed from the noise{/i}"

    Marge "No not usually… but that crying doesn’t sound like Mikey."

    Charles "Then there must something be going on outside. Probably just a drunk woman or something."

    Charles "It’ll probably get settled in the morning.  Tomorrow we’ll go to the front desk and ask what that crying we heard was about."

    Marge "Yeah, we’ll do that."

    scene bg room #Montage 3
    with fade

    scene bg room #back at the hotel at the end of montage
    with fade

    Marge "Did anyone else file a noise complaint for last night?"

    Charles "No, it seems that we were the only one who heard it. What about the kids?"

    Marge "Hm?"

    Charles "Did they also hear the crying?"

    Marge "I didn’t ask… but neither of them said anything about waking up to it."

    "loud crying almost screaming can be heard"

    Charles "There it is again, it's even louder than yesterday"

    Marge "What is that?"

    "{i}Charles opens the door to the kids room. Both Micheal and Lisa are peacefully asleep, as if completely unaware of the shrieking.{/i}"
    "{i}Charles quietly closes the door and returns to Margaret.{/i}"

    Charles "It sounds like something is dying outside. If this continues for another night we’ll need to at least report this."

    Marge "Yes, we should"

    scene bg room #next morning
    with fade

    "{i}The next morning{/i}"

    Marge "Charles, go wake the kids up and tell them to get ready for breakfast"

    "{i}Charles gets out of the chair and goes over to the kids’ room{/i}"

    Charles "Lisa, Michael, wake up, breakfast is going to be ready soon!"

    "{i}--Silence--{/i}"
    "{i}Upon not seeing any movement indicating that they kids are waking up, Charles walks up to Michael’s bed{/i}"

    Charles "Wake up Mikey, mom’s making your favorite, ‘eggs n bakey’."

    "{i}Charles pulls back the blanket and is shocked to discover that Michael and Lisa were not in their bed{/i}"

    Charles "Kids, we don’t have time to play hide and seek! We’re on a tight-"

    "{i}Charles notices Michael’s favorite train lying on the floor, wet and cold. He picks it up, surprised that Michael would go anywhere without it…{/i}"

    "{i}Charles begins to run around the room, checking every space of the room and closets. Only then, Charles finally realizes the dire situation…{/i}"

    Charles "MARGE! THE KIDS ARE GONE!"

    scene bg room #Black screen
    with fade

    "END OF INTRODUCTION"

    # This ends the game.

    return
