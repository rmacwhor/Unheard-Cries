# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define Charles = Character("Charles", color="#335eff")
define Marge = Character("Margaret", color="#fbff33")
define Lisa = Character("Lisa", color="#33ff66")
define Mikey = Character("Michael", color="#33fff6")
define Police = Character("Police", color="#0000ff")
define Maria = Character("Maria", color="#800080")




# The game starts here.
#WHEN ONE CHARACTER IS TALKING HIDE THE OTHER CHARACTERS
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene l room with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show l room
    # These display lines of dialogue.
    "{i}Music Playing{/i}"

    Marge "Lisa, dinner’s ready! Put the radio down and come eat dinner"

    "{i}Lisa replies with an annoyance in her tone{/i}"

    show lisa
    Lisa "Coming"
    hide lisa

    #hide lisa #clear the scene
    "{i}Lisa puts her radio away and heads out into the hall where
    she can see her younger brother playing with a toy train set{/i}"

    show lisa #lisa
    Lisa "{i}Michael really loves that train set I got him last christmas.{/i}"
    Lisa "Let’s go eat, Mikey"
    hide lisa

    show mikey #Mikey
    Mikey "Mmmkay!!"
    hide mikey

    "{i}Michael rushes towards Lisa’s side, clutching his toy train.{/i}"

    scene dining room with fade
    show dining room

    show marge #Marge
    Marge "Kids! We’ve got some exciting news! Your father’s been given 3 weeks of paid leave."
    hide marge

    show charles #Charles
    Charles "Since I haven’t been able to spend some quality time with you guys… We were planning on doing something fun"
    hide charles #Charles

    show mikey #Mikey
    Mikey "OH OH… ARE WE GOING TO RIDE ON A TRAIN?"
    hide mikey

    show lisa #Lisa
    Lisa "Tickets to see The Beatles next week?!?"
    hide lisa

    show charles #Charles
    Charles "We can do all that and more because your mother and I have been planning a trip to Mexico for the Olympics"
    hide charles

    show lisa #Lisa
    Lisa "REALLY?!?!"
    hide lisa #clear the scene
    "{i}Lisa nearly jumps out of her chair in excitement{/i}"

    show marge #Marge
    Marge "And we get to ride the train while we’re there!"
    hide marge

    show mikey #Mikey
    Mikey "YAY!"
    hide mikey

    show charles #Charles
    Charles "My vacation starts next Monday.  The plane leaves on Sunday night.  Kids, after dinner start packing what you want to bring on the trip with you."
    hide charles

    show lisa #Lisa
    Lisa "Alright"
    hide lisa

    show mikey #Mikey
    Mikey "OK Dad!"
    hide mikey

    scene leave airport #leaving the airport
    with fade

    "{i}Some time later... {/i}"
    "{i}The Reed family can be seen leaving airport in Mexico City{/i}"

    show lisa
    "Lisa (holding her radio)" "Mikey, I told you to leave that toy train at home, it’s embarrassing to have you next to me in public"
    hide lisa

    show mikey #Mikey
    Mikey "NO MR. TRAIN WOULD MISS ME"
    hide mikey

    show marge #Marge
    Marge "It’s alright, Lisa. If Mr. Train wants to go on a trip with Mikey then let him. The more the merrier!"
    hide marge

    show charles #Charles
    Charles "I see that we’re all tired after a long flight. Let’s check into our hotel, drop off our bags there, and explore the city."
    hide charles #clear the scene
    "Lisa and Michael" "Fineee"

    "After they dropped off their luggage at the hotel..."
    scene anthro museum with fade #Montage 1
    #back at the hotel at the end of montage
    "... the family went to see a museum."
    show lisa
    show mikey at right
    show marge at left
    pause 5
    scene lr hotel with fade

    play sound "cry.wav" volume 0.3
    pause 3
    "Marge sits up from the bed"

    show marge #Marge
    Marge "Was that Mikey?"
    hide marge

    show charles #Charles
    Charles "Huh?"
    hide charles

    show marge #Marge
    Marge "I heard something crying just now… is Mikey awake?"
    hide marge #clear the scene
    "{i}The two stay silent, listening for any noise from the children’s room but they don’t hear anything.{/i}"

    show charles #Charles
    Charles "It’s probably Mikey having a bad dream. With Lisa there she’ll take care of him"
    hide charles

    show marge #Marge
    Marge "Yeah you’re probably right. Let’s go to bed"
    hide marge

    "The pair goes back to sleep"
    "The next day..."
    scene chap castle with fade #Montage 2
    "... They went to see the castle."
    pause 4
    scene lr hotel with fade #back at the hotel at the end of montage

    play sound "cry.wav" volume 0.6
    pause 3

    show charles #Charles
    "Charles" "Marge, Marge. Did you hear that? Was that the crying noise you heard last night?"

    Charles "Does Mikey usually have this many nightmares?"
    hide charles#clear the scene
    "{i}Charles sits up on the bed and turns on the bedside lamp, clearly annoyed from the noise{/i}"

    show marge #Marge
    Marge "No not usually… but that crying doesn’t sound like Mikey."
    hide marge

    show charles #Charles
    Charles "Then there must something be going on outside. Probably just a drunk woman or something."

    Charles "It’ll probably get settled in the morning.  Tomorrow we’ll go to the front desk and ask what that crying we heard was about."
    hide charles

    show marge #Marge
    Marge "Yeah, we’ll do that."
    hide marge

    "On the third day..."
    scene art palace with fade #Montage 3
    "... they explored the town"
    pause 4
    scene lr hotel with fade#back at the hotel at the end of montage

    show marge #Marge
    Marge "Did anyone else file a noise complaint for last night?"
    hide marge

    show charles #Charles
    Charles "No, it seems that we were the only one who heard it. What about the kids?"
    hide charles

    show marge #Marge
    Marge "Hm?"
    hide marge

    show charles #Charles
    Charles "Did they also hear the crying?"
    hide charles

    show marge #Marge
    Marge "I didn’t ask… but neither of them said anything about waking up to it."
    hide marge

    #Clear the scene
    play sound "cry.wav" volume 1.0
    pause 3

    show charles #Charles
    Charles "There it is again, it's even louder than yesterday"
    hide charles

    show marge #Marge
    Marge "What is that?"
    hide marge

    #Clear the scene
    "{i}Charles opens the door to the kids room. Both Micheal and Lisa are peacefully asleep, as if completely unaware of the shrieking.{/i}"
    "{i}Charles quietly closes the door and returns to Margaret.{/i}"

    show charles #Charles
    Charles "It sounds like something is dying outside. If this continues for another night we’ll need to at least report this."
    hide charles

    show marge #Marge
    Marge "Yes, we should"
    hide marge

    scene lr hotel #hotel
    with fade

    "{i}The next morning{/i}"

    show marge #Marge
    Marge "Charles, go wake the kids up and tell them to get ready for breakfast"
    hide marge

    #clear the scene
    "{i}Charles gets out of the chair and goes over to the kids’ room{/i}"

    show charles #Charles
    Charles "Lisa, Michael, wake up, breakfast is going to be ready soon!"
    hide charles

    #clear the scene
    "{i}--Silence--{/i}"
    "{i}Upon not seeing any movement indicating that they kids are waking up, Charles walks up to Michael’s bed{/i}"

    show charles #Charles
    Charles "Wake up Mikey, mom’s making your favorite, ‘eggs n bakey’."


    hide charles #clear the scene
    "{i}Charles pulls back the blanket and is shocked to discover that Michael and Lisa were not in their bed{/i}"


    show charles #Charles
    Charles "Kids, we don’t have time to play hide and seek! We’re on a tight-"
    hide charles

    #clear the scene
    "{i}Charles notices Michael’s favorite train lying on the floor, wet and cold. He picks it up, surprised that Michael would go anywhere without it…{/i}"

    "{i}Charles begins to run around the room, checking every space of the room and closets. Only then, Charles finally realizes the dire situation…{/i}"

    show charles #Charles
    Charles "MARGE! THE KIDS ARE GONE!"
    hide charles

    scene black screen #Black screen
    with fade

    "END OF INTRODUCTION"

