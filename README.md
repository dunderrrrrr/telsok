
# TelSök - Sök telefonnummer. Överallt!

[TelSök](https://telsök.se/) is a tool designed to facilitate the search for Swedish phone numbers across multiple search engines. It leverages APIs and performs web scraping on a variety of predefined search engines to gather comprehensive results. Whether you are trying to look up contact details for individuals or businesses, TelSök simplifies the process, saving you time and effort in your search endeavors.

## ✨ Features

Implemented search engines:

- Inabler (fetches data from PTS)
- Ratsit
- Eniro
- Google

![screenshot](https://i.imgur.com/k4rMMut.png)


## 💁‍♀️ How to use

All you need to do to play around locally with TelSök is to create two `env` files. When done, run `make start`.

- `.env`
  - This holds only the Google API key. It's not required, but Google search will be disabled if not set.
  ```
    GOOGLE_API_KEY=yOuR_kEy
  ```
- `scraper/.env`
  - Use defaults from [jaypyles/Scraperr](https://github.com/jaypyles/Scraperr).
  ```
    MONGODB_URI=mongodb://root:example@webscrape-mongo:27017
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=600
    HOSTNAME="localhost"
    HOSTNAME_DEV="localhost"
  ```
TelSök can be accessed at https://localhost:9191 and Scraperr backend at https://localhost:9292.

## 🛠️ Development

- Add `env` files, see above.
- Start scraping backend
  - `cd scraper && make up`
- Start main application
  - `flask run --debug`

There are also some usefull `make` commands used for production.

```
$ make help
Usage:
  make start     - Build and load docker image, run TelSök and Scraper backend
  make destroy   - Stop and destroy containers
  make build     - Only build and load docker image.
  make run       - Only run TelSök and Scraper backend.
```

## 📝 Notes

- Source repo: https://github.com/dunderrrrrr/telsok

