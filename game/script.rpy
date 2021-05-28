# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define Charles = Character("Charles")
define Marge = Character("Margaret")
define Lisa = Character("Lisa")
define Mikey = Character("Michael")
define Police = Character("Policeman")
define Maria = Character("Maria")

# The game starts here.
#WHEN ONE CHARACTER IS TALKING HIDE THE OTHER CHARACTERS
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

    show eileen happy #lisa
    Lisa "Coming"

    hide eileen happy #clear the scene
    "{i}Lisa puts her radio away and heads out into the hall where
    she can see her younger brother playing with a toy train set{/i}"

    show eileen happy #lisa
    Lisa "{i}Michael really loves that train set I got him last christmas.{/i}"

    show eileen happy #lisa
    Lisa "Let’s go eat, Mikey"

    show eileen happy #MIkey
    Mikey "Mmmkay!!"

    show eileen happy #lisa's room
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

    hide eileen happy #clear the scene
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

    show eileen happy #Mikey
    Mikey "NO MR. TRAIN WOULD MISS ME"

    show eileen happy #Marge
    Marge "It’s alright, Lisa. If Mr. Train wants to go on a trip with Mikey then let him. The more the merrier!"

    show eileen happy #Charles
    Charles "I see that we’re all tired after a long flight. Let’s check into our hotel, drop off our bags there, and explore the city."

    hide eileen happy #clear the scene
    "Lisa and Micheal" "Fineee"

    scene bg room #Montage 1
    with fade

    scene bg room #back at the hotel at the end of montage
    with fade

    "faint crying can be heard"
    "Marge sits up from the bed"

    show eileen happy #Marge
    Marge "Was that Mikey?"

    show eileen happy #Charles
    Charles "Huh?"

    show eileen happy #Marge
    Marge "I heard something crying just now… is Mikey awake?"

    hide eileen happy #clear the scene
    "{i}The two stay silent, listening for any noise from the children’s room but they don’t hear anything.{/i}"

    show eileen happy #Charles
    Charles "It’s probably Mikey having a bad dream. With Lisa there she’ll take care of him"

    show eileen happy #Marge
    Marge "Yeah you’re probably right. Let’s go to bed"

    "The pair goes back to sleep"

    scene bg room #Montage 2
    with fade

    scene bg room #back at the hotel at the end of montage
    with fade

    "{i}faint crying can be heard but louder than the previous night{/i}"

    show eileen happy #Charles
    "Charles (to Margaret quietly)" "Marge, Marge. Did you hear that? Was that the crying noise you heard last night?"

    Charles "Does Mikey usually have this many nightmares?"

    hide eileen happy #clear the scene
    "{i}Charles sits up on the bed and turns on the bedside lamp, clearly annoyed from the noise{/i}"

    show eileen happy #Marge
    Marge "No not usually… but that crying doesn’t sound like Mikey."

    show eileen happy #Charles
    Charles "Then there must something be going on outside. Probably just a drunk woman or something."

    Charles "It’ll probably get settled in the morning.  Tomorrow we’ll go to the front desk and ask what that crying we heard was about."

    show eileen happy #Marge
    Marge "Yeah, we’ll do that."

    scene bg room #Montage 3
    with fade

    scene bg room #back at the hotel at the end of montage
    with fade

    show eileen happy #Marge
    Marge "Did anyone else file a noise complaint for last night?"

    show eileen happy #Charles
    Charles "No, it seems that we were the only one who heard it. What about the kids?"

    show eileen happy #Marge
    Marge "Hm?"

    show eileen happy #Charles
    Charles "Did they also hear the crying?"

    show eileen happy #Marge
    Marge "I didn’t ask… but neither of them said anything about waking up to it."

    hide eileen happy #Clear the scene
    "loud crying almost screaming can be heard"

    show eileen happy #Charles
    Charles "There it is again, it's even louder than yesterday"

    show eileen happy #Marge
    Marge "What is that?"

    hide eileen happy #Clear the scene
    "{i}Charles opens the door to the kids room. Both Micheal and Lisa are peacefully asleep, as if completely unaware of the shrieking.{/i}"
    "{i}Charles quietly closes the door and returns to Margaret.{/i}"

    show eileen happy #Charles
    Charles "It sounds like something is dying outside. If this continues for another night we’ll need to at least report this."

    show eileen happy #Marge
    Marge "Yes, we should"

    scene bg room #next morning
    with fade

    "{i}The next morning{/i}"

    show eileen happy #Marge
    Marge "Charles, go wake the kids up and tell them to get ready for breakfast"

    hide eileen happy #clear the scene
    "{i}Charles gets out of the chair and goes over to the kids’ room{/i}"

    show eileen happy #Charles
    Charles "Lisa, Michael, wake up, breakfast is going to be ready soon!"

    hide eileen happy #clear the scene
    "{i}--Silence--{/i}"
    "{i}Upon not seeing any movement indicating that they kids are waking up, Charles walks up to Michael’s bed{/i}"

    show eileen happy #Charles
    Charles "Wake up Mikey, mom’s making your favorite, ‘eggs n bakey’."

    hide eileen happy #clear the scene
    "{i}Charles pulls back the blanket and is shocked to discover that Michael and Lisa were not in their bed{/i}"

    show eileen happy #Charles
    Charles "Kids, we don’t have time to play hide and seek! We’re on a tight-"

    hide eileen happy #clear the scene
    "{i}Charles notices Michael’s favorite train lying on the floor, wet and cold. He picks it up, surprised that Michael would go anywhere without it…{/i}"

    "{i}Charles begins to run around the room, checking every space of the room and closets. Only then, Charles finally realizes the dire situation…{/i}"

    show eileen happy #Charles
    Charles "MARGE! THE KIDS ARE GONE!"

    scene bg room #Black screen
    with fade

    "END OF INTRODUCTION"

