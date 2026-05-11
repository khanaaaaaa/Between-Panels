label chapter_2:

    scene bg class at bg_fit with dissolve

    show screen chapter_card("Chapter 2", "I Was Going To Be Invisible")

    show sooneutralquiet at center_char with dissolve

    thought "Three days in. My plan was going well. Nobody paid special attention to me."
    thought "I was successfully a background character."
    thought "And then."

    hide sooneutralquiet
    show jihoquiet at center_char with dissolve

    "The classroom went quiet. Not the polite kind."

    jiho "Who's Sara Lee?"

    thought "Oh no."

    hide jihoquiet
    show saraneutraltalk at center_char with dissolve

    sara "That's me."

    hide saraneutraltalk
    show jihoquiet at center_char

    jiho "You scored first place. Above me."

    hide jihoquiet
    show saraneutraltalk at center_char

    sara "...Yes."

    hide saraneutraltalk
    show jihoquiet at center_char

    jiho "Don't get comfortable. I won't go easy on you next time."

    hide jihoquiet
    show saradisturbed at center_char

    sara "Were you actually going easy on me?"

    hide saradisturbed
    show jihotalking at center_char

    jiho "Just wait and see."

    hide jihotalking

    npc1 "Did she just talk back to Ji-ho?! He's going to destroy her on the next exam."

    thought "He just walks up to people and declares academic war. Who does that."

    show woosmile at center_char with dissolve

    woo "You're the first person to ever talk back to Ji-ho like that! I'm Woo Ju-in. Let's be friends!"

    hide woosmile
    show sarasmiletalk at center_char with dissolve

    sara "Ji-ho?"

    hide sarasmiletalk
    show woosmile at center_char

    woo "Eun Ji-ho. Don't worry about him — he's like that with everyone he finds interesting."

    hide woosmile
    show sarasmiletalk at center_char

    sara "...Interesting."

    hide sarasmiletalk

    thought "He challenged her because he found her interesting. Such a male lead thing to do."
    thought "I need to be the least interesting person in this building."

    scene black with dissolve

    npc1 "Bye—"
    npc2 "See you tomorrow—"

    thought "I zoned out. By the time I noticed, school was over."

    scene bg school_hallway at bg_fit with dissolve

    show saraneutraltalk at center_char with dissolve

    sara "Soo-ah. Let's walk home."
    soo "Oh. Yeah."
    sara "Since this morning you've been acting like I'm a stranger."
    soo "..."
    sara "I kept looking at you in class. You kept looking away."

    thought "What do I say. I literally don't know who she is."

    soo "I'm not avoiding you. First day jitters."

    hide saraneutraltalk
    show saradisturbed at center_char

    sara "Is this because of what happened before?"
    soo "What...?"

    thought "SOMETHING HAPPENED. What did I do."

    sara "I thought when you said hi this morning it meant things were okay."
    sara "Was I wrong?"

    menu:
        "\"No. You weren't wrong. I'm sorry.\"":
            $ affection_sara += 2
            soo "No, you weren't wrong."
            soo "I wasn't mad at you."
            soo "I've just been in my head."
            hide saradisturbed
            show sarasmilequiet at center_char
            sara "Really?"
            soo "Really. Sorry if it seemed like I was pushing you away."
            sara "That's a relief."

        "Stay quiet and look away.":
            $ affection_sara += 1
            soo "..."
            hide saradisturbed
            show saraquiet at center_char
            sara "...Okay."

    show sarasmilequiet at center_char

    sara "You're my best friend, Soo-ah. I don't have another one."

    thought "She said it so simply."
    thought "I felt something twist in my chest."

    $ add_observation("Sara", "She said I'm her only best friend. She's been patient this whole time.")

    hide sarasmilequiet

    scene bg room at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve

    soo "Okay. Let's think about this seriously."

    thought "This world is real enough. The people in it are real. Sara is real."
    thought "I'm living someone else's life and I've already made a mess of it."

    hide sooneutralquiet
    show sooneutraltalk at center_char

    soo "Option one: find a way back. Option two: figure this out and survive it."
    soo "I've already done option three — panic."
    soo "Let's try option two."

    hide sooneutraltalk

    scene black with dissolve

    thought "I fell asleep thinking about it. Woke up still here. Of course."

    jump chapter_3
