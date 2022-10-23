# This is an example Docker File
#  Command to build it
# docker built -t <image name > .
FROM osrf/ros:noetic-desktop-full

RUN apt-get update
RUN apt-get install -y git && apt-get install -y python3-pip
RUN mkdir -p ~/catkin_ws/src && \
    cd ~/catkin_ws/src/

RUN git clone https://github.com/noshluk2/ros1_wiki && \
    cd ~/catkin_ws

RUN echo "ALL Done"




