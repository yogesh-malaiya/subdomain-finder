<h1 align="center">🔍 Bug Bounty Recon Automation Toolkit</h1>

<p align="center">
  A powerful OSINT & subdomain reconnaissance tool to automate recon for bug bounty hunting.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Sublist3r-supported-lightgrey?style=flat-square" />
  <img src="https://img.shields.io/badge/httpx-required-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/dnsx-optional-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/subjack-optional-red?style=flat-square" />
</p>

---

## 🚀 Features

- 📜 Pulls subdomains from [crt.sh](https://crt.sh)
- 🔎 Discovers more using `Sublist3r`
- 🧠 Merges and deduplicates all results
- 🌐 Checks live domains using `httpx`
- 📡 Resolves DNS with `dnsx` _(optional)_
- 🚨 Detects subdomain takeover with `subjack` _(optional)_
- 🗂 Saves all outputs in a structured folder: `crtsh_output/<domain>/`

---

## 📦 Dependencies

Make sure the following tools are installed and added to your `PATH`:

| Tool                                                            | Install Guide                                                   |
| --------------------------------------------------------------- | --------------------------------------------------------------- |
| `Python 3.6+`                                                   | https://python.org                                              |
| `requests` module                                               | `pip install requests`                                          |
| [`Sublist3r`](https://github.com/aboul3la/Sublist3r)            | `git clone && python setup.py install`                          |
| [`httpx`](https://github.com/projectdiscovery/httpx)            | `go install github.com/projectdiscovery/httpx/cmd/httpx@latest` |
| [`dnsx`](https://github.com/projectdiscovery/dnsx) _(optional)_ | `go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest`   |
| [`subjack`](https://github.com/haccer/subjack) _(optional)_     | `go install github.com/haccer/subjack@latest`                   |

---

## 📁 Output Structure

```
crtsh_output/
└── target.com/
    ├── target.com_crtsh.txt           # From crt.sh
    ├── target.com_sublist3r.txt       # From Sublist3r
    ├── target.com_all_subdomains.txt
    ├── target.com_live.txt            # Live domains from httpx
    ├── target.com_dnsx.txt            # DNS resolution
    └── target.com_subjack.txt         # Takeover scan
```

---

## 🧪 Usage

```bash
python3 recon_combined.py <domain>
```

**Example:**

```bash
python3 recon_combined.py capital.com
```

---

### 🔐 Notes on subjack

Ensure the following file exists:

```
C:\Users\<your-name>\go\src\github.com\haccer\subjack\fingerprints.json
```

If it doesn't, download it:

```bash
wget https://raw.githubusercontent.com/haccer/subjack/master/fingerprints.json
```

---

## 🧠 Why Use This?

This toolkit helps bug bounty hunters:

- 🔄 Automate repetitive recon steps
- 🎯 Find targets across multiple sources
- 🛡️ Detect takeover vulnerabilities faster
- 💼 Save organized output for reporting

---

## 🤖 Planned Features

- Add assetfinder, amass, and github-subdomains
- Slack/Discord webhook alerts
- HTML report generation

---

## 👨‍💻 Author

Made with ❤️ by a bug bounty hunter for bug bounty hunters.  
If this helps you — ⭐ the repo and share the knowledge.

---

## ⚠️ Legal

This script is for educational and authorized security testing purposes only.  
Do NOT use against domains you don't own or have permission to test.

---

## 📜 License

MIT License — use freely and responsibly.
