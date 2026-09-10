#!/usr/bin/env python3
"""ASCII Terrarium - a tiny world of critters living in your terminal.

Run it:   python3 terrarium.py

Controls:
    q         quit
    f         drop a food pellet at a random spot
    g / s / m spawn a Guppy / Snail / Moth
    space     pause / resume

No third-party dependencies. Standard library only.
"""

import curses
import random
import time

import creatures

TICK = 0.08          # seconds per simulation step
FOOD_GLYPH = "."
STARVE_AFTER = 250   # ticks without eating before a critter gives up


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.critters = []
        self.food = set()
        self.tick = 0

    # -- spawning -----------------------------------------------------------
    def spawn(self, species_key):
        make = creatures.SPECIES[species_key]
        c = make()
        c["x"] = random.randint(1, self.width - 2)
        c["y"] = random.randint(1, self.height - 2)
        c["last_ate"] = self.tick
        self.critters.append(c)

    def drop_food(self):
        x = random.randint(1, self.width - 2)
        y = random.randint(1, self.height - 2)
        self.food.add((x, y))

    # -- queries ----------------------------------------------------------
    def nearest_food(self, x, y):
        if not self.food:
            return None
        return min(self.food, key=lambda p: (p[0] - x) ** 2 + (p[1] - y) ** 2)

    def occupied(self, x, y):
        return any(c["x"] == x and c["y"] == y for c in self.critters)

    # -- movement -------------------------------------------------------
    def move(self, critter, nx, ny):
        if nx < 1 or nx > self.width:
            return
        if ny < 1 or ny > self.height - 2:
            return
        critter["x"] = nx
        critter["y"] = ny
        if (nx, ny) in self.food:
            self.food.discard((nx, ny))
            critter["last_ate"] = self.tick

    # -- simulation ---------------------------------------------------
    def step(self):
        self.tick += 1
        for c in self.critters:
            if self.tick % c["speed"] == 0:
                c["behave"](c, self)
        for c in self.critters:
            if self.tick - c["last_ate"] > STARVE_AFTER:
                self.critters.remove(c)

    # -- census ------------------------------------------------------
    def census(self):
        counts = {}
        for c in self.critters:
            counts[c["name"]] = counts.get(c["name"], 0)
        return counts


def draw(stdscr, world):
    stdscr.erase()
    h, w = stdscr.getmaxyx()

    # border
    stdscr.border()

    # food
    for (x, y) in world.food:
        stdscr.addch(y, x, FOOD_GLYPH)

    # critters
    for c in world.critters:
        stdscr.addch(c["y"], c["x"], c["glyph"])

    # census panel
    line = "  ".join(f"{name}:{n}" for name, n in world.census().items())
    footer = f" tick {world.tick} | food {len(world.food)} | {line} "
    stdscr.addnstr(h - 1, 2, footer, w - 4)

    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    h, w = stdscr.getmaxyx()

    world = World(w - 1, h - 1)
    for _ in range(4):
        world.spawn("guppy")
    world.spawn("snail")
    for _ in range(6):
        world.drop_food()

    paused = False
    last = time.monotonic()

    while True:
        key = stdscr.getch()
        if key in (ord("q"), 27):
            break
        elif key == ord(" "):
            paused = not paused
        elif key == ord("f"):
            world.drop_food()
        elif key == ord("g"):
            world.spawn("guppy")
        elif key == ord("s"):
            world.spawn("snail")
        elif key == ord("m"):
            world.spawn("moth")

        now = time.monotonic()
        if not paused and now - last >= TICK:
            world.step()
            last = now

        draw(stdscr, world)
        time.sleep(0.01)


if __name__ == "__main__":
    curses.wrapper(main)
