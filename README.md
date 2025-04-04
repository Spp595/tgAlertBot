# Telegram Alert Bot

This is a simple bot designed to mention participants in a group or chat using the @all command


## Run

```shell
docker run -d \
  -e BOT_TOKEN="YouBotToken" \
  -e APIID="YouAppId" \
  -e APIHASH="YouApiHash" \
  sp595s/tgalertbot

```
## Docker Compose
```yaml
version: "3.7"
services:
  tgalertbot:
    image: sp595s/tgalertbot
    restart: unless-stopped
    environment:
      APIID: "YouAppId"
      APIHASH: "YouApiHash"
      BOT_TOKEN: "YouBotToken"
```

## Environment variables
`BOT_TOKEN:` bot token obtained from @BotFather

`APIID:` App api_id which can be obtained from [my.telegram.org/apps](https://my.telegram.org/apps)

`APIHASH:` App api_hash which can be obtained from [my.telegram.org/apps](https://my.telegram.org/apps)


## Build

```bash
git clone https://github.com/Spp595/tgAlertBot.git

cd tgAlertBot

docker build --rm --tag tgalertbot:latest .

docker run -e BOT_TOKEN="YouBotToken" -e APIID="YouAppId" -e APIHASH="YouApiHash" tgalertbot
```
