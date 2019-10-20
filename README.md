# Chess-Scraper

**Please check the 'Screenshots for AWS usage' folder for the output.**

# What is this?

This a web scraper that utilizes Beautiful Soup 4 python library to parse and extract data from multiple websites that list top ranking chess players in the world (both chess and chinese chess). 

'https://en.wikipedia.org/wiki/FIDE_world_rankings'

'http://www.01xq.com/xqplayer/xqrating.asp'


# My Thoughts/What I learned:

Although this is a relatively simple program, my goal for this project is to actually learn how Docker and AWS ECS/Fargate works in the process. By creating a simple, yet practical sample program, I was able to apply a lot of the concepts to good use.

The major goal of this project in my portfolio is to learn Docker, and how to build and deploy Docker images (e.g. a multi-stage build found here https://docs.docker.com/develop/develop-images/multistage-build/). After a lot of tinkering and trial and error I finally got it to work and the total image size was 1.83 GB. The challenge was that this project uses both python libaries and node.js modules; the docker image needed an "intermediate" build to process the python files first, and then set the node.js file as the main container. 

Thanks to AWS, I was able to upload this local docker image to the cloud using AWS ECR, so that it can be found when I actually deploy the docker container at ECS/Fargate (see screenshots of a working task completed successfully in the github folder called Screenshots for AWS usage). To prevent any additional charges using AWS products, I deleted the Fargate task and the cluster as well in the end.


Docker Image can be found at Docker Hub here: 
https://hub.docker.com/r/br14nbrlam/node-python-chess
or run the command from Docker CLI: docker pull br14nbrlam/node-python-chess


# Credits

-AWS ECR from Amazon

-AWS ECS/Fargate from Amazon

-Beautiful Soup from Leonard Richardson

-Docker developed by Docker, Inc.


# Author

Brian Lam * brlam@brianlam.info * http://brianlam.info/
