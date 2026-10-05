# Slithering Robot Snake Prototype

A ten-link robot snake, about 0.95 m long, with nine yaw joints: a CAD assembly, robot description files, and a MuJoCo simulation where it slithers with lateral undulation, notices an obstacle with a range sensor, detours around it without touching it, and rejoins its route. Twelve tests check the geometry, joints, gait and clearance.

## How it was made

An AI agent made this. Codex built it in one recorded session, starting from the `$possible` skill: it asked what to build, how it should behave, where, and what result was wanted, then prepared a build pack. The answers in this recipe came from a scripted test run, not typed live. The agent used the text-to-cad and robotics skills listed below, MuJoCo for simulation and pytest for checks. Possible captured the session with `possible capture`; tool outputs and file contents are left out.

## What to know

This is a digital prototype. Propulsion in the simulation uses a surrogate, so real-world slithering, servo choice, friction, strength and manufacturability are unproven. The video and renders were regenerated from the session's own files after the originals were lost; link count, joints, tests and simulated distances match the session's report.
