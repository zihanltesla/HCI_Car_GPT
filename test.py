from color import create_html_with_colors,save_html_file
data_dict={
  'camera_data': "smile",
  'speed_data': "smile",
  'acceleration_data': "smile",
  'heartrate_data': "smile",
  'skin_temperature_data': "smile",
  'voice_data': "smile"
}
html_content = create_html_with_colors(['#FF1001'], "aaaaa","https://www.youtube.com/embed/BP5Jm5HAbiQ","angry",data_dict)
save_html_file(html_content)