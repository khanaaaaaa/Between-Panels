################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

screen phone_notification(sender, message):
    zorder 50

    fixed:
        xalign 0.99
        yalign 0.99
        xsize 280
        ysize 480
        at phone_anim

        ## phone body
        frame:
            xsize 280
            ysize 480
            xpos 0
            ypos 0
            background Solid("#1a1a1a")
            padding (0, 0, 0, 0)

        ## rounded screen area
        frame:
            xsize 252
            ysize 420
            xpos 14
            ypos 30
            background Solid("#0d0d1a")
            padding (0, 0, 0, 0)

        ## top notch
        frame:
            xsize 80
            ysize 18
            xpos 100
            ypos 30
            background Solid("#1a1a1a")
            padding (0, 0, 0, 0)

        ## camera dot
        frame:
            xsize 10
            ysize 10
            xpos 135
            ypos 34
            background Solid("#333333")
            padding (0, 0, 0, 0)

        ## status bar
        frame:
            xsize 252
            ysize 24
            xpos 14
            ypos 54
            background Solid("#111122")
            padding (0, 0, 0, 0)

        text "9:02":
            xpos 22
            ypos 57
            size 11
            color "#ffffff"
            bold True

        text "▸ ▸":
            xpos 220
            ypos 57
            size 10
            color "#aaaaaa"

        ## notification card
        frame:
            xsize 232
            ysize 110
            xpos 24
            ypos 90
            background Solid("#1e1e2e")
            padding (0, 0, 0, 0)

        ## app label bar
        frame:
            xsize 232
            ysize 24
            xpos 24
            ypos 90
            background Solid("#2a1a2e")
            padding (0, 0, 0, 0)

        text "✉  Messages":
            xpos 32
            ypos 93
            size 11
            color "#c9748f"
            bold True

        text "now":
            xpos 218
            ypos 93
            size 10
            color "#888888"

        ## sender
        text "[sender]":
            xpos 32
            ypos 122
            size 16
            color "#ffffff"
            bold True

        ## message
        text "[message]":
            xpos 32
            ypos 146
            xmaximum 210
            size 13
            color "#aaaaaa"

        ## home bar
        frame:
            xsize 80
            ysize 5
            xpos 100
            ypos 444
            background Solid("#444444")
            padding (0, 0, 0, 0)

        ## side power button
        frame:
            xsize 4
            ysize 50
            xpos 276
            ypos 120
            background Solid("#333333")
            padding (0, 0, 0, 0)

        ## side volume buttons
        frame:
            xsize 4
            ysize 34
            xpos 0
            ypos 110
            background Solid("#333333")
            padding (0, 0, 0, 0)

        frame:
            xsize 4
            ysize 34
            xpos 0
            ypos 154
            background Solid("#333333")
            padding (0, 0, 0, 0)

        ## red notification dot
        frame:
            xsize 16
            ysize 16
            xpos 240
            ypos 86
            background Solid("#ff0033")
            padding (0, 0, 0, 0)
            at notif_dot_pulse

        text "1":
            xpos 245
            ypos 87
            size 11
            color "#ffffff"
            bold True

transform notif_dot_pulse:
    block:
        ease 0.6 alpha 1.0
        ease 0.6 alpha 0.3
        repeat

transform phone_anim:
    on show:
        xoffset 300 alpha 0
        ease 0.4 xoffset 0 alpha 1.0
    on hide:
        ease 0.3 xoffset 300 alpha 0

transform bubble_pop:
    alpha 0 zoom 0.8
    ease 0.25 alpha 1.0 zoom 1.0

