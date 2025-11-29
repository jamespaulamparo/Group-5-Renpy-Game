# The script of the game goes in this file.

define a = Character("Andrea", who_color="#d2e2eb", what_color="#FFFFFF")
define r = Character("Rafaela", who_color="#dacd7f", what_color="#FFFFFF")
define k = Character("Kira", who_color="#d3ad8b", what_color="#FFFFFF")
define j = Character("Jamie", who_color="#a15656", what_color="#FFFFFF")

define c = Character("Ms. Cassandra", who_color="#9e8677", what_color="#FFFFFF")
define l = Character("Loraine", who_color="#a298c6", what_color="#FFFFFF")
define h = Character("Haifa", who_color="#93c386", what_color="#FFFFFF")

# add dan, choco for sub haraters
# Example: define dan = Character("Dan", color="#...")
# Example: define choco = Character("Choco", color="#...")


# ---------------------------------------

# relation points
default andrea_rel = 0
default rafaela_rel = 0
default kira_rel = 0
default jamie_rel = 0

default cassie_rel = 0
default loraine_rel = 0
default haifa_rel = 0

# question Flags
default kira_asked = False
default andrea_asked = False
default rafaela_asked = False
default jamie_asked = False

# The game starts here.
label start:

    $ renpy.movie_cutscene("images/videos/prologue.webm")

    "......."
    "....."
    "..."

    play music "audio/bgm/spring.mp3" fadein 7.0 volume 0.6
    scene bg classroom
    with dissolve 

    show mc neutral at left:
        zoom 1.5
    with dissolve
    "(Mmm.)"

    "(I wonder how my parents are doing.)"
    
    "..."
    
    show cassie happy at right:
        zoom 1.5
    with dissolve
    
    c "Alright, class, ilagay niyo na pangalan niyo sa wheel of names para makapagdecide na ng groupings."
    
    show cassie neutral at right
    c "Ayusin niyo yung ilalagay niyo ha, {w}first name then surname muna."
    
    "..."
    "She stared directly at me for some reason."
    
    show cassie angry at right
    c "Again, groupings niyo nakasalalay dito. Kaya ayusin niyo or babagsak talaga kayo."
    
    show mc neutral at left
    "(Is she talking to me or threatening me? {w}Either way, let’s just get this over with.)"

    define mc = Character("[firstname]", who_color="#FFFFFF", what_color="#FFFFFF")
    python:
        firstname = renpy.input("What is your first name? (Default = Sabrina)", length=15)
        firstname = firstname.strip()

        if firstname == "":
            firstname = "Sabrina"

    define mc2 = Character("[lastname]", who_color="#FFFFFF", what_color="#FFFFFF")
    python:
        lastname = renpy.input("Now, what is your name name? (Default = Carpintero)", length=15)
        lastname = lastname.strip()

        if lastname == "":
            lastname = "Carpintero"
            
    "You've submitted the name: [firstname] [lastname]."

    show cassie neutral at right
    c "Only twenty-four out of thirty-five students have submitted. {w}Kung hindi pa kayo kasama doon, bilisan niyo. May meeting pa ako."

    c "While we're waiting for the rest, {w}I'll go over the project again, okay?"

    c "As you all know, The school foundation week is coming up, {w}and one of the main highlights will be a student-led school fair."
    
    show mc cringe at left
    mc "(Ugh, {w}another performance task? I thought we'd be done by now and complete this semester.)"

    "???" "Hey~"
    
    show cassie happy at right
    c "So, for your final project in my class, you are all required to participate in the school fair by selling products or services, whatever your group prefers really."

    "???"  "Heeeeyy."
    
    show cassie neutral at right
    c "It’s sudden, I know. But it's part of the new curriculum so we can't do anything about it."
    c "It's a task that requires much effort and time-{nw}"

    "???"  "Hey, [firstname]~" 

    show mc angry at left
    mc "Holy shit, what is it, Loraine?"
    play sound "audio/rustle.mp3"

    hide cassie neutral with dissolve
    
    show loraine neutral at right:
        zoom 1.5
    with dissolve

    l "Damn, you woke up in a bad mood or something?"

    menu: 
        "Sorry.":
            jump sorryloraine
        
        "None of your business.":
            jump rudeloraine

    label sorryloraine:
        $ loraine_rel += 1 # plus point relation here with loraine
        show mc neutral at left
        mc "Yeah I did, sorry."
        l "It's alright."
        
        l "Anyway, it's urgent, can you submit Jamie's name in the wheel of groupings?"

        show mc sad at left
        mc "...Can't she do it herself?"

        l "She’s not here, duh. But I owe her one from last time I was absent, so I figured… maybe you could help me help her?"

        mc "Why won't you just do it yourself, then?"
        
        show loraine sweat at right
        l "...lowbat na 'ko eh. As in."

        show mc neutral at left
        mc "Mmm, fine."
        mc "What's her full name?"
        
        show loraine happy at right
        l "Jamie Paulette Cielo~ Thanks, queen."
        jump loraine

    label rudeloraine:
        $ loraine_rel -= 1 # minus relationship point here with loraine
        show mc angry at left
        mc "None of your business."

        show loraine sad at right
        l "Sheesh, my bad. Can I just ask you for a favor?"
        
        show loraine neutral at right
        l "Can you submit Jamie's name in the wheel of groupings whatever?"
        l "I owe her one when I was absent the other day. And she isn't here right now so..."

        mc "Just do it yourself."
        
        show loraine sweat at right
        l "...lowbat na 'ko eh. As in."
        
        show mc cringe at left
        mc "Tragic."
        
        show loraine sad at right
        l "Please, [firstname], para sa grades niya 'to."

        show mc neutral at left
        mc "Fine."
        mc "Her name?"

        show loraine happy at right
        l "Thanks, It's Jamie Paulette Cielo."
        jump loraine
    
    label loraine:
        show mc neutral at left
        mc "Done."
        
        show loraine neutral at right
        l "Thanks again."
        
        c "AHEM. {w}Are you girls done talking?"
        
        show cassie angry at center:
            zoom 1.5
        with dissolve
        
        show loraine sad at right
        l "Oh, sorry ma'am."

        "*Ms. Cassandra shakes her head.*"
        
        show cassie neutral at center
        c "Since *some* students are not listening anymore {w}and it looks like the wheel of names is complete, let's finish the meeting."
        
        play sound "audio/s_notification.ogg"
        "*DING*" 
        "*The bell sound comes from the professor's laptop as the wheel of names starts spinning*"

        c "You’ll be randomly assigned to groups of five. No complaining. No switching." 
        hide cassie neutral with dissolve
        
        show mc sad at left
        mc "I just hope I pass."
        
        show loraine happy at right
        "*Loraine chuckles beside me*"
        show loraine neutral at right
        l "Amen."
        
        "When the wheel finally stopped, seven boxes appeared on the screen, each with five names."
        show mc neutral at left
        show loraine happy at right
        l "YIPPEE"
        l "I got group one!"
        
        mc "Damn you have a decent group."
        
        show loraine happy at right
        l "And I'm kinda close with some of them, thank god."
        show loraine neutral at right
        l "How about you, who are ya grouped with?"
        
        show mc neutral at left
        mc "Let’s see… {w}Not group two. {w}Not four either..."
        mc "There we go, I'm group five."
        
        show loraine sweat at right
        l "Oh, {w}oh sh-good luck."

        show mc neutral at left
        mc "What, why?"
        
        "*Loraine starts reading the group name from the screen.*"
        
        show loraine neutral at right
        l "You, Kira, Andrea, Rafaela, and Jamie? That's... uhm, {w}challenging HAHAHAH-"
        
        show mc sad at left
        mc "You're not doing a good job encouraging me."
        
        show loraine neutral at right
        l "Am I supposed to?"
        
        show mc sad at left
        mc "I'm gonna die."
        
        show loraine neutral at right
        l "I mean… maybe it’s not that bad? You know… character development?"

        show mc neutral at left
        mc "Fuck that. Why are they so bad anyway? Like for example..."
        
        # --- LOCALIZED FLAG INITIALIZATION ---
        $ kira_asked = False
        $ andrea_asked = False
        $ rafaela_asked = False
        $ jamie_asked = False
        # -------------------------------------
        jump questionLoraine

    label questionLoraine:
        python:
            choices = []

            if not kira_asked:
                choices.append(("Isn't Kira an honor student?", "kiraLoraine"))
            
            if not andrea_asked:
                choices.append(("You had fun being Andrea's groupmate before.", "andreaLoraine"))

            if not rafaela_asked:
                choices.append(("Rafaela's not that bad right?", "rafaelaLoraine"))
            
            if not jamie_asked:
                choices.append(("Didn't you owe Jamie something?", "jamieLoraine"))
            
            if kira_asked and andrea_asked and rafaela_asked and jamie_asked:
                choices.append(("I'm done asking.", "finishLoraine"))
            
            result = renpy.display_menu(choices)
            
            if result:
                renpy.jump(result)

    label kiraLoraine:
        $ kira_asked = True
        
        show mc neutral at left
        mc "Isn't Kira an honor student? Like, top of the class, honor student?"
        
        show loraine sweat at right
        "*Loraine looks around and pulls me close, nearly knocking over my chair.*"
        play sound "audio/rustle.mp3"
        l "Shh, she might overhear."
        
        show loraine neutral at right
        l "Kira's great, yeah, {w}but she has zero chill. Last time I was her groupmate, I couldn't tell if she was being sarcastic or not."
        
        show mc cringe at left
        mc "Yikes."
        
        show loraine sad at right
        l "Yeah. Good luck having her as your leader if it came down to that."
        
        jump questionLoraine

    label andreaLoraine:
        $ andrea_asked = True
        
        show mc neutral at left
        mc "You had fun being Andrea's groupmate before, right?"
        
        show loraine sweat at right
        l "She's active most of the time but... {w}I think she lags in real life. Like, you'd have to call her name multiple times to even get her attention."
        
        show loraine sad at right
        l "Plus, look. She's not even present in the class right now. {w}I don't even know how she got her name in the wheel in the first place."
        
        show mc sad at left
        mc "Oh."
        
        show loraine neutral at right
        l "She'll help, dont worry."
        
        jump questionLoraine

    label rafaelaLoraine:
        $ rafaela_asked = True
        
        show mc neutral at left
        mc "Rafaela's not that bad right? I honestly don't know anything about her."
        
        show loraine neutral at right
        l "Ehh, she's okay I guess."
        
        show loraine happy at right
        l "But to be honest, I don't know her much, {w}I'm pretty sure no one does either. She just exists."
        
        show mc neutral at left
        mc "Doesn't sound too bad. At least she's quiet."
        
        jump questionLoraine

    label jamieLoraine:
        $ jamie_asked = True
        
        show mc neutral at left
        mc "Didn't you owe Jamie something? What's the deal with her being in the group, anyway?"
        
        show loraine sad at right
        l "Ugh, she's basically a ghost. She helps me out in OTHER classes, but the thing is, she's absent almost everyday from this one."
        
        show loraine sweat at right
        l "I'm pretty sure she dropped this class already, but she just shows up sometimes for some reason. {w}But again, not in this class."
        
        show mc cringe at left
        mc "So, a guaranteed absent member. Great."
        
        show loraine sad at right
        l "Pretty much."
        
        jump questionLoraine

    label finishLoraine:
        show mc sad at left
        mc "Shit."
        
        show loraine neutral at right
        l "And, you. You have to lock in. Aren't you like, one class away from failing?"
        
        show mc angry at left
        mc "You're reaaally good at motivating people."
        
        show loraine happy at right
        l "Heh, but anyway, I do believe in you."
        l "I know you aren't the lazy ass everyone thinks you are."
        
        "*Loraine gives me a fist bump and looks at the professor.*"
        
        show cassie neutral at center:
            zoom 1.5
        with dissolve
        
        show loraine neutral at right
        show mc neutral at left
        c "The idea pitching is due until saturday but the first three groups that will submit their plans today will get sponsored slots."
        c "Meaning, they will get some budget provided by the school, reserved booth spots, and other perks that I'd rather not go over again."
        
        show cassie angry at center
        c "Again, I'll only accept the first three groups. So bilisan niyo kung gusto niyo."

        show loraine neutral at right
        l "I'ma go to my group now, just message me if you need help with something."
        
        show mc neutral at left
        mc "Alright, thanks."

        hide loraine with dissolve

        show cassie neutral at center
        c "...and Ms. [lastname]? Before I forget, may I have a word with you outside?"
        c "The rest of the class, you may approach me after our talk for slots."

        show mc sad at left
        mc "What does she want from me this time?"
        
        "........"
        "....."
        "..."
        
        hide cassie neutral with dissolve
        hide mc sad with dissolve
        
        jump hallwayProfessor

    label hallwayProfessor:
        scene bg hallway
        with dissolve 

        show mc neutral at left:
            zoom 1.5
        with dissolve

        show cassie neutral at right:
            zoom 1.5
        with dissolve
        
        c "...Ms. [lastname]?"
        c "Hello? [lastname], are you listening?"

        show mc neutral at left
        mc "Not really, Ma'am, what was it again?"
        show cassie dismayed at right
        "*Professor Cassandra exhales hard*"

        show mc sad at left
        mc "(She really wants me dead, huh.)"

        show cassie neutral at right
        c "Look. I’m going to be straight with you."
        c "If you keep going at this rate, you’re gonna fail my class."

        show mc sad at left
        mc "(Ah, this kind of talk.)"
        mc "(I've heard this before, probably word-for-word in a different hallway with a different teacher.)"
        mc "(Really, let's just get this over with.)"

        c "I’ve done the math. You’ve missed three minor activities, flunked more than a couple quizzes, {w}and your midterm was..."
        "*She lets the silence hang*"
        show mc happy at left
        mc "Yay, love to see the consistency."

        c "If you don’t pull through on this final project, you’re not passing. You know that, right?"
        show mc neutral at left
        mc "Yeah. {w}You’ve mentioned."
        c "And you don’t even look worried."

        mc "Yeah, yeah. I got it. Sell some product or whatever. Happy now?"
        show cassie angry at right
        c "Don’t joke. I’m serious."
        c "Look. If this were just about the grade, I’d move on. Let you dig your own grave and call it a day."

        menu:
            "Why are you telling me this?":
                jump whyProfessor

            "Why do you even care?":
                jump okProfessor

    label whyProfessor:

        show mc neutral at left
        mc "...why are you telling me this?"
        c "Because you're not some lost cause, no matter how much you try to be."
        c "You’re not stupid, Ms. [lastname]. Far from it. {w}I've seen the way you write when you actually write. The way you connect ideas. "
        show cassie neutral at right
        c "If you actually tried, really tried. You could've avoided this altogether."
        c "You notice things most people don’t even think about."
        c "You think I don't read your essay papers you submit right before the deadline?"
        c "I always wait for your submissions because I know they’ll be good. {w}But other than that? you're doing everything in your power to do nothing."
        c "So what is it?"
        c "You lazy? Bored? Or are you just... {w}scared?"
        show mc cringe at left
        mc "...scared of what? Group projects and capitalism?"
        mc "Both are pretty tricky in my experience."
        c "Capitalism? Where did that even..."
        show cassie happy at right
        "*Professor Cassandra shakes her head.*"
        c "There it is."
        c "Same lines. Same jokes. Every time someone gets too personal with you." 

        "..."
        show cassie neutral at right
        c "...look. {w}I don’t care if you fail your other classes or end up having to stop your education."
        c "But you’re in my class right now. So I care just enough to tell you this."
        c "You’re better than what you’re settling for."

        show mc cringe at left
        mc "...I don't know what you're talking about, Ma'am, but I appreciate it."
        c "..."
        c "Alright then."
        c "Anyway. I’ve got thirty-four other students to deal with. {w}I don’t have time to babysit kids who don't even try."
        c "You want to fail? Be my guest."

        c "Go back inside. Try not to be a burden your groupmates. Maybe surprise yourself this time."

        "She went back inside the room, leaving me alone in the hallway."
        hide cassie neutral with dissolve
        
        show mc neutral at left
        mc "(I hate this.)"
        mc "(Is it that hard to mind your own business?)"
        mc "(...whatever. Not like this changes anything.)"
        "..."
        mc "(I don't want to go back.)"

        menu:
            "Think for a while.":
                jump stayHallway

            "Leave the damn school.":
                jump leaveShool

    label okProfessor:
        $ cassie_rel -= 1 # minus relationship point here with cassie
        show mc angry at left
        mc "Why do you even care? It’s not like I’m your best student or something."
        mc "And...  {w}aren't you just some student teacher who wants to quit this... {w}fuckass job-{nw}"
        show cassie dismayed at right
        c "Shut up before you say anything you'll regret."
        c "I will consider it that you misspoke and forget it."
        c "Sure, I wanna quit. So I swear to god, if I’m still stuck here, I will purposely make your life harder."

        jump whyProfessor

    label stayHallway:
        hide mc sad
        stop music fadeout 1.0

        "I didn't go back right away."
        "The hallway was quiet, finally. I can finally think."
        
        show mc neutral at center:
            zoom 1.5
        with dissolve 

        mc "(God, why do people always expect more?)"
        mc "(Why does everyone act like they know what's best for me?)"
        
        c "(You’re better than what you’re settling for.)"
        
        show mc cringe at center
        mc "(Bullshit. Or maybe not. I don't know anymore.)"
        jump stayHallway2
    
    label stayHallway2:
        show mc neutral at center:
            zoom 1.5
        with dissolve
        "I sighed and looked up at the ceiling. Hoping that it would just collapse on me to save me the trouble."

        play sound "audio/running.mp3"
        
        "???" "Excuse me!" 
        mc "(Huh?)"
    
        "???" "move-MOVEMOVEMOVEMOVE"
        
        play sound "audio/s_shove2.ogg"
        with vpunch
        play music "audio/bgm/pillow_dreams.mp3" fadein 5.0 volume 0.5 loop

        
        # Introduce Andrea
        show mc neutral at left:
            zoom 1.5
            
        show andrea dismayed at right: 
            zoom 1.5
        with dissolve
        
        a "Shit, are you okay?" 
        
        mc "Mmm."
        mc "Siguro?"
        
        show andrea sad at right
        a "I'm so sorry, I was in a hurry and kala ko walang tao dito. {w}Nasaktan ka ba?"
        
        show mc neutral at left
        mc "You missed my head, sayang."
        
        show andrea happy at right 
        a "...noted for next time?"

        "She laughs and looks relieved for some reason. She then picks up her scattered things on the floor."
        
        play sound "audio/backpack.mp3"

        menu:
            "Help":
                jump helpAndrea
            
            "Don't Help":
                jump ignoreAndrea

    label helpAndrea:
        $ andrea_rel += 1 # + relationship point with Andrea 
        
        show mc neutral at left
        mc "Here, let me grab that."
        
        show andrea happy at right
        a "Oh. {w}Thank youuuu~"

        "On one of the notebooks that was scattered, I noticed her name on the cover."
        "Andrea Gale Morales."

        jump ontinueAndrea

    label ignoreAndrea:
        $ andrea_rel -= 1 # - relationship point with Andrea
        
        show mc neutral at left
        mc "Don't worry about me. But you should probably hurry up."
        
        show andrea neutral at right
        a "Right, right. Sorry again." 
        
        show mc neutral at left
        mc "(I'm supposed to hate being a burden, not help with other people's.)"

        "On one of the notebooks that was scattered, I noticed her name on the cover."
        "Andrea Gale Morales."
        
        jump ontinueAndrea

    label ontinueAndrea:
        show mc neutral at left
        mc "Wait, hold on."
        mc "You're Andrea?"
        show andrea happy at right #insert andrea curious / confused sprite 
        a "Hm? Yeah, Bakit?"
        show andrea neutral at right
        a "...wait, classmate kita diba?"

        mc "Groupmate mo, actually.."
        a "Groupmate? May project tayo?"
        a "Before that though, {w}can you remind me of your name again?"

        show mc cringe at left
        mc "You seriously don't know? {w}Its-{nw}"
        show andrea dismayed at right
        a "WAIT, is it..."
        a "Mikaela?"
        show mc angry at left
        mc "Who the hell is that?"
        show andrea happy at right
        a "Danica!"
        show mc neutral at left
        mc "???"

        show andrea sad at right
        "*She tries looking at my I.D. but my name was covered by a sticker.*"
        a "Uhh, I forgot."
        mc "It's [firstname], [firstname] [lastname]."
        show andrea happy at right
        a "[firstname], how did I forget? {w}Anyway, I hope your head's fine."
        show mc neutral at left
        mc "Yeah, I'm okay. But uh, weren't you in a hurry? {w}You were running down the hallway."
        a "OH RIGHT. Late na kasi ako."
        "*She checks her things one last time before leaving.*"

        a "Di ka rin ba papasok? Classes aren't over yet."
        show mc cringe at left
        mc "I'll follow later, I was on my way to the cr."

        a "kayyy, I'll see you later."

        hide andrea happy with dissolve
        "With that, she enters the classroom and I was left alone again in the hallway."
        
        show mc neutral at center :
            zoom 1.5
        with dissolve

        mc "Now, should I go back?"
        mc "I have this thing called free will."
        mc "Gives me the option to always just avoid this whole mess altogether."
        mc "Should I?"
        
        menu:
            "Go back inside.":
                jump headBackInside

            "Leave.":
                jump leaveShool

    label leaveShool:
        stop music fadeout 1.0
        hide mc neutral with dissolve
        "Are you sure? Actually leave?"
        "Like, really?"
    
        menu:
            "Yep.":
                jump endingQuitter
            "On second thought, go back inside.":
                jump headBackInside

    label endingQuitter:
        "I sighed one last time, turned around, and walked away from the school."
        "Maybe this was for the best after all."
        "..."
        "....."
        "......."
        "Ending: Quitter"
        "jeez you didn't even try."
        "bye."
        return

    label headBackInside:
    stop music fadeout 1.0 
    stop sound 

    scene bg classroom
    with dissolve
    
    play music "audio/a_classroom1.ogg" volume 1.3 loop

    show mc neutral at left:
        zoom 1.5
    
    mc "(I definitely took the long route to the comfort room.)"

    "When I walked back, I found myself in a noisy class divided into small seats organized according to their groups."
    
    show cassie neutral at right:
        zoom 1.5
    with dissolve
    "I first saw the professor looking at me in her peripheral but ultimately ending up ignoring me as I walk inside, which was relieving, honestly."
    
    hide cassie neutral with dissolve 
    hide mc neutral with dissolve
    
    "I recognize my other groupmates in the corner of the room talking with each other."

    show kira neutral at right:
        zoom 1.5
    with dissolve
    
    show andrea sad at left:
        zoom 1.5
    with dissolve
    
    "Andrea has an oddly serious face while listening to an orange-haired girl."

    "The orange-haired girl, who I presume is Kira, was writing something on a yellow pad {w}and it doesn't look like she's enjoying this brainstorming session so far."
    "(I don't know why, but I have a feeling that I won't get along with her at all.)"
    show kira sarcastic at right
    k "We don't have the budget to experiment with gimmicks. Let's just stick with something straightforward and practical."
    
    show andrea dismayed at left
    a "Yeah, but if it's too basic, wala nang bibili. Let's make it interesting naman."
    
    # Rafaela suggestion
    show rafaela happy at center:
        zoom 1.5
    with vpunch

    r "We could do a FNAF style cupcake booth, and we're like animatronics type shit."
    
    show andrea happy at left
    a "Lowkey kind of genius."

    show kira worried at right 
    k "Seryoso ako ah, wag nga."
    
    show andrea neutral at left
    "*Andrea grumbles.*"

    k "I just want something that the professor would like to secure us a sponsored slot."
    k "We don't have to do anything flashy right now, Just something that would sell."
    a "Can't we just use the siomai idea?"
    
    show kira sarcastic at right
    k "There will be a billion stalls selling the exact same thing, no?"
    
    show andrea dismayed at left
    "*Andrea grumbles again and just opens her phone to use Tiktok.*"

    hide andrea dismayed with dissolve

    show rafaela neutral at center
    r "Wait. Hold up."
    r "What if League of Legends themed delicacies."
    
    show kira confused at right
    k "What does that even mean?"

    # --- Self-Intro ---
    hide rafaela neutral with dissolve
    show mc neutral at center:
        zoom 1.5
    with dissolve

    "*I cleared my throat.*"

    show kira neutral at right
    k "Finally. You're late. Sit."
    
    play sound "audio/chair_move.mp3" volume 0.55
    mc "Glad to be here. I'm [firstname], by the way. This sounds like a fun group."

    k "You know who we are. Then sit and focus. We need to pitch something, there are only three sponsor slots."
    
    show andrea neutral at left:
        zoom 1.5
    with dissolve
    a "Jamie's not even here."
    
    show kira neutral at right
    k "I made a messenger groupchat, if she doesn't reply by Friday, I'll ask the prof to drop her from the group."

    show mc neutral at center
    mc "Isn't that a bit harsh?"
    
    show kira sarcastic at right
    k "I'm just tired of deadweights."
    
    hide andrea neutral

    show rafaela happy at left:
        zoom 1.5
    with dissolve
    
    r "Maybe she died."
    
    show mc happy at center
    mc "Mood."

    show rafaela neutral at left
    r "So uh, no animatronics?"
    
    show kira sarcastic at right

    "*Kira seems to ignore her.*"
    k "Anyway, so?"
    
    show mc neutral at center
    mc "Coffee jelly is always good. We can prep it in batches, it's cheap, people buy it."
    
    hide rafaela neutral with dissolve
    show andrea dismayed at left:
        zoom 1.5
    with dissolve

    a "Sabi nga ni Kira, I bet there will be like ten other groups from other classes selling the exact same thing."
    a "Can we please consider something fun, though?"
    
    show mc neutral at center
    mc "League themed coffee jelly then."
    
    hide andrea dismayed with dissolve

    show rafaela neutral at left:
        zoom 1.5
    with dissolve
    r "Straight from the summoner's rift."
    
    show kira worried at right
    k "What the hell are you guys talking about?"
    k "I swear to god, if this project tanks my grade..."

    # --- MC Confrontation ---
    show mc cringe at center
    mc "..."
    mc "(This girl... I'm getting reaalllyy tired of people trying to boss me around.)"
    mc "(Always so stuck up, always so...)"
    
    show kira neutral at right
    k "Do you want to say something, [firstname]?"
    
    show mc angry at center
    mc "..."
    mc "Matter of fact. I do."
    k "And that is?"
    mc "If this project tanks YOUR grade... {w}then what?"
    mc "You gonna drop all of us and work alone in the booth? {w}Calm down."
    
    $ kira_rel -= 1
    $ rafaela_rel += 1 
    
    show rafaela happy at left
    r "Hell yeah, calm down."

    # --- Sponsor Slot 1 Announcement ---
    play sound "audio/s_notification.ogg" # needs a better ring sound sfx
    "*DING*"
    "Before it could escalate even more, the professor rings a bell on her table to announce something."

    hide rafaela happy with dissolve
    hide mc angry with dissolve
    hide kira neutral with dissolve

    show cassie neutral at center:
        zoom 1.5
    with dissolve 
    
    c "Okay, students. Just to update you all, the first sponsor slot has been officially claimed."
    c "Congrats to group one for their spam musubi 'Missubibi' proposal."
    c "Group one, please come here to discuss the details of the sponsor. The rest may continue."
    
    # needs an applause and groans sfx from students here
    "*Claps and groans were scattered from the class.*"
    
    hide cassie neutral with dissolve
    show kira worried at center: # CG SCENE ILLUSTRATION
        zoom 1.5
    with dissolve
    "*Kira grumbles and then looks at me.*"

    k "..."
    "It really seemed like she was about to say something but decided against it."
    
    # --- Cookies Discussion & Theft ---
    
    show kira neutral at right :
        zoom 1.5
    with dissolve
    show andrea neutral at left:
        zoom 1.5
    with dissolve
    show rafaela neutral at center:
        zoom 1.5
    with dissolve
    
    a "...what if cookies nalang?"
    
    show kira sarcastic at right
    k "Do you even know how to bake?"
    
    show andrea neutral at left
    a "Isang beses lang nasubukan magbake, {w}pero masarap naman."
    
    show rafaela happy at center
    r "Wait, that's a banger idea."
    
    show kira neutral at right
    k "Okay, that's good, we're saved."
    k "I'll think of something to make it more interesting, since that's what *you guys* want."

    hide rafaela happy with dissolve
    show mc neutral at center:
        zoom 1.5
    with dissolve
    mc "(What's with the emphasis?)"

    play sound "audio/s_phone_vibration.mp3"
    show andrea neutral at left
    a "Uy, wait. Si Jamie nag-seen na sa groupchat, {w}should we wait for her input before submitting it to the prof?"
    mc "(Oh yeah, groupmate nga pala namin siya.)"
    
    show kira neutral at right
    k "...sure, let's do that."

    hide andrea neutral with dissolve
    hide mc neutral with dissolve
    hide kira neutral with dissolve
    "........"
    "....."
    "..."
    "After waiting for ten minutes, Jamie didn't message at all and nothing of value was gained."

    # Sponsor Slot 2 
    play sound "audio/s_notification.ogg"
    "*DING*"
    show cassie neutral at center:
        zoom 1.5
    with dissolve
    c "Announcement, the second sponsor slot is officially taken. Group four is selling assorted cookies and desserts. {w}Please proceed to the front."

    "*The class claps and groans again.*"

    hide cassie neutral with dissolve
    show rafaela neutral at left:
        zoom 1.5
    with dissolve
    r "They fucking stole our idea."
    
    show mc neutral at center:
        zoom 1.5
    with dissolve
    mc "Well, at least we proved it was a good idea."
    
    show kira worried at right:
        zoom 1.5
    with dissolve
    k "You think this is funny?"
    
    show mc happy at center 
    mc "A little."

    "Once again, Kira looks like she's about to say something but just sighs."
    hide kira worried with dissolve

    show andrea neutral at right:
        zoom 1.5
    with dissolve

    show mc neutral at center:
        zoom 1.5
    with dissolve


    "Looking over to the rest of the group, {w}I see both Rafaela and Andrea on their phones."
    "(Honestly, not a bad idea.)"
    "(Doomscrolling might be more productive than what we're doing right now.)"
    
    hide rafaela neutral with dissolve
    hide mc neutral with dissolve
    hide andrea neutral with dissolve
    "........"
    "....."
    "..."
    show mc neutral at center:
        zoom 1.5
    with dissolve
    "And doomscroll I did. {w}The others were occassionaly sharing ideas but it eventually goes nowhere."
    # cg illustration of looking at a phone here while kira is staring at Sabrina
    # insert an atual funny meme you'll see srolling through reels and shorts tho, like maybe a short lip or some shit
    stop music fadeout 1.0
    play sound "audio/vineboom.mp3" volume 0.3
    mc "(Heh, {w}funny vine boom sound.)"
    play sound "audio/vineboom.mp3" volume 0.3 loop

    mc "(Heh heh.)"
    play sound "audio/rustle.mp3" volume 0.3
    hide mc neutral with dissolve
    "*Someone elbows me.*"
    show rafaela neutral at right:
        zoom 1.5
    with dissolve

    show mc neutral at left:
        zoom 1.5
    with dissolve
    r "Yo, {w}she's calling you."
    mc "Huh?"

    hide rafaela neutral with dissolve

    show kira neutral at right:
        zoom 1.5
    with dissolve
  
    play sound "audio/a_classroom1.ogg" volume 1.0 loop
    play music "audio/bgm/UT_Threat Imminent.mp3" fadein 2.0 volume 0.6 
    k "..."
    mc "So..."
    mc "Why're you staring at me? {w}Okay ka lang?"
    k "You're not even trying."
    mc "Sorry?"
    k "Tulungan mo naman mag-suggest ng kahit ano. Wag puro tawa."
    mc "I already suggested something???"
    "*Kira just sighs and writes something down*"
    mc "Look, {w}even half the class isn't doing much either."
    k "But we're not half the class. Put in more effort."

    "*I roll my eyes.*"
    mc "(This girl...)"
    mc "You are seriously getting worked up over nothing. May ambag naman ako eh."
    k "I'm not angry, I'm... {w}I'm just saying that-{nw}"
    mc "What's the point of this, anyway?"
    mc "I can't take this project seriously."

    show kira neutral at right
    k "..."
    k "Why are you even here if you're not gonna take this seriously?"
    mc "Because it's a requirement? Like everyone else?"
    show kira worried at right
    k "Then at least act like it matters!"
    
    mc "..."
    show kira sarcastic at right
    k "You know, if *you’re* planning to laze around the whole meeting, maybe just tell us now so we can adjust."
    k "Kanina mo pa ako tinititigan ng masama."

    mc "I.."
    mc "(I don't know what to say, {w}Seems like she already set her mind to be against me.)"
    "(I glanced around the room. A few groups were looking at us now. {w}None of them looks like they were taking my side.)"
    "..."
    mc "(The others are on their phones, pero bakit ako lang yung sinasabihan?)"
    mc "(Bakit, ganito na ba talaga yung imahe nila sakin? {w}Tamad? {w}Walang nagagawang tama?)"
    mc "(Whatever.)"
    
    k "I'm just setting boundaries now, {w}para mas madali sa lahat."
    k "So, do you get it?"
    show mc cringe at left
    mc "I’m listening. I just don’t see why you’re acting like this is life or death."
    k "Oh, I don’t know, {w}maybe because it’s *sixty percent* of our final grade?"
    mc "I thought it was better to shut up than being a hardass and dramatic over a project."


    show andrea neutral at center:
        zoom 1.5
    with dissolve
    a "Guys, can we not... fight?"
    
    k "We're not fighting. May nangiinis lang."
    
    show mc angry at left
    mc "May pabida 'e."
    
    show andrea dismayed at center
    a "What's both of your problems, seriously?"
    
    show kira sarcastic at right
    k "Gee, I wonder."
    
    hide andrea dismayed with dissolve
    show rafaela neutral at center:
        zoom 1.5
    with dissolve
    r "So, what are you guys saying?"
    
    show kira neutral at right
    k "I’m saying that if no one actually does anything, I’m not going to sit here wasting my time. I can just join another group."
    
    hide rafaela neutral with dissolve
    show andrea dismayed at center:
        zoom 1.5
    with dissolve
    a "...okay. {w}Okay, wow."
    
    show mc cringe at left
    mc "Then drop us. We're all dying to be free."
    
    show andrea sad at center
    a "Guys, please naman..."
    
    hide andrea sad with dissolve

    show rafaela happy at center:
        zoom 1.5
    with dissolve
    r "What if you guys punch each other?"
    
    show kira sarcastic at right
    k "You know what? {w}Aalis nalang ako-{nw}"

    # Andrea's Breakdown
    
    hide kira sarcastic
    hide rafaela happy 
    hide mc cringe 

    
    show andrea cry at center:
        zoom 1.5
    with vpunch 
 
    stop sound
    stop music

    play sound "audio/stand_up.mp3" volume 0.75

    a "CAN YOU ALL JUST SHUT UP?"
    
    # CG ILLUSTRATION SCENE HERE
    # TOTAL SILENCE HERE. CUT ALL AMBIENCE
   

    "........"
    "....."
    "..."
    "Silence."
    
    "The whole class seems to be listening to us now."
    "..."
    play music "audio/a_classroom1.ogg" volume 1.2 loop
    "We let the silence linger until the groups start talking amongst themselves again."
    
    show andrea sad at left:
        zoom 1.5
    with dissolve

    show mc neutral at center:
        zoom 1.5
    with dissolve

    show kira sarcastic at right:
        zoom 1.5
    with dissolve
    a "Uh..."
    a "I didn't mean to yell."
    a "Sorry, I just... kung babagsak ako dito, If I fail the course, I have to repeat the year. And... I can't do that."

    mc "Uh..."
    mc" ..."

    mc "(Shit, What the hell do I say to that?)"
    mc "(Sorry. I'm gonna fail, too. Don't worry?)"
    mc "(Tangina.)"

    a "Sorry. {w}I... {w}I just need some air."
    play sound "audio/chair_move.mp3" volume 0.55
    hide andrea sad with dissolve
    "*She grabs her phone and walks out without waiting for permission.*"
    
    hide kira sarcastic at right with dissolve
    "*Kira also stands up to join a group with her friends in it.*"
    mc "(She's probably going try and join other groups.)"
    
    show mc cringe at center
    mc "(But, I doubt that will happen. The prof did explicitly tell us that changing groups isn't allowed.)"

    $ andrea_rel -= 1
    $ kira_rel -= 1

    hide mc cringe with dissolve
    show rafaela neutral at right:
        zoom 1.5
    with dissolve
    r "Uh, now what? Are we still doing cookies?"
    
    show mc sad at left:
        zoom 1.5
    with dissolve
    mc "..."
    mc "(This group is a mess.)"

    return

    ## WIP HERE
    ## EDIT HERE
    ## BOOKMARK

    
