# A personal discord bot

instructions for myself:

### bot:
make application in https://discord.com/developers/applications

add bot to guild install scope in Installation tab of settings

use install link to add to server

add message content intent in Bot tab of settings (no need to reinstall)

change username/icon/banner as desired

### server:
```
cd /srv
git clone https://github.com/01-1/discordia.git
vi discordia/secrets.py # add secrets here
sudo apt install python3-discord # change for non-debian
sudo cp discordia/Discordia.service /etc/systemd/system/Discordia.service
sudo useradd discordia
sudo chown discordia discordia
sudo systemctl daemon-reload
sudo systemctl enable Discordia
sudo systemctl start Discordia
```
