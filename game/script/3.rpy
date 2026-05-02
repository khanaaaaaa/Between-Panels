label chapter_2:

    scene bg class at bg_fit with dissolve

    show screen chapter_card("Chapter 2", "The Plan Was To Be Invisible")
    pause 2.5

    thought "Three days into the school year."
    thought "My plan was going well."
    thought "I sat in the middle. I answered when called on. I ate lunch quietly."
    thought "Nobody paid special attention to me."
    thought "I was successfully a background character."
    thought "And then."

    show jihoquiet at right_char with dissolve

    "The classroom went quiet."
    "Not the polite kind of quiet."
    "The held-breath kind."

    jiho "Who's Sara Lee?"

    thought "..."
    thought "Oh no."

    hide sarasmilequiet
    show saraneutraltalk at left_char with dissolve

    sara "..."
    sara "That's me."

    jiho "You scored first place on the entrance exam."
    sara "Yes."
    jiho "Above me."
    sara "...Yes."
    jiho "Interesting."
    jiho "Don't get comfortable. I won't go easy on you next time."

    hide saraneutraltalk
    show saradisturbed at left_char

    sara "Seriously?"
    sara "Were you actually going easy on me?"

    hide jihoquiet
    show jihotalking at right_char

    jiho "Just wait and see."

    hide jihotalking
    show jihoquiet at right_char

    hide saradisturbed

    npc1 "Did she just— talk back to Ji-ho?!"
    npc2 "That girl is insane."
    npc1 "He's going to destroy her on the next exam."

    show sooneutralquiet at center_char with dissolve

    thought "He's the strangest one out of all of them."
    thought "The others at least have normal social behavior."
    thought "Ji-ho just walks up to people and declares academic war."
    thought "Who does that."

    hide jihoquiet

    show woosmile at right_char with dissolve

    woo "Wow! You're the first person to ever talk back to Ji-ho like that!"
    woo "I'm Woo Ju-in. Let's be friends!"

    hide sarasmilequiet
    show sarasmiletalk at left_char with dissolve

    sara "Ji-ho?"
    woo "That's his name, yeah. Eun Ji-ho."
    woo "Don't worry about him. He's like that with everyone he finds interesting."
    sara "...Interesting."

    hide sarasmiletalk
    hide woosmile

    thought "Interesting."
    thought "He challenged her because he found her interesting."
    thought "That is such a male lead thing to do."
    thought "I need to not be interesting."
    thought "I need to be the least interesting person in this building."

    scene black with dissolve

    npc1 "Bye—"
    npc2 "See you tomorrow—"

    thought "I zoned out for the rest of the day."
    thought "By the time I noticed, school was over."

    scene bg school_hallway at bg_fit with dissolve

    show saraneutraltalk at center_char with dissolve
    show sooneutralquiet at left_char with dissolve

    sara "Soo-ah. Let's walk home."
    soo "Oh. Yeah."

    thought "We walked in silence for a while."
    thought "I kept waiting for her to say something."
    thought "She kept waiting for me to say something."
    thought "Neither of us did."

    sara "Soo-ah."
    soo "Mm?"
    sara "Since this morning... you've been acting like I'm a stranger."
    soo "..."

    thought "Is she upset?"
    thought "She looks upset."

    sara "I kept looking at you in class. You kept looking away."
    sara "Why are you acting like this?"

    thought "What do I say."
    thought "I literally don't know who she is."
    thought "I can't say that."

    soo "I'm not avoiding you. I've just been... adjusting."
    sara "Adjusting."
    soo "First day jitters."

    hide saraneutraltalk
    show saradisturbed at center_char

    sara "Soo-ah. Is this because of what happened before?"
    soo "What...?"

    thought "SOMETHING HAPPENED."
    thought "Between us. Something happened."
    thought "What did I do."

    sara "I thought when you said hi to me this morning it meant things were okay."
    sara "But then you spent the whole day avoiding me."
    sara "Was I wrong to think that?"

    thought "I don't know what I'm supposed to have done."
    thought "I don't know what the Soo-ah of this world did."
    thought "But whatever it was — she's been waiting for an apology."
    thought "And she's been patient about it."
    thought "That's worse somehow."

    soo "No. You weren't wrong."
    soo "I'm not mad at you. I was never mad at you."
    soo "I've just been... in my head."

    hide saradisturbed
    show sarasmilequiet at center_char

    sara "Really?"
    soo "Really. I'm sorry if it seemed like I was pushing you away."

    thought "She smiled."
    thought "Like she'd been holding her breath and finally let it out."

    sara "That's a relief."
    sara "You're my best friend, Soo-ah."
    sara "I don't have another one."

    thought "..."
    thought "She said it so simply."
    thought "Like it was just a fact."
    thought "I don't have another one."
    thought "I felt something twist in my chest."
    thought "I don't know what to do with that."

    $ add_observation("Sara", "She said I'm her only best friend. She's been waiting for me to stop avoiding her. She's been patient this whole time.")

    hide sarasmilequiet

    scene bg room at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve

    thought "I got home and sat on my bed for a long time."
    thought "Thinking."

    soo "Okay."
    soo "Let's think about this seriously."

    thought "This world is real."
    thought "Or at least — it's real enough."
    thought "The people in it are real."
    thought "Sara is real."
    thought "And whatever happened between us — the Soo-ah of this world and Sara — that's real too."
    thought "I'm living someone else's life."
    thought "And I've already made a mess of it."

    hide sooneutralquiet
    show sooneutraltalk at center_char

    soo "..."
    soo "What do I do."

    hide sooneutraltalk
    show sooneutralquiet at center_char

    thought "Option one: find a way back to my original world."
    thought "Option two: figure out what this world is and survive it."
    thought "Option three: panic."
    thought "I've already done option three."
    thought "Let's try option two."

    scene black with dissolve

    thought "I fell asleep thinking about it."
    thought "And woke up still in this world."
    thought "Of course."

    jump chapter_3
