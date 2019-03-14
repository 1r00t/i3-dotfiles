#!/bin/bash

wal -i $HOME/Wallpapers/ -a 90
feh --bg-fill "$(< "${HOME}/.cache/wal/wal")"
python $HOME/.config/sublime-text-3/pywal_sublime.py
i3-msg restart
