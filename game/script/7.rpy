label chapter_7:

    scene bg school at bg_fit with dissolve

    show screen chapter_card("Chapter 7", "The Moment Before Paths Split")

    show saraneutralquiet at center_char with dissolve

    soo "Sara. I've been meaning to say something."
    hide saraneutralquiet
    show saraneutraltalk at center_char
    sara "Okay."
    hide saraneutraltalk
    show saraneutralquiet at center_char
    soo "Things have been off between us for a long time. And I know it's because of me."
    soo "I'm not asking you to forget it. I just want you to know I'm not going anywhere."
    sara "..."
    hide saraneutralquiet
    show saraneutraltalk at center_char
    sara "I hear you."

    hide saranetralquiet
    thought "That felt underwhelming."

    "The bus ride took two hours. City to hills. Hills to trees."
    "Soo-ah watched the scenery and thought about nothing in particular."
    "First time she'd done that in months."

    scene bg school at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve

    thought "The mountains looked like a background illustration. Everything here does."
    thought "But for the first time that didn't feel like a warning."

    hide sooneutralquiet

    "Day one. Cabins assigned. First evening free."

    show woosmile at center_char with dissolve

    thought "Jooin was sitting on a rock doing absolutely nothing. No phone. No book."
    thought "I almost didn't recognize him."

    soo "You look different."
    hide woosmile
    show woosmiletalk at center_char
    woo "Different how?"
    hide woosmiletalk
    show woosmile at center_char
    soo "Like yourself."
    hide woosmile
    show woosmiletalk at center_char
    woo "Is that a compliment?"
    hide woosmiletalk
    show woosmile at center_char
    soo "Yes."

    thought "He moved over. Making room. I sat."

    hide woosmile
    show woosmiletalk at center_char
    woo "You always walk like you're going somewhere important."
    hide woosmiletalk
    show woosmile at center_char
    soo "I'm just walking."
    hide woosmile
    show woosmiletalk at center_char
    woo "That's what I mean." 
    woo "Even when you're just walking it looks intentional."
    woo "Hey Soo-ah. I'm glad you came on this trip."
    hide woosmiletalk
    show woosmile at center_char
    soo "Me too."
    hide woosmile
    show woosmiletalk at center_char
    woo "Good."
    hide woosmiletalk
    show woosmile

    thought "He smiles so easily." 
    thoguht "I've learned to look for it."

    hide woosmile

    scene bg school at bg_fit with dissolve

    show eunhyeongquiet at center_char with dissolve

    thought "Eunhyeong had a deck of cards and no one to play with. Which seemed wrong."

    soo "Where is everyone?"
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "Around."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "And you're here alone."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "I wanted a break from performing for people."
    eunhyeong "Don't look at me like that."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "Like what?"
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "Like you figured something out."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "I just listened."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "That's worse."
    eunhyeong "You want to play?"
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "Sure."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "I should warn you I'm very good."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "I should warn you I don't care."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "I like you, Soo-ah."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char

    thought "He said it like a fact. I believed him."

    hide eunhyeongquiet

    scene bg school at bg_fit with dissolve

    show jihoquiet at center_char with dissolve

    thought "Ji-ho was at the overlook. Sketchbook open. Not drawing. Just looking."
    thought "I sat on the railing beside him."

    hide jihoquiet
    show jihotalking at center_char

    jiho "You've been walking for a while."
    hide jihotalking
    show jihoquiet at center_char
    soo "How do you know that?"
    hide jihoquiet
    show jihotalking at center_char
    jiho "Your face tells me a lot of things."
    hide jihotalking
    show jihoquiet at center_char
    soo "..."

    thought "I looked at the view." 
    thought "He opened the sketchbook and started drawing."

    soo "What are you drawing?"
    hide jihoquiet
    show jihotalking at center_char
    jiho "The light. And what's in it."
    hide jihotalking
    show jihoquiet at center_char

    thought "He tilted the page away. Which meant it was me. Again."
    thought "I smiled. The corner of his mouth moved. Just slightly."
    thought "That was number six. I was still counting."

    hide jihoquiet

    scene bg school at bg_fit with dissolve

    show sarasmilequiet at center_char with dissolve

    thought "Sara was sitting outside the cabin."

    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "Hey."
    hide sarasmiletalk
    show sarasmilequiet at center_char
    soo "Hey."
    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "It's pretty here."
    hide sarasmiletalk
    show sarasmilequiet at center_char
    soo "Yeah."
    hide sarasmilequiet
    show saeasmiletalk at center_char
    sara "I keep thinking I should take a photo but I don't want to look away."
    hide sarasmiletalk 
    show sarasmilequiet at center_char
    soo "Then don't."
    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "Yeah."
    hide sarasmiletalk
    show sarasmilequiet at center_char

    menu:
        "Take a photo together anyway.":
            $ affection_sara += 2
            soo "Here. One photo. Then we stop."
            sara "..."
            hide sarasmilequiet
            show sarasmiletalk at center_char
            sara "Okay. One."
            hide sarasmiletalk
            show sarasmilequiet at center_char
            thought "She leaned into me slightly."
            thought "I took the photo."
            thought "A photo with an angel."

        "Just sit with her.":
            $ affection_sara += 1
            thought "I didn't say anything. Neither did she."
            thought "The light kept changing. Neither of us moved."

    thought "We sat until it got dark." 
    thought"Not saying much." 
    thought "Not needing to."

    hide sarasmilequiet
    show sarasmiletalk at center_char

    sara "I'm glad you said something this morning."
    hide sarasmiletalk
    show sarasmilequiet at center_char
    soo "Me too."
    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "I missed you. Even when you were right there. I missed you."
    hide sarasmiletalk
    show sarasmilequiet at center_char
    soo "I'm here now."
    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "I know. That's why I said it."
    hide sarasmiletalk
    show sarasmilequiet at center_char

    $ add_observation("Sara", "She said she missed me even when I was right there. I said I'm here now.")

    hide sarasmilequiet

    scene black with dissolve

    show sooneutralquiet at center_char with dissolve

    thought "I lay in the cabin that night thinking about all of them."
    thought "Jooin making room. Eunhyeong saying I like you like it was nothing."
    thought "Ji-ho tilting the sketchbook away."
    thought "Sara saying I missed you even when you were right there."
    thought "I've been so focused on not getting pulled in."
    thought "I didn't notice I already was."

    hide sooneutralquiet

    menu:
        "Ji-ho. The way he tilted the sketchbook away.":
            $ route = "jiho"
            $ affection_jiho += 3
            jump route_jiho_school

        "Eunhyeong. The way he said I like you like it cost him nothing.":
            $ route = "eunhyeong"
            $ affection_eunhyeong += 3
            jump route_eunhyeong_school

        "Jooin. The way he made room without saying anything.":
            $ route = "woo"
            $ affection_woo += 3
            jump route_woo_school

        "Sara. The way she said I missed you even when you were right there.":
            $ route = "sara"
            $ affection_sara += 3
            jump route_sara_school
