cmake_minimum_required(VERSION 3.8)
project(ecn_aquabot)

# find dependencies
find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})

ament_package()
