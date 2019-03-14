#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias ll='ls -la --color=auto'

PS1="\[\033[38;5;8m\][\[$(tput bold)\]\[\033[38;5;215m\]\W\[$(tput sgr0)\]\[$(tput sgr0)\]\[\033[38;5;8m\]]\[$(tput sgr0)\]\[\033[38;5;15m\]\\$ \[$(tput sgr0)\]"

#PS1='[\u@\h \W]\$ '


# wal settings
(cat ~/.cache/wal/sequences &)
source ~/.cache/wal/colors-tty.sh