# --- Start of archived code block ---
"""

    show rafaela neutral at right
    r "Seriously, what now?"
    mc "We bake our own cookies and sabotage group four?"
    r "I don't even have an oven."
    mc "...same."
    "I didn't know what to add after that."
    "At least when the rest were here, we were discussing something. Now it's just too quiet."
    "Andrea and Kira's chair were empty, they never came back."

    show mc neutral at left
    mc "You think Andrea's okay?"
    r "Probably not. I don't know."
    mc "My brain feels like it's melting."
    r "Same."

    "Time drags on. The class were still talking about what to do with their groups, some were even arguing but nothing comparable to what happened earlier."

    "I stared at the clock. Ten minutes passed. Then fifteen."

    "The group beside us is already sketching their booth layout. Another one is practicing how to sell their product. All I had in front of me was a doodle that Rafaela made of a cupcake getting eaten by an animatronic fox."

    # --- Final Sponsor Slot Announcement ---
    play sound "audio/s_notification.ogg"
    "*DING*"
    
    show cassie neutral at right
    c "Final announcement. Group six just submitted their pitch and claimed the final sponsor slot."

    "Murmurs spread through the class."

    c "To the rest of the class, don't panic. You can still get booths, but you'll have to provide your own tents and coordinate with the student event organizers on where you'll be placing them. But again, having a booth is entirely optional."
    c "If you need further guidance, just contact me."

    "The professor closes her laptop and dismisses the class."
    
    # --- Scene Exit ---
    hide cassie neutral with dissolve
    "The students start leaving one by one, some were still discussing what to do with their projects, but some just looked so done with it."
    
    show rafaela neutral at right
    "I noticed Rafaela getting up her seat."

    mc "Where are you going?"
    r "Ima dip."
    
    show mc sad at left
    mc "Hey-"
    mc "(Aaaand she's gone. Great.)"
    
    hide r neutral with dissolve
    
    "Silence settled in again. This time. I was alone in the room."
    "I didn't really like this kind of quiet. It made you think."

    show mc cringe at center
    mc "Tangina talaga."

    "I got up and went home."

"""
# --- End of archived code block ---

return