def create_html_with_colors(colors):
    html_content = "<html><body><h1>Detected Colors</h1>"
    
    for color in colors:
        if color != "No color detected":
            html_content += f"<div style='width:100px; height:100px; background-color:{color}; margin:10px;'></div>"

    html_content += "</body></html>"
    return html_content

def save_html_file(content, filename='colors.html'):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"HTML file saved as {filename}")

