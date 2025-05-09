﻿init:
    # Screen configuration.
    $ config.screen_width = 1920
    $ config.screen_height = 1080
    $ config.window_title = "Oath"

    # Charcter definitions
    define mc = Character("[MC_name]")
    default MC_name = "Cecil"
    default MC_pronouns = "they/them"
    define i = Character("Ivy")
    define p = Character("Pat")
    define y = Character("Yubin")
    define k = Character("Karina")
    define mr = Character("Mr. Mahraun")
    define idk = Character("???")

    # Character sprites
    image karina_neutral = "karina_neutral.png"
    image karina_sad = "karina_sad.png"
    image ivy = "wide_ivy.png"
    image pat = "wide_pat.png"
    image cecil = "wide_cecil.png"
    image yubin = "wide_yubin.png"

    # Images
    image bg_black = "bg_black.png"
    image bg_temp_class = "temp_classroom.jpg"
    image bg_cafe = "cafe.png"
    image bg_class = "classroom.png"
    image bg_hall = "hallway.png"
    image bg_mc_bedroom = "mc_bedroom.png"
    image bg_yubin_bedroom = "yubin_bedroom.png"
    image bg_library = "library.png"
    image bg_icerink = "icerink.png"
    image bg_neighbor = "neighborhood.png"

    # White flash
    $ flash = Fade(.25, 0, .75, color="#ffffff")

    # Black fade
    $ fade = Fade(.25, 0, .75, color="#000000")


# The game starts here.