#CHAPTER 1 Jingyu's part

    scene kid hotel #Kid's room
    with fade

    show marge
    "Marge trembling" "Where did our kids go, Charlie? The front door is locked. There is no way they disappear from our room."
    hide marge

    show charles
    Charles "Oh wait, Marge. We have only checked this room so far and they can’t leave the suite since the front door is locked. Then, they must be in the other room."
    hide charles

    show marge
    Marge "But, why did they leave their room and stay in other rooms at midnight?"
    hide marge

    show charles
    Charles "It is a little prank Marge. Kids love making pranks.
    Waking up their dad and mum with wired noise and pretending to disappear from the room. It was all just a trick.
    Now, all we need to do is find which room they are hiding in."
    hide charles

    show marge
    Marge "Guess we need to find them as soon as possible. It’s already too late."
    hide marge

    menu initial_choice:
        "Search the living room":
            scene lr hotel #living room
            with fade
            "Nobody is there"
            jump choose_living_room
        "Search the balcony":
            scene balc hotel #balcony
            with fade
            "Nobody is there"
            jump choose_balcony

    menu choose_living_room:
        "Search the balcony":
            scene balc hotel #balcony
            with fade
            "Nobody is there"
            jump choose_bathroom

    menu choose_balcony:
        "Search the living room":
            scene lr hotel #living room
            with fade
            "Nobody is there"
            jump choose_bathroom

    menu choose_bathroom:
        "Search the bathroom":
            scene black screen #bathroom
            with fade
            Charles "They must be hiding in the bathroom. It is the only one left."

    "{i}Charles and Marge walk towards the bathroom, and suddenly there is a small sound from the bathroom door.{/i}"

    "{i}Charles opens the door.{/i}"


    Charles "Kids, we found you!"


    "{i}The bathroom is in the dark, and there is a strange smell in the air.{/i}"

    menu:
        "Turn on the lights":
            scene bath hotel
            "{i}Charles feels for the lightswitch on the wall and turns it on.  Upon the lights coming on Charles can see the room clearly.{/i}"

    "{i}The bathtub is filled with bloody water, and on the washbasin mirror: “Your kids are mine!” written in bloody red.{/i}"

    show charles
    Charles "Marge, we should call the police. Right now."
    hide charles

    scene lr hotel #living room
    with fade

    "{i}Charles and Marge sit on the sofa, anxiously waiting for the arrival of police.{/i}"

    scene lr hotel #scene with talking to police in hotel room
    with fade

    show police
    Police "Sir, we have checked every space in your room and collected all evidence we can find."
    hide police

    show marge
    Marge "Can you find our kids?"
    hide marge

    show police
    Police "I really wanna say yes. But, currently there is no evidence proving where your kids go. Actually, we can’t even prove that there was trespassing so far."
    hide police

    show charles
    Charles "I swear someone took our kids!"
    hide charles

    show police
    Police "Law only trusts evidence. Not your words, sir. As police, we will do our best to find your kids. Please stay in the hotel and wait for our messages."
    hide police

    "{i}The police leave the hotel room leaving Charles and Margaret Alone to themselves{/i}"

    scene black screen #black screen
    with fade

    "END OF PART 1"

