#!/usr/local/bin/python3

import argparse
import random

from alert import email_alert
from EIaDDictionary import dictionary as d

# Parse the command line for your variables, man
parser = argparse.ArgumentParser(
    description="Send a random British idiom and definition to a mailing list",
    prog="English Idiom a Day®",
)

parser.add_argument(
    "-f",
    "--file",
    type=str,
    metavar="",
    required=False,
    help="a file with a list of email addresses to alert",
)

parser.add_argument("-V", "--version", action="version", version="%(prog)s v0.9")

args = parser.parse_args()
if not args.file:
    email_list=['yourphone#@vzwpix.com', 'yourname@gmail.com']
else:
    email_list = []
    try:
        with open(args.file, 'r') as file:
            for line in file:
                email_list.append(line.strip('\n'))
    except FileNotFoundError:
        print(f"* ERROR: File not found: {args.file}")
        exit(-1)

subject, body = random.choice(list(d.items()))

for email_address in email_list:
    email_alert(subject, body, email_address)