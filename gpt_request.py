import requests
import json
from color import create_html_with_colors, save_html_file

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
            {"role": "user", "content": f"I feel {emotion}. What would be a single appropriate ambient light color or color combination for this emotion?"},
        ]
    }

    response = requests.post(
        "https://one.aiskt.com/v1/chat/completions",
        headers=headers,
        data=json.dumps(data)
    )
    return response.json()

def extract_colors(text):
    # 预定义的颜色列表
    colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "white", "black", "grey", "cyan", "magenta", "brown", "teal", "navy", "maroon", "beige", "olive", "lime", "aqua", "fuchsia", "coral", "mauve", "lavender", "indigo", "violet", "tan", "sienna", "gold", "silver", "bronze", "mint", "emerald", "turquoise", "sapphire", "amber", "charcoal", "ivory", "salmon", "plum"]

    # 将文本分割成单词，并转换为小写
    words = text.lower().split()

    # 查找匹配的颜色并添加到列表中
    found_colors = []
    for word in words:
        if word in colors and word not in found_colors:
            found_colors.append(word)

    return found_colors if found_colors else ["No color detected"]

# 示例：发送一个请求
emotion = input("Enter your emotion: ")
response = get_light_color(emotion)

# 提取并打印氛围灯颜色

if response.get('choices') and len(response['choices']) > 0:
    color_response = response['choices'][0]['message']['content']
    colors = extract_colors(color_response)
    if colors == ["No color detected"]:
        print(f"No specific color detected for the emotion '{emotion}'.")
    else:
        colors_str = ", ".join(colors)
        print(f"The appropriate ambient light colors for '{emotion}' are: {colors_str}")
        html_content = create_html_with_colors(colors)
        save_html_file(html_content)
else:
    print("No response or invalid response received.")



