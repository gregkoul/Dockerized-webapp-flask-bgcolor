# Dockerized-webapp-flask-bgcolor
This is a simple flask webapp that displays a colored background and a greeting message. 
The color can be specified in two different ways:

  1. As a command line argument with --color as the argument. Accepts one of the following colors according the list below.
  2. As an Environment variable APP_COLOR. Accepts one of the following colors according the list below.
    
In any other case, a random color is picked from the list below.

Note 1: Accepted colors ["red", "green", "blue", "olive", "purple", "navy"]    
Note 2: Command line argument precedes over environment variable.

# Follow these steps in order to create your Dockerized-webapp-flask-bgcolor

1. First of all you have to clone this repository on your server.
```bash
    -$ mkdir -p ~/MyProjects
    -$ cd ~/MyProjects
    -$ git clone https://github.com/gregkoul/Dockerized-webapp-flask-bgcolor.git
                      OR via SSH
    -$ git clone git@github.com:gregkoul/Dockerized-webapp-flask-bgcolor.git
```
2. Now you have to build the Docker Image locally.
```bash
    -$ cd ~/MyProjects/Dockerized-webapp-flask-bgcolor
    -$ docker build . -t gregkoul/webapp-flask-bgcolor:1.0
```
3. Now you have to spin up as many containers you want in different ports.

Blue color with environmental variable:
```bash
    -$ docker run -p 8000:8000 -e APP_COLOR=blue gregkoul/webapp-flask-bgcolor:1.0
```
Navy color with command line argument:
```bash
    -$ docker run -p 8001:8000 gregkoul/webapp-flask-bgcolor:1.0 --color=navy
```
Random color without any command line argument nor environmental variable.
```bash
    -$ docker run -p 8002:8000 gregkoul/webapp-flask-bgcolor:1.0
```
