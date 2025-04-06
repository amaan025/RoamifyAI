from google import genai

def prompt_json():
    prompt = """I am in Manchester, I have budget of 50 pounds, and I like arcade games and clubbing. Give me a plan of what should I do. Make sure the plan contains minimum travel between locations. Also give the co-ordinates of these locations.

    Give your response only using the JSON schema:

    Plan = {'Location 1': str, 'opening time': str, 'estimated spending': int,'lat':float, 'lon': float },
            {'Location 2': 'location_2': str, 'opening time': str, 'estimated spending': int, short description: str, 'lat':float, 'lon': float},
            ...}
    Return: list[Recipe]"""

    client = genai.Client(api_key="AIzaSyA64UDrH42FCnZUmsxEdpJwY1EMwXKaQ-I")

    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt,
    )

    # Use the response as a JSON string.
    return response.text

