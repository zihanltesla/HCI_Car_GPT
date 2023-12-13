import requests
import json
from color import create_html_with_colors, save_html_file
import re

def get_light_color(emotion):
    api_key = 'sk-U8rQg1LkmQXjMwAH0351D50eFd134e1e96B64aC7059d9d60'  # 使用你的 API 密钥
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"I am currently feeling {emotion}. Can you suggest a light color or color combination that would either complement or help to soothe this emotion?"},
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

    # Create a regular expression pattern to match any of the color words
    pattern = r'\b(' + '|'.join(colors) + r')\b'

    # Find all unique color occurrences in the text using the pattern
    found_colors = re.findall(pattern, text, re.IGNORECASE)

    # Convert all found colors to lowercase to maintain uniformity and avoid duplicates like "Blue" and "blue"
    found_colors = set([color.lower() for color in found_colors])

    # Return the list of found colors or ["No color detected"] if none are found
    return found_colors if found_colors else ["No color detected"]

color_name_to_hex = {
    "red": "#FF0000",
    "green": "#008000",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
    "orange": "#FFA500",
    "purple": "#800080",
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
    "lavender": "#E6E6FA",
    "indigo": "#4B0082",
    "violet": "#EE82EE",
    "tan": "#D2B48C",
    "sienna": "#A0522D",
    "gold": "#FFD700",
    "silver": "#C0C0C0",
    "bronze": "#CD7F32",
    "mint": "#F5FFFA",
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
# 示例：发送一个请求
emotion = input("Enter your emotion: ")
response = get_light_color(emotion)

# 提取并打印氛围灯颜色

if response.get('choices') and len(response['choices']) > 0:
    color_response = response['choices'][0]['message']['content']
    print("GPTresponse:",color_response)
    colors = extract_colors(color_response)
    if colors == ["No color detected"]:
        print(f"No specific color detected for the emotion '{emotion}'.")
    else:
        colors_str = ", ".join(colors)
        print(f"The appropriate ambient light colors for '{emotion}' are: {colors_str}")
        colors_hex = map_colors_to_hex(colors, color_name_to_hex)
        html_content = create_html_with_colors(colors_hex, color_response)
        save_html_file(html_content)
else:
    print("No response or invalid response received.")



