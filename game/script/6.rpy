label chapter_5:

    scene bg class at bg_fit with dissolve

    show screen chapter_card("Chapter 5", "Something Already Slipping")

    show sooneutralquiet at center_char with dissolve

    thought "One month in. I had a rhythm. Stay invisible. It was working."
    thought "And then it wasn't."

    hide sooneutralquiet

    scene bg school_hallway at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve
    show sarasmilequiet at left_char with dissolve

    thought "Three years ago I decided to avoid Sara. Not dramatically. Just quietly."
    thought "I started leaving earlier. Taking different routes. Sitting somewhere new at lunch."
    thought "I told myself she wouldn't notice."

    sara "Soo-ah."
    soo "Oh — hey. Running late, sorry—"
    sara "You're always running late lately."
    sara "It's okay. I'll see you in class."

    thought "She smiled. A real smile. That was worse."
    thought "She was giving me room to come back. And I used it to walk away."

    hide sarasmilequiet
    hide sooneutralquiet

    scene bg class at bg_fit with dissolve

    show yeomin at right_char with dissolve
    show sooneutralquiet at center_char with dissolve

    thought "Baek Yeo-min. Easy smile, comfortable energy. No history, no weight."
    thought "Nobody waiting for me to remember something I didn't do."

    yeomin "Sit with us at lunch?"
    soo "Sure."

    thought "I told myself it was temporary. I never asked if Sara understood."

    hide yeomin

    show sarasmilequiet at left_char with dissolve

    thought "She watched me cross the room to sit with Yeo-min. I saw her. I didn't turn around."
    thought "That's how most things break. Not with a fight. With a direction you keep choosing."

    $ add_observation("Sara", "Three years ago I walked away and didn't turn around. She watched me go.")

    hide sarasmilequiet

    show chunyeon at right_char with dissolve
    show sarasmilequiet at left_char with dissolve

    thought "A few days later Chun-young walked up to Sara's desk."

    chunyeon "Do you know the answer to question six?"
    sara "Oh. It's the second law applied to the variable — here."
    chunyeon "Right."

    thought "He smiled. Small and brief. Like it surprised him."

    npc "Did Chun-young just smile?! At Sara?!"

    thought "He's warmer toward her than anyone else. Filed."

    $ add_observation("Chun-young", "He smiled at Sara when she helped him. Small. Like it surprised him.")

    hide chunyeon
    hide sarasmilequiet

    show yeomin at right_char with dissolve

    yeomin "Want to go to the shop after school?"
    soo "Yeah, sure."

    hide yeomin

    show sarasmilequiet at left_char with dissolve

    sara "Soo-ah...?"

    thought "She was at the end of the hallway. Watching me leave with Yeo-min. I kept walking."

    $ add_observation("Sara", "She watched me leave with Yeo-min. I saw her. I kept walking.")

    hide sarasmilequiet
    hide sooneutralquiet

    scene bg class at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve

    npc "You know Baek Yeo-min talks about Sara behind her back, right? In the bathroom. Every day."

    thought "I knew Yeo-min didn't like Sara. Hearing it out loud felt worse."

    show sarasmilequiet at left_char with dissolve

    sara "Soo-ah, I—"
    soo "Sorry. I need to finish these problems."
    sara "..."

    thought "She stopped talking. The silence between us was heavier than before. I'd made it that way."

    hide sarasmilequiet
    hide sooneutralquiet

    scene bg school_hallway at bg_fit with dissolve

    show jihoquiet at right_char with dissolve
    show woosmile at left_char with dissolve

    woo "You keep looking at Soo-ah and Sara during break."
    jiho "They're hard to ignore. Soo-ah is being cold."
    jiho "Sara keeps trying and Soo-ah just pushes her away."
    woo "Doesn't she look scared to you? More than cold."
    jiho "..."
    jiho "Maybe."

    thought "I wasn't there for this. Found out much later."
    thought "The fact that Ji-ho had been watching. That Ju-in saw it more clearly than I did."

    $ add_observation("Ji-ho", "He told Ju-in Sara doesn't seem like the type to hurt anyone. He was watching us even then.")
    $ add_observation("Woo Ju-in", "He said I looked scared more than cold. He was right.")

    hide jihoquiet
    hide woosmile

    scene bg room at bg_fit with dissolve

    show sarasmilequiet at center_char with dissolve

    "A few days later. Sara's brother found her sitting quietly in her room."

    "What's wrong?"

    sara "...I think Soo-ah is avoiding me."
    sara "She keeps cutting conversations short. She's spending all her time with someone who doesn't like me."
    sara "Does she not want to be friends anymore?"

    "Just talk to her. You've known each other since you were little."

    sara "...Okay. I'll go now."

    hide sarasmilequiet

    scene black with dissolve

    show saraneutraltalk at center_char with dissolve

    sara "Soo-ah, I need to talk to you—"

    hide saraneutraltalk
    show saradisturbed at center_char with dissolve

    sara "Yeo-min?!"
    sara "Why is Yeo-min in Soo-ah's room."

    thought "That was the moment. Not a fight. Just Sara in a doorway, seeing what I'd chosen."

    hide saradisturbed

    scene black with dissolve

    thought "She left. And I let her. That was the worst part."

    $ add_observation("Sara", "She came to fix things. Found Yeo-min in my room. Left without saying anything. I let her go.")

    jump chapter_6


