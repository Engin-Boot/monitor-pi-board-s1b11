Build Linux Distribution for Raspberrypi
===========================================

This README file contains information on building core-image-sato image for
Pi board and design and development of meta-stats layer. 

Please see the corresponding sections below for details.

Dependencies
==================================================

  Clone the below dependencies.

  URI: git://git.yoctoproject.org/poky.git
  
  layers: meta, meta-poky, meta-yocto-bsp
  
  branch: zeus
  
  URI: https://github.com/agherzan/meta-raspberrypi.git
  
  branch: zeus
  
  URI: https://github.com/openembedded/meta-openembedded.git
  
  layers: meta-oe, meta-python, meta-networking, meta-multimedia
  
  branch: zeus
  
  URI: https://github.com/meta-qt5/meta-qt5.git
  
  branch: zeus
  
  URI: https://github.com/openembedded/openembedded-core.git
  
  branch: zeus
  
Table of Contents
==============================================

  I. Building core-image-sato image for Pi board
  
  II. Creating meta-stats layer
  
  III. Adding the meta-stats layer to your build
  
  IV. Building the recipe and final image
  
  V. Results
  
# I. Building core-image-sato image for Pi board

## 1. Setting up the yocto build environment

  source oe-build-init-env script inside poky directory
   
  Run `source oe-build-init-env sato-build` to setup local path
  and other variables for build directory
  
  It creates `sato-build` directory with `conf` directory inside it
  
## 2. Adding dependant layers in conf/bblayers.conf
  
  Run `bitbake-layers add-layer layer-name`
  or manually edit conf/bblayers.conf to add layers
  
  Add poky, meta-poky, meta-yocto-bsp, meta-
  raspberrypi, meta-oe, meta-python, meta-networking, meta-multimedia
  and meta-qt5 layers
  
## 3. Local configuration file

  Set the target machine and other local user settings in conf/local.conf
  
  Set `MACHINE` to "raspberrypi4-64" from default machine
  
  Set `ENABLE_UART = "1"` to enable UART for serial communication
  
## 4. Build core-image-sato for Pi Board
  Run `bitbake core-image-sato` to build the Linux distribution for Pi board