label start:
    # Week 1 Introduction Scene
    scene bg_black

    "January 20XX"
    "For the seniors of Willow Creek High, January marked the start of their last semester at the now familiar school. Some were already planning their futures, early admissions and decisions making the remaining months stress-free."
    
    show cecil with fade
    
    "…Others, less so. You are one of them, opening your locker to pull out your school supplies for the first day back since winter break. Neatly written on the cover is your name…"

    $ MC_name = renpy.input("What is your name?", default="Cecil")
    $ MC_name = MC_name.strip()

    if not MC_name:
        $MC_name = "Cecil"

    "And your pronouns?"

    menu:
        "He/Him":
            $ MC_pronouns = "he/him"
        "She/Her":
            $ MC_pronouns = "she/her"
        "They/Them":
            $ MC_pronouns = "they/them"

    hide cecil
    scene bg_hall with fade

    "You can’t believe the break went by so fast. The last semester had been hectic, applying to colleges taking up most of your time. Now, you can try to relax and enjoy the last high school semester of your life."

    i "[MC_name!u]!!"

    show ivy with flash

    "Your best friend, Ivy, comes barreling into you, picking you up into a spinning hug. It makes you a little dizzy, but she sets you down carefully as she always does. Your family had gone on a trip over break, so you haven’t seen her in a little while."

    "… Which would explain the dramatics."

    i "It’s been so long! How have you {i}been{/i}? We need to catch up!"

    menu:
        "Good! How have you been?":
            i "That’s good! I’ve been up to the usual, hehe. Not much to do around here!"
        "Tired, actually.":
            i "Oh… Was the trip that busy?"
        "We’ve been texting this whole time, Ivy…":
            i "I know, I know! But I want to hear it from you. It’s not the same otherwise."

    i "Anyway, when’s your first free period?"

    "You show her your schedule."

    i "Oh, damn… Not until the afternoon. That sucks. At least we have English together~ I’ll see you then!"

    hide ivy
    show cecil

    mc "See you!"

    hide cecil

    "She leaves as quickly as she came. You remember that her first class is all the way across the building, and wish her luck silently. You’re sure she’ll make it before the first bell… probably."

    scene bg_class with fade

    "Class is normal as always. Senior year, the teachers always start acting more relaxed, even allowing for some students to skip class. It’ll be the time of tours and admissions soon, so you kind of get it."

    "You’re pretty sure the person behind you is actually just snoring, though."

    mr "… will be working in pairs. This project is worth 10\% of your final grade, and we’ll be working on it alongside our classwork the entire semester."

    "The entire class perks up. You can see friends start to surreptitiously scooch closer together."

    mr "These pairs will be randomly determined. Everybody, stand up."

    "After a bit of shuffling around a small game that you think that Mr. Mahraun just wanted to play, you are left face-to-face with a stranger."

    "It’s not strange for you to not know everybody in your grade, but you’re pretty sure you’ve seen most of the people around town. It’s not a big one, anyway- even if you don’t know their name. But this person is a bona-fide stranger."

    show pat

    idk "Um..."

    hide pat
    show cecil

    mc "Um, hello! My name is [MC_name], [MC_pronouns]. It’s nice to meet you!"

    hide cecil
    show pat

    p "Pat… Pat Cordova, they/them."

    hide pat
    show cecil

    mc "..."

    hide cecil
    show pat

    p "..."

    hide pat

    "You come to the conclusion that you definitely haven’t seen them before, either in town or school. Maybe seeing the confusion on your face, they sigh and offer an explanation."

    show pat
    
    p "I just moved here a few days ago."

    menu:
        "For the second half of your senior year? That must be tough…":
            p "...I guess."
        "Welcome to Willow Creek!":
            p "Thanks..."
        "Let me know if you need any help.":
            p "Thanks, I will."

    hide pat
    
    "Conversation dies down as all other pairs finish introducing themselves to each other- or so they’d claim. You’re pretty sure that they’re just catching up from break."

    "You exchange contact information with Pat."

    show pat

    p "We should message about the project later…"

    hide pat
    show cecil

    mc "Yeah, sure! The proposal’s due in a week, so we can message after school."

    hide cecil

    "The bell rings."

    show pat

    p "We really spent a lot of time in that activity… I’ll see you, then."

    hide pat
    show cecil

    mc "See you!"


    hide cecil
    with fade

    "You’re lucky that your lunch period is during a normal lunch time. The cafeteria is packed, and you have to weave around students in order to find a seat to quickly eat."

    "It’s too bad that Ivy doesn’t have the same lunch as you, but it’s not like you don’t know anyone else. You approach one of those such friends."

    show cecil

    mc "Hey, Karina!"

    hide cecil
    show karina_neutral at center

    k "[MC_name], fancy seeing you here!"

    hide karina_neutral

    "You smile, finding your place across the table. It’s a joke between you two, after you had slipped up upon seeing her in your advising group- the advising group that you shared with her."

    show karina_neutral at center
    
    k "Had a lively break?"

    hide karina_neutral
    show cecil

    mc "You don’t even know…"

    hide cecil
    show karina_neutral at center

    k "You’re telling me. I need to figure out how to tell Mrs. Hughes that I won’t be around for an entire week."

    menu:
        "Ouch. Good luck.":
            k "Thanks. I’ll figure it out, hopefully… "
        "A whole week? What are you doing?":
            k "College tours, what else? My parents want me to know what the campuses look like before I make a decision."
        "(Give an empathetic sigh.)":
            k "Don’t give me that look. You know me, I’ll be able to figure out… somehow."

    hide karina_neutral

    "She laughs it off."

    show karina_neutral at center

    k "Let’s talk about something else, though. That’s a problem for the future!"

    hide karina_neutral
    show cecil

    mc "Yeah, right."

    hide cecil

    "She’s probably already drafted up an email in her head, knowing her. You wonder if the word procrastination is even in her dictionary."

    "The rest of lunch goes by with idle chatter. It’s nice, and you two catch each other up on what you had been doing over break."

    "If you had told your freshman self that you and Karina would have been friends in senior year, you probably would have laughed. Though not exactly {i}popular{/i}, the two of you had been in different circles all throughout middle school, and you had expected that to stay like that."

    show karina_neutral at center
    
    k "I’ve gotta run! Can’t be late to class on the first day of school."

    hide karina_neutral
    show cecil

    mc "Go, go! Text you later!"

    hide cecil
    show karina_neutral at center

    k "Bye!"

    hide karina_neutral

    scene bg_hall with fade

    idk "[MC_name]? Is that you?"

    "A voice calls out to you as you are packing to leave. Glancing over your shoulder, you look around for the source."

    idk "[MC_name]!"

    show cecil

    mc "...?"

    hide cecil

    "An unfamiliar student walks over to you."

    show yubin

    idk " It’s me. We used to play together all the time as kids!"

    "A vague memory comes to you, but it doesn’t match with the person you see before you. You used to play with a neighbor’s kid all the way back in elementary school, but…"

    y "It’s me, Yubin! Yubin Kim? Does that name ring a bell?"

    hide yubin
    show cecil

    mc "The neighbor’s kid?"

    hide cecil
    show yubin

    y "Yes! It’s been a long time!"

    "That’s an understatement. It’s been, what, how many years?"

    hide yubin
    show cecil

    mc "Woah, did you just move back? When did you get here?"

    hide cecil
    show yubin

    y "I just moved back over winter break."

    "An awkward silence follows. While you two were incredibly close as children, it’s been years since you’ve talked. What would you even talk about?"

    menu:
        "So… how have you been?":
            y "I’ve been well! … I mean, that’s a bit of a broad summary of everything that happened, but, you know."
        "Let’s catch up sometime!":
            y "We should! Are you free this weekend?"
        "Why did you move back?":
            y "Well, the same reason I moved away. Dad’s job and all."
    
    hide yubin
    show cecil

    mc "It’s great to see you again! Do you need any help settling in, or…"

    hide cecil
    show yubin
    
    y "Nah, all the teachers have been super helpful. I’ll let you know if I need anything, though."
    
    y "That reminds me: what’s your number? The last time we saw each other, neither of us had phones, haha!"

    hide yubin

    "The two of you exchange contact information. It feels a little strange, like you’ve jumped from childhood to near-adulthood in just minutes."

    "In a way, you have."

    show cecil

    mc "Are you back in the same house again?"

    hide cecil
    show yubin

    y "That would have been a huge coincidence! But no, we’re a couple streets over. You can still come visit if you want, though! Just like old times!"
    
    hide yubin
    show cecil

    mc "I’ll look forward to it!"

    hide cecil

    "The interaction still ends with some awkwardness, but you wave bye to Yubin as you head down opposite ends of the hallway."

    jump weekend

