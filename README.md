## smap2domain
Convert smap/nmap results to \<domain>:\<port> format. Helper script that takes as input a Lepus resolution file and a .gnmap file from smap and prints to stdout and optionally to a file.

```
usage: smap2domain.py [-h] [-o OUTPUT] resFile gnmapFile

Combine Lepus resolution files with gnmaps for <domain>:<port> combinations

positional arguments:
  resFile               File containing lepus resolutions (e.x. results_public.csv)
  gnmapFile             gnmap file containing portscan results

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file location
```
