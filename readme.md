#Harmony

Harmony is a web application built to upload, analyze and visualize HTTP Archive (HAR) files. Using Harmony, users can see details about request type and size that may be impacting their site's performance. Harmony was developed by [Maria Moy] (http://www.linkedin.com/in/maria-k-moy) as a part of the Developer Week 2017 Hackathon.

##Contents
- Tech Stack
- Features
- Installation
- About Me

##Tech Stack

Backend: Python, Flask

Frontend: Javascript, jQuery, AJAX, HTML5, CSS3, Bootstrap

##Features

- Users can upload HAR files for analysis.

![upload page](https://github.com/Gerdie/harmony/blob/master/static/img/upload.png)

- Harmony will parse the file and graph the sum of all requests by Content-Type.

![doughnut chart](https://github.com/Gerdie/harmony/blob/master/static/img/donut.png)

- Harmony will analyze requests for their load size, and display a bar chart of all requests over 5000 bytes.

![bar chart](https://github.com/Gerdie/harmony/blob/master/static/img/bar.png)


##Installation


To create and activate a virtual environment:
```
virtualenv env
source env/bin/activate
```

To install the project's dependencies:
```
pip install -r requirements.txt
```

##About Me

Harmony was developed by Maria Moy. Find her on [LinkedIn]
(http://www.linkedin.com/in/maria-k-moy) or [GitHub]
(http://www.github.com/gerdie). Maria is a San Francisco-based software engineer at Radius Intelligence.