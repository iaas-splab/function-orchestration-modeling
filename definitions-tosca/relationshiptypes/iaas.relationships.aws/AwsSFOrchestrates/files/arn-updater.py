import json
import sys
import os

def update_spec(path, function_name, function_arn):
    path = '/tmp/' + path
    
    with open(path, "r") as asl:
        string_to_replace = function_name + '_ARN'
        upadted_sm = asl.read().replace(string_to_replace, function_arn)

    with open(path, "w") as f:
        f.write(upadted_sm)


def main():
    print(sys.argv)
    if len(sys.argv) < 4:
        sys.exit("Not enough args")
    update_spec(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()
