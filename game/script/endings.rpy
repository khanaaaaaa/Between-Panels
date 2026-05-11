label final_chapter:

    scene bg school_hallway at bg_fit with dissolve

    show screen chapter_card("Final Chapter", "Presence")

    show sooneutralquiet at center_char with dissolve

    thought "End of first year."
    thought "I stopped waiting to wake up somewhere else."
    thought "I don't know exactly when that happened."
    thought "But it did."

    thought "This world still looks drawn by hand."
    thought "The light still hits everything too perfectly."
    thought "The cherry blossoms are still in bloom in March."
    thought "None of that changed."
    thought "I just stopped treating it like a warning."

    hide sooneutralquiet

    scene bg school at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve

    thought "I walked to school on the last day of the year."
    thought "Same gate. Same courtyard. Same impossible light."
    thought "And I thought — okay."
    thought "I don't know why I'm here."
    thought "I don't know if I'll ever go back."
    thought "But I'm here."
    thought "And here has people in it."
    thought "Real ones."

    hide sooneutralquiet

    if route == "jiho":
        jump ending_jiho
    elif route == "eunhyeong":
        jump ending_eunhyeong
    elif route == "woo":
        jump ending_woo
    elif route == "sara":
        jump ending_sara
    else:
        jump ending_shared


label ending_jiho:

    scene bg school at bg_fit with dissolve

    show jihoquiet at center_char with dissolve

    thought "He was at the gate when I arrived."
    thought "Not waiting. Just there."
    thought "Sketchbook under his arm."
    thought "He looked up when he heard me."

    hide jihoquiet
    show jihotalking at center_char

    jiho "You're on time."
    hide jihotalking
    show jihoquiet at center_char
    soo "Don't sound so surprised."
    jiho "..."
    hide jihoquiet
    show jihotalking at center_char
    jiho "I'm not surprised."
    hide jihotalking
    show jihoquiet at center_char

    thought "He fell into step beside me."
    thought "We walked through the gate together."
    thought "Neither of us said anything."
    thought "We didn't need to."

    thought "At some point his hand brushed mine."
    thought "He didn't move away."
    thought "Neither did I."

    hide jihoquiet

    scene black with dissolve

    "First year ended."
    "Kang Soo-ah did not go back."
    "She wasn't sure she could."
    "She was less sure she wanted to."

    scene bg school at bg_fit with dissolve

    show jihoquiet at center_char with dissolve

    thought "Second year. New classroom. Same window."
    thought "Ji-ho was already there when I arrived."
    thought "He had saved me a seat."
    thought "Right next to him."
    thought "Not two away."
    thought "Right next to him."

    soo "..."
    hide jihoquiet
    show jihotalking at center_char
    jiho "Sit down."
    hide jihotalking
    show jihoquiet at center_char
    soo "You saved me a seat."
    jiho "..."
    hide jihoquiet
    show jihotalking at center_char
    jiho "The view is better from here."
    hide jihotalking
    show jihoquiet at center_char

    thought "I sat down."
    thought "He opened his sketchbook."
    thought "I looked out the window."
    thought "The cherry blossoms were still there."
    thought "Still impossible."
    thought "I didn't mind."

    hide jihoquiet

    scene black with dissolve

    "I don't know when this stopped feeling like a story."
    "I just know that it did."

    scene black with dissolve
    return


label ending_eunhyeong:

    scene bg school_hallway at bg_fit with dissolve

    show eunhyeongquiet at center_char with dissolve

    thought "He found me in the hallway before the last bell."
    thought "Which was new."
    thought "Eunhyeong usually let people come to him."

    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "Hey."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "Hey."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "Last day."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "Last day."
    eunhyeong "..."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "I've been thinking."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "About what?"
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "About next year."
    eunhyeong "About whether things will be different."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "Will they?"
    eunhyeong "..."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "I think so."
    eunhyeong "I think I want them to be."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char

    thought "He said it quietly."
    thought "Not performing it."
    thought "Just saying it."
    thought "To me."

    soo "Different how?"
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "Less careful."
    eunhyeong "With you, at least."
    soo "..."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "I'd like that."
    eunhyeong "..."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "Yeah."
    eunhyeong "Me too."

    hide eunhyeongtalk

    scene black with dissolve

    "First year ended."
    "Eunhyeong still held every room together."
    "But there was one person he didn't perform for."
    "He was still figuring out what that meant."
    "So was she."

    scene bg school at bg_fit with dissolve

    show eunhyeongquiet at center_char with dissolve

    thought "Second year. He still came to school early."
    thought "So did I."
    thought "We never talked about why."

    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "You're here."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char
    soo "So are you."
    eunhyeong "..."
    hide eunhyeongquiet
    show eunhyeongtalk at center_char
    eunhyeong "Yeah."
    hide eunhyeongtalk
    show eunhyeongquiet at center_char

    thought "He smiled."
    thought "The real one."
    thought "Before anyone else arrived."
    thought "Just for me."

    hide eunhyeongquiet

    scene black with dissolve

    "I don't know when this stopped feeling like a story."
    "I just know that it did."

    scene black with dissolve
    return


