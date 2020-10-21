import json
from collections import OrderedDict


def create_package_json_object(input_manifest_file):
	manifest_file_object = open(input_manifest_file, 'r')
	package_dict = {'packages': []}

	while True:
		line = manifest_file_object.readline()
		if not line:
			break
		package_info = line.split()
		package_info_dict = OrderedDict([("package_name", package_info[0]), ("version", package_info[2])])
		package_dict['packages'].append(package_info_dict)
	package_json_object = json.dumps(package_dict, indent=1)
	manifest_file_object.close()
	return package_json_object
