label chapter_4_extras:

    scene bg class at bg_fit with dissolve

    show eunhyeong at center_char with dissolve

    thought "Something I noticed about Eunhyeong."
    thought "He remembers everything everyone tells him."
    thought "Not in a creepy way. In a way that makes you feel like what you said mattered."

    eunhyeong "You mentioned last week you hadn't slept well."
    soo "...You remembered that?"
    eunhyeong "You said it in passing. You didn't think I was listening."
    eunhyeong "Are you sleeping better?"
    soo "A little."
    eunhyeong "Good."

    thought "He said it simply and moved on."
    thought "Like checking in was just something he did."
    thought "Like I was someone worth checking in on."
    thought "I didn't know what to do with that."

    $ add_observation("Eunhyeong", "He remembered something I said in passing a week ago. Said he's always listening. Moved on like it was nothing.")

    hide eunhyeong

    scene bg school_hallway at bg_fit with dissolve

    show woosmile at center_char with dissolve

    thought "The four of them were in the same room at the same time."
    thought "Every time it happened the energy was completely different from when they were alone."

    woo "Ji-ho. You're doing it wrong."

    hide woosmile
    show jihoquiet at center_char

    jiho "I'm not doing anything."

    hide jihoquiet
    show woosmile at center_char

    woo "Exactly. That's the wrong thing to do."

    hide woosmile
    show minhoquiet at center_char with dissolve

    minho "He has a point."

    hide minhoquiet
    show jihoquiet at center_char

    jiho "You too?"

    hide jihoquiet
    show minhoquiet at center_char

    minho "I'm just observing."

    hide minhoquiet
    show woosmile at center_char

    woo "Min-ho agrees with me. This is historic."

    thought "Min-ho did not look like he agreed."
    thought "He looked like he regretted speaking."

    hide woosmile
    show minhoquiet at center_char

    minho "I said you had a point. Not that you were right."

    hide minhoquiet
    show woosmile at center_char

    woo "What's the difference?"

    hide woosmile
    show minhoquiet at center_char

    minho "..."
    minho "Significant."

    thought "Ji-ho almost smiled. I caught it. Number seven."

    hide minhoquiet
    show eunhyeong at center_char with dissolve

    chunyeon "Are you all going to do this the entire lunch break."

    hide eunhyeong
    show woosmile at center_char

    woo "Yes."

    hide woosmile
    show jihoquiet at center_char

    jiho "No."

    hide jihoquiet
    show minhoquiet at center_char

    minho "Probably."

    thought "Chun-young sat down anyway. Which meant yes."

    hide minhoquiet
    show sooneutralquiet at center_char with dissolve

    soo "You're all insane."

    hide sooneutralquiet
    show woosmile at center_char

    woo "She gets it."

    hide woosmile
    show jihoquiet at center_char

    jiho "She doesn't get it."

    hide jihoquiet
    show minhoquiet at center_char

    minho "She's observing."

    hide minhoquiet
    show eunhyeong at center_char

    chunyeon "..."
    chunyeon "She's right."

    menu:
        "\"Thank you, Chun-young.\"":
            $ affection_chunyeon += 2
            soo "Thank you, Chun-young."
            hide eunhyeong
            show woosmile at center_char
            woo "She's playing favorites!"
            hide woosmile
            show jihoquiet at center_char
            jiho "She's not wrong."
            hide jihoquiet
            thought "Ji-ho said that. Out loud. To other people."
            thought "I need a moment."

        "Laugh and say nothing.":
            $ affection_chunyeon += 1
            hide eunhyeong
            thought "I just laughed."
            thought "Chun-young looked at me."
            thought "Something warm in it. Brief. But there."

    hide eunhyeong
    hide jihoquiet
    hide woosmile
    hide minhoquiet

    thought "The conversation ended."
    thought "I laughed. Actually laughed. Out loud."
    thought "That was new."

    jump chapter_5
