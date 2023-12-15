import requests
import json
from color import create_html_with_colors, save_html_file
import re

def get_light_color_and_music(emotion):
    api_key = 'sk-U8rQg1LkmQXjMwAH0351D50eFd134e1e96B64aC7059d9d60'  # key of api
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"I am currently feeling {emotion}. Can you suggest a light color or color combination that would either complement or help to soothe this emotion?"},
            {"role": "user", "content": "Also, could you recommend some music for this emotion from youtube ? Please provide a music link if possible."}
        ]
    }

    response = requests.post(
        "https://one.aiskt.com/v1/chat/completions",
        headers=headers,
        data=json.dumps(data)
    )
    return response.json()


def map_colors_to_hex(color_names, color_name_to_hex):
    # Convert color names to hex, discarding any that are not recognized
    colors_hex = [color_name_to_hex.get(color.lower(), '#000000') for color in color_names]
    return colors_hex


def extract_colors(text):
    # Predefined list of colors
    colors = [
        "red", "green", "blue", "yellow", "orange", "purple", "pink", "white", "black", "grey",
        "cyan", "magenta", "brown", "teal", "navy", "maroon", "beige", "olive", "lime", "aqua",
        "fuchsia", "coral", "mauve", "lavender", "indigo", "violet", "tan", "sienna", "gold",
        "silver", "bronze", "mint", "emerald", "turquoise", "sapphire", "amber", "charcoal",
        "ivory", "salmon", "plum"
    ]

    # Create a regular expression pattern to match any of the color words, allowing an optional 's' at the end
    pattern = r'\b(' + '|'.join(colors) + r')s?\b'

    # Find all unique color occurrences in the text using the pattern
    found_colors = re.findall(pattern, text, re.IGNORECASE)

    # Convert all found colors to lowercase and remove trailing 's' if present
    found_colors = set([color.lower().rstrip('s') for color in found_colors])

    # Return the list of found colors or ["No color detected"] if none are found
    return found_colors if found_colors else ["No color detected"]

color_name_to_hex = {
    "red": "#FF0000",
    "green": "#C9DDC5",
    "blue": "#CEE4FE",
    "yellow": "#FFF8C0",
    "orange": "#FFA500",
    "purple": "#A4AED4",
    "pink": "#FFC0CB",
    "white": "#FFFFFF",
    "black": "#000000",
    "grey": "#808080",
    "cyan": "#00FFFF",
    "magenta": "#FF00FF",
    "brown": "#A52A2A",
    "teal": "#008080",
    "navy": "#000080",
    "maroon": "#800000",
    "beige": "#F5F5DC",
    "olive": "#808000",
    "lime": "#00FF00",
    "aqua": "#00FFFF",
    "fuchsia": "#FF00FF",
    "coral": "#FF7F50",
    "mauve": "#E0B0FF",
    "lavender": "#B2A4D4",
    "indigo": "#4B0082",
    "violet": "#EE82EE",
    "tan": "#D2B48C",
    "sienna": "#A0522D",
    "gold": "#FFD700",
    "silver": "#C0C0C0",
    "bronze": "#CD7F32",
    "mint": "#A5FFD6",
    "emerald": "#50C878",
    "turquoise": "#40E0D0",
    "sapphire": "#0F52BA",
    "amber": "#FFBF00",
    "charcoal": "#36454F",
    "ivory": "#FFFFF0",
    "salmon": "#FA8072",
    "plum": "#DDA0DD",
    # Add any other colors you need to translate
}



print("-----------System Start to Collect Sensors Data----------------")
camera_data= input("1. Enter the camera data:") or "face_smile"
print("👌")
#120
speed_data= input("2. Enter the Speed data:") or "120"
print("👌")
#10
acceleration_data= input("3. Enter the acceleration data:") or "0"
print("👌")
#150
heartrate_data = input("4. Enter the heart rate data:") or "100"
print("👌")
#37
skin_temperature_data = input("5. Enter the skin temperature data:") or "34"
print("👌")
#100
voice_data = input("6. Enter the voice volume data:") or "70"


data_dict={
  'camera_data': camera_data,
  'speed_data': speed_data,
  'acceleration_data': acceleration_data,
  'heartrate_data': heartrate_data,
  'skin_temperature_data': skin_temperature_data,
  'voice_data': voice_data
}

print("-----------Collection Finished----------------")
print("")
print(data_dict)
print("")
print("-----------GPT Start to think----------------")
if(camera_data!="face_smile"):
    emotion="angry"
else:
    emotion="happy"

print("✅ GPT get the emotion:", emotion)
print("")
print("-----------System Start to visulize the effects----------------")
response = get_light_color_and_music(emotion)


if response.get('choices') and len(response['choices']) > 0:

    response = response['choices'][0]['message']['content']
    url_pattern = r'https?://www\.youtube\.com/watch\?v=[\w-]+'
    # youtube_links = re.findall(url_pattern, response)[0]
    youtube_links_dict = {
        "happy": "https://www.youtube.com/embed/BP5Jm5HAbiQ",
        "sad": "https://www.youtube.com/embed/UfcAVejslrU",  # Replace with the actual video ID for 'sad'
        "angry": "https://www.youtube.com/embed/UfcAVejslrU"  # Assuming this is the link for 'excited'
    }

    print("GPT Color Response:", response)
    colors = extract_colors(response)
    if colors == ["No color detected"]:
        print(f"No specific color detected for the emotion '{emotion}'.")
    else:
        colors_str = ", ".join(colors)
        print(f"The appropriate ambient light colors for '{emotion}' are: {colors_str}")
        colors_hex = map_colors_to_hex(colors, color_name_to_hex)
        html_content = create_html_with_colors(colors_hex, response,youtube_links_dict[emotion],emotion,data_dict)
        save_html_file(html_content)

    print("GPT Music Response:", youtube_links_dict[emotion])
else:
    print("No response or invalid response received.")



