I did the homework with the following steps:
1. Created simple static profile by basic-profile.html, style.css and avatar.JPG.
2. Wrote basic-app.py to serve to frontend in static folder using app.send_static_file().
3. For advanced part, firstly I created advanced-profile.html based on basic-profile.html but I added a variable called "view" to indicate the number of views. Then I used render_template() to render advanced-profile.html with random "view" variable.
4. To configure github page firstly I pushed all files to a github repository. Then I went to Pages >> Build and deployment >> Deploy from a branch >> main >> /root and saved the options. Because github page only read the html file in root directory, I created addition index.html in root directory to link to the basic-profile.html in static folder. Now we can go to https://tvtra.github.io/tvtra/ and see the result.