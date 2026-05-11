label chapter_4:

    scene bg school at bg_fit with dissolve

    call screen chapter_card("Chapter 4", "The People Are Real")

    show sarasmilequiet at center_char with dissolve

    thought "Third week. I started paying attention to the people, not the story."

    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "You didn't bring lunch again."
    hide sarasmiletalk
    show sarasmilequiet at center_char
    soo "I forgot."
    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "You forget a lot."
    sara "Here."
    hide sarasmiletalk
    show sarasmilequiet at center_char

    thought "She slid her extra lunch across without being asked." 
    thought "Like she'd been doing it for years."
    thought "She probably was."

    soo "You don't have to keep doing this."
    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "I know." 
    sara "I want to."
    hide sarasmiletalk
    show sarasmilequiet at center_char

    thought "I just ate the lunch. It was really good. Of course it was."

    $ add_observation("Sara", "She brings two lunches every day. Gives the extra to whoever forgot. Today that was me.")

    hide sarasmilequiet

    scene bg school_hallway at bg_fit with dissolve

    show minhoquiet at center_char with dissolve

    thought "Min-ho. He doesn't invite conversation. Just completely self-contained."
    thought "He was reading by the window. I sat two seats away because the other spots felt wrong."

    hide minhoquiet
    show minhotalking at center_char
    minho "You're staring."
    hide minhotalking
    show minhoquiet at center_char
    soo "I'm thinking."
    hide minhoquiet
    show minhotalking at center_char
    minho "About what?"
    hide minhotalking
    show minhoquiet at center_char
    soo "Whether you ever get tired of being quiet."
    hide minhoquiet
    show minhotalking at center_char
    minho "No. Quiet is easier than most people think."
    minho "They just don't try it long enough."
    hide minhotalking
    show minhoquiet at center_char

    menu:
        "\"Can I try it? Sitting here quietly with you.\"":
            $ affection_minho += 2
            soo "Can I try it? Sitting here quietly?"
            minho "..."
            hide minhoquiet
            show minhotalking at center_char
            minho "You already are."
            hide minhotalking
            show minhoquiet at center_char
            thought "Oh. I was."

        "Say nothing and just stay.":
            $ affection_minho += 1
            thought "I didn't say anything."
            thought "He didn't tell me to leave."
            thought "That was enough."

    thought "He went back to his book. Didn't tell me to leave. I stayed."
    thought "Twenty minutes of silence. Most comfortable I'd felt all week."

    $ add_observation("Kang Min-ho", "Quiet is easier than people think. He didn't tell me to leave.")

    hide minhoquiet

    scene bg class at bg_fit with dissolve

    show woosmiletalk at center_char with dissolve

    woo "Soo-ah, do you believe in fate?"
    hide woosmiletalk
    show woosmile at center_char
    soo "No."
    hide woosmile
    show woosmiletalk at center_char
    woo "Not even a little?"
    hide woosmiletalk
    show woosmile at center_char
    soo "I think things happen and we make meaning out of them after."
    hide woosmile
    show woosmiletalk at center_char
    woo "That's kind of sad."
    hide woosmiletalk
    show woosmile at center_char
    soo "Or it means we have more control than we think."
    woo "..."
    hide woosmile
    show woosmiletalk at center_char
    woo "I never thought about it that way."
    hide woosmiletalk
    show woosmile at center_char

    thought "He actually listened. That's rarer than it sounds."

    $ add_observation("Woo Ju-in", "He asked if I believe in fate and actually listened to the answer.")

    hide woosmile

    scene bg school at bg_fit with dissolve

    show jihoquiet at center_char with dissolve

    thought "Ji-ho was on the roof after school. I don't know why I went up there."
    thought "I was just walking and the stairs were there. That's my story."

    hide jihoquiet
    show jihotalking at center_char
    jiho "You followed me."
    hide jihotalking
    show jihoquiet at center_char
    soo "I didn't know you were up here."
    hide jihoquiet
    show jihotalking at center_char
    jiho "The door has my name on it."
    hide jihotalking
    show jihoquiet at center_char
    soo "It does not."
    jiho "..."
    hide jihoquiet
    show jihotalking at center_char
    jiho "It should."
    hide jihotalking
    show jihoquiet at center_char

    menu:
        "\"Did you just make a joke?\"":
            $ affection_jiho += 2
            soo "Did you just make a joke?"
            jiho "..."
            hide jihoquiet
            show jihotalking at center_char
            jiho "No."
            hide jihotalking
            show jihoquiet at center_char
            thought "He absolutely did."

        "Pretend you didn't notice.":
            $ affection_jiho += 1
            thought "I decided not to acknowledge it."
            thought "He looked almost relieved."
            thought "Almost disappointed."

    thought "I'm absolutely writing that down."

    $ add_observation("Ji-ho", "He made a joke on the roof. Looked surprised that he did it.")

    soo "What are you drawing?"
    hide jihoquiet
    show jihotalking at center_char
    jiho "The city."
    hide jihotalking
    show jihoquiet at center_char
    soo "Can I see?"
    hide jihoquiet
    show jihotalking at center_char
    jiho "No. It's not finished."
    hide jihotalking
    show jihoquiet at center_char
    soo "I don't mind unfinished things."
    jiho "..."

    thought "He closed the sketchbook." 
    thought "Which means it wasn't the city."
    thought "I think he knew that I knew."

    hide jihoquiet

    scene black with dissolve

    thought "End of the third week. I'd stopped counting the days until I went home."
    thought "I hadn't noticed when that happened. But it had."

    jump chapter_4_extras