#CHAPTER 1 Jingyu's part

    scene bg room #Kid's room
    with fade

    "Marge trembling" "Where did our kids go, Charlie? The front door is locked. There is no way they disappear from our room."

    Charles "Oh wait, Marge. We have only checked this room so far and they can’t leave the suite since the front door is locked. Then, they must be in the other room."

    Marge "But, why did they leave their room and stay in other rooms at midnight?"

    Charles "It is a little prank Marge. Kids love making pranks.
    Waking up their dad and mum with wired noise and pretending to disappear from the room. It was all just a trick.
    Now, all we need to do is find which room they are hiding in."


    Marge "Guess we need to find them as soon as possible. It’s already too late."

    menu initial_choice:
        "Search the living room":
            scene bg room #living room
            with fade
            "Nobody is there"
            jump choose_living_room
        "Search the balcony":
            scene bg room #balcony
            with fade
            "Nobody is there"
            jump choose_balcony

    menu choose_living_room:
        "Search the balcony":
            scene bg room #balcony
            with fade
            "Nobody is there"
            jump choose_bathroom

    menu choose_balcony:
        "Search the living room":
            scene bg room #living room
            with fade
            "Nobody is there"
            jump choose_bathroom

    menu choose_bathroom:
        "Search the bathroom":
            scene bg room #bathroom
            with fade
            Charles "They must be hiding in the bathroom. It is the only one left."

    "{i}Charles and Marge walk towards the bathroom, and suddenly there is a small sound from the bathroom door.{/i}"

    "{i}Charles opens the door.{/i}"

    Charles "Kids, we found you!"

    "{i}The bathroom is in the dark, and there is a strange smell in the air.{/i}"

    menu:
        "Turn on the lights":
            "{i}Charles feels for the lightswitch on the wall and turns it on.  Upon the lights coming on Charles can see the room clearly.{/i}"

    "{i}The bathtub is filled with bloody water, and on the Washbasin mirror: “Your kids are mine!” written in bloody red.{/i}"

    Charles "Marge, we should call the police. Right now."

    scene bg room #living room
    with fade

    "{i}Charles and Marge sit on the sofa, anxiously waiting for the arrival of police.{/i}"

    scene bg room #scene with talking to police
    with fade


    Police "Sir, We have checked every space in your room and collected all evidence we can find."

    Marge "Can you find our kids?"

    Police "I really wanna say yes. But, currently there is no evidence proving where your kids go. Actually, we can’t even prove that there was trespassing so far."

    Charles "I swear someone took our kids!"

    Police "Law only trusts evidence. Not your words, sir. As police, we will do our best to find your kids. Please stay in the hotel and wait for our messages."

    "{i}The police leave the hotel room leaving Charles and Margaret Alone to themselves{/i}"

    scene bg room #black screen
    with fade

    "END OF PART 1"