label chapter_6:

    scene bg room at bg_fit with dissolve

    show screen chapter_card("Chapter 6", "Guilt Without Confrontation")

    show sooneutralquiet at center_char with dissolve

    thought "Back to now. Three years later and I'm still carrying it."
    thought "Guilt doesn't announce itself. It just sits in the corner of every interaction."
    thought "Every time Sara smiles at me. Every time she's patient when she doesn't have to be."

    hide sooneutralquiet

    scene bg school at bg_fit with dissolve

    show sarasmilequiet at left_char with dissolve
    show sooneutralquiet at center_char with dissolve

    sara "You look tired."
    soo "Didn't sleep well."
    sara "Again?"
    soo "I keep thinking about old things."
    sara "..."
    sara "Okay. Eat your lunch."

    thought "She didn't push. She never pushes. She just waits."
    thought "And I keep making her wait."

    $ add_observation("Sara", "I said I'm thinking about old things. She said eat your lunch. She's always waiting.")

    hide sarasmilequiet
    hide sooneutralquiet

    scene bg school_hallway at bg_fit with dissolve

    show jihoquiet at right_char with dissolve
    show sooneutralquiet at center_char with dissolve

    thought "Ji-ho was in the library. I sat down without asking. He made space without being asked."
    thought "We'd developed a rhythm. Neither of us named it."

    jiho "You've been on the same page for twenty minutes."
    soo "I'm thinking."
    jiho "About what?"
    soo "Something I did a long time ago."
    jiho "Does thinking about it change it?"
    soo "No."
    jiho "Then stop."
    soo "It's not that simple."
    jiho "..."
    jiho "No. I know."

    thought "He said it like he had his own version of it."

    $ add_observation("Ji-ho", "He said stop thinking about old things. Then said he knows it's not that simple.")

    hide jihoquiet
    hide sooneutralquiet

    scene bg class at bg_fit with dissolve

    show woosmile at center_char with dissolve
    show sooneutralquiet at left_char with dissolve

    woo "You're usually quiet and watching. Today you're just quiet."
    soo "Is there a difference?"
    woo "When you're watching you're present. Right now you're somewhere else."
    soo "Ju-in. If you hurt someone a long time ago and you've been trying to fix it — does that count?"
    woo "Depends on whether the person knows you're trying."
    woo "Fixing things quietly doesn't always reach people. Sometimes you have to say it out loud."
    soo "What if you don't know how?"
    woo "Start with something small. And don't stop."

    $ add_observation("Woo Ju-in", "He said fixing things quietly doesn't reach people. Start small and don't stop.")

    hide woosmile
    hide sooneutralquiet

    scene bg school at bg_fit with dissolve

    show minhoquiet at right_char with dissolve
    show sooneutralquiet at center_char with dissolve

    thought "Min-ho was reading on the steps. I sat beside him."

    minho "Something's bothering you."
    soo "I did something a long time ago. I don't think you can undo things."
    soo "I think you can only build something new on top of them."
    minho "That's more accurate than most people get."
    minho "Pretending costs more in the long run."

    thought "He shifted slightly toward me. Just slightly. Like proximity was the thing he could offer."

    $ add_observation("Kang Min-ho", "Pretending costs more in the long run. He shifted closer without saying anything.")

    hide minhoquiet
    hide sooneutralquiet

    scene bg room at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve

    thought "That night I wrote it all down."
    thought "Start small. Don't stop. You can't undo things — build on top of them."
    thought "Does thinking about it change it? No. So stop."
    thought "Tomorrow I'm going to say something out loud. And I'm not going to stop."

    hide sooneutralquiet

    scene black with dissolve

    jump chapter_7
