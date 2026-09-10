"""Creature definitions for the Terrarium.

Each creature is a plain dict-factory. Want to add your own critter?
Write a function that returns a dict with these keys and register it in
SPECIES at the bottom. That's the whole contract.

    name    : str   - shown in the census panel
    glyph   : str   - single character drawn on screen
    speed   : int   - ticks between moves (1 = fast, 5 = sluggish)
    behave  : func  - (self, world) -> None, called when it's time to move
"""

import random


def _wander(self, world):
    """Move one step in a random direction, most of the time."""
    if random.random() < 0.15:
        return  # take a breather
    dx, dy = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
    world.move(self, self["x"] + dx, self["y"] + dy)


def _chase_food(self, world):
    """Head toward the nearest pellet; wander if there is none."""
    target = world.nearest_food(self["x"], self["y"])
    if target is None:
        return _wander(self, world)
    tx, ty = target
    dx = (tx > self["x"]) - (tx < self["x"])
    dy = (ty > self["y"]) - (ty < self["y"])
    world.move(self, self["x"] + dx, self["y"] + dy)


def guppy():
    return {"name": "Guppy", "glyph": "@", "speed": 1, "behave": _chase_food}


def snail():
    return {"name": "Snail", "glyph": "e", "speed": 5, "behave": _wander}


def moth():
    return {"name": "Moth", "glyph": "*", "speed": 2, "behave": _wander}


SPECIES = {
    "guppy": guppy,
    "snail": snail,
    "moth": moth,
}
