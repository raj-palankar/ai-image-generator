import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        self.API_KEY = os.getenv("GEMINI_API_KEY")
        # self.API_KEY = ""

    def generate_image(self, prompt, style="No specific style"):
        try:
            response = requests.post(
                "https://clipdrop-api.co/text-to-image/v1",
                headers={
                    "x-api-key": self.API_KEY
                },
                files={
                    "prompt": (None, prompt)
                }
            )

            # ❗ Error check
            if response.status_code != 200:
                return False, response.text

            # Convert image to base64
            img_base64 = base64.b64encode(response.content).decode()

            return True, img_base64

        except Exception as e:
            return False, str(e)

    def generate_prompt_suggestions(self, category=None):
        return [
            "A cyberpunk city at night",
            "A futuristic robot",
            "A dragon flying in the sky",
            "A realistic human portrait",
            "A fantasy world landscape"
        ]