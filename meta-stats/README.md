# meta-stats

This README file contains information on the contents of the meta-stats layer.

Please see the corresponding sections below for details.

Table of Contents
=================

   I. Creating meta-stats layer
  II. Adding the meta-stats layer to your build
 III. Misc

I. Creating meta-stats layer
================================================

1. Create meta-stats layer using bitbake-layers command
## bitbake-layers create-layer meta-stats

2. Create recipe-apps directory inside meta-stats
## mkdir recipe-apps

3. Create json-report-generator-sources directory inside recipe-apps
## mkdir json-report-generator-sources

4. Create json-report-generator-sources_1.00.bb source recipe file inside json-report-generator-sources directory
## touch json-report-generator-sources_1.00.bb

5. Create the following python scripts

II. Adding the meta-stats layer to your build
=================================================

Run 'bitbake-layers add-layer meta-stats' to add the meta-stats layer to conf/bblayers.conf
Alternatively, add the meta-stats layer by manually editing the conf/bblayers.conf

III. Misc
========

--- replace with specific information about the meta-stats layer ---