label weekend:
    scene bg_mc_bedroom with fade

    "And before you know it, it’s the weekend. There’s a lot that you can do, now that you have free time."

    menu:
        "Do you..."

        "Hang Out with Ivy":
            jump ivy_w1

        "Study with Pat":
            jump pat_w1
        
        "Catch Up with Yubin":
            jump yubin_w1
        
        "Meet with Karina":
            jump karina_w1
        
        "Stay at Home":
            jump stay_at_home

label stay_at_home:
    "You have too much to do this week to meet up with anyone. You remain at home, spending time with family and catching up on homework."

    "It’s a little bit lonely, but at the end of it all, you feel relieved. You can still spend time with people next weekend!"

    jump end_demo

label ivy_w1:
    "Over the weekend, Ivy texts you asking if you’re free. After you confirm, she proposes that the two of you go ice skating. On Saturday, you bundle up and join her at the local ice rink."

    scene bg_icerink with fade

    show ivy
    
    i "Two hours of skating in circles! I couldn’t ask for anything better."

    hide ivy

    "Neither of you have much ice-skating experience, so the two of you strap on your skates and wobble onto the ice. Ivy suddenly grabs onto you, almost causing you to fall over."

    show ivy
    
    i "Oops, sorry! I thought I was going to fall over. How do you move again? I forgot!"

    hide ivy

    "After a couple of near-death experiences (according to Ivy), the two of you start on your cyclic ice-skating adventure."

    show ivy

    i "Tell me all the deets about your trip! I know you already told me most of it, but tell me more."

    hide ivy

    "You describe your family’s winter break trip to Ivy again in great detail."

    show ivy

    i "Ugh, that sounds like so much fun! My winter break was just writing a million essays and practicing my German."

    hide ivy

    "They try to sound nonchalant, but you can hear the hint of uncertainty in their voice. You know they’re really hoping to study abroad in Germany for university. But you also know that underneath Ivy’s bubbly exterior, they’re incredibly smart, so you’re confident they’ll succeed."

    show cecil
    
    mc "Don’t worry too much about it. I’m sure all your hard work will pay off."

    hide cecil

    "Ivy laughs a little sheepishly."

    show ivy

    i "Was it that obvious? Thanks, [MC_name]."

    i "Oh, speaking of school - I heard that there’s a new student in our grade! Do you know if anyone knows them?"

    hide ivy
    show cecil

    mc "Oh, they’re my partner for Mr. Mahraun’s class project! Their name is Pat."

    hide cecil
    show ivy

    i "Awesome! You {i}need{/i} to introduce me sometime."

    hide ivy
    show cecil

    mc "Sure! Maybe next weekend."

    hide cecil

    "You’re surprised Ivy hasn’t actually met Pat yet, considering she’s friends with just about everyone in your grade. Honestly, you’re a bit jealous of these connections - with them, she got some good recommendation letters for college."

    show ivy
    
    i "Moving here so late into the school year must be hard… I wonder what major they’re aiming for!"

    hide ivy

    idk "Um- hey there!"

    "An unfamiliar girl approaches the two of you. Judging from Ivy’s reaction, they don’t recognize the girl either."

    show ivy

    i "Oh, hey! Need something?"

    hide ivy

    idk "Hi. I- uh, I thought you look kinda cute! Would you want to exchange numbers and chat sometime?"

    show ivy

    i "Aww, thanks! I’d love to, but I’m not looking for a romantic relationship- although I’d totally want to be friends!"

    hide ivy

    idk "Oh, are you not into girls…?"

    show ivy

    i "Nope, sorry! Not into guys either- I’m just not into anyone."

    hide ivy

    "The girl looks between the two of you, confused."

    idk "Is this, like, abstinence…?"

    show ivy

    i "Actually, I’m aro-ace, so I’m just not interested in anyone romantically or sexually."

    hide ivy

    idk "Oh. Uh… okay…"

    "The girl skates away back to a group of other people that seem to be her friends. They start talking quietly amongst themselves. Ivy looks at you and sighs."

    show ivy

    i "Should we add another one to the “is it abstinence” counter?"

    hide ivy

    "You pull out your phone and open your messages with Ivy. You’ve been keeping track of the various unwarranted comments people give the two of you when you talk about your asexuality."

    show cecil

    mc "…That makes four."

    hide cecil
    show ivy

    i "Man, that really sucks. She looked cute, too- I wanted to exchange fashion tips!"

    hide ivy
    show cecil

    mc "Hey, you could always talk fashion with me."

    hide cecil
    show ivy

    i "Of course not! You keep wearing that old vest! How many times have I told you to get another one!"

    hide ivy

    "The two of you laugh and resume skating while chatting aimlessly. You try to put the incident out of your mind, but it nags at you until you fall asleep that night."

    jump end_demo

