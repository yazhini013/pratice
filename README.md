# ASCII Terrarium

A practice repo for learning to drive a coding agent like opencode.

The code is a small terminal toy: ASCII critters wander a fenced tank,
chase food pellets, and starve if they do not eat. It is written in plain
Python with no dependencies, so there is nothing to install and the whole
thing fits in two short files. That keeps the focus on the workflow, not
on the codebase.

It ships with four bugs and two feature requests, filed as GitHub issues.
You fix them with the agent. The bugs are real and reproducible, not
`# TODO` comments, and they are spread across different functions so a
group can each take one without colliding.

## Run it

```
python3 terrarium.py
```

Needs Python 3 and the `curses` module, which is in the standard library
on Linux and macOS. On Windows use WSL.

| key | action |
|-----|--------|
| `q` | quit |
| `f` | drop a food pellet |
| `g` / `s` / `m` | spawn a Guppy / Snail / Moth |
| `space` | pause / resume |

## The files

- `terrarium.py` is the world, the simulation loop, and the curses drawing
- `creatures.py` is one small function per species, with a comment at the
  top explaining how to add your own

## Suggested order

1. Open the repo with your agent and run `/init`. Read the `AGENTS.md` it
   writes and correct anything it got wrong. That is issue #1.
2. Pick an issue. Start with the ones tagged `good first issue`.
3. Ask the agent to reproduce the bug first, then fix it, then confirm the
   fix. Watch what it does and push back when it goes sideways.

`TASKS.md` has the same list as the issues if you want it in one file.
yazhini

