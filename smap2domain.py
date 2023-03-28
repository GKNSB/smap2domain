#!/usr/bin/env python

import re
import sys
from argparse import ArgumentParser

parser = ArgumentParser(prog="smap2domain.py", description="Combine Lepus resolution files with gnmaps for <domain>:<port> combinations")
parser.add_argument("resFile", help="File containing lepus resolutions results. (e.x. results_public.csv)", type=str)
parser.add_argument("gnmapFile", help="gnmap file containing portscan results", type=str)
parser.add_argument("-o", "--output", action="store", dest="output", help="Output file location", type=str, default=None)
args = parser.parse_args()

results = []

with open(args.resFile, "r") as domainsFile:
	resolutions = domainsFile.readlines()
	for domainentry in resolutions:
		domainIPs = []
		domainentry = domainentry.strip()
		domainDomain = domainentry.split("|")[0]
		tmp = domainentry.split("|")[1]

		if "," in tmp:
			domainIPs = tmp.split(",")

		else:
			domainIPs.append(tmp)

		with open(args.gnmapFile, "r") as infile:
			for tmpline in infile:
				line = tmpline.strip()
	
				if "Nmap" in line:
					pass

				else:
					openports = re.findall("(\d+)\/open", line.strip())
					ip = re.findall("Host:\s(\d+\.\d+\.\d+\.\d+)", line)

					if ip:
						ip = ip[0]
						
						if openports and ip in domainIPs:
							for openport in openports:
								results.append(f"{domainDomain}:{openport}")

results = set(results)

if args.output:
	with open(args.output, "w") as outfile:
		for item in results:
			sys.stdout.write(f"{item}\n")
			if args.output: outfile.write(f"{item}\n")

else:
	for item in results:
		sys.stdout.write(f"{item}\n")
