label chapter_3:

    scene bg room at bg_fit with dissolve

    show screen chapter_card("Chapter 3", "The Part Where I Make A Decision")
    pause 2.5

    show sooneutralquiet at center_char with dissolve

    thought "Second week."
    thought "Still here."
    thought "Still in this world."
    thought "Still waking up in a room that looks like it was drawn by hand."

    mom "Soo-ah! Breakfast!"

    soo "Coming!"

    hide sooneutralquiet

    scene bg class at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve

    thought "I've been doing research."
    thought "Quietly. In my head."
    thought "Cataloguing everything I know about this world."
    thought "The Panel Kings — Ji-ho, Ju-in, Min-ho, Eunhyeong."
    thought "Sara Lee — the protagonist. Beautiful, brilliant, kind."
    thought "And me — Kang Soo-ah. Sara's best friend. The one who, for some reason, started avoiding her."
    thought "I don't know why the original Soo-ah did that."
    thought "But I'm the one living with the consequences."

    show npcquiet at left_char with dissolve

    npc1 "Did you hear? Ji-ho and Sara had another exchange in the library."
    npc2 "Already?! It's only been two weeks!"
    npc1 "He keeps finding reasons to talk to her."
    npc2 "He says it's about the exam rankings."
    npc1 "Sure it is."

    hide npcquiet

    thought "Of course."
    thought "The rival-to-lovers pipeline is already activating."
    thought "Right on schedule."
    thought "This is a very standard chapter one."

    show jihoquiet at right_char with dissolve

    thought "He walked past my desk without looking at me."
    thought "Which is fine."
    thought "That's what I want."
    thought "Invisible. Background. Safe."

    hide jihoquiet

    thought "..."
    thought "He glanced back."
    thought "Just for a second."
    thought "At me, not at Sara."
    thought "That's probably nothing."
    thought "That's definitely nothing."
    thought "I'm not writing that down."

    $ add_observation("Ji-ho", "He glanced back at me in the hallway. Probably nothing. Definitely nothing.")

    scene bg school_hallway at bg_fit with dissolve

    show woosmile at center_char with dissolve
    show sooneutralquiet at left_char with dissolve

    woo "Soo-ah!"
    soo "Oh. Ju-in."
    woo "You always look like you're solving something."
    soo "I'm just walking."
    woo "You walk like you're solving something."

    thought "He's not wrong."

    woo "Hey, are you and Sara okay? She seemed a little quiet this morning."
    soo "We're fine. We talked it out."
    woo "Good. She was worried about you."

    thought "She was worried about me."
    thought "Even after I spent a week avoiding her."
    thought "She was worried about me."

    soo "...She told you that?"
    woo "She didn't have to. I just notice things."

    thought "He said it simply."
    thought "Like noticing people was just something he did."
    thought "I filed that away."

    $ add_observation("Woo Ju-in", "He notices things about people without being asked. He knew Sara was worried before she said anything.")

    hide woosmile

    scene bg room at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve

    thought "That night I made a decision."
    thought "I sat on my bed with a notebook — an actual paper notebook — and I wrote it down."
    thought "So I wouldn't talk myself out of it."

    soo "Okay."
    soo "New plan."

    thought "I can't go back. Not yet. Maybe not ever."
    thought "I don't know how I got here."
    thought "I don't know if there's a way out."
    thought "But I know this:"
    thought "The people in this world are real."
    thought "Sara is real. Ju-in is real. Min-ho is real."
    thought "Even Ji-ho — as annoying as he is — is real."
    thought "And I'm living Soo-ah's life."
    thought "Which means I have her relationships. Her history. Her mistakes."
    thought "I can keep running from all of it."
    thought "Or I can actually live it."

    hide sooneutralquiet
    show sooneutraltalk at center_char

    soo "I'm going to stop trying to be invisible."
    soo "I'm going to fix what the original Soo-ah broke."
    soo "And I'm going to figure out what this world actually is."
    soo "In that order."

    hide sooneutraltalk
    show sooneutralquiet at center_char

    thought "..."
    thought "That's a lot."
    thought "Let's start with Sara."

    hide sooneutralquiet

    scene black with dissolve

    jump chapter_4
