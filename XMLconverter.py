import xml.etree.ElementTree as etree
import json
import sys

def convert_xml_to_json(xml_file):
    tweets = []
    try:

        tree = etree.parse(xml_file)
        root = tree.getroot()
            
        for child in root:

            tweet = {
                "Text": child.findtext("text"),
                "ID": int(child.findtext("ID", 0),
                "QuotedID": int(child.findtext("QuotedID", 0)),
                "RetweetedText": child.findtext("RetweetedText"),
                "RetweetedHandle": child.findtext("RetweetedHandle"),
                "RetweetedName": child.findtext("RetweetedName"),
                "Retweets": int(child.findtext("Retweets", 0)),
                "Source": child.findtext("Source"),
                "UserHandle": child.findtext("UserHandle"),
                "UserName": child.findtext("UserName")
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