screen cute_bubble(who, what, side="left"):
    zorder 40

    if side == "left":
        frame at bubble_pop:
            xalign 0.05
            yalign 0.72
            xmaximum 600
            padding (24, 16, 24, 16)
            background Frame(Solid("#fff0f5"), 20, 20, 20, 20)
            vbox:
                spacing 6
                text who:
                    size 22
                    color "#c9748f"
                    bold True
                text what:
                    size 26
                    color "#3a2a32"
    else:
        frame at bubble_pop:
            xalign 0.95
            yalign 0.72
            xmaximum 600
            padding (24, 16, 24, 16)
            background Frame(Solid("#f0f5ff"), 20, 20, 20, 20)
            vbox:
                spacing 6
                text who:
                    size 22
                    color "#748fc9"
                    bold True
                text what:
                    size 26
                    color "#3a2a32"

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame at skip_bounce:
        xalign 0.5
        yalign 0.0
        yoffset 12
        padding (20, 10, 20, 10)
        background Frame(Solid("#fce4ec"), 30, 30, 30, 30)

        hbox:
            spacing 10
            yalign 0.5

            text "✿":
                size 22
                color "#c9748f"
                at spin

            text _("skipping"):
                size 22
                color "#c9748f"
                italic True

            text "✿" at delayed_blink(0.0, 0.9):
                size 18
                color "#e8a0bf"
                style "skip_triangle"

            text "✿" at delayed_blink(0.2, 0.9):
                size 18
                color "#e8a0bf"
                style "skip_triangle"

            text "✿" at delayed_blink(0.4, 0.9):
                size 18
                color "#e8a0bf"
                style "skip_triangle"

transform delayed_blink(delay, period):
    alpha 0.0
    pause delay
    block:
        linear (period / 2) alpha 1.0
        linear (period / 2) alpha 0.0
        repeat

transform skip_bounce:
    yoffset 12
    block:
        ease 0.6 yoffset 6
        ease 0.6 yoffset 12
        repeat

transform spin:
    rotate 0
    linear 3.0 rotate 360
    repeat

screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_pop:
        xalign 0.98
        yalign 0.06
        padding (20, 12, 20, 12)
        background Frame(Solid("#fce4ec"), 30, 30, 30, 30)

        hbox:
            spacing 10
            yalign 0.5
            text "♡":
                size 22
                color "#c9748f"
            text "[message!tq]":
                size 22
                color "#7a5c6e"

    timer 3.0 action Hide("notify")

transform notify_pop:
    on show:
        alpha 0 yoffset -20
        ease 0.3 alpha 1.0 yoffset 0
    on hide:
        ease 0.3 alpha 0.0 yoffset -20

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 18

        for i in items:
            button:
                action i.action
                xalign 0.5
                xminimum 500
                xmaximum 900
                padding (40, 18, 40, 18)
                background Frame(Solid("#c9748f"), 40, 40, 40, 40)
                hover_background Frame(Solid("#c9748f"), 40, 40, 40, 40)
                at choice_pop

                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 12
                    text "✦":
                        size 18
                        color "#c9748f"
                        yalign 0.5
                    text i.caption:
                        size 28
                        color "#3a2a32"
                        hover_color "#ffffff"
                        xalign 0.5
                        yalign 0.5
                    text "✦":
                        size 18
                        color "#c9748f"
                        yalign 0.5

transform choice_pop:
    on show:
        alpha 0 zoom 0.92
        ease 0.2 alpha 1.0 zoom 1.0

transform textbox_fadein:
    on show:
        linear 0 alpha 0.0
        ease 0.2 alpha 1.0
    on hide:
        ease 0.15 alpha 0.0

screen say(who, what):
    zorder 1
    style_prefix "say"

    if who is None:
        frame at textbox_fadein:
            xalign 0.5
            yalign 0.85
            xsize 1400
            padding (50, 22, 50, 22)
            background Frame(Solid("#f5e6f080"), 40, 40, 40, 40)

            text what id "what":
                xalign 0.5
                yalign 0.5
                size 28
                color "#2a1a22"
                italic True
                text_align 0.5
                xmaximum 1280

    else:
        frame at textbox_fadein:
            xalign 0.5
            yalign 1.0
            xfill True
            ysize 210
            padding (70, 30, 70, 30)
            background Frame(Solid("#fdf4f7e6"), 0, 0, 0)

            fixed:
                xsize 6
                yfill True
                xpos 0
                ypos 0
            frame:
                xsize 6
                yfill True
                background Solid("#c9748f")

            text what id "what":
                xpos 30
                ypos 50
                xmaximum 1760
                size 30
                color "#3a2a32"
                line_spacing 10
                adjust_spacing False

            frame at textbox_fadein:
                xpos 70
                yalign 1.0
                yoffset -178
                xsize None
                ysize None
                padding (28, 10, 28, 10)
                background Frame(Solid("#c9748f"), 40, 40, 40)

                text who id "who":
                    size 26
                    color "#ffffff"
                    bold True

        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0

    textbutton "✿ skip":
        action Skip()
        xalign 0.98
        yalign 0.02
        padding (16, 8, 16, 8)
        background Frame(Solid("#c9748f"), 30, 30, 30, 30)
        hover_background Frame(Solid("#e8a0bf"), 30, 30, 30, 30)
        text_style "skip_button_text"

    textbutton "✿ back":
        action Rollback()
        xalign 0.98
        yalign 0.08
        padding (16, 8, 16, 8)
        background Frame(Solid("#7a5c6e"), 30, 30, 30, 30)
        hover_background Frame(Solid("#e8a0bf"), 30, 30, 30, 30)
        text_style "skip_button_text"

    textbutton "✦ notebook":
        action Show("notebook")
        xalign 0.02
        yalign 0.02
        padding (16, 8, 16, 8)
        background Frame(Solid("#7a5c6e"), 30, 30, 30, 30)
        hover_background Frame(Solid("#c9748f"), 30, 30, 30, 30)
        text_style "skip_button_text"

