label chapter_4:

    scene bg school at bg_fit with dissolve

    show screen chapter_card("Chapter 4", "The People Are Real")

    show sarasmilequiet at center_char with dissolve
    show sooneutralquiet at left_char with dissolve

    thought "Third week. I started paying attention to the people, not the story."

    sara "You didn't bring lunch again."
    soo "I forgot."
    sara "You forget a lot."
    sara "Here."

    thought "She slid her extra lunch across without being asked. Like she'd been doing it for years."

    soo "You don't have to keep doing this."
    sara "I know. I want to."

    thought "I just ate the lunch. It was really good. Of course it was."

    $ add_observation("Sara", "She brings two lunches every day. Gives the extra to whoever forgot. Today that was me.")

    hide sarasmilequiet
    hide sooneutralquiet

    scene bg school_hallway at bg_fit with dissolve

    show minhoquiet at right_char with dissolve
    show sooneutralquiet at center_char with dissolve

    thought "Min-ho. He doesn't invite conversation. Just completely self-contained."
    thought "He was reading by the window. I sat two seats away because the other spots felt wrong."

    minho "You're staring."
    soo "I'm thinking."
    minho "About what?"
    soo "Whether you ever get tired of being quiet."
    minho "No. Quiet is easier than most people think. They just don't try it long enough."

    thought "He went back to his book. Didn't tell me to leave. I stayed."
    thought "Twenty minutes of silence. Most comfortable I'd felt all week."

    $ add_observation("Kang Min-ho", "Quiet is easier than people think. He didn't tell me to leave.")

    hide minhoquiet
    hide sooneutralquiet

    scene bg class at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve
    show woosmile at right_char with dissolve

    woo "Soo-ah, do you believe in fate?"
    soo "No."
    woo "Not even a little?"
    soo "I think things happen and we make meaning out of them after."
    woo "That's kind of sad."
    soo "Or it means we have more control than we think."
    woo "..."
    woo "I never thought about it that way."

    thought "He actually listened. That's rarer than it sounds."

    $ add_observation("Woo Ju-in", "He asked if I believe in fate and actually listened to the answer.")

    hide woosmile
    hide sooneutralquiet

    scene bg school at bg_fit with dissolve

    show jihoquiet at right_char with dissolve
    show sooneutralquiet at center_char with dissolve

    thought "Ji-ho was on the roof after school. I don't know why I went up there."
    thought "I was just walking and the stairs were there. That's my story."

    jiho "You followed me."
    soo "I didn't know you were up here."
    jiho "The door has my name on it."
    soo "It does not."
    jiho "..."
    jiho "It should."

    thought "Did Eun Ji-ho just make a joke. I'm not writing that down."
    thought "I'm absolutely writing that down."

    $ add_observation("Ji-ho", "He made a joke on the roof. Looked surprised that he did it.")

    soo "What are you drawing?"

    hide jihoquiet
    show jihoquiet at right_char

    jiho "The city."
    soo "Can I see?"
    jiho "No. It's not finished."
    soo "I don't mind unfinished things."
    jiho "..."

    thought "He closed the sketchbook. Which means it wasn't the city."
    thought "I think he knew that I knew."

    hide jihoquiet
    hide sooneutralquiet

    scene black with dissolve

    thought "End of the third week. I'd stopped counting the days until I went home."
    thought "I hadn't noticed when that happened. But it had."

    jump chapter_4_extras
