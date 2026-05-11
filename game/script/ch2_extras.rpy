label chapter_2_extras:

    scene bg class at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve

    thought "Eunhyeong sat two seats ahead of me."
    thought "He never seemed to be paying attention."
    thought "But I kept catching him looking at the board like he was somewhere else entirely."

    hide sooneutralquiet
    show eunhyeongtalk at center_char with dissolve

    eunhyeong "Hey."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "...Me?"
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "You were watching me just now."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "I watch everyone."
    eunhyeong "..."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "That's a strange thing to admit."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "Is it?"
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "Most people pretend they weren't."
    hide eunhyeongtalk
    show eunhyeongsmile at center_char
    soo "That seems exhausting."
    eunhyeong "..."

    thought "He turned back to the board." 
    thought "But he was almost smiling."

    $ add_observation("Eunhyeong", "He noticed me watching. Said most people pretend they weren't.")

    hide eunhyeong

    scene bg school_hallway at bg_fit with dissolve

    show eunhyeongquiet at center_char with dissolve

    thought "Eunhyeong was the easiest person in the building to be around."
    thought "Which made me suspicious of him immediately."
    thought "Nobody is that comfortable with everyone. Nobody."

    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "You look like you're doing math."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "I'm always doing math."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "What kind?"
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "Figuring out what people actually mean versus what they say."
    eunhyeong "..."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "And what do I actually mean?"
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "I haven't figured that out yet."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "Let me know when you do."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char

    menu:
        "\"What if I already have?\"":
            $ affection_eunhyeong += 2
            soo "What if I already have?"
            eunhyeong "..."
            hide eunhyeongquiet
            show eunhyeongtalk at center_char
            eunhyeong "Then I'd say you're more perceptive than most."
            hide eunhyeongtalk
            show eunhyeongquiet at center_char
            thought "He said it carefully. Like he was deciding how much to give away."

        "\"I'll let you know.\"":
            $ affection_eunhyeong += 1
            soo "I'll let you know."
            eunhyeong "..."
            hide eunhyeongquiet
            show eunhyeongtalk at center_char
            eunhyeong "I'll be waiting."
            hide eunhyeongtalk
            show eunhyeongquiet at center_char
            thought "He smiled. Easy and uncomplicated."
            thought "I still didn't fully trust it."

    thought "He said it lightly." 
    thought "But there was something underneath it."
    thought "Like he was genuinely curious what I'd find."

    $ add_observation("Eunhyeong", "He asked what he actually means. Said let me know when you figure it out.")

    hide eunhyeongquiet

    jump chapter_3
