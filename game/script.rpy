# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Andrea", who_color="#d2e2eb", what_color="#FFFFFF")
define r = Character("Rafaela", who_color="#dacd7f", what_color="#FFFFFF")
define k = Character("Kira", who_color="#d3ad8b", what_color="#FFFFFF")
define j = Character("Jamie", who_color="#a15656", what_color="#FFFFFF")
define c = Character("Ms. Cassandra", who_color="#9e8677", what_color="#FFFFFF")
define l = Character("Loraine", who_color="#a298c6", what_color="#FFFFFF")
define h = Character("Haifa", who_color="#93c386", what_color="#FFFFFF")

# Custom positions

# The game starts here.

label start:
    play music "audio/bgm/spring.mp3" fadein 2.0 volume 0.6
    scene bg classroom
    with dissolve 

    show mc happy at left:
        zoom 1.5
    with dissolve
    "......."
    "....."
    "..."

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

    define mc = Character("[firstname]", who_color="#72a5d4", what_color="#FFFFFF")
    python:
        firstname = renpy.input("What is your first name? (Default = Sabrina)", length=15)
        firstname = firstname.strip()

        if firstname == "":
            firstname = "Sabrina"

    define mc2 = Character("[lastname]", who_color="#72a5d4", what_color="#FFFFFF")
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
        #have a plus point relation here with loraine
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
        #have a minus relationship point here with loraine
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
        l "Oh, oh sh-good luck."

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
    menu: 
        "Isn't Kira an honor student?" if not kira_asked:
            jump kiraLoraine
        
        "You had fun being Andrea's groupmate before." if not andrea_asked:
            jump andreaLoraine

        "Rafaela's not that bad right?" if not rafaela_asked:
            jump rafaelaLoraine

        "Didn't you owe Jamie something?" if not jamie_asked:
            jump jamieLoraine

        "I'm done asking.":
            jump finishLoraine

    label kiraLoraine:
        # Set flag to True
        $ kira_asked = True
        
        show mc neutral at left
        mc "Isn't Kira an honor student?"
        
        "*Loraine looks around and pulls me close*"
        show loraine sweat at right
        l "Shh, she might overhear. {w}Kira's great and all but she has zero chill."
        l "Last time I was her groupmate, {w}I couldn't tell if she was being sarcastic or not."
        
        show mc cringe at left
        mc "Yikes..."
        jump questionLoraine

    label andreaLoraine:
        # Set flag to True
        $ andrea_asked = True
        
        show mc neutral at left
        mc "You had fun being Andrea's groupmate before."
        
        show loraine sweat at right
        l "She's active most of the time but... {w}I think she lags in real life. Like, you'd have to call her name multiple times to even get her attention."
        l "Look, she's not even present in the class right now. {w}I don't even know how she got her name in the wheel."
        
        show mc sad at left
        mc "Oh."
        jump questionLoraine

    label rafaelaLoraine:
        # Set flag to True
        $ rafaela_asked = True
        
        show mc neutral at left
        mc "Rafaela's not that bad right?"
        
        show loraine neutral at right
        l "Ehh, she's okay I guess. {w}But to be honest, I don't know her much, I'm pretty sure no one does either."
        
        show mc neutral at left
        mc "Doesn't sound too bad."
        jump questionLoraine

    label jamieLoraine:
        # Set flag to True
        $ jamie_asked = True
        
        show mc neutral at left
        mc "Didn't you owe Jamie something? What's that about?"
        
        show loraine neutral at right
        l "She helps around when in OTHER classes, but the thing is she's absent almost everyday. I'm pretty sure she dropped this class already."
        l "She just shows up sometimes for some reason."
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
        hide loraine neutral with dissolve
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

    mc "Not really, Ma'am, what was it again?"
    show cassie dismayed at right
    "*Professor Cassandra exhales hard*"

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
        mc "...scared of what? Group projects and capitalism?"
        mc "Both are pretty tricky in my experience."
        c "Capitalism? Where did that even..."
        show cassie happy at right
        "*Professor Cassandra shakes her head.*"
        c "There it is."
        c "Same lines. Same jokes. Every time someone gets too personal with you." 

        "..."
        show cassie neutral at right
        c "...look. I don’t care if you fail your other classes or end up having to stop your education."
        c "But you’re in my class right now. So I care just enough to tell you this."
        c "You’re better than what you’re settling for."

        show mc cringe at left
        mc "...I don't know what you're talking about, Ma'am, but I appreciate it."
        c "..."
        c "Alright then."
        c "Anyway. I’ve got thirty-four other students to deal with. {w}I don’t have time to babysit kids who don't even try."
        c "You want to fail? Be my guest."

        # "I cleared my throat and forced a grin."
        # $firstname ""...So no free pass then?""
        # c ""If I gave you one, you’d just waste it too."

        c "Go back inside. Try not to be a burden your groupmates. Maybe surprise yourself this time."

        "She went back inside the room, leaving me alone in the hallway."
        hide cassie neutral with dissolve
        
        show mc neutral at left
        mc "(God, why do people always expect more?)"
        mc "(Is it that hard to mind your own business?)"
        mc "(...whatever. Not like this changes anything.)"
        mc "(Right?)"
        "..."
        mc "(I don't want to go back.)"

        menu:
            "Think for a while.":
                jump stayHallway

            "Leave the damn school.":
                jump leaveHallway

    label okProfessor:
        # have a minus relationship point here with cassie
        show mc angry at left
        mc "Why do you even care? It’s not like I’m your best student or something."
        mc "And...  {w}aren't you just some student teacher who wants to quit her fuckass job-{nw}"
        show cassie dismayed at right
        c "Shut up before you say anything you'll regret."
        c "I will consider it that you misspoke and forget it."
        c "Sure, I wanna quit. So I swear to god, if I’m still stuck here, I will purposely make your life harder."

        jump whyProfessor

    label stayHallway:
        hide mc sad
        play sound "audio/campus_ambiance.mp3" volume 0.2 fadein 1.0 loop

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

        show mc neutral at center
        "I sighed and looked up at the ceiling. Hoping that it would just collapse on me to save me the trouble."

        play sound "audio/s_footsteps.ogg"
        
        "???" "Excuse me!" 
        
        play sound "audio/running.mp3"
        "???" "move-MOVEMOVEMOVEMOVE"
        
        hide mc neutral with vpunch
        play sound "audio/s_shove2.ogg"
        
        # Introduce Andrea
        show andrea dismayed at right: 
            zoom 1.5
        with dissolve
        

        a "Shit, are you okay?" 
        
        show mc neutral at left:
            zoom 1.5
        with dissolve
        mc "Mmm."
        mc "Siguro?"
        
        show andrea sad at right
        "???" "I'm so sorry, I was in a hurry and kala ko walang tao dito. {w}Nasaktan ka ba?"
        
        show mc neutral at left
        mc "You missed my head, sayang."
        
        show andrea happy at right # Andrea laughs, relieved that MC is joking
        "???" "...noted for next time?"

        "She laughs and looks relieved for some reason. She then picks up her scattered things on the floor."
        
        play sound "audio/backpack.mp3"

        menu:
            "Help":
                jump helpAndrea
            
            "Don't Help":
                jump ignoreAndrea

    label helpAndrea:
        # + relationship point with Andrea 
        
        show mc neutral at left
        mc "Here, let me grab that."
        
        show andrea happy at right
        a "Oh. {w}Thank youuuu."

        "On one of the notebooks that was scattered, I noticed her name on the cover."
        "Andrea Gale Morales."

        jump ontinueAndrea

    label ignoreAndrea:
        # - relationship point with Andrea
        
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
        mc "You're Andrea?"
        a "Hm? Yeah, Bakit?"
        a "...wait, classmate kita diba?"

        mc "Groupmate mo, actually.."
        a "Groupmate? May project tayo?"
        a "Before that though, {w}can you remind me of your name again?"

        mc "You seriously don't know? {w}Its-{nw}"
        a "WAIT, is it..."
        a "Mikaela?"
        mc "Who the hell is that?"
        a "Danica!"
        mc "???"

        "*She tries looking at my I.D. but my name was covered by a sticker.*"
        a "Uhh, I forgot."
        mc "It's {firstname}, {firstname} {lastname}."
        a "{firstname}, how did I forget? {w}Anyway, I hope your head's fine."
        mc "Yeah, I'm okay. But uh, weren't you in a hurry? {w} Tumatakbo ka 'e."
        a "OH RIGHT. Late na kasi ako."
        "*She checks her things one last time before leaving.*"

        a "Di ka rin ba papasok? Classes aren't over yet."
        mc "I'll follow later, I was on my way to the cr."

        a "kayyy, I'll see you later."

        "With that, she enters the classroom and I was left alone again in the hallway."
        mc "Now, should I go back?"
        mc "I have this thing called free will."
        mc "Gives me the option to always just avoid this whole mess altogether."
        mc "Should I?"
        
        menu:
            "Go back inside.":
                jump headBackInside

            "Leave.":
                jump leaveShool

    label headBackInside:
        
        # Stop the campus sound effects
        stop sound
        stop music fadeout 1.0
        
        # Go back to the main classroom scene (assuming you'll continue with the rest of the class)
        scene bg classroom
        with dissolve
        
        # (Continue the script here)
        # return # Or return to end the demo/script

    label leaveShool
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
        "Ending: The Quitter"
        "jeez you didn't even try."
        "bye."

    stop music fadeout 1.0
    return