import csv
import json
import sys

def convert_csv_to_json(csv_file):
    tweets = []
    try:
        with open(csv_file, newline = '', encoding='utf-8') as f:

            reader = csv.reader(f)
            
            for row in reader:

                tweet = {
                    "Text": row[0],
                    "ID": int(row[1]),
                    "QuotedID": int(row[2]),
                    "RetweetedText": row[3],
                    "RetweetedHandle": row[4],
                    "RetweetedName": row[5],
                    "Retweets": int(row[6]),
                    "Source": row[7],
                    "UserHandle": row[8],
                    "UserName": row[9]
                }
                tweets.append(tweet)
        
        output = {"Tweets": tweets}
        json_out = json.dumps(output, ensure_ascii=False, separators=(',', ':'))
        json_out = json_out.replace("<", "\\u003c").replace(">", "\\u003e")
        print(json_out)
        
    except FileNotFoundError:
        print(f"Error: File {csv_file} not found.", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Error: Please provide a CSV file.")
        sys.exit(1)

    convert_csv_to_json(sys.argv[1])