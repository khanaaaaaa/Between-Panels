default observations = {}

init python:
    def add_observation(character, text):
        if character not in observations:
            observations[character] = []
        if text not in observations[character]:
            observations[character].append(text)

screen notebook():
    zorder 200
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 700
        background Frame(Solid("#fdf6ee"), 20, 20, 20, 20)
        padding (0, 0, 0, 0)

        frame:
            xsize 18
            yfill True
            xpos 0
            ypos 0
            background Solid("#c9748f")
            padding (0, 0, 0, 0)

        vbox:
            xpos 40
            ypos 30
            xsize 840
            spacing 0

            hbox:
                xfill True
                ysize 60
                spacing 0
                text "✦ Soo-ah's Observations ✦":
                    size 30
                    color "#3a2a32"
                    bold True
                    xalign 0.0
                    yalign 0.5
                textbutton "✕":
                    action Hide("notebook")
                    xalign 1.0
                    yalign 0.5
                    padding (10, 6, 10, 6)
                    background Frame(Solid("#c9748f"), 20, 20, 20, 20)
                    hover_background Frame(Solid("#e8a0bf"), 20, 20, 20, 20)
                    text_style = "skip_button_text"

            frame:
                xfill True
                ysize 2
                background Solid("#c9748f80")
                padding (0, 0, 0, 0)

            viewport:
                xsize 840
                ysize 580
                scrollbars "vertical"
                mousewheel True
                yinitial 0.0

                vbox:
                    xsize 820
                    spacing 24
                    ypos 20

                    if not observations:
                        text "( nothing written yet... )":
                            size 22
                            color "#9a6a8a"
                            italic True
                            xalign 0.5
                    
                    for character, entries in observations.items():
                        vbox:
                            spacing 8
                            xsize 820

                            frame:
                                xsize None
                                ysize None
                                padding (20, 6, 20, 6)
                                background Frame(Solid("#c9748f"), 20, 20, 20, 20)
                                text character:
                                    size 22
                                    color = "#ffffff"
                                    bold True

                            for entry in entries:
                                hbox:
                                    spacing 10
                                    xsize 800
                                    text "-":
                                        size 20
                                        color "#c9748f"
                                        yalign 0.0
                                    text entry:
                                        size 22
                                        color "#3a2a32"
                                        italic True
                                        xmaximum 760
                                        line_spacing 6