#ISAAC'S PART

    scene lr hotel #living room
    with fade

    "{i}After talking with investigators, Margaret and Charles gather their thoughts, as silence between them grows. {/i}"

    menu:
        "Margaret speaks":
            show marge
            Marge "We can’t just sit here; we got to go and find our children!"
            hide marge
            jump door_knock
        "Charles speaks":
            show charles
            Charles "Someone has to know something, especially with that wailing..."
            hide charles
            jump door_knock
        "Silence":
            jump door_knock



    menu door_knock:
        "{i}Suddenly an unexpected knock on their door interrupts them.{/i}"

        "Answer the door":
            jump answer_door
        "Ask who is at the door":
            jump ask_door
        "Ignore the knock":
            jump ignore_door


    menu ignore_door:
        "{i}Another knock on the door. This time louder than the last.{/i}"
        "Answer the door":
            jump answer_door
        "Ask who is at the door":
            jump ask_door

    label ask_door:
        show charles
        Charles "Who's at the door?"
        hide charles

        "Woman" "Hotel services"
        jump answer_door
    label answer_door:

        "{i}Charles gets up to open the door{/i}"
        "House maid" "Hola señores, the police wanted me to give back your belongings they took from the room"
        show charles
        Charles "Thank you. What's your name?"
        hide charles

        show maria
        Maria "Maria"
        hide maria



    "{i}María starts to bring Margaret and Charles' items into their room. The rustling fills the silent room.{/i}"

    show marge
    Marge "Can I ask you some questions, María?"
    hide marge
    menu ask_questions:
        "Has anyone else heard cries in the hotel before?":
            jump answer_1
        "Did you know if anyone hear any cries over the last few nights?":
            jump answer_2

    label answer_2:
        show maria
        Maria "No not recently, however...."
        hide maria
        jump answer_1
    label answer_1:
        show maria
        Maria "You didn't hear this from me but several years ago,
        another family also reported similar cries, however they left soon after."
        hide maria

        show charles
        Charles "Why did they leave?"
        hide charles

        show maria
        Maria "Because they believe in la Llorona."
        hide maria

        show marge
        "Confused Margaret" "Who is that?"
        hide marge
        jump llorona_story

    label llorona_story:

    show maria
    Maria "Well she is said to be un fantasma that drowned her two children then herself because of the betrayal of her husband.
    Her husband supposedly returned to his other woman back in Spain and never returned.
    In grief or madness of she did those things supposedly"
    hide maria

    "{i}A brief moment of silence{/i}"

    show marge
    Marge "Did this actually happen?"
    hide marge

    show maria
    Maria "Personally, I don't think so, but it is said that she wanders the night looking for children to take away,
    haha maybe she's the one you heard and took your children"
    hide maria

    show charles
    Charles "Maybe someone was impersonating this woman who took our children!"
    hide charles

    show maria
    Maria "Well if you think that you should visit my relative, Francisco. I can tell you where he works, if you are interested"
    hide maria

    show charles
    Charles "Yes! Anything to get us closer to finding our children"
    hide charles

    show maria
    Maria "It's not too far from the hotel, and when you get there tell him María sent you"
    hide maria

    "{i}As Maria finishes bringing their items, she leaves the room{/i}"

    "{i}Left with the note from María, Charles and Margaret think if they really should visit this place.{/i}"

    show marge
    Marge "Charlie do you really think that we should go there?"
    hide marge

    show charles
    Charles "Marge, I think this may be our only lead we have ourselves, and who says the police are gonna keep us in the loop? I'm going regardless"
    hide charles

    show marge
    Marge "All I'm saying is that we need to be careful"
    hide marge

    "{i}And soon after their conversation They gather some of their belongings and head out to the address to hopefully get some lead to where their children have gone.{/i}"

    scene black screen #black screen
    with fade

    "END OF PART 2"

