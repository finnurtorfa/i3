# -*- coding: utf-8 -*-
# file:     i3pystatus
# author:   moparx     - http://moparx.com/configs
# last mod: 08/16/2014 - 10:55 EDT
# vim: set ai et fenc=utf-8 ft=python nu si sts=0 sw=4 ts=8 tw=0 :
# ----------------------------------------------------------------------

import subprocess

from i3pystatus import Status
from i3pystatus.mail import maildir
from i3pystatus.mail import Mail

status = Status(standalone=True)

#Clock
status.register("clock",
    format = " %a %_d %b %H:%M W%V", )

# Audio
status.register("alsa",
    format = " {volume} ",
    format_muted = " muted {volume} ", )

# Battery status
status.register("battery",
    format="{status} {consumption:.2f}W {percentage:.2f}% {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=5,
    status={
        "DIS": "↓",
        "CHR": "↑",
        "FULL": "=",
    },)

# CPU temperature
status.register("temp",
    format = " {temp:.0f}°C ", )

# Average load
status.register("cpu_usage",
    format = "CPU: {usage}",
    format_all = "CPU{core}: {usage}", )

# MPD status
status.register("mpd",
    format = "[ {status} {artist} - {title} ]",
    status = {
      "pause": "▷",
      "play": "▶",
      "stop": "◾",
    }, )

# Email
status.register("mail",
    format = " {unread} new email ",
    format_plural = " {unread} new emails ",
    color_unread = "#00FF00",
    email_client = "urxvtc -e mutt",
    backends = [
        maildir.MaildirMail(
            directory = "/home/fstorfa/.mail/inbox/INBOX"
        )
    ])
status.run()