#ISAAC'S PART

    scene bg room #living room
    with fade

    "{i}After talking with investigators, Margaret and Charles gather their thoughts, as silence between them grows. {/i}"

    menu:
        "Margaret speaks":
            Marge "We can’t just sit here; we got to go and find our children!"
            jump door_knock
        "Charles speaks":
            Charles "Someone has to know something, especially with that wailing..."
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
        Charles "Who's at the door?"

        "Woman" "Hotel services"
        jump answer_door
    label answer_door:

        "{i}Charles gets up to open the door{/i}"
        "House maid" "Hola señores, the police wanted me to give back your belongings they took from the room"

        Charles "Thank you. What's your name?"

        Maria "Maria"



    "{i}María starts to bring Margaret and Charles' items into their room. The rustling fills the silent room.{/i}"

    menu ask_questions:
        Marge "Can I ask you some questions, María?"

        "Has anyone else heard cries in the hotel before?":
            jump answer_1
        "Did you know if anyone hear any cries over the last few nights?":
            jump answer_2

    label answer_2:
        Maria "No not recently, however...."
        jump answer_1
    label answer_1:
        Maria "You didn't hear this from me but several years ago,
        another family also reported similar cries, however they left soon after."

        Charles "Why did they leave?"

        Maria "Because they believe in la Llorona."

        "Confused Margaret" "Who is that?"
        jump llorona_story
    label llorona_story:
    Maria "Well she is said to be un fantasma that drowned her two children then herself because of the betrayal of her husband.
    Her husband supposedly returned to his other woman back in Spain and never returned.
    In grief or madness of she did those things supposedly"

    "{i}A brief moment of silence{/i}"

    Marge "Did this actually happen?"

    Maria "Personally, I don't think so, but it is said that she wanders the night looking for children to take away,
    haha maybe she's the one you heard and took your children"

    Charles "Maybe someone was impersonating this woman who took our children!"

    Maria "Well if you think that you should visit my relative, I can tell you where he works, if you are interested"

    Charles "Yes! Anything to get us closer to finding our children"

    Maria "It's not too far from the hotel, and when you get there tell him María sent you"

    "{i}As Maria finishes bringing their items, she leaves the room{/i}"

    "{i}Left with the note from María, Charles and Margaret think if they really should visit this place.{/i}"

    Marge "Charlie do you really think that we should go there?"

    Charles "Marge, I think this may be our only lead we have ourselves, and who says the police are gonna keep us in the loop? I'm going regardless"

    Marge "All I'm saying is that we need to be careful"

    "{i}And soon after their conversation They gather some of their belongings and head out to the address to hopefully get some lead to where their children have gone.{/i}"

    scene bg room #black screen
    with fade

    "END OF PART 2"

