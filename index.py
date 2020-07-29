import functools
import argparse

PROPERTY_MAP = {}
METRIC = "net_sales"

def rowObject(property_names, file_row, metric):
	fields = file_row.strip().split("|")
	row = {}
	currentPropertyMap = PROPERTY_MAP
	for index in range(len(fields)):
		property_name = property_names[index]
		field = fields[index]
		row[property_name] = field
		if "property" in property_name:
			if not field in currentPropertyMap:
				currentPropertyMap[field] = {}
			currentPropertyMap = currentPropertyMap[field]
		elif property_name == metric:
			currentPropertyMap[property_name] = field
	return row

def fileParser(file_location, metric):
	file = open(file_location, "r")
	property_names = file.readline().strip().split("|")
	rowObjects = []
	while True:
		line = file.readline()
		if not line:
			break 
		row = rowObject(property_names, line, metric)
		rowObjects.append(row)
	file.close()
	return rowObjects

def compare(row1, row2):
	property_map_row1 = PROPERTY_MAP
	property_map_row2 = PROPERTY_MAP
	has_same_group = True
	for key in row1.keys():
		row1_key = row1[key] if has_same_group else "$total"
		row2_key = row2[key] if has_same_group else "$total"
		if "property" in key:
			if row1_key == "$total" and row2_key != "$total":
				return -1;
			elif row1_key != "$total" and row2_key == "$total":
				return 1;
			elif row1_key != row2_key:
				has_same_group = False
			property_map_row1 = property_map_row1[row1_key]
			property_map_row2 = property_map_row2[row2_key]
	return float(property_map_row2[METRIC]) - float(property_map_row1[METRIC])

def convertor(row):
	string = "|".join(row[x] for x in row.keys())
	return string + "\n"


def main():
	args = parse_arguments()
	global METRIC
	METRIC = args.metric
	rows = fileParser(args.input_file, METRIC)
	output = sorted(rows, key=functools.cmp_to_key(compare))
	f = open(args.output_file, "w")
	for row in output:
		f.write(convertor(row))
	f.close()

def parse_arguments():
	parser = argparse.ArgumentParser(description='Hierarchical Sorting 42CodeChallenge')
	parser.add_argument('--input_file', help='location of input file')
	parser.add_argument('--output_file', help='location of output file')
	parser.add_argument('--metric', help='metric used for sorting')

	args = parser.parse_args()
	return args

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))











