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
  
# II. Creating meta-stats layer

## 1. Create meta-stats layer using bitbake-layers command

  `bitbake-layers create-layer meta-stats`

## 2. Create recipe-apps directory inside meta-stats

  `mkdir recipe-apps`

## 3. Create json-report-generator-sources directory inside recipe-apps

     `mkdir json-report-generator-sources`

## 4. Create json-report-generator-sources_1.00.bb source recipe file inside json-report-generator-sources directory

     `touch json-report-generator-sources_1.00.bb`

## 5. Create json-report-generator-sources directory inside json-report-generator-sources (current) and create the python scripts and license file inside it 

     a. json-report-generator.py: main source file, imports package_json_object_creator and package_json_report_writer

     b. package_json_object_creator.py: contains create_package_json_object module, which reads an input manifest file,
        creates a python dictionary containing information about the packages and converts this to a JSON object
        The format of the manifest file is as follows:
        
        packagename, packagearch, version
        
     c. package_json_report_writer: contains write_json_report module, which writes the JSON object to a JSON file
        The format of the JSON file is as follows:
        
        {
         "packages": [
          {
           "package_name": "adwaita-icon-theme"
           "version": "3.32.0"
          }
         ]
        }
        
     d. COPYING: MIT license file
        
## 6. Modify the json-report-generator-sources_1.00.bb recipe
      a. Add the SUMMARY - description of the recipe
      
      b. Add LICENSE - License name
      
      c. Add LIC_FILES_CHKSUM - It is always necessary to make sure that no one tampers the file
      
      d. Add SRC_URI - Consists the list of required URL's, files
      
      e. Add S - Specifies the location of the source codes
      
      f. Add do_compile - Normal recipe build task which compiles the source code
      
      g. Add do_install - Normal recipe build task which installs binary to the destination directory