# BRIAN'S PART

    scene bg room #Francisco's office
    with fade

    define Francisco = Character("Francisco")
    define YoungFrancisco = Character("Younger Francisco")
    define Julia = Character("Julia")
    define Jose = Character ("José")
    define Sofia = Character("Sofia")

    menu photo:
        "{i}Francisco is sitting at this desk with a photo of a family{/i}"

        "Inspect the photo":
            jump inspect_photo
        "Put the photo down":
            jump ignore_photo


    label inspect_photo:
        Francisco "Ah, how I miss the good times, when everything seemed simple and I had everything to look forward to still..."

        scene bg room #standing outside a house
        with fade

        YoungFrancisco "How do you think he’ll react to being a big brother now Maria"

        Julia "Honey, you shouldn’t worry about the little things in life.
        Just get in there and do what you always do."

        "{i}Nervously Francisco opens the door.  Upon opening the door, a young child rushes to the front door to greet his parents.{/i}"

        "???" "Hello papa, mama, what were you guys talking about outside the house?"

        YoungFrancisco "Nothing Jose. Anyways, congratulations! You’re a big brother now!"

        "{I}Jose, as soon as Francisco said that, looked around to see where his new younger sister was.
        Eventually, his eyes fixated on the little baby wrapped in cloth in his mother’s arms{/I}"

        Jose "What’s her name, do I get to name her?"

        YoungFrancisco "Your mother and I have already named her.  Today, we welcome Sofia into our family."

        scene bg room #francisco's office
        with fade

        Francisco "Sofia, Jose, when we were still a family, everything seemed like it was going to work itself out in the end."

        jump basket


    label ignore_photo:
        Francisco "I shouldn’t start getting emotional now, it’s been 20 years since I had any emotion left in me.
        I’m still on the clock until I finish my job."

        jump basket
    menu basket:
        "{i}Francisco looks around the desk and notices a basket of gifts that a previous client had given him for hunting a ghost for them.{/i}"

        "Pick up the basket":
            Francisco "A basket of goods huh, they really shouldn’t have.  For them, it was just a job that I got paid to do.
            This basket does remind me of a certain picnic many years ago.."

            scene bg room #picnic under a tree
            with fade

            YoungFrancisco "These churros are great! chocolate covered are my favorite! Nothing beats a chocolate churro."

            YoungFrancisco "Maria, you always make great food."

            Julia "Thank you Francisco, I do my best for our family"

            "{i}During the middle of the conversation with Maria, Sofia starts to make some noise{/i}"

            Sofia "Pa… pa….. Papa"

            Julia "Oh my gosh, Sofia just spoke her first word!.  It sounds like she was trying to say papa"

            Jose "I guess someone really likes our papa."

            Sofia "Papa!. Papa!"

            YoungFrancisco "Yes Sofia, I’m right here, I’ll always be here for you."

            scene bg room #back in francisco's office
            with fade

            Francisco "Oh, why did things have to turn out like this, we had our whole lives to look forward to."

            jump toy
        "Ignore the basket":
            Francisco "I told them many times that I don’t accept gifts"
            jump toy

    menu toy:
        "{i}Francisco returns to his desk but along the way, he notices a toy that had fallen from a shelf in his office.{/i}"

        "Pick up the toy":
            Francisco "When did this get here.  I don’t have any reason to be hanging onto kid’s toys..."

            scene bg room #francisco's house in the past
            with fade

            "{i}Francisco frantically running through their house{/i}"

            YoungFrancisco "JOSE, SOFIA! WHERE ARE YOU! DON’T PLAY A JOKE LIKE THIS TO YOUR PAPA!!"

            "{i}Silence...{/i}"

            Julia "Francisco what are we going to do, it’s been 2 days since our kids disappeared and they never returned home."

            YoungFrancisco "We just have to have patience and wait, the police will find them.  The police are trying their best to find our kids and bring them back."

            Julia "But what if the police aren’t good enough?  What happens if they take too long to find our kids? I don’t want to be the mother of dead kids."

            YoungFrancisco "Julia calm down.  They aren’t dead.  We’ll find them"

            Julia  "I really hope so, I don’t want anything to happen to them."

            #play distant crying noise here

            scene bg room #francisco's office

            Francisco "..."

            jump gun
        "Kick the toy":

            Francisco "Who left this here, I don’t have any use for this.  Gonna have to put it away later."

            jump gun
    menu gun:
        "{i}As Francisco arrives at this desk, he looks at the gun that is in his vest hanging on a coat rack.{/i}"

        "Inspect the gun":
            "{i}Francisco picks up the gun. Francisco notices the two words engraved on the gun.  “La Familia”{/i}"

            Francisco "..."

            scene bg room #Young Francisco's house
            with fade

            #Play gunshot sound here
            "{i}Younger Francisco is rushing around the house after hearing sounds of a gunshot{/i}"

            YoungFrancisco "Julia! Julia! Where are you!"

            "{i}Younger Francisco frantically searches the house. He searches every room but can’t find her.  The last room he hasn’t checked yet is the children’s bedroom.{/i}"

            scene bg room #outside kids bedroom
            with fade

            "{i}Younger Francisco frantically searches the house. He searches every room but can’t find her.
            The last room he hasn’t checked yet is the children’s bedroom.  {/i}"

            "{i}Francisco slowly opens the door to reveal his wife slouched over in a chair while still holding a
            smoking gun in one hand and a letter in another hand.{/i}"

            "{i}Francisco picks up the letter and reads:{/i}"

            "{i}“Francisco my darling, you said everything would be fine.
            It’s been three months since our children have disappeared.
            Your faith in the police was misguided as they’ve given up the search and declared them dead.
            I’ve decided to search for our children myself.  Don’t look for me as it will be easy to find me.
            Our neighbors have told me they heard of similar occurrences and the cause is La Llorona.
            I’ll find her myself and rescue our children”{/i}"

            "{i}-Maria{/i}"

            "{i}Upon finishing the letter, Francisco breaks down into tears upon the loss of his wife{/i}"

            scene bg room #Francisco's office
            with fade

            Francisco "I’ll avenge my family if it’s the last thing I do.  La Llorona has to pay for what she has done to them."

            jump part_ending
        "Ignore the gun":
            jump part_ending


    label part_ending:
    "{i}Francisco is done thinking about the past just as a knock on the door can be heard{/i}"

    scene bg room #black screen
    with fade

    "END OF PART 3"

    return
