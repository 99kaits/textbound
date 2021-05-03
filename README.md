# Starman III
markov chain text generator that generates nonsense text vaguely resembling earthbound (with a web frontend!! wow!!!!)

https://starman-iii.herokuapp.com/

## how to use
- clone the repo or download it as a zip
- run `pip install -r requriements`(preferably in a venv)
- run `gunicorn main:app`
- open a web browser to `http://localhost:8000`
- refresh the page for new text

## discord bot
yeah i got a discord bot now B^)
also on heroku here: https://discord.com/oauth2/authorize?client_id=610159887619719179&scope=bot&permissions=52224
if it doesnt work try going to the heroku site above, free tier puts it to sleep sometimes :((((
you can run your own by doing the first two steps above and then
- put your discord bot token in `token.txt`, you can get this at the developer portal
- make a link and invite it into your server (google can help here!)
- run `python bot.py`
- profit

## credits
script dump from https://earthboundcentral.com/misc/script.htm
