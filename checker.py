import requests


class LanguageToolChecker:
    def __init__(self, server_url="http://localhost:8081", language="en-US"):
        self.server_url = server_url.rstrip("/")
        self.language = language
        self.endpoint = f"{self.server_url}/v2/check"

    def check(self, text):
        """
        Send text to LanguageTool and return the matches.
        """
        response = requests.post(
            self.endpoint,
            data={
                "text": text,
                "language": self.language,
            },
        )

        response.raise_for_status()

        data = response.json()
        return data["matches"]