label karina_w1:
    "You and Karina exchange messages for some time, when she abruptly asks if you’re free at the moment. You are, and you say so, so you two arrange to meet at a nearby cafe."

    scene bg_cafe with fade

    "The moment you open the door, you’re greeted to Karina’s almost overenthusiastic greeting. She’s not usually this showy."
    
    show karina_neutral at center

    k "[MC_name]! It's {i}so{/i} good to see you."
    
    hide karina_neutral
    show cecil

    mc "Karina! Is everything ok? Your message made it seem like it was urgent."

    hide cecil
    show karina_neutral at center

    k "Huh? Oh yeah! Everything’s fine. Thought that if we were going to be spending our weekend texting each other anyway, we might as well actually chat in person."

    hide karina_neutral

    "You get the sense that it’s not the full truth, but you decide not to push. If Karina wanted to talk about it, you trusted that she would."

    show cecil

    mc "That’s true. You got me out of the house, at least."

    hide cecil
    show karina_neutral at center

    k "Mhm!"

    k "I’ve been to this cafe a few times before, and their lattes are pretty good!"

    hide karina_neutral

    "You take a sip of your own drink. It's too bad you didn't get a latte."

    "The two of you make some small talk as she plays with the edge of her drink. Soon enough, her expression grows more serious."

    show karina_sad at center

    k "Hey, [MC_name]... Have you ever been in a relationship?"

    hide karina_sad

    "That’s a bit out of the blue… You think about responding, but you feel like it might be a hypothetical question. She sighs."

    show cecil

    mc "Karina… is this about your breakup?"

    hide cecil
    show karina_sad at center

    k "A little bit, yeah."

    hide karina_sad
    show cecil

    mc "Oh... is everything alright?"

    hide cecil
    show karina_neutral at center

    k "Yeah, sorry to worry you. I just really needed to get out of the house."

    hide karina_neutral

    "You nod. Though you don’t know all the details, Karina has mentioned her struggle with coming out to her parents in passing a few times."

    show karina_sad at center

    menu:
        k "Have you talked to your parents about this sort of thing?"

        "This sort of thing?":
            k "You know… Coming out, their thoughts on the community, and so on."

        "Yes, I was lucky it went well.":
            hide karina_sad
            show karina_neutral at center
            k "Oh? That's good. I’m happy for you."
            hide karina_neutral
            show karina_sad at center

        "Yes, but they didn’t take it well.":
            k "You and me both. I’m… sorry to hear that."

        "Not really.":
            k "I’m wondering if that would have been the better option, to be honest."

    k "Somehow, they took the fact that I had a girlfriend better than explaining what my sexuality was."

    k "It wouldn’t be so bad if they didn’t bring it up so… condescendingly. I’m thinking I might stop trying to explain it to them."

    hide karina_sad
    show cecil

    mc "You should do what makes you feel most comfortable. Nobody is owed an explanation for your identity, no matter who it is."

    hide cecil
    show karina_sad at center

    k "You’re right. I know you're right, but..."
    
    k "It’s just such an important part of myself... I hoped the people I cared about could accept it."

    hide karina_sad

    "You know that there isn't much you can do to help. You put your hand on their's, and they smile, though not completely genuinely."

    show karina_neutral at center

    k "Thanks, [MC_name]."

    k "This is my problem, though. Sorry for dragging you out just to hear me rant."

    hide karina_neutral
    show cecil

    mc "No worries. I’m glad to help."

    hide cecil
    show karina_neutral at center

    k "Next time, let me treat you to something. I can’t just keep letting you listen to my problems with nothing in exchange!"

    hide karina_neutral

    "You laugh, and the seriousness is broken. The two of you spend some more time on more lighthearted conversation before Karina gets a message and gives you a quick goodbye."

    "You finish your drink and head home."

    jump end_demo

