# We will create a basic HTML structure with inline CSS to mimic the neumorphic design and functionality described in the uploaded image. 
# Note: This will be a static example and will not have the full interactive capabilities without JavaScript.

html_template = """
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
      transition: background-color 0.5s ease; /* Smooth transition for hover effect */
      /* Position and size of the strip to match the image */
      top: 57%; /* Example position */
      left: 59%; /* Example position */
      width: 21%; /* Example width */
      height: 10px; /* Example height */
    }
    
  .light-strip-45 {
  position: absolute;
  background-color: red; /* Initial color similar to the strip */
  transition: background-color 0.5s ease; /* Smooth transition for hover effect */
  /* Position and size of the strip to match the image */
  top: 57%; /* Example position */
  left: 80%; /* Example position */
  width: 21%; /* Example width */
  height: 10px; /* Example height */
  transform: rotate(25deg); /* Rotate 45 degrees from horizontal */
}

.light-strip-135 {
  position: absolute;
  background-color: red; /* Initial color similar to the strip */
  transition: background-color 0.5s ease; /* Smooth transition for hover effect */
  /* Position and size of the strip to match the image */
  top: 57%; /* Example position */
  left: 5%; /* Example position */
  width: 15%; /* Example width */
  height: 10px; /* Example height */
  transform: rotate(160deg); /* Rotate 135 degrees from horizontal */
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
        <div class="light-strip"></div>
        <div class="light-strip-45"></div>
        <div class="light-strip-135"></div>
      </div>
    </div>
  
</div>
</body>
</html>
"""

# Save the HTML content to a file
filename = 'car_emotion_recognition_system.html'
with open(filename, 'w') as file:
    file.write(html_template)
