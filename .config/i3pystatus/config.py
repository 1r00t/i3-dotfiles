from i3pystatus import Status
from get_colors import colors

special = colors["special"]
colors = colors["colors"]

status = Status(logfile='$HOME/.config/i3pystatus/log.txt')

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    hints = {"markup": "pango", "separator_block_width": 0, "separator": False},

    format = f"<span color='{colors['color2']}' background='{colors['color3']}'>\ue0ba</span>" +\
             f"<span color='{special['background']}' background='{colors['color2']}'> \uf455 %d.%m.%y </span>" +\
             f"<span color='{colors['color1']}' background='{colors['color2']}'>\ue0ba</span>" +\
             f"<span color='{special['background']}' background='{colors['color1']}'> \uf64f %H:%M </span>"

    #format = "%A %d %b %y - %X"
)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load",
    hints = {"markup": "pango", "separator_block_width": 0, "separator": False},
    format = f"<span color='{colors['color3']}' background='{colors['color4']}'>\ue0ba</span>" +\
             f"<span color='{special['background']}' background='{colors['color3']}'> \ue266 {{avg1}} </span>"
)

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    hints = {"markup": "pango", "separator_block_width": 0, "separator": False},
    format = f"<span color='{colors['color4']}' background='{colors['color5']}'>\ue0ba</span>" +\
             f"<span color='{special['background']}' background='{colors['color4']}'> \uf2c9 {{temp:.0f}}°C </span>"
)

# The battery monitor has many formatting options, see README for details

# This would look like this, when discharging (or charging)
# ↓14.22W 56.15% [77.81%] 2h:41m
# And like this if full:
# =14.22W 100.0% [91.21%]
#
# This would also display a desktop notification (via D-Bus) if the percentage
# goes below 5 percent while discharging. The block will also color RED.
# If you don't have a desktop notification demon yet, take a look at dunst:
#   http://www.knopwob.org/dunst/
status.register("battery",
    hints = {"markup": "pango", "separator_block_width": 0, "separator": False},
    format = f"<span color='{special['background']}' background='{colors['color5']}'>{{percentage:.0f}}% </span>",

    #format="{status}/{consumption:.2f}W {percentage:.2f}% [{percentage_design:.2f}%] {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=15,
)

status.register("battery",
    hints = {"markup": "pango", "separator_block_width": 0, "separator": False},
    format = f"<span color='{colors['color5']}' background='{colors['color6']}'>\ue0ba</span>" +\
             f"<span color='{special['background']}' background='{colors['color5']}'> {{glyph}} {{status}}</span>",

    glyphs = "\uf244\uf243\uf242\uf241\uf240",
    status={
        "DPL": "",
        "DIS": "\ufba4",
        "CHR": "\ufba3",
        "FULL": "",
    },
)

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
status.register("network",
    interface = "enp2s0",
    hints = {"markup": "pango", "separator_block_width": 0, "separator": False},
    color_up = f"{special['foreground']}",
    format_up = f"<span color='{colors['color6']}' background='{colors['color7']}'>\ue0ba</span>" +\
                f"<span color='{special['background']}' background='{colors['color6']}'> \uf700 {{v4cidr}} </span>",
    format_down = "",


)

# Note: requires both netifaces and basiciw (for essid and quality)
status.register("network",
    interface="wlp3s0",
    hints = {"markup": "pango", "separator_block_width": 0, "separator": False},
    color_up = f"{special['foreground']}",
    format_up = f"<span color='{colors['color6']}' background='{colors['color7']}'>\ue0ba</span>"+\
                f"<span color='{special['background']}' background='{colors['color6']}'> \uf1eb {{essid}} </span>",
    format_down = "",

)

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    hints = {"markup": "pango", "separator_block_width": 0, "separator": False},
    path="/",
    format = f"<span color='{colors['color7']}' background='{colors['color8']}'>\ue0ba</span>" +\
             f"<span color='{special['background']}' background='{colors['color7']}'> \ue706 {{avail}}G </span>",
    #format="{used}/{total}G [{avail}G]",
)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    step = 5,
    hints = {"markup": "pango", "separator_block_width": 0, "separator": False},
    #format="\ufa7d {volume}%",
    format = f"<span color='{colors['color8']}' background='{special['background']}'>\ue0ba</span>" +\
             f"<span color='{special['background']}' background='{colors['color8']}'> \ufa7d {{volume}}% </span>",
    format_muted = f"<span color='{colors['color8']}' background='{special['background']}'>\ue0ba</span>" +\
                   f"<span color='{special['background']}' background='{colors['color8']}'> \ufa80 {{volume}}% </span>",
)

# Shows mpd status
# Format:
# Cloud connected▶Reroute to Remain
status.register("mpd",
    format="{title}{status}{album}",
    status={
        "pause": "▷",
        "play": "▶",
        "stop": "◾",
    },)

status.run()