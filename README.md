# TelSök

Readme soon...

Make sure to set `GOOGLE_API_KEY` environment variable.


## Development
`cd` into directory and `direnv allow`. Everything should be installed and virtual environment should be created thanks to `nix`.

To run local dev environment, start server with `flask run`, add `--debug` for auto-reloading.

## Environments
Add `scraper/.env`.
```
MONGODB_URI=mongodb://root:example@webscrape-mongo:27017
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=600
HOSTNAME="localhost"
HOSTNAME_DEV="localhost"
```
https://github.com/jaypyles/Scraperr

Add `.env`.
```
GOOGLE_API_KEY="your_key"
```

## Build image

Three steps. Build image, load it into `docker` and start image.

```
nix build .#dockerImage && docker load < result && docker run -p 9191:9191 -t telsok:latest
```
