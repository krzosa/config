#!/bin/bash
WINDOW=$(xdotool search --name __scratchpad)
sstr="$1 $2 $3
"
xdotool type --delay 0 --clearmodifiers --window $WINDOW "$sstr"

