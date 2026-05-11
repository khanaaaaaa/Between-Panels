label chapter_4_extras:

    scene bg class at bg_fit with dissolve

    show eunhyeongquiet at center_char with dissolve

    thought "Something I noticed about Eunhyeong."
    thought "He remembers everything everyone tells him."
    thought "Not in a creepy way. In a way that makes you feel like what you said mattered."

    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "You mentioned last week you hadn't slept well."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "...You remembered that?"
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "You said it in passing. You didn't think I was listening."
    eunhyeong "Are you sleeping better?"
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "A little."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "Good."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char

    thought "He said it simply and moved on."
    thought "Like checking in was just something he did."
    thought "Like I was someone worth checking in on."
    thought "I didn't know what to do with that."

    $ add_observation("Eunhyeong", "He remembered something I said in passing a week ago. Said he's always listening. Moved on like it was nothing.")

    hide eunhyeongquiet

    scene bg school_hallway at bg_fit with dissolve

    show woosmile at center_char with dissolve

    thought "The four of them were in the same room at the same time."
    thought "Every time it happened the energy was completely different from when they were alone."

    hide woosmile
    show woosmiletalk
    woo "Ji-ho. You're doing it wrong."

    hide woosmiletalk
    show jihotalking at center_char

    jiho "I'm not doing anything."

    hide jihotalking
    show woosmiletalk at center_char

    woo "Exactly. That's the wrong thing to do."

    hide woosmiletalk
    show minhotalking at center_char with dissolve

    minho "He has a point."

    hide minhotalking
    show jihotalking at center_char

    jiho "You too?"

    hide jihotalking
    show minhotalking at center_char

    minho "I'm just observing."

    hide minhotalking
    show woosmiletalk at center_char

    woo "Min-ho agrees with me. This is historic."

    hide woosmiletalk
    show minhotalking at center_char

    minho "I said you had a point. Not that you were right."

    hide minhotalking
    show woosmiletalk at center_char

    woo "What's the difference?"

    hide woosmiletalk
    show minhoquiet at center_char

    minho "..."
    hide minhoquiet
    show minhotalking at center_char
    minho "Significant."

    hide minhotalking
    show eunhyeongtalk at center_char with dissolve

    eunhyeong "Are you all going to do this the entire lunch break."

    hide eunhyeongtalk
    show woosmiletalk at center_char

    woo "Yes."

    hide woosmiletalk
    show jihotalking at center_char

    jiho "No."

    hide jihotalking
    show minhotalking at center_char

    minho "Probably."

    thought "Eunhyeong sat down anyway. Which meant yes."

    hide minhotalking
    show sooneutraltalk at center_char with dissolve

    soo "You're all insane."

    hide sooneutraltalk
    show woosmiletalk at center_char

    woo "She gets it."

    hide woosmiletalk
    show jihotalking at center_char

    jiho "She doesn't get it."

    hide jihotalking
    show minhotalking at center_char

    minho "She's observing."

    hide minhotalking
    show eunhyeongquiet at center_char

    eunhyeong "..."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "She's right."

    menu:
        "\"Thank you, Eunhyeong.\"":
            $ affection_eunhyeong += 2
            hide eunhyeongtalk
            show eunheongquiet at center_char
            soo "Thank you, Eunhyeong."
            hide eunhyeongquiet
            show woosmiletalk at center_char
            woo "She's playing favorites!"
            hide woosmiletalk
            show jihotalking at center_char
            jiho "She's not wrong."
            hide jihotalking
            show jihoquiet at center_char
            thought "Ji-ho said that. Out loud. To other people."
            thought "I need a moment."

        "Laugh and say nothing.":
            $ affection_eunhyeong += 1
            hide eunhyeongtalk
            show eunhyeongquiet at center_char
            thought "I just laughed."
            thought "Eunhyeong looked at me."
            thought "Something warm in it. Brief. But there."

    hide eunhyeongquiet

    thought "The conversation ended."
    thought "I laughed. Actually laughed. Out loud."
    thought "That was new."

    jump chapter_5
