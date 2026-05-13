# Between Panels

## What It Is
A visual novel built in Ren'Py about a girl who wakes up inside a manhwa and slowly stops trying to get out. Story-driven with multiple routes, and choices that shape how the relationships develop.

## Why I Made It
I wanted to make something that felt like reading a manhwa but with actual player agency. The "protagonist who knows they're in a story" concept has always been interesting to me and I wanted to explore what happens when that character stops treating the world like a temporary situation and starts actually living in it.

## How I Made It

**Tech Stack:**
- Ren'Py

The route system branches at chapter 7 based on a `route` variable set by the player's choice, with affection tracking running in the background throughout. The notebook screen pulls from `add_observation()` whenever Soo-ah notices something significant about a character.

## What I Learnt And What I Struggled With
The biggest struggle was keeping the UI readable across different scene backgrounds. The dialogue box went through several iterations before landing on a dark semi-transparent background with light text. Managing a branching script across multiple files also got complicated fast. Jump targets broke whenever a file got renamed or restructured.

## Art Credits
None of the art in the story belong to me. All credits to wawawa_o_o_ on X! Got all the assests from https://picrew.me/en/image_maker/2308695.
