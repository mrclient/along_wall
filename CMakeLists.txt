cmake_minimum_required(VERSION 2.8.3)
project(along_wall)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  sensor_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(along_wall_cpp src/along_wall.cpp)

target_link_libraries(along_wall_cpp
  ${catkin_LIBRARIES}
)
