# TelSök

Readme soon...

Make sure to set `GOOGLE_API_KEY` environment variable.


## Development
`cd` into directory and `direnv allow`. Everything should be installed and virtual environment should be created thanks to `nix`.

To run local dev environment, start server with `flask run`, add `--debug` for auto-reloading.

## Build image

Three steps. Build image, load it into `docker` and start image.

```
nix build .#testBuild && docker load < result && docker run -p 9191:9191 -t telsok:latest
```
