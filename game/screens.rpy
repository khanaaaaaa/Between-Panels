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

    frame:
        xalign 0.97
        yalign 0.08
        xsize 420
        ysize 180
        padding (0, 0, 0, 0)
        background None

        fixed:
            xsize 420
            ysize 180

            frame:
                xsize 420
                ysize 180
                xpos 0
                ypos 0

            frame:
                xisize 390
                ysize 155
                xpos 15
                ypos 13
                background Solid("#f8f0f5")

            frame:
                xsize 390
                ysize 28
                xpos 15
                ypos 13
                background Solid("#2d1b2e")

            text "● ● ●":
                xpos 25
                ypos 17
                size 8
                color: "#c9748f"

            text "9:02 AM":
                xpos 310
                ypos 17
                size 10
                color "#e8c4d4"

            frame:
                xsize 36
                ysize 36
                xpos 25
                ypos 25
                ypos 52
                background Solid("#c9748f")

            text "✉":
                xpos 32
                ypos 56
                size 20
                color "#ffffff"

            text"[sender]":
                xpos 72
                ypos 52
                size 18
                color "#3a2a32"
                bold True

            text"[message]":
                xpos 72
                ypos 76
                xmaximum 310
                size 15
                color "#7a5c6e"

            frame:
                xsize 80
                ysize 4
                xpos 170
                ypos 162
                background Solid("#c9748f")

        frame:
            xalign 0.97
            yalign 0.08
            xoffset 8
            yoffset 30
            xsize 6
            ysize 30
            background Solid("#111122")

        frame:
            xalign 0.97
            yalign 0.08
            xoffset 8
            yoffset 68
            xsize 6
            ysize 30
            background Solid("#111122")

transform phone_slide_in():
    xoffset 460 alpha 0
    ease 0.4 xoffset 0 alpha 1.0

transform phone_slide_out():
    xoffset 0 alpha 1.0
    ease 0.3 xoffset 460 alpha 0.0