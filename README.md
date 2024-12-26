# A personal discord bot

instructions for myself:

### bot:
make application in https://discord.com/developers/applications
add bot to guild install scope in Installation tab of settings
use install link to add to server
add message content intent in Bot tab of settings (no need to reinstall)
change username/icon/banner as desired

### server:
place in /srv (/srv/discordia)
copy over secrets.py
`useradd discordia`
`chown discordia discordia`
copy over Discordia.service to `/etc/systemd/system/Discordia.service`
`apt install python3-discord`
`sudo systemctl daemon-reload`
`sudo systemctl enable Discordia`
`sudo systemctl start Discordia`
