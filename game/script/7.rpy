label chapter_7:

    scene bg school at bg_fit with dissolve

    show screen chapter_card("Chapter 7", "The Moment Before Paths Split")

    show sarasmilequiet at center_char with dissolve

    soo "Sara. I've been meaning to say something."
    sara "Okay."
    soo "Things have been off between us for a long time. And I know it's because of me."
    soo "I'm not asking you to forget it. I just want you to know I'm not going anywhere."
    sara "..."
    sara "I hear you."

    thought "Not it's fine. Not I forgive you. I hear you."
    thought "The door was open."

    $ add_observation("Sara", "I told her I'm choosing to be here. She said I hear you.")

    hide sarasmilequiet

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
    woo "Different how?"
    soo "Like yourself."
    woo "Is that a compliment?"
    soo "Yes."

    thought "He moved over. Making room. I sat."

    woo "You always walk like you're going somewhere important."
    soo "I'm just walking."
    woo "That's what I mean. Even when you're just walking it looks intentional."
    woo "Hey Soo-ah. I'm glad you came on this trip."
    soo "Me too."
    woo "Good."

    thought "He smiled. The quiet one. The one I'd learned to look for."

    hide woosmile

    scene bg school at bg_fit with dissolve

    show eunhyeong at center_char with dissolve

    thought "Eunhyeong had a deck of cards and no one to play with. Which seemed wrong."

    soo "Where is everyone?"
    eunhyeong "Around."
    soo "And you're here alone."
    eunhyeong "I wanted a break from performing for people."
    eunhyeong "Don't look at me like that."
    soo "Like what?"
    eunhyeong "Like you figured something out."
    soo "I just listened."
    eunhyeong "That's worse."

    thought "He laughed. Quietly. Like something had loosened."

    eunhyeong "You want to play?"
    soo "Sure."
    eunhyeong "I should warn you I'm very good."
    soo "I should warn you I don't care."
    eunhyeong "I like you, Soo-ah."

    thought "He said it like a fact. I believed him."

    hide eunhyeong

    scene bg school at bg_fit with dissolve

    show chunyeon at center_char with dissolve

    thought "Chun-young was at the lake. Shoes off. Feet in the water."
    thought "He always looked carefully placed. This was different. He just looked like a person."

    chunyeon "The water's cold."
    soo "I wasn't going to—"
    chunyeon "You were thinking about it."
    soo "Maybe."

    thought "He moved over. I sat at the edge. Took my shoes off. Put my feet in."
    thought "It was very cold."

    soo "Okay. It's cold."
    chunyeon "I told you."
    soo "Why are you doing this?"
    chunyeon "Because I wanted to feel something that wasn't expected of me."
    soo "I think I know what you mean."
    chunyeon "Yeah. I think you do."

    hide chunyeon

    scene bg school at bg_fit with dissolve

    show jihoquiet at center_char with dissolve

    thought "Ji-ho was at the overlook. Sketchbook open. Not drawing. Just looking."
    thought "I sat on the railing beside him. Not close. Just nearby. He didn't move away."

    jiho "You've been walking for a while."
    soo "How do you know that?"
    jiho "Your face tells me a lot of things."
    soo "..."

    thought "I looked at the view. He opened the sketchbook and started drawing."

    soo "What are you drawing?"
    jiho "The light. And what's in it."

    thought "He tilted the page away. Which meant it was me. Again."
    thought "I smiled. The corner of his mouth moved. Just slightly."
    thought "That was number six. I was still counting."

    hide jihoquiet

    scene bg school at bg_fit with dissolve

    show sarasmilequiet at center_char with dissolve

    thought "Sara was sitting outside the cabin. Knees pulled up. Hair loose."
    thought "She looked younger like this. More like the Sara I was supposed to remember."

    sara "Hey."
    soo "Hey."
    sara "It's pretty here."
    soo "Yeah."
    sara "I keep thinking I should take a photo but I don't want to look away."
    soo "Then don't."
    sara "Yeah."

    menu:
        "Take a photo together anyway.":
            $ affection_sara += 2
            soo "Here. One photo. Then we stop."
            sara "..."
            sara "Okay. One."
            thought "She leaned into me slightly."
            thought "I took the photo."
            thought "I didn't look at it. I didn't need to."

        "Just sit with her.":
            $ affection_sara += 1
            thought "I didn't say anything. Neither did she."
            thought "The light kept changing. Neither of us moved."

    thought "We sat until it got dark. Not saying much. Not needing to."

    sara "I'm glad you said something this morning."
    soo "Me too."
    sara "I missed you. Even when you were right there. I missed you."
    soo "I'm here now."
    sara "I know. That's why I said it."

    $ add_observation("Sara", "She said she missed me even when I was right there. I said I'm here now.")

    hide sarasmilequiet

    scene black with dissolve

    show sooneutralquiet at center_char with dissolve

    thought "I lay in the cabin that night thinking about all of them."
    thought "Jooin making room. Eunhyeong saying I like you like it was nothing."
    thought "Chun-young with his feet in cold water. Ji-ho tilting the sketchbook away."
    thought "Sara saying I missed you even when you were right there."
    thought "I've been so focused on not getting pulled in."
    thought "I didn't notice I already was."

    hide sooneutralquiet

    menu:
        "Ji-ho. The way he tilted the sketchbook away.":
            $ route = "jiho"
            $ affection_jiho += 3
            jump route_jiho_trip

        "Chun-young. The way he said because I wanted to feel something real.":
            $ route = "chunyeon"
            $ affection_chunyeon += 3
            jump route_chunyeon_trip

        "Eunhyeong. The way he said I like you like it cost him nothing.":
            $ route = "eunhyeong"
            $ affection_eunhyeong += 3
            jump route_eunhyeong_trip

        "Jooin. The way he made room without saying anything.":
            $ route = "woo"
            $ affection_woo += 3
            jump route_woo_trip

        "Sara. The way she said I missed you even when you were right there.":
            $ route = "sara"
            $ affection_sara += 3
            jump route_sara_trip
