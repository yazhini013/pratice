# Tasks

Do these with your agent. Small, self-contained, no dependency changes.

## 0. Warm-up: run `/init`

Have the agent generate `AGENTS.md` for this repo and skim it. Fix anything
it got wrong about how the project works.

## 1. Bug: critters escape through the right wall

Spawn a bunch of guppies (`g` a few times), drop food near the right edge
(`f`), and watch. Sometimes a critter walks off the edge and the program
crashes with a curses error. Find out why and fix it so critters stay
inside the border.

_Hint: look at `World.move`._

## 2. Bug: the census panel always shows 0

The footer says `Guppy:0  Snail:0` no matter how many are swimming around.
The count should be real.

_Hint: `World.census`._

## 3. Bug: guppies swim to the wrong food

Guppies are supposed to head for the **nearest** pellet. Drop one pellet
far to the side and one just below a guppy - it often picks the far one.

_Hint: `World.nearest_food` - how is "nearest" measured?_

## 4. Feature: add a new creature

Add a species to `creatures.py` and register it in `SPECIES`. Give it a
key so it can be spawned with a keypress in `terrarium.py`. Make its
behaviour do something the others don't (flee from critters? sit still and
grow? split in two?).

## 5. Stretch: creatures get hungry visibly

Right now a critter silently vanishes after `STARVE_AFTER` ticks. Make
hunger visible - dim the glyph, change it, or show a count in the footer -
so you can see who is about to starve.