label yubin_w1:
    "Over the weekend, you decide to head to Yubin’s to catch up with him. As soon as you ring the doorbell, the door swings open and you’re immediately attacked by a small, white, fluffy mass."

    show yubin

    y "Dubu, get back here! Sorry about that! Hey, [MC_name]!"

    "Yubin picks up the wriggling mass and smiles at you apologetically."

    y "Dubu’s just a puppy, so she’s very excitable. Come in! You can put your shoes here."

    hide yubin

    "You go inside and take off your shoes, then follow Yubin (and Dubu) upstairs to his room."

    scene yubin_bedroom with fade

    show yubin

    y "So, um..."

    hide yubin

    "The air around the two of you becomes extremely awkward again. Dubu yips."

    show yubin

    y "Uh... yea, it’s been a while. Hey, do you want to see pictures from Korea?"

    hide yubin

    "He opens up his phone and shows you a multitude of photos: high school, Korean scenery, him with his friends."
    
    "As he shows you memories of the past, an understanding starts to dawn in your mind."

    show cecil

    mc "Yubin, um..."

    hide cecil
    show yubin

    y "Yeah, I knew you would ask. I… I should explain, huh?"

    hide yubin

    "He laughs a little nervously and stares down at Dubu."

    show yubin

    y "When I was a girl, it always felt weird. Like I shouldn’t be a girl. But God made me a girl, and God doesn’t make mistakes. Then I saw people online talking about... being transgender. Like, actually being a boy when you were born a girl."

    y "It sounded similar to what I felt, so, um in high school, I decided to be a boy… I started wearing the boy’s uniform. And yeah. I’m a boy. I guess… God made me a boy that looks like a girl, haha."
    
    y "Lucky for me, Korean doesn’t often use gendered language, but it was harder for me to adjust in English. Um..."

    hide yubin

    "You can see Yubin start to fidget with the hem of his shirt. He looks at you cautiously, as though he’s expecting something from you."

    show cecil

    mc "I’m happy for you, Yubin! I’m glad that you figured it out and you feel more comfortable now. How did telling your parents go?"

    hide cecil
    show yubin

    "Yubin looks relieved. He starts to pet Dubu."

    y "Thanks. Um... I was scared to tell my parents, since I thought they’d think I was wrong or going against God’s will… but they actually understood me and wanted to help me."
    
    y "You know, they told my little cousins to call me “Hyung” - like, big brother - instead of “Noona” - like, big sister - ... I feel so blessed to have parents like them."

    y "Some of the people at my old church didn’t like me anymore, though... We ended up moving churches."

    hide yubin

    "He sighs. You know religion is a big part of his identity. Even if members of his religious community weren’t accepting of him anymore, you’re relieved that he was able to reconcile his beliefs with his gender identity."

    show yubin
    
    y "It’s funny, though. Instead of guys, they keep asking me if there are any girls I like."

    y "I’m not sure how to break it to them that, um, I’ve never really liked anyone like that..."

    hide yubin

    "Hmm, could it be...?"

    show cecil

    mc "Do you think you’re aromantic? That means you don’t feel romantic attraction to anybody. You could be asexual as well, which means you don’t feel sexual attraction either."

    hide cecil
    show yubin
    
    y "There’s a word for that? Wait, I didn’t know that. How did you know?"

    hide yubin
    show cecil

    mc "I, along with some of my friends, identify as some form of aromatic or asexual! It’s also kind of a spectrum - sometimes you can feel romantic or sexual attraction, but not all the time."

    hide cecil
    
    "You spend a couple of minutes explaining the aromantic-asexual umbrella, which you’ve researched extensively after you - and some of your friends - began identifying as ace. Yubin nods and takes in your every word."

    show yubin
    
    y "That makes sense. Then, yes... I think I’m aro-ace. I always thought it was weird that other people wanted boyfriends or girlfriends, but I never did. Thanks, [MC_name]... um, how do I explain this to my parents?"

    hide yubin
    
    "You help Yubin figure out how to explain the concept to his parents. Soon, the smell of delicious food wafts through the house, and his mother calls the two of you downstairs to eat lunch." 
    
    "Over your meal, Yubin explains his feelings to his parents, while you provide some support. They don’t quite seem to understand, but Yubin assures you they’ll get it in time. Apparently, they were the same way when he told them he was trans."

    "After lunch, the two of you play with Dubu for a while. Eventually, you take your leave."

    show yubin

    y "Thanks again, [MC_name]. It was really nice to see you! We should hang out again soon."

    hide yubin

    "You hear the pattering of small feet behind Yubin, and he quickly waves and shuts the door. You hear him scold Dubu and tell her to stay put, and you laugh as you make your way back home."

    jump end_demo

label pat_w1:
    "With a quick exchange of messages, you and Pat decide to meet up at the local library to work on your project together." 

    scene bg_library with fade

    "You thought you were early, but once you arrive you see Pat sitting at one of the tables in the center, books and computer already out."

    "They don’t seem to notice you until you slide into the seat across from them."

    show cecil

    mc "Hey, Pat!"

    hide cecil

    "They jump."

    show pat

    p "[MC_name]! You scared me!"

    hide pat
    show cecil

    mc "Haha, sorry. What are you focused on?"

    hide cecil
    show pat

    p "My other assignments... I don’t really have anything else to do."

    hide pat

    "While you {i}are{/i} unpacking your stuff, you decide to stop to look at them, for emphasis."

    show cecil

    mc "...Nothing? No extracurriculars or anything?"

    hide cecil
    show pat

    p "...No, not really. "

    p "I mean, I just moved in... so there’s no clubs that I’m already a part of. And it’s just my last semester in high school anyway, so there’s no point in joining any clubs. Applications have already been submitted and everything."

    hide pat
    show cecil
    
    mc "I guess that makes sense… Still, isn’t that a little lonely?"

    hide cecil
    show pat

    p "A little bit, yeah. But that’s kind of par for the course moving anywhere, you know?"

    hide pat

    "They don’t seem super interested in talking more about it, and you guess that you should focus on the assignment for the time being."

    "The two of you make quick work of the first step in the project, and you hit submit with a satisfied sigh."

    "As you lean back in your chair you notice that Pat has a thoughtful look in their eyes."

    show pat

    p "Hey, [MC_name]... does Willow Creek have a club for members of the LGBTQA+ community? Like, y’know, a GSA?"

    hide pat
    show cecil

    mc "GSA?"

    hide cecil
    show pat

    p "That’s what my old school called it, at least. I think they were thinking of coming up with a new name... but I left before I could hear the results of that."

    hide pat

    "You think about the school's clubs. While it was true that many members of that community were friends and met together, you don’t think that there was an official club for it."

    show cecil
    
    mc "I don’t think so. I can ask around, though!"

    hide cecil
    show pat

    p "No... it’s ok. I was just thinking about what you said about extracurriculars and clubs. I don’t know, my old school had one and I never joined, so I guess it wouldn’t matter either way..."

    hide pat
    show cecil
    
    mc "It’s not too late to start one here! I think the process for starting a club is pretty simple. Let me search it up..."

    hide cecil

    "Pat watches as you click through the links with interest."

    "You find the form after a little bit of snooping around."

    show cecil

    mc "Here! We can probably find a teaching advisor next week if we ask around."

    hide cecil

    "There’s an awkward silence as you realize you might have gotten ahead of yourself."

    show cecil

    mc "If you want to, that is."

    hide cecil
    show pat

    p "I don’t know... I feel like it would be weird if I decided to lead a GSA here."

    hide pat
    show cecil

    mc "Weird? How so?"

    hide cecil
    show pat

    p "The whole reason I didn’t join GSA at my old school was that I felt like I didn’t really belong. So here, where I don’t know anyone..."

    hide pat

    "You frown. You don’t know all the details, but still, that wasn't a particuarly promising choice of words."

    show cecil

    mc "Is there any reason that you think that? Everyone should be welcomed at this club, whether they identify on the spectrum or just to support it."

    hide cecil
    show pat

    p "I know that, but..."

    hide pat

    "They stop, then clarifiy."

    show pat

    p "I identify as asexual. "

    hide pat

    "You nod- so do you, but you recognize that you have been lucky in your experience on the spectrum in your relatively small circle of friends. "

    show pat

    p "I didn’t really hide it, but I wasn’t really out in my old school. Everyone else in the club was... out, that is, so I didn’t fit in."
    
    p "All of them had boyfriends or girlfriends or were talking about things like hormones and surgeries... and I didn’t really have anything to say."

    hide pat
    show cecil

    mc "Oh."

    hide cecil

    "You had similar concerns when you first came out, but thankfully, none of those situations really happened."

    show pat

    p "They were all super welcoming but... none of their activities really applied to me every time I showed up so I just..."
    
    p "Stopped going."

    hide pat
    show cecil

    mc "I’m sorry to hear that. We definitely don’t need to make a club if you’re not comfortable. "

    hide cecil
    show pat

    p "It’s not just the club. I’m worried that it’ll keep happening in college too. I want to join these communities but I end up having nothing to say, or worse, I feel like I don’t belong, and..."

    p "Sorry, that’s a lot."

    hide pat
    show cecil

    mc "No, don’t be! These are big concerns, and I'm sure moving doesn't help with all the stress."
    
    mc "Even if you don’t want to form a club here, I could help you research how universities handle these communities."

    mc "That way, you won’t have to feel this way after we graduate."

    hide cecil
    show pat

    p "...Thanks, [MC_name]."

    hide pat

    "They smile, and you feel like while you might not have resolved the issue, you’ve taken the first step in making another friend. The rest of your study session goes by peacefully, and the two of you part to go home after a productive day."

    jump end_demo

label end_demo:
    scene bg_black with fade

    "Thank you for playing the Philautia Demo! This marks the end of week one. In a full game, there would be multiple weeks with a similar setup."

    "We hope you enjoyed!"

    return