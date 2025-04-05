import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(api_key="AIzaSyA64UDrH42FCnZUmsxEdpJwY1EMwXKaQ-I")

    model = "gemini-2.5-pro-preview-03-25"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a outing planner. Your task is to engage in conversation with user. Once the greetings is done. You will ask the user their location. Then you will ask them what type of outing they prefer. Then you will ask them their budget. Based on their responses, you will create a plan for them that meets their criteria. You need to make sure that the user do not have to travel much and the locations are near to each other and convinient. I need small but friendly responses. After the response you will ask if you want a map with these locations."""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