init python:
    config.character_id_prefixes.append('namebox')


style say_dialogue:
    xpos 30
    xsize 1760
    ypos 50
    size 30
    color "#3a2a32"
    line_spacing 10
    adjust_spacing False

style say_thought:
    size 28
    color "#9a6a8a"
    italic True
    adjust_spacing False

style say_label:
    size 26
    color "#ffffff"
    bold True
    xalign 0.0
    yalign 0.5

style skip_button_text:
    size 20
    color "#ffffff"
    bold True

style skip_triangle:
    size 18
    color "#e8a0bf"

screen letterbox():
    zorder 90
    frame:
        xfill True
        ysize 80
        ypos 0
        background Solid("#000000")
    frame:
        xfill True
        ysize 80
        yalign 1.0
        background Solid("#000000")

transform letterbox_in:
    on show:
        linear 0 alpha 0.0
        ease 0.4 alpha 1.0
    on hide:
        ease 0.3 alpha 0.0

screen chapter_card(number, title):
    zorder 150

    frame:
        xfill True
        yfill True
        background Solid("#000000cc")
        padding (0, 0, 0, 0)

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 16

        text "[number]":
            xalign 0.5
            size 24
            color "#c9748f"
            italic True

        frame:
            xalign 0.5
            xsize 400
            ysize 2
            background Solid("#c9748f")
            padding (0, 0, 0, 0)

        text "[title]":
            xalign 0.5
            size 44
            color "#ffffff"
            bold True
            text_align 0.5

        frame:
            xalign 0.5
            xsize 400
            ysize 2
            background Solid("#c9748f")
            padding (0, 0, 0, 0)

        text "✦":
            xalign 0.5
            size 24
            color "#c9748f"
            at spin

    timer 2.5 action Hide("chapter_card")

transform chapter_card_anim:
    on show:
        linear 0 alpha 0.0
        ease 0.5 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0

screen quick_thought(text_str):
    zorder 80

    frame at bubble_pop:
        xalign 0.5
        yalign 0.22
        padding (30, 14, 30, 14)
        background Frame(Solid("#2a1a2299"), 30, 30, 30, 30)

        hbox:
            spacing 10
            yalign 0.5
            text "...":
                size 20
                color "#c9748f"
            text "[text_str]":
                size 24
                color "#d0e0f0"
                italic True
                yalign 0.5
            text "...":
                size 20
                color "#c9748f"
                yalign 0.5
    timer 2.0 action Hide("quick_thought")

screen mood_overlay(color_hex, strength="40"):
    zorder 5
    frame:
        xfill True
        yfill True
        background Solid(color_hex + strength)
        padding (0, 0, 0, 0)

transform mood_fade:
    on show:
        linear 0 alpha 0.0
        ease 1.0 alpha 1.0
    on hide:
        ease 0.8 alpha 0.0

screen impact_flash():
    zorder 200
    frame:
        xfill True
        yfill True
        background Solid("#ffffff")
        padding (0, 0, 0, 0)
    timer 0.08 action Hide("impact_flash")

transform flash_in:
    linear 0 alpha 1.0
    linear 0.08 alpha 0.0

style chapter_card_number:
    size 28
    color "#c9748f"
    italic True
    xalign 0.5

style chapter_card_title:
    size 48
    color "#ffffff"
    bold True
    xalign 0.5
