#!/bin/bash

# Check if a filename is provided as an argument
if [ "$#" -eq 0 ]; then
    # No arguments, use git diff
    git diff | python cr.py
else
    # Use the provided file as the diff
    python cr.py "$1"
fi
