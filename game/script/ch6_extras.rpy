label chapter_6_extras:

    scene bg school_hallway at bg_fit with dissolve

    show woosmile at right_char with dissolve
    show sooneutralquiet at center_char with dissolve

    thought "Ju-in asked me something I wasn't ready for."

    woo "Hey. Can I ask you something weird?"
    soo "You always ask that and then ask anyway."
    woo "Do you ever feel like you don't fully belong here?"
    soo "..."
    woo "Not in a sad way. Just like you're slightly outside of everything."
    woo "Watching."
    soo "..."

    thought "I almost said it."
    thought "I almost said yes, because I'm not actually from here."
    thought "I almost said I woke up one day and everything was different."
    thought "I almost said all of it."

    soo "Sometimes."
    woo "Yeah. Me too."

    thought "He didn't push. He just nodded like that was enough."
    thought "And somehow it was."

    hide woosmile
    hide sooneutralquiet

    scene bg school at bg_fit with dissolve

    show minhoquiet at right_char with dissolve
    show sooneutralquiet at center_char with dissolve

    thought "Min-ho found me on the steps. Which was unusual."
    thought "He didn't usually find people."

    minho "You're different lately."
    soo "Different how?"
    minho "More present."
    minho "You used to watch everything from a distance."
    minho "Now you're actually in it."
    soo "Is that good?"
    minho "..."
    minho "Yes. It suits you better."

    thought "He went back inside. That was it. Four sentences."
    thought "I stood there for a full minute after."

    $ add_observation("Kang Min-ho", "He said I'm more present now. That it suits me better.")

    hide minhoquiet
    hide sooneutralquiet

    scene bg school_gate at bg_fit with dissolve

    show jihoquiet at right_char with dissolve
    show sooneutralquiet at center_char with dissolve

    thought "I found the first drawing."
    thought "Not in his sketchbook. Folded up, slipped under the cover of a library book I'd borrowed."
    thought "The courtyard. The cherry blossoms."
    thought "A girl with her back turned. My uniform."
    thought "He'd drawn me before he knew my name."

    soo "Ji-ho."
    jiho "..."
    soo "The library book."
    jiho "..."
    jiho "I didn't know whose it was."
    soo "You drew me before you knew who I was."
    jiho "..."
    jiho "You were in the frame."
    soo "You keep saying that."
    jiho "..."
    jiho "Because it keeps being true."

    menu:
        "\"Then draw me properly. Ask first.\"":
            $ affection_jiho += 3
            soo "Then draw me properly next time. Ask first."
            jiho "..."
            jiho "Can I draw you?"
            soo "..."
            soo "Yes."
            thought "He opened the sketchbook."
            thought "I stood very still."
            thought "I don't know how long it took. I didn't mind."

        "\"Keep the drawing.\"":
            $ affection_jiho += 2
            soo "Keep it. The one from the book."
            jiho "..."
            jiho "I have copies."
            soo "Of course you do."
            jiho "..."
            thought "He almost smiled. Number seven."

    thought "I kept the drawing. I didn't tell him that."
    thought "But I think he knew."

    $ add_observation("Ji-ho", "He drew me before he knew my name. Said I was in the frame. I kept the drawing.")

    hide jihoquiet
    hide sooneutralquiet

    jump chapter_7
