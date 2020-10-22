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
