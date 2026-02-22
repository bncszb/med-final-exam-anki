from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_URL: str = "https://aok.zarovizsga.hu/zvb-service/methods"
    JSESSIONID: str = ""
    COLLECTION_ID: int = 26
    TEST_RUN: bool = False

    class Config:
        env_file = ".env"


settings = Settings()

HEADERS = {
    "Accept": "application/json",
    "Accept-Language": "hu,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Cookie": f"JSESSIONID={settings.JSESSIONID}; zvSchoolId=1;",
    "Origin": "https://aok.zarovizsga.hu",
    "Referer": "https://aok.zarovizsga.hu/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
}
