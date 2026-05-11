label chapter_2:

    scene bg class at bg_fit with dissolve

    call screen chapter_card("Chapter 2", "I Was Going To Be Invisible")

    show sooneutralquiet at center_char with dissolve

    thought "Three days in. My plan was going well. Nobody paid special attention to me."
    thought "I was successfully a background character."
    thought "And then."

    hide sooneutralquiet
    show jihoquiet at center_char with dissolve

    "The classroom went quiet. Not the polite kind."

    hide jihoquiet
    show jihotalking at center_char

    jiho "Who's Sara Lee?"

    hide jihotalking
    show jihoquiet at center_char

    thought "Oh no."

    hide jihoquiet
    show saraneutraltalk at center_char with dissolve

    sara "That's me."

    hide saraneutraltalk
    show jihotalking at center_char

    jiho "You scored first place. Above me."

    hide jihotalking
    show saraneutraltalk at center_char

    sara "...Yes."

    hide saraneutraltalk
    show jihotalking at center_char

    jiho "Don't get comfortable. I won't go easy on you next time."

    hide jihotalking
    show saraneutraltalk at center_char

    sara "Were you actually going easy on me?"

    hide saraneutraltalk
    show jihotalking at center_char

    jiho "Just wait and see."

    hide jihotalking

    npc1 "Did she just talk back to Ji-ho?! He's going to destroy her on the next exam."

    thought "He just walks up to people and declares academic war. Who does that."

    show woosmiletalk at center_char with dissolve

    woo "You're the first person to ever talk back to Ji-ho like that! I'm Woo Ju-in. Let's be friends!"

    hide woosmiletalk
    show sarasmiletalk at center_char with dissolve

    sara "Ji-ho?"

    hide sarasmiletalk
    show woosmiletalk at center_char

    woo "Eun Ji-ho. Don't worry about him — he's like that with everyone he finds interesting."

    hide woosmiletalk
    show sarasmiletalk at center_char

    sara "...Interesting."

    hide sarasmiletalk

    thought "He challenged her because he found her interesting."
    thought "Such a male lead thing to do."
    thought "I need to be the least interesting person in this building."

    scene black with dissolve

    npc1 "Bye—"
    npc2 "See you tomorrow—"

    thought "I zoned out. By the time I noticed, school was over."

    scene bg school_hallway at bg_fit with dissolve

    show saraneutraltalk at center_char with dissolve

    sara "Soo-ah. Let's walk home."

    hide saraneutraltalk
    show saraquiet at center_char

    soo "Oh. Yeah."

    hide saraquiet
    show saraneutraltalk at center_char

    sara "Since this morning you've been acting strange."
    sara "I kept looking at you in class. You kept looking away."

    hide saraneutraltalk
    show saraquiet at center_char

    thought "What do I say. I literally don't know who she is."

    soo "I'm not avoiding you. First day jitters."

    hide saraquiet
    show saraneutraltalk at center_char

    sara "You sure? You can tell me if something's wrong."
    sara "I'm not going anywhere."

    hide saraneutraltalk
    show saraquiet at center_char

    thought "She's not asking about the old falling out."
    thought "They already made up. She thinks everything is fine."
    thought "She's just asking about today."
    thought "And I have no idea how to answer that."

    menu:
        "\"I'm okay. Just tired.\"":
            $ affection_sara += 2
            soo "I'm okay. Just tired."
            hide saraquiet
            show sarasmiletalk at center_char
            sara "Okay. But if something's bothering you, tell me."
            sara "That's what I'm here for."
            hide sarasmiletalk
            show sarasmilequiet at center_char

        "\"Yeah. I'm sure.\"":
            $ affection_sara += 1
            soo "Yeah. I'm sure."
            hide saraquiet
            show saraquiet at center_char
            sara "..."
            sara "Okay."

    thought "She said it simply."
    thought "Like it was just a fact."
    thought "I'm not going anywhere."
    thought "I felt something twist in my chest."

    $ add_observation("Sara", "She noticed I was off today and asked if I was okay. Said she's not going anywhere. She meant it.")

    hide sarasmilequiet

    scene bg room at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve

    soo "Okay. Let's think about this seriously."

    thought "This world is real enough. The people in it are real. Sara is real."
    thought "And she thinks we're best friends. We were. We made up."
    thought "She doesn't know I'm not the same Soo-ah."

    hide sooneutralquiet
    show sooneutraltalk at center_char

    soo "Option one: find a way back. Option two: figure this out and survive it."
    soo "I've already done option three — panic."
    soo "Let's try option two."

    hide sooneutraltalk

    scene black with dissolve

    thought "I fell asleep thinking about it. Woke up still here. Of course."

    jump chapter_3
