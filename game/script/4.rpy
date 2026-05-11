label chapter_3:

    scene bg room at bg_fit with dissolve

    call screen chapter_card("Chapter 3", "New Plan")

    show sooneutralquiet at center_char with dissolve

    thought "Second week. Still here. Still waking up in a room that looks drawn by hand."

    mom "Soo-ah! Breakfast!"

    hide sooneutralquiet
    show sooneutraltalk at center_char
    soo "Coming!"

    hide sooneutraltalk

    scene bg class at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve

    thought "The Panel Kings — Ji-ho, Ju-in, Min-ho, Eunhyeong."
    thought "Sara Lee — the protagonist. Beautiful, brilliant, kind."
    thought "And me — Kang Soo-ah. Sara's best friend who started avoiding her for some reason."
    thought "I don't know why the original Soo-ah did that. But I'm the one living with it."


    npc1 "Ji-ho and Sara had another exchange in the library."
    npc2 "Already?! It's only been two weeks!"
    npc1 "He keeps finding reasons to talk to her."


    thought "The rival-to-lovers pipeline is already activating. Right on schedule."

    hide sooneutralquiet
    show jihoquiet at center_char with dissolve

    thought "He walked past my desk without looking at me. Good. That's what I want."
    thought "...He glanced back. At me, not at Sara."
    thought "That's nothing. I'm not writing that down."

    $ add_observation("Ji-ho", "He glanced back at me in the hallway. Probably nothing.")

    hide jihoquiet

    scene bg school_hallway at bg_fit with dissolve

    show woosmiletalk at center_char with dissolve

    woo "Soo-ah! You always look like you're solving something."
    hide woosmiletalk
    show woosmile at center_char
    soo "I'm just walking."
    hide woosmile
    show woosmiletalk at center_char
    woo "You walk like you're solving something."
    woo "Are you and Sara okay?" 
    woo "She seemed quiet this morning."
    hide woosmiletalk
    show woosmile at center_char
    soo "We talked it out."
    hide woosmile
    show woosmiletalk at center_char
    woo "Good. She was worried about you."
    hide woosmiletalk
    show woosmile at center_char
    soo "...She told you that?"
    hide woosmile
    show woosmiletalk at center_char
    woo "She didn't have to." 
    woo "I just notice things."
    hide woosmiletalk
    show woosmile

    $ add_observation("Woo Ju-in", "He knew Sara was worried before she said anything. He just notices.")

    hide woosmile

    scene bg room at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve

    thought "That night I made a decision." 
    thought "Wrote it down so I wouldn't talk myself out of it."

    hide sooneutralquiet
    show sooneutraltalk at center_char

    soo "New plan."
    soo "I can't go back, not yet. Maybe not ever."
    soo "But the people here are real. Sara is real. And I'm living her life."
    soo "I can keep running from it. Or I can actually live it."

    hide sooneutraltalk
    show sooneutralquiet at center_char

    thought "That's a lot. Let's start with Sara."

    hide sooneutralquiet

    scene black with dissolve

    jump chapter_4
