sudo apt-get install -y --reinstall pcmanfm
sudo apt-get install -y build-essential cmake
sudo apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev
sudo apt-get install -y libv4l-dev v4l-utils
sudo apt-get install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
sudo apt-get install -y libgtk2.0-dev
sudo apt-get install -y mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev
sudo apt-get install -y libatlas-base-dev gfortran libeigen3-dev
sudo apt-get install -y python2.7-dev python3-dev python-numpy python3-numpy
sudo apt-get install -y qt5-default qtbase5-dev qtdeclarative5-dev qt5-qmake qtcreator libqt5gui5 qtscript5-dev qtmultimedia5-dev libqt5multimedia5-plugins qtquickcontrols2-5-dev libqt5network5 cmake build-essential libqt5svg5-dev 
sudo apt-get install -y qtcreator qt5-default
git clone https://github.com/WiringPi/WiringPi.git
cd WiringPi/
git pull origin 
./build
