label chapter_one:

    scene bg class_board at bg_fit with dissolve
    show teachertalking at center_char
    teacher "Everyone... look over here."
    teacher "Yes, yes. You guys don't plan on listening to me either way."
    hide teachertalking
    show sarasmilequiet at center_char
    npc "That's Sara Lee, right?"
    npc "She's so pretty"
    thought "Please stop staring at me like that..."
    thought "I just met you for the first time today..."
    thought "Let me just look somewhere else."
    hide sarasmilequiet
    show wooquiet at center_char
    thought "We're only in the first year of High School, how can he be so handome."
    hide wooquiet 
    show woosmile at center_char
    npc "ACK!!"
    npc "MY HEART!!"
    npc "HE JUST SMILED AT ME!!"
    npc "NO! HE JUST SMILED AT ME!!"
    hide woosmile
    show sooneutralquiet at center_char
    thought "Yeah.. If it was any other day, my reaction would've been like that too."
    thought "But why?!"
    thought "Why doesn't anyone notice their weird hair and eye colors?"
    thought "Come on..."
    thought "Huh? A message?"

    show screen phone_notification("Sara Lee ♡", "Soo-ah, are you sick? You've been acting weird since the morning.") at phone_slide_in
    pause 2.5
    hide screen phone_notification at phone_slide_out
    pause 0.3

    thought "Huh?"

    return
