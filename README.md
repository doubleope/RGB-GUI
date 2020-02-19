# RGBGUI

# How to run:

The following works on CentOS 7:

1. Clone the repository
2. sudo yum install docker
3. sudo systemctl start docker
4. sudo docker build -t rgb-app:latest .
5. sudo docker run -p 5000:5000 rgb-app
