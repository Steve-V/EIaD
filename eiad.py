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
    "-u",
    "--user",
    type=str,
    metavar="",
    required=True,
    help="email address to send from",
    )
parser.add_argument(
    "-p",
    "--password",
    type=str,
    metavar="",
    required=True,
    help="password of user email address",
    )

parser.add_argument(
    "-f",
    "--file",
    type=str,
    metavar="",
    required=False,
    help="a file with a list of email addresses to alert",
    )

parser.add_argument(
    "-e",
    "--email",
    type=str,
    metavar="",
    required=False,
    help="an email addresse to alert",
)

parser.add_argument("-V", "--version", action="version", version="%(prog)s v0.9")

args = parser.parse_args()

if args.email:
    email_list=[args.email]
elif args.file:
    try:
        with open(args.file, 'r') as file:
            for line in file:
                email_list.append(line.strip('\n'))
    except FileNotFoundError:
        print(f"* ERROR: File not found: {args.file}")
        exit(-1)
else:
    email_list = ['yourPhoneNumber@vizpw.com', 'yourgmail@gmail.com']

subject, body = random.choice(list(d.items()))

for email_address in email_list:
    email_alert(args.user, args.password, subject, body, email_address)