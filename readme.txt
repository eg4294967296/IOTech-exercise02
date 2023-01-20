
# README for IOTechSystems Exercise 02

-This python file processes a JSON file with format provided in https://github.com/IOTechSystems/exercises/blob/main/exercise-02/data/data.json
	-Discards devices where the timestamp values (in UNIX format) are before current time
	-Sums all value entries, where values are base64 strings containing integer values, and stores it as an integer
	-Parses the uuid from the info field of each entry, where uuids are selected with regex for "uuid:{uuid_data},"
-Outputs the values total and the list of uuids in the format described by the JSON schema in https://github.com/IOTechSystems/exercises/blob/main/exercise-02/output-schema/schema.json
	-This output file is saved in the same directory as the input file, as input_file + _output.json
	-for example, if the input file is data/data.json, the output will be stored in data/data_output.json


REQUIERMENTS
-Python 3
	-json, time, re, base64 libraries are all part of the default installation
	-input file following the format in https://github.com/IOTechSystems/exercises/blob/main/exercise-02/data/data.json
	-write permissions to the directory where the input file is stored (for changing this, see usage)


USAGE
-Run the script with "python Ege_Gunal_IOTech_Excercise02.py" or through other means
-The script is set to auto run only if its called directly. if its called indirectly, you need to call "exercise02()" function
-Follow the prompt to enter input directory (can leave blank if data is stored in "data/data.json")
-Follow the prompt to enter if the output should be displayed on terminal, or just output to file. Default is Yes and any input other than n or N will display the result.
-If you want to change the output directory, refer to line 34-36 in script
