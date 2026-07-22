import os
import time
from google import genai


class GeminiService:
    """
    Shared Gemini client for the entire application.

    Handles:
    - API key loading
    - retries
    - model fallback
    - friendly error handling
    """

    MODELS = [
        "gemini-3.5-flash",
        "gemini-3.5-flash-lite",
    ]

    MAX_RETRIES = 3

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise EnvironmentError(
                "GEMINI_API_KEY was not found in the environment."
            )

        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str) -> str:

        last_error = None

        for model in self.MODELS:

            for attempt in range(self.MAX_RETRIES):

                try:

                    response = self.client.models.generate_content(
                        model=model,
                        contents=prompt,
                    )

                    if response.text:
                        return response.text

                    raise RuntimeError("Gemini returned an empty response.")

                except Exception as e:

                    last_error = e
                    error_text = str(e)

                    temporary_error = any(
                        code in error_text
                        for code in [
                            "503",
                            "UNAVAILABLE",
                            "429",
                            "RESOURCE_EXHAUSTED",
                        ]
                    )

                    if temporary_error:

                        time.sleep(2 ** attempt)
                        continue

                    raise

        raise RuntimeError(
            f"""
Google Gemini is temporarily unavailable.

Please try again in a few moments.

Last Error:

{last_error}
"""
        )