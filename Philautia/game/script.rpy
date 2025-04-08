init:
    # Screen configuration.
    $ config.screen_width = 1920
    $ config.screen_height = 1080
    $ config.window_title = "Oath"

    # Charcter definitions
    define mc = Character("[MC_name]")
    default MC_name = "Cecil"
    define i = Character("Ivy")
    define p = Character("Pat")
    define y = Character("Yubin")
    define k = Character("Karina")

    # White flash
    $ flash = Fade(.25, 0, .75, color="#ffffff")


# The game starts here.

label start:
    "January 20XX"
    "For the seniors of Willow Creek High, January marked the start of their last semester at the now familiar school. Some were already planning their futures, early admissions and decisions making the remaining months stress-free."
    "…Others, less so. You are one of them, opening your locker to pull out your school supplies for the first day back since winter break. Neatly written on the cover is your name…"
    $ MC_name = renpy.input("What is your name?")
    $ MC_name = MC_name.strip()

    if not MC_name:
         $MC_name = "Cecil"

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


    return