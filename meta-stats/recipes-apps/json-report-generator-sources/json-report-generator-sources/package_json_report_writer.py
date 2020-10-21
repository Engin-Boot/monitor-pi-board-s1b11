import os

def write_json_report(output_directory, package_json_object):
	# create output JSON file path
	json_file = os.path.join(output_directory, 'package-json-report.json')

	with open(json_file, "w") as package_json_report:
		package_json_report.write(package_json_object)
	print("JSON report creation successful")
