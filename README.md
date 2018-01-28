# fake-commit-bot
Fake commit bot automatically generates GitHub activity.

## How to?
Clone the repository.
Add the following line to your crontab (of course you can edit it if you want to)

0,30 21,22,23 * * * python /path/to/fake-commit-bot/bot.py

Don't forget that, at every execution chance of creating fake activity is 50%

## The idea
The idea is based on [commit-bot](https://github.com/theshteves/commit-bot). The difference is randomized call of shell script makes activity look more realistic.