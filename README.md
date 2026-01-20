# TxMake UI

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![RenderMan](https://img.shields.io/badge/RenderMan-TxMake-red)
![VFX](https://img.shields.io/badge/VFX-Pipeline-black)
![Status: Paused](https://img.shields.io/badge/Status-Paused-lightgrey)

---

## What is TxMake UI?
**TxMake UI** is a lightweight Python-based tool that provides a simple interface for generating **RenderMan `.tex` textures** using Pixar’s **TxMake** command — without the need to open Houdini, Maya, or any DCC.

It allows artists and technical users to prepare textures **at the very beginning of the pipeline**, as a side task, independently from scene setup.

---

## The Problem It Solves
When working with RenderMan, creating `.tex` files often requires:
- Launching a DCC (Houdini / Maya)
- Context switching away from asset preparation
- Slowing down early lookdev or lighting workflows

During texture creation for RenderMan, this became a repeated friction point.  
TxMake UI was created to make texture conversion:
- Faster
- DCC-independent
- Available before any scene work begins

---

## How It Works
TxMake UI is a wrapper around Pixar RenderMan’s **TxMake** command-line tool.

It converts common image formats into optimized `.tex` files by calling `txmake` directly from the system, while exposing the process through a clean UI.

---

## Requirements
To use TxMake UI, **TxMake must be correctly installed and accessible from your system**.

### Verify TxMake Installation
Open a command prompt or terminal and run:
txmake

## Devices
✅ Windows (tested)

⚠️ macOS / Linux (not tested)

Project Status

## ⏸ On Hold

This project is currently not under active development and no further improvements are planned at this time.
The repository is kept as a portfolio and reference project.
