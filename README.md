# Nuke Frame Add

A nuke gizmo which injects single new frames into a clip using Optical Flow.

## Use

This script was originally used to solve a specific problem for a sequence on All Eyez On Me. It can easily be extended to other similar use cases.

It also serves as a good template for extending the Nuke user interface through new gizmos and key bindings.

## Getting Started

Add everything in the `gizmos` folder to your `.nuke/gizmos` folder.

Repeat the same with the `python` folder from this project and your `.nuke/python` folder.

If you would like a button to immediately add a frame and add a keyboard shortcut, then append the contents of `menu.py` to `.nuke/menu.py`.

### Prerequisites

You will need a working Nuke installation with the Kronos plug-in.
