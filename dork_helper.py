import os
import sys

def generate_dork(domain):
    
    dork_templates = [
        "site:{domain} filetype:pdf",
        "site:{domain} filetype:xls OR filetype:xlsx",
        "site:{domain} filetype:doc OR filetype:docx",
        "site:{domain} inurl:login",
        "site:{domain} inurl:admin",
        "site:{domain} intitle:\"index of\"",
        "site:{domain} intext:password",
        "site:{domain} ext:sql OR ext:db OR ext:mdb",
        "site:{domain} inurl:wp-admin",
        "site:{domain} \"-www\"",
    ]

    dorks = [template.format(domain=domain) for template in dork_templates]
    return dorks

def save_to_file(dorks, filename="dorks.txt"):
    with open(filename, 'w') as file:
        for dork in dorks:
            file.write(dork + "\n")
    print(f"Dorks saved to {filename}")
    