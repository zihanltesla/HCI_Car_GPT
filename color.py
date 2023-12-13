def create_html_with_colors(colors):
    html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Car Emotion Recognition System</title>
        <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #e0e5ec;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background: #e0e5ec;
            border-radius: 25px;
            box-shadow: 20px 20px 60px #bebebe, -20px -20px 60px #ffffff;
            padding: 10px;
            width: 60%;
            height: 70%;
            display: flex;
            flex-direction: column;
            
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        .image_container {
            border-radius: 25px;
            width: 100%;
            height: 100%;
            position: relative; 
        }
        .car-image {
            background-image: url('car_inside.jpg'); /* Placeholder for car image */
            background-size: cover;
            height: 100%;
            border-radius: 15px;
        }

        .light-strip {
            position: absolute;
            background-color: red; /* Initial color similar to the strip */
            top: 57%; /* Example position */
            left: 59%; /* Example position */
            width: 21%; /* Example width */
            height: 10px; /* Example height */
            }

        </style>
        </head>


        <body>
        <div class="container">
        <div class="header">
            <h1>Car Emotion Recognition System</h1>
        </div>
            <div class="image_container">
            <div class="car-image">



                <div class="car-interior">
                """
    for color in colors:
                # If colors were detected, create light-strip divs with those colors
                if colors != ["No color detected"]:
                    for color in colors:
                        # Add each light-strip with the corresponding background color
                        html_content += f"<div class='light-strip' style='background-color:{color};'></div>"
                else:
                    # Default color if no specific colors were detected
                    html_content += "<div class='light-strip' style='background-color:red;'></div>"

                # Closing the car-interior div and the rest of the HTML content
                html_content += """
                    </div>

            </div>
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

