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

    return