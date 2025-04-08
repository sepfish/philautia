init:
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

    # White flash
    $ flash = Fade(.25, 0, .75, color="#ffffff")

    # Black fade
    $ fade = Fade(.25, 0, .75, color="#000000")


# The game starts here.

label start:
    # Week 1 Introduction Scene

    "January 20XX"
    "For the seniors of Willow Creek High, January marked the start of their last semester at the now familiar school. Some were already planning their futures, early admissions and decisions making the remaining months stress-free."
    "…Others, less so. You are one of them, opening your locker to pull out your school supplies for the first day back since winter break. Neatly written on the cover is your name…"
    $ MC_name = renpy.input("What is your name?")
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

    "You can’t believe the break went by so fast. The last semester had been hectic, applying to colleges taking up most of your time. Now, you can try to relax and enjoy the last high school semester of your life."

    i "[MC_name!u]!!"

    with flash

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

    mc "See you!"

    "She leaves as quickly as she came. You remember that her first class is all the way across the building, and wish her luck silently. You’re sure she’ll make it before the first bell… probably."

    with fade

    "Class is normal as always. Senior year, the teachers always start acting more relaxed, even allowing for some students to skip class. It’ll be the time of tours and admissions soon, so you kind of get it."

    "You’re pretty sure the person behind you is actually just snoring, though."

    mr "… will be working in pairs. This project is worth 10\% of your final grade, and we’ll be working on it alongside our classwork the entire semester."

    "The entire class perks up. You can see friends start to surreptitiously scooch closer together."

    mr "These pairs will be randomly determined. Everybody, stand up."

    "After a bit of shuffling around a small game that you think that Mr. Mahraun just wanted to play, you are left face-to-face with a stranger."

    "It’s not strange for you to not know everybody in your grade, but you’re pretty sure you’ve seen most of the people around town. It’s not a big one, anyway- even if you don’t know their name. But this person is a bona-fide stranger."

    idk "Um..."

    mc "Um, hello! My name is [MC_name], [MC_pronouns]. It’s nice to meet you!"

    p "Pat… Pat Cordova, they/them."

    mc "..."

    p "..."

    "You come to the conclusion that you definitely haven’t seen them before, either in town or school. Maybe seeing the confusion on your face, they sigh and offer an explanation."

    p "I just moved here a few days ago."

    menu:
        "For the second half of your senior year? That must be tough…":
            p "...I guess."
        "Welcome to Willow Creek!":
            p "Thanks..."
        "Let me know if you need any help.":
            p "Thanks, I will."
    
    "Conversation dies down as all other pairs finish introducing themselves to each other- or so they’d claim. You’re pretty sure that they’re just catching up from break."

    "You exchange contact information with Pat."

    p "We should message about the project later…"

    mc "Yeah, sure! The proposal’s due in a week, so we can message after school."

    "The bell rings."

    p "We really spent a lot of time in that activity… I’ll see you, then."

    mc "See you!"

    with fade

    "You’re lucky that your lunch period is during a normal lunch time. The cafeteria is packed, and you have to weave around students in order to find a seat to quickly eat."

    "It’s too bad that Ivy doesn’t have the same lunch as you, but it’s not like you don’t know anyone else. You approach one of those such friends."

    mc "Hey, Karina!"

    k "[MC_name], fancy seeing you here!"

    "You smile, finding your place across the table. It’s a joke between you two, after you had slipped up upon seeing her in your advising group- the advising group that you shared with her."

    k "Had a lively break?"

    mc "You don’t even know…"

    k "You’re telling me. I need to figure out how to tell Mrs. Hughes that I won’t be around for an entire week."

    menu:
        "Ouch. Good luck.":
            k "Thanks. I’ll figure it out, hopefully… "
        "A whole week? What are you doing?":
            k "College tours, what else? My parents want me to know what the campuses look like before I make a decision."
        "(Give an empathetic sigh.)":
            k "Don’t give me that look. You know me, I’ll be able to figure out… somehow."

    "She laughs it off."

    k "Let’s talk about something else, though. That’s a problem for the future!"

    mc "Yeah, right."

    "She’s probably already drafted up an email in her head, knowing her. You wonder if the word procrastination is even in her dictionary."

    "The rest of lunch goes by with idle chatter. It’s nice, and you two catch each other up on what you had been doing over break."

    "If you had told your freshman self that you and Karina would have been friends in senior year, you probably would have laughed. Though not exactly {i}popular{/i}, the two of you had been in different circles all throughout middle school, and you had expected that to stay like that."

    k "I’ve gotta run! Can’t be late to class on the first day of school."

    mc "Go, go! Text you later!"

    k "Bye!"

    with fade

    idk "[MC_name]? Is that you?"

    "A voice calls out to you as you are packing to leave. Glancing over your shoulder, you look around for the source."

    idk "[MC_name]!"

    mc "...?"

    "An unfamiliar student walks over to you."

    idk " It’s me. We used to play together all the time as kids!"

    "A vague memory comes to you, but it doesn’t match with the person you see before you. You used to play with a neighbor’s kid all the way back in elementary school, but…"

    y "It’s me, Yubin! Yubin Kim? Does that name ring a bell?"

    mc "The neighbor’s kid?"

    y "Yes! It’s been a long time!"

    "That’s an understatement. It’s been, what, how many years?"

    mc "Woah, did you just move back? When did you get here?"

    y "I just moved back over winter break."

    "An awkward silence follows. While you two were incredibly close as children, it’s been years since you’ve talked. What would you even talk about?"

    menu:
        "So… how have you been?":
            y "I’ve been well! … I mean, that’s a bit of a broad summary of everything that happened, but, you know."
        "Let’s catch up sometime!":
            y "We should! Are you free this weekend?"
        "Why did you move back?":
            y "Well, the same reason I moved away. Dad’s job and all."
            mc "It’s great to see you again! Do you need any help settling in, or…"
            y "Nah, all the teachers have been super helpful. I’ll let you know if I need anything, though."
    
    y "That reminds me: what’s your number? The last time we saw each other, neither of us had phones, haha!"

    "The two of you exchange contact information. It feels a little strange, like you’ve jumped from childhood to near-adulthood in just minutes."

    "In a way, you have."

    mc "Are you back in the same house again?"

    y "That would have been a huge coincidence! But no, we’re a couple streets over. You can still come visit if you want, though! Just like old times!"

    mc "I’ll look forward to it!"

    "The interaction still ends with some awkwardness, but you wave bye to Yubin as you head down opposite ends of the hallway."

    return