label ending_woo:

    scene bg school at bg_fit with dissolve

    show woosmile at center_char with dissolve

    thought "He was waiting outside the classroom on the last day."
    thought "Leaning against the wall."
    thought "Not performing ease."
    thought "Just easy."
    hide woosmile
    show woosmiletalk at center_char
    woo "Hey."
    hide woosmiletalk
    show woosmilequiet at center_char
    soo "Hey."
    hide woosmile
    show woosmiletalk at center_char
    woo "Last day."
    hide woosmiletalk
    show woosmilequiet at center_char
    soo "Last day."
    woo "..."
    hide woosmile
    show woosmiletalk at center_char
    woo "Soo-ah."
    hide woosmiletalk
    show woosmilequiet at center_char
    soo "Mm?"
    hide woosmile
    show woosmiletalk at center_char
    woo "I figured something out."
    hide woosmiletalk
    show woosmilequiet at center_char
    soo "What?"
    hide woosmile
    show woosmiletalk at center_char
    woo "The version of me that doesn't perform."
    woo "I think I know what he's like now."
    hide woosmiletalk
    show woosmilequiet at center_char
    soo "Yeah?"
    hide woosmile
    show woosmiletalk at center_char
    woo "He's quieter."
    woo "He notices more."
    woo "He's kind of terrible at history quizzes."
    hide woosmiletalk
    show woosmilequiet at center_char
    soo "I know."
    woo "..."
    hide woosmile
    show woosmiletalk at center_char
    woo "He likes you."
    woo "A lot."
    woo "That part I'm sure about."
    hide woosmiletalk
    show woosmilequiet at center_char
    thought "He said it simply."
    thought "No deflection."
    thought "No joke after."
    thought "Just that."

    soo "..."
    soo "I know that too."
    woo "..."
    hide woosmilequiet
    show woosmiletalk at center_char
    woo "Good."

    hide woosmiletalk

    scene black with dissolve

    "First year ended."
    "Woo Ju-in still made every room louder."
    "But there was one person he was quiet with."
    "On purpose."
    "That was new."

    scene bg school at bg_fit with dissolve

    show woosmile at center_char with dissolve

    thought "Second year. He still came to school early."
    thought "So did I."
    thought "Same bench. Same quiet."
    thought "Different kind of comfortable."

    hide woosmile
    show woosmiletalk at center_char
    woo "You're smiling."
    hide woosmiletalk
    show woosmilequiet at center_char
    soo "I'm just sitting here."
    hide woosmile
    show woosmiletalk at center_char
    woo "You're smiling while sitting here."
    soo "..."
    hide woosmiletalk
    show woosmile at center_char
    soo "So are you."
    woo "..."
    hide woosmile
    show woosmiletalk at center_char
    woo "Yeah."
    woo "I noticed."

    hide woosmiletalk

    scene black with dissolve

    "I don't know when this stopped feeling like a story."
    "I just know that it did."

    scene black with dissolve
    return


label ending_sara:

    scene bg school at bg_fit with dissolve

    show sarasmilequiet at center_char with dissolve

    thought "Last day of first year."
    thought "Sara was waiting at the gate."
    thought "She had two drinks."
    thought "One for her. One for me."
    thought "She didn't say anything about it."
    thought "She just handed one over."

    soo "You didn't have to—"
    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "I know."
    sara "I wanted to."
    hide sarasmiletalk
    show sarasmilequiet at center_char

    thought "I took it."
    thought "We walked in together."
    thought "The courtyard was full of people."
    thought "She stayed close."
    thought "I let her."

    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "Soo-ah."
    hide sarasmiletalk
    show sarasmilequiet at center_char
    soo "Mm?"
    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "I'm glad this year happened."
    hide sarasmiletalk
    show sarasmilequiet at center_char
    soo "Even the bad parts?"
    sara "..."
    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "Especially the bad parts."
    sara "Because we got through them."
    sara "Together."
    hide sarasmiletalk
    show sarasmilequiet at center_char
    soo "..."
    soo "Yeah."
    soo "We did."

    thought "She bumped my shoulder."
    thought "I bumped back."
    thought "Some things stay the same."
    thought "Some things get better."
    thought "This was both."

    hide sarasmilequiet

    scene black with dissolve

    "First year ended."
    "Sara still saved Soo-ah a seat every day."
    "Right next to her."
    "Not one over."
    "Never one over again."

    scene bg school at bg_fit with dissolve

    show sarasmilequiet at center_char with dissolve

    thought "Second year. Same classroom. Same seat."
    thought "She was already there when I arrived."
    thought "She looked up and smiled."
    thought "The real one."
    thought "Like she'd been waiting."
    thought "Like she was glad I came."

    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "You're on time."
    hide sarasmiletalk
    show sarasmilequiet at center_char
    soo "Don't make it weird."
    hide sarasmilequiet
    show sarasmiletalk at center_char
    sara "I'm making it weird."
    hide sarasmiletalk
    show sarasmilequiet at center_char
    soo "You're making it weird."

    hide sarasmilequiet

    scene black with dissolve

    "I don't know when this stopped feeling like a story."
    "I just know that it did."

    scene black with dissolve
    return


label ending_shared:

    scene bg school at bg_fit with dissolve

    show sooneutralquiet at center_char with dissolve

    thought "Last day of first year."
    thought "I stood at the gate for a moment before going in."
    thought "Just stood there."
    thought "Looking at it."

    thought "This world still looks like it was drawn by hand."
    thought "It probably always will."
    thought "I've stopped minding."

    hide sooneutralquiet

    scene black with dissolve

    "I don't know when this stopped feeling like a story."
    "I just know that it did."

    scene black with dissolve
    return
