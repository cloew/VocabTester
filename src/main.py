#!/usr/bin/python3
from Driver import VocabImporter
from Server import server

import sys

def main(args):
    """ Run the main file """
    with server.app.app_context():
        VocabImporter('importer').run(args)

if __name__ == "__main__":
	main(sys.argv[1:])