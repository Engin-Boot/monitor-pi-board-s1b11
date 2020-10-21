import argparse
import os
import sys
import package_json_object_creator
import package_json_report_writer

# parse the command line arguments
parser = argparse.ArgumentParser(description='manifest file to JSON file convertor')
parser.add_argument('-i', '--input', help='absolute path to input manifest file in .manifest format', type=os.path.abspath, required=True)
parser.add_argument('-o', '--output', help='absolute path to output directory', type=os.path.abspath, required=True)
args = parser.parse_args()

print("Received arguments, input manifest file path: " + args.input + " , output directory: " + args.output)

# check if input manifest file exists
input_manifest_file = args.input
if not os.path.exists(input_manifest_file):
	print("ERROR: input manifest file not found!")
	sys.exit(1)
	

# check if output directory exists
output_directory = args.output
if not os.path.exists(output_directory):
	print("ERROR: output directory not found!")
	sys.exit(1)

# create package JSON object
package_dict = package_json_object_creator.create_package_json_object(input_manifest_file)

# create package-json-report.json file
package_json_report_writer.write_json_report(output_directory, package_dict)
