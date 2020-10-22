# meta-stats

This README file contains information on the contents of the meta-stats layer.

Please see the corresponding sections below for details.

Table of Contents
=================

   I. Creating meta-stats layer
   
  II. Adding the meta-stats layer to your build
  
 III. Build the recipe and final image

## I. Creating meta-stats layer

### 1. Create meta-stats layer using bitbake-layers command

     bitbake-layers create-layer meta-stats

### 2. Create recipe-apps directory inside meta-stats

     mkdir recipe-apps

### 3. Create json-report-generator-sources directory inside recipe-apps

     mkdir json-report-generator-sources

### 4. Create json-report-generator-sources_1.00.bb source recipe file inside json-report-generator-sources directory

     touch json-report-generator-sources_1.00.bb

### 5. Create json-report-generator-sources directory inside json-report-generator-sources (current) and create the python scripts and license file inside it 

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
        
### 6. Modify the json-report-generator-sources_1.00.bb recipe
      a. Add the SUMMARY - description of the recipe
      
      b. Add LICENSE - License name
      
      c. Add LIC_FILES_CHKSUM - It is always required to make sure that no one tampers the file
      
      d. Add SRC_URI - Consists the list of required URL's, files
      
      e. Add S - Specify the location of the source codes
      
      f. Add do_compile - Normal recipe build task which compiles the source code
      
      g. Add do_install - Normal recipe build task which install binary to the destination directory
      
II. Adding the meta-stats layer to your build
=================================================

   Run 'bitbake-layers add-layer meta-stats' to add the meta-stats layer to conf/bblayers.conf

   Alternatively, add the meta-stats layer by manually editing the conf/bblayers.conf

III. Build the recipe and final image
========

   Run 'bitbake json-report-generator-sources' to build the recipe

   Run 'bitbake core-image-sato' to build the final image
