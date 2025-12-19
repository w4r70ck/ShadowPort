# ShadowPort
ShadowPort is a simple terminal-based port scanner written in Python. Designed for simplicity, it scans specified ports or the full range, detects running services.
---

### ✨ Features

- ⚡ **Fast port scanning**  
- 🎯 **Detects open ports and services**  
- 🧙 **Created by:** [w4r70ck](https://github.com/w4r70ck)

---

### 📦 Installation

```bash
git clone https://github.com/w4r70ck/shadowport.git
cd shadowport

```

---

### 🚀 Usage

```bash
python scanner.py
```

- 🔹 Enter the **target IP address**
- 🔹 Optionally specify **ports (comma-separated)** or leave blank to scan all (1–65535)
- 🔹 Watch the magic happen in your terminal!

---

### ⚠️ Disclaimer

> 🛡️ This tool is designed for **educational and authorized security testing** only.  
> 🚫 Do not use it on networks without explicit permission.  
> 👨‍💻 Author is not responsible for misuse.

---

**🧠 Stay curious. Stay ethical.**


http – show all HTTP traffic

http.request – show only HTTP requests

http.response – show only HTTP responses

http.request.method == "GET" – filter GET requests

http.request.method == "POST" – filter POST requests

http.request.method == "PUT" – filter PUT requests

http.request.method == "DELETE" – filter DELETE requests

http.host == "example.com" – filter HTTP traffic for a specific host

http.request.uri contains "login" – filter HTTP traffic for a specific URI

http.response.code == 200 – filter HTTP responses with status code 200

http.response.code == 404 – filter HTTP responses with status code 404

tcp.port == 80 – filter HTTP traffic on port 80

dns – show all DNS traffic

dns.flags.response == 0 – show only DNS queries

dns.flags.response == 1 – show only DNS responses

dns.qry.name == "google.com" – filter DNS traffic for a specific domain

dns.qry.name contains "google" – filter DNS traffic containing a keyword

dns.qry.type == 1 – filter DNS A record queries

dns.qry.type == 28 – filter DNS AAAA record queries

dns.qry.type == 15 – filter DNS MX record queries

udp.port == 53 – filter DNS over UDP

tcp.port == 53 – filter DNS over TCP

http || dns – show HTTP or DNS traffic

tcp.port == 80 || udp.port == 53 – show HTTP and DNS on standard ports

(ip.addr == 8.8.8.8) && (http || dns) – show HTTP/DNS traffic to or from a specific IP
