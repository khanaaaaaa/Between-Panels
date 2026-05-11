label chapter_2_extras:

    scene bg class at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve
    show chunyeon at right_char with dissolve

    thought "Chun-young sat two seats ahead of me."
    thought "He never turned around."
    thought "But I kept catching him looking at the board like he was somewhere else entirely."

    chunyeon "Hey."
    soo "...Me?"
    chunyeon "You were watching me just now."
    soo "I watch everyone."
    chunyeon "..."
    chunyeon "That's a strange thing to admit."
    soo "Is it?"
    chunyeon "Most people pretend they weren't."
    soo "That seems exhausting."
    chunyeon "..."

    thought "He turned back to the board. But he was almost smiling."
    thought "I filed that away."

    $ add_observation("Chun-young", "He noticed me watching. Said most people pretend they weren't.")

    hide chunyeon

    scene bg school_hallway at bg_fit with dissolve

    show eunhyeong at right_char with dissolve

    thought "Eunhyeong was the easiest person in the building to be around."
    thought "Which made me suspicious of him immediately."
    thought "Nobody is that comfortable with everyone. Nobody."

    eunhyeong "You look like you're doing math."
    soo "I'm always doing math."
    eunhyeong "What kind?"
    soo "Figuring out what people actually mean versus what they say."
    eunhyeong "..."
    eunhyeong "And what do I actually mean?"
    soo "I haven't figured that out yet."
    eunhyeong "Let me know when you do."

    menu:
        "\"What if I already have?\"":
            $ affection_eunhyeong += 2
            soo "What if I already have?"
            eunhyeong "..."
            eunhyeong "Then I'd say you're more perceptive than most."
            thought "He said it carefully. Like he was deciding how much to give away."

        "\"I'll let you know.\"":
            $ affection_eunhyeong += 1
            soo "I'll let you know."
            eunhyeong "..."
            eunhyeong "I'll be waiting."
            thought "He smiled. Easy and uncomplicated."
            thought "I still didn't fully trust it."

    thought "He said it lightly. But there was something underneath it."
    thought "Like he was genuinely curious what I'd find."

    $ add_observation("Eunhyeong", "He asked what he actually means. Said let me know when you figure it out.")

    hide eunhyeong

    scene bg class at bg_fit with dissolve

    show yeomin at right_char with dissolve
    show sooneutralquiet at center_char with dissolve

    thought "Yeo-min. I'd been avoiding thinking about her."
    thought "Which was ironic given the whole situation."

    yeomin "You've been weird lately."
    soo "I've always been weird."
    yeomin "Weirder than usual."
    yeomin "Is it about Sara?"
    soo "..."
    yeomin "You've been sitting with her again."
    soo "Yeah."
    yeomin "..."
    yeomin "Okay. I'm not going to make it a thing."
    yeomin "I just — I know I wasn't always nice about her."
    yeomin "That wasn't fair."
    soo "..."
    soo "No. It wasn't."
    yeomin "Are we still okay?"
    soo "..."
    soo "Yeah. We're okay."

    thought "She nodded and went back to her phone."
    thought "It wasn't a big conversation. But it was honest."
    thought "That counted for something."

    hide yeomin
    hide sooneutralquiet

    jump chapter_3
