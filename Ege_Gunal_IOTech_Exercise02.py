import json, time, re
from base64 import b64decode

#given file containing json data, return its contents as a json object
def get_json_from_file(filename):
    with open(filename, "r") as infile:
        json_content = json.loads(infile.read())
    return json_content

#given json object of known format, remove timestamps that are in the past
def discard_old_timestamps(json_obj, unix_time):
    for itt, cont in enumerate(json_obj["Devices"]):
        #check timestamp
        if float(cont["timestamp"]) < unix_time:
            json_obj["Devices"].pop(itt)

#decode base 64 values and add them up
#it is assumed that all value fields are populated with valid integers encoded in base64
def decode_sum_value(json_obj):
    #add values in the "value" fields after decoding them in base 64
    return sum(map(lambda cont : int(b64decode(cont["value"])), json_obj))

#pull uuids from strings in known format
#format: UUID is between "uuid:" and a comma
def get_uuids_regex(json_obj):
    #regex for between "uuid:" and a comma
    #store uuid values as strings inside an array and return it
    return [re.search(r"uuid:(.*?),", item["Info"]).group(1) for item in json_obj]

#save results in target format
def save_post_processing(filename, total, UUIDs):
    #combine resulting values into an object
    json_obj = {"ValueTotal": total, "UUIDs": UUIDs}
    #change the line underneath to change output file. default is to
    #add _output to input fileand save in the same directory as it
    outfile_name = re.search(r"(.*?).json", filename).group(1) + "_output.json"
    #clean file output format
    output_val = json.dumps(json_obj, indent=4)
    #write to file
    with open(outfile_name, "w") as outfile:
        outfile.write(output_val)
    #return some values for feedback
    return (outfile_name, output_val)

#main function but for calling form the outside
def exercise02():
    #get user input for file location and verbose
    filename = input("Please enter the file location with excercise 02 data (leave empty for data/data.json): ").strip()
    if (filename == ""): filename = "data/data.json"
    verbose = input("Would you like to see the results on terminal once finished? (Y/n)").strip()

    #parse data
    json_content = get_json_from_file(filename)

    #remove past timestamps
    discard_old_timestamps(json_content, time.time())

    #get the total of value entries
    total = decode_sum_value(json_content["Devices"])

    #get uuids
    UUIDs = get_uuids_regex(json_content["Devices"])

    #output to file
    outfile_name, outfile_contents = save_post_processing(filename, total, UUIDs)

    #print contents if verbose
    if (verbose.upper() != "N"):
        print(outfile_contents)

    #print output location
    print("Processed data saved to {}".format(outfile_name))
    #wait for user input to terminate
    input("Press enter to quit...")


if __name__ == "__main__":
    exercise02()

