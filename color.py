def create_html_with_colors(colors,contents,music,emotion):
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
        margin-left: 20px;
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
        background-image: url('images/open_ai.jpg');
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
        background-image: url('images/car_inside.jpg'); /* Placeholder for car image */
        background-size: cover;
        height: 100%;
        border-radius: 15px;
    }

    .music-image {
        
        background-size: cover;
        height: 100%;
        border-radius: 15px;
    }

    .light-strip_side {
        position: absolute;
        top: 57%;
        left: 59%;
        width: 21.5%;
        height: 10px;
        background-color: red;
        animation: flowColors 3s infinite linear;
        border-radius: 5px;
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

    .light-strip_driver_below {
        position: absolute;
        top: 68%;
        left: 36.5%;
        width: 7.6%;
        height: 10px;
        background-color: red;
        animation: flowColors 3s infinite linear;
        border-radius: 5px;
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
        border-radius: 5px;
        }

    .light-strip-135 {
        position: absolute;
        background-color: red; /* Initial color similar to the strip */
        transition: background-color 0.5s ease; /* Smooth transition for hover effect */
        /* Position and size of the strip to match the image */
        top: 60%; /* Example position */
        left: 10%; /* Example position */
        width: 9.5%; /* Example width */
        height: 10px; /* Example height */
        animation: flowColors 3s infinite linear;
        transform: rotate(171deg); /* Rotate 135 degrees from horizontal */
        border-radius: 5px;
        }
        
    .light-strip_side_below {
        position: absolute;
        top: 73%;
        left: 56.5%;
        width: 12.5%;
        height: 10px;
        background-color: red;
        animation: flowColors 3s infinite linear;
        border-radius: 5px;
    }

    .light-strip-45_below {
        position: absolute;
        background-color: red; /* Initial color similar to the strip */
        transition: background-color 0.5s ease; /* Smooth transition for hover effect */
        /* Position and size of the strip to match the image */
        top: 79%; /* Example position */
        left: 66.5%; /* Example position */
        width: 7.5%; /* Example width */
        height: 10px; /* Example height */
        transform: rotate(70deg); /* Rotate 45 degrees from horizontal */
        animation: flowColors 3s infinite linear;
        border-radius: 5px;
    }

    .music-monitor {
        position: absolute;
        top: 54.5%;
        left: 50.3%;
        background-color: #ffffff;
        transform: translate(-50%, -50%);
        width: 145px;  /* Or the width of the screen in the car image */
        height: 90px;  /* Or the height of the screen in the car image */
        box-shadow: 0px 0px 10px #888888;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #333333;
        font-size: 20px;
        overflow: hidden; /* This will hide the overflow from the iframe */
    }

    .music-monitor-image {
        background-image: url('images/monitor_sad.jpg');
        background-size: cover; /* This will ensure that the image covers the entire area */
        background-repeat: no-repeat;
        background-position: center;
        width: 100%;
        height: 100%;
        position: absolute; /* This positions the image absolutely within the music-monitor div */
    }

    .logo-image {
        background-image: url('images/car_logo.jpg');
        background-size: contain; /* This will ensure the entire image fits within the area */
        background-repeat: no-repeat;
        background-position: center;
        width: 8%;
        height: 8%;
        top: 52%;
        left: 25%;
        position: absolute;
        border-radius: 5px;
    }

    .music-monitor-iframe {
        position: absolute; /* Position the iframe absolutely within the music-monitor-image */
        top: 66%;  /* Center vertically */
        left: 50%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset the iframe by half its width and height */
        width: 20px;
        height: 10px; /* Adjust height as needed */
        border-radius: 5px;
    
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
                    <div class="light-strip_driver_below"></div>
                    <div class="light-strip-45"></div>
                    <div class="light-strip-135"></div>
                    <div class="light-strip_side_below"></div>
                    <div class="light-strip-45_below"></div>
                    <div class="music-monitor">
                        <div class="music-monitor-image">
                                <iframe class="music-monitor-iframe" src="{music}?autoplay=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                        </div>
                        
                    </div>
            </div>
        </div>
    </div>

    """
    js_content = f"""
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            var emotion = '{emotion}';
            var musicMonitorImage = document.querySelector('.music-monitor-image');
            if (musicMonitorImage) {{
                musicMonitorImage.style.backgroundImage = 'url(images/monitor_' + emotion + '.jpg)';
            }}
        }});
    </script>
    """
    html_content += f"""
    </body>
    {js_content}
    </html>
    """
    
    return html_content


def save_html_file(content, filename='colors.html'):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"HTML file saved as {filename}")

if __name__ == '__main__':
   colors = ["red", "blue", "green"]
   contents = "You are feeling sad"
   emotion = "https://open.spotify.com/embed/track/4uLU6hMCjMI75M1A2tKUQC"
   html = create_html_with_colors(colors,contents,emotion)
   save_html_file(html)


