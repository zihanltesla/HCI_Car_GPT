def create_html_with_colors(colors):
    html_content = """
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                text-align: center;
            }
            .header {
                background-color: #333;
                color: white;
                padding: 10px 0;
            }
            .color-container {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 20px;
            }
            .color-box {
                width: 100px;
                height: 100px;
                margin: 10px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                transition: transform 0.3s ease;
            }
            .color-box:hover {
                transform: translateY(-10px);
            }
            .car-interior {
                background-image: url('car-interior.jpg'); /* Placeholder for car interior background */
                background-size: cover;
                padding: 50px 0;
            }
            .light-strip {
                height: 20px;
                border-radius: 10px;
                margin-bottom: 5px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Detected Colors in Car Interior</h1>
        </div>
        <div class="car-interior">
            <div class="color-container">
    """

    for color in colors:
        if color != "No color detected":
            html_content += f"<div class='color-box' style='background-color:{color};'></div>"

    html_content += """
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

def save_html_file(content, filename='colors.html'):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"HTML file saved as {filename}")

