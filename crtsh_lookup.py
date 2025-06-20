#!/usr/bin/env python3

import requests
import sys
import os
import shutil
import subprocess
import time

def get_crtsh_data(domain, retries=3, timeout=30):
    print(f"[+] Fetching data from crt.sh for domain: {domain}")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                data = response.json()
                subdomains = set()
                for entry in data:
                    name_value = entry.get("name_value")
                    if name_value:
                        for sub in name_value.split("\n"):
                            sub = sub.strip()
                            if "*" not in sub:
                                subdomains.add(sub)
                return sorted(subdomains)
            else:
                print(f"[-] Non-200 response: {response.status_code}")
        except Exception as e:
            print(f"[-] Attempt {attempt+1} failed: {e}")
            time.sleep(5)
    print("[-] All attempts failed.")
    return []

def run_sublist3r(domain, output_file):
    print(f"[+] Running Sublist3r on {domain}")
    command = f"sublist3r -d {domain} -n -o {output_file} > nul"
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"[-] Sublist3r failed: {e}")

def merge_and_dedupe(files, merged_file):
    print("[+] Merging and deduplicating subdomain results")
    all_subs = set()
    for file in files:
        if os.path.isfile(file):
            with open(file, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and "*" not in line:
                        all_subs.add(line)
    with open(merged_file, "w") as f:
        for sub in sorted(all_subs):
            f.write(sub + "\n")
    print(f"[+] Combined {len(all_subs)} unique subdomains into: {merged_file}")
    return merged_file

def run_tool(command, tool_name):
    print(f"[+] Running: {tool_name}")
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"[-] Failed to run {tool_name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 recon_combined.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    output_dir = os.path.join("crtsh_output", domain)
    os.makedirs(output_dir, exist_ok=True)

    crtsh_file = os.path.join(output_dir, f"{domain}_crtsh.txt")
    sublist3r_file = os.path.join(output_dir, f"{domain}_sublist3r.txt")
    all_subs_file = os.path.join(output_dir, f"{domain}_all_subdomains.txt")
    live_file = os.path.join(output_dir, f"{domain}_live.txt")
    dnsx_file = os.path.join(output_dir, f"{domain}_dnsx.txt")
    httpx_file = os.path.join(output_dir, f"{domain}_httpx.txt")
    subjack_file = os.path.join(output_dir, f"{domain}_subjack.txt")

    subdomains_crtsh = get_crtsh_data(domain)
    with open(crtsh_file, "w") as f:
        for sub in subdomains_crtsh:
            f.write(sub + "\n")

    run_sublist3r(domain, sublist3r_file)

    merge_and_dedupe([crtsh_file, sublist3r_file], all_subs_file)

    if shutil.which("httpx"):
        run_tool(f"httpx -l {all_subs_file} -silent -o {live_file}", "httpx (live domain check)")

    if shutil.which("dnsx"):
        run_tool(f"dnsx -l {all_subs_file} -a -resp -o {dnsx_file}", "dnsx")

    if shutil.which("subjack"):
        run_tool(f"subjack -w {all_subs_file} -t 50 -timeout 30 -ssl -a -o {subjack_file}", "subjack")

    print(f"[+] All results saved in: {output_dir}")