# BRIAN'S PART

    scene office #Francisco's office
    with fade

    define Francisco = Character("Francisco", color="#ff3333")
    define YoungFrancisco = Character("Younger Francisco", color="#ff3333")
    define Julia = Character("Julia", color = "#006400")
    define Jose = Character ("José", color = "#008080")
    define Sofia = Character("Sofia", color = "#E6E6FA")

    menu photo:
        "{i}Francisco is sitting at this desk with a photo of a family{/i}"

        "Inspect the photo":
            jump inspect_photo
        "Put the photo down":
            jump ignore_photo


    label inspect_photo:
        show francisco
        Francisco "Ah, how I miss the good times, when everything seemed simple and I had everything to look forward to still..."
        hide francisco

        scene y franciscohome #standing outside a house
        with fade

        show young_francisco
        YoungFrancisco "How do you think he’ll react to being a big brother now Maria"
        hide young_francisco

        show julia
        Julia "Honey, you shouldn’t worry about the little things in life.
        Just get in there and do what you always do."
        hide julia

        "{i}Nervously Francisco opens the door.  Upon opening the door, a young child rushes to the front door to greet his parents.{/i}"

        "???" "Hello papa, mama, what were you guys talking about outside the house?"

        show young_francisco
        YoungFrancisco "Nothing Jose. Anyways, congratulations! You’re a big brother now!"
        hide young_francisco

        "{i}Jose, as soon as Francisco said that, looked around to see where his new younger sister was.
        Eventually, his eyes fixated on the little baby wrapped in cloth in his mother’s arms{/i}"

        show jose
        Jose "What’s her name, do I get to name her?"
        hide jose

        show young_francisco
        YoungFrancisco "Your mother and I have already named her.  Today, we welcome Sofia into our family."
        hide young_francisco

        scene office #francisco's office
        with fade

        show francisco
        Francisco "Sofia, Jose, when we were still a family, everything seemed like it was going to work itself out in the end."
        hide francisco

        jump basket


    label ignore_photo:
        show francisco
        Francisco "I shouldn’t start getting emotional now, it’s been 20 years since I had any emotion left in me.
        I’m still on the clock until I finish my job."
        hide francisco

        jump basket
    menu basket:
        "{i}Francisco looks around the desk and notices a basket of gifts that a previous client had given him for hunting a ghost for them.{/i}"

        "Pick up the basket":
            show francisco
            Francisco "A basket of goods huh, they really shouldn’t have.  For them, it was just a job that I got paid to do.
            This basket does remind me of a certain picnic many years ago.."
            hide francisco

            scene picnic #picnic under a tree
            with fade

            show young_francisco
            YoungFrancisco "These churros are great! chocolate covered are my favorite! Nothing beats a chocolate churro."

            YoungFrancisco "Maria, you always make great food."
            hide young_francisco

            show julia
            Julia "Thank you Francisco, I do my best for our family"
            hide julia

            "{i}During the middle of the conversation with Maria, Sofia starts to make some noise{/i}"

            show sofia
            Sofia "Pa… pa….. Papa"
            hide sofia

            show julia
            Julia "Oh my gosh, Sofia just spoke her first word!  It sounds like she was trying to say papa"
            hide julia

            show jose
            Jose "I guess someone really likes our papa."
            hide jose

            show sofia
            Sofia "Papa! Papa!"
            hide sofia

            show young_francisco
            YoungFrancisco "Yes Sofia, I’m right here, I’ll always be here for you."
            hide young_francisco

            scene office #back in francisco's office
            with fade

            show francisco
            Francisco "Oh, why did things have to turn out like this, we had our whole lives to look forward to."
            hide francisco

            jump toy
        "Ignore the basket":
            show francisco
            Francisco "I told them many times that I don’t accept gifts"
            hide francisco
            jump toy

    menu toy:
        "{i}Francisco returns to his desk but along the way, he notices a toy that had fallen from a shelf in his office.{/i}"

        "Pick up the toy":
            show francisco
            Francisco "When did this get here.  I don’t have any reason to be hanging onto kid’s toys..."
            hide francisco

            scene y franciscohome #francisco's house in the past
            with fade

            "{i}Francisco frantically running through their house{/i}"

            show young_francisco
            YoungFrancisco "JOSE, SOFIA! WHERE ARE YOU! DON’T PLAY A JOKE LIKE THIS TO YOUR PAPA!!"
            hide young_francisco

            "{i}Silence...{/i}"

            show julia
            Julia "Francisco what are we going to do, it’s been 2 days since our kids disappeared and they never returned home."
            hide julia

            show young_francisco
            YoungFrancisco "We just have to have patience and wait, the police will find them.  The police are trying their best to find our kids and bring them back."
            hide young_francisco

            show julia
            Julia "But what if the police aren’t good enough?  What happens if they take too long to find our kids? I don’t want to be the mother of dead kids."
            hide julia

            show young_francisco
            YoungFrancisco "Julia calm down.  They aren’t dead.  We’ll find them"
            hide young_francisco

            show julia
            Julia  "I really hope so, I don’t want anything to happen to them."
            hide julia

            play sound "cry.wav" volume 0.3
            pause 3

            scene office #francisco's office

            show francisco
            Francisco "..."
            hide francisco

            jump gun
        "Kick the toy":
            show francisco
            Francisco "Who left this here, I don’t have any use for this.  Gonna have to put it away later."
            hide francisco
            jump gun
    menu gun:
        "{i}As Francisco arrives at this desk, he looks at the gun that is in his vest hanging on a coat rack.{/i}"

        "Inspect the gun":
            "{i}Francisco picks up the gun. Francisco notices the two words engraved on the gun.  “La Familia”{/i}"

            show francisco
            Francisco "..."
            hide francisco

            scene y franciscohome #Young Francisco's house
            with fade

            #Play gunshot sound here
            "{i}Younger Francisco is rushing around the house after hearing sounds of a gunshot{/i}"

            show young_francisco
            YoungFrancisco "Julia! Julia! Where are you!"
            hide young_francisco

            scene inside franciscohome #outside kids bedroom
            with fade

            "{i}Younger Francisco frantically searches the house. He searches every room but can’t find her.
            The last room he hasn’t checked yet is the children’s bedroom.  {/i}"

            "{i}Francisco slowly opens the door to reveal his wife slouched over in a chair while still holding a
            smoking gun in one hand and a letter in another hand.{/i}"

            "{i}Francisco picks up the letter and reads:{/i}"

            "{i}“Francisco my darling, you said everything would be fine.
            It’s been three months since our children have disappeared.
            Your faith in the police was misguided as they’ve given up the search and declared them dead.{/i}"

            "{i}I’ve decided to search for our children myself.  Don’t look for me as it will be easy to find me.
            Our neighbors have told me they heard of similar occurrences and the cause is La Llorona.
            I’ll find her myself and rescue our children”{/i}"

            "{i}-Maria{/i}"

            "{i}Upon finishing the letter, Francisco breaks down into tears upon the loss of his wife{/i}"

            scene office #Francisco's office
            with fade

            show francisco
            Francisco "I’ll avenge my family if it’s the last thing I do.  La Llorona has to pay for what she has done to them."
            hide francisco

            jump part_ending
        "Ignore the gun":
            jump part_ending


    label part_ending:
    "{i}Francisco is done thinking about the past just as a knock on the door can be heard{/i}"

    scene black screen #black screen
    with fade

    "END OF PART 3"

    jump chp2_2

    return
