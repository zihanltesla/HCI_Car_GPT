def create_html_with_colors(colors,contents):
    # Start building the HTML content with the head, including styles and keyframes for animations
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

    .side-container {
        display: flex;
        flex-direction: column;
        background: #e0e5ec;
        border-radius: 25px;
        align-items: center;
        justify-content: space-around;
        width: 500px; /* Adjust the width as needed */
        padding: 10px;
        box-shadow: 20px 20px 60px #bebebe, -20px -20px 60px #ffffff;
    }
    .container {
        background: #e0e5ec;
        border-radius: 25px;
        box-shadow: 20px 20px 60px #bebebe, -20px -20px 60px #ffffff;
        padding: 10px;
        width: 900px;
        height: 600px;
        display: flex;
        flex-direction: column;
    }

    .logo {
        background-image: url('open_ai.jpg');
        width: 400px;
        height: 120px;
        border-radius: 15px;
        }

    .header {
        text-align: center;
        margin-bottom: 20px;
    }

    .contents {
        text-align: center;
        margin-bottom: 20px;
        font-size: 10px;
        font-weight: light;
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
    .light-strip_side {
        position: absolute;
        top: 57%;
        left: 59%;
        width: 21%;
        height: 10px;
        background-color: red;
        animation: flowColors 3s infinite linear;
    }

    .light-strip_driver {
        position: absolute;
        top: 57%;
        left: 39%;
        width: 2.5%;
        height: 10px;
        background-color: red;
        animation: flowColors 3s infinite linear;
        }

    .light-strip-45 {
        position: absolute;
        background-color: red; /* Initial color similar to the strip */
        transition: background-color 0.5s ease; /* Smooth transition for hover effect */
        /* Position and size of the strip to match the image */
        top: 60%; /* Example position */
        left: 80%; /* Example position */
        width: 20%; /* Example width */
        height: 10px; /* Example height */
        transform: rotate(10deg); /* Rotate 45 degrees from horizontal */
        animation: flowColors 3s infinite linear;
        }

    .light-strip-135 {
        position: absolute;
        background-color: red; /* Initial color similar to the strip */
        transition: background-color 0.5s ease; /* Smooth transition for hover effect */
        /* Position and size of the strip to match the image */
        top: 60%; /* Example position */
        left: 10%; /* Example position */
        width: 10%; /* Example width */
        height: 10px; /* Example height */
        animation: flowColors 3s infinite linear;
        transform: rotate(171deg); /* Rotate 135 degrees from horizontal */
        }
    

    
    """

    # If colors are detected, create a keyframes animation
    if colors and colors != ["No color detected"]:
        # Define the keyframes based on the colors
        html_content += "@keyframes flowColors {"
        for i, color in enumerate(colors):
            percentage = i * (100 / len(colors))
            html_content += f"{percentage}% {{ background-color: {color}; }}"
        # Ensure the animation loops smoothly
        html_content += f"100% {{ background-color: {colors[0]}; }}"
        html_content += "}"

    # Close the style tag
    html_content += f"""
    </style>
    </head>
    <body>

    <div class="side-container">
        <div class="logo"></div>
        <div class="contents">
            <h1>{contents}</h1>
        </div>
    </div>

    <div class="container">
        <div class="header">
            <h1>Car Emotion Recognition System</h1>
        </div>
        <div class="image_container">
            <div class="car-image">
                <!-- Single light-strip element for the flowing color effect -->
                    <div class="light-strip_side"></div>
                    <div class="light-strip_driver"></div>
                    <div class="light-strip-45"></div>
                    <div class="light-strip-135"></div>
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


