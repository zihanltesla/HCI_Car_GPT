from color import create_html_with_colors,save_html_file
data_dict={
  'camera_data': "smile",
  'speed_data': "smile",
  'acceleration_data': "smile",
  'heartrate_data': "smile",
  'skin_temperature_data': "smile",
  'voice_data': "smile"
}
html_content = create_html_with_colors(['#FF1001'], "If you're feeling angry and looking for a color to help soothe your emotions, try focusing on cool and calming colors. Light blue, such as baby blue or sky blue, is often associated with feelings of peace and tranquility. Light green, like mint or seafoam green, can also have a calming effect. Alternatively, combining light blue and light green in a color combination can create a refreshing and serene atmosphere.As for music, instntal tracks or genres that encourage relaxation and mindfulness can help in calming your anger. One example is by Marconi Union, which is a specially designed track known for its soothing qualities. Here's a link to the song on YouTube: https://www.youtube.com/watch?v=UfcAVejslrURemember that everyone's preferences and reactions to colors and music may vary, so these suggestions are not guaranteed to work for everyone. It's important to explore and find what resonates with you personally.The appropriate ambient light colors for 'angry' are: green, blue, mint","https://www.youtube.com/embed/BP5Jm5HAbiQ","angry",data_dict)
save_html_file(html_content)