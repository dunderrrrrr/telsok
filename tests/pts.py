import requests


def test_pts_cookie():
    URL = "https://nummer.pts.se/NbrSearch"
    session = requests.Session()

    response = session.get(URL)
    cookie = session.cookies.get_dict()
    print(session.cookies.get_dict())

    token = cookie["__RequestVerificationToken"]

    cookie_str = [f"{k}={v};" for k, v in session.cookies.get_dict().items()]

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate, br, zstd",
        # "Accept-Language": "en-US,en;q=0.5",
        # "Connection": "keep-alive",
        # "Content-Length": "158",
        # "Content-Type": "application/x-www-form-urlencoded",
        # "Cookie": " ".join(cookie_str),
        # "Host": "nummer.pts.se",
        # "Origin": "https://nummer.pts.se",
        # "Priority": "u=1",
        # "Referer": "https://nummer.pts.se/NbrSearch",
        # "Sec-Fetch-Dest": "document",
        # "Sec-Fetch-Mode": "navigate",
        # "Sec-Fetch-Site": "same-origin",
        # "Sec-Fetch-User": "?1",
        # "TE": "trailers",
        # "Upgrade-Insecure-Requests": "1",
    }

    response = session.post(
        URL,
        data={
            # "__RequestVerificationToken": token,
            # "NbrToSearch": "0760531600",
        },
        json=""
        __RequestVerificationToken="i6fXmIb4C7B8FGG574eM3MslIrVBKAlqGg1J2rkRWqdHu4nGCDWIsWJcpx60eHiehKQsEidGdlrQB2NK4JPF9dPUlUaTLjHKu9qQNjd8gZ81",
        NbrToSearch="0760531600",
        cookies=session.cookies,
        headers=headers,
    )
    print(response)


if __name__ == "__main__":
    test_pts_cookie()
