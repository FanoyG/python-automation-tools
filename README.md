<div align="center">
  <img src="https://github.com/FanoyG/python-automation-tools/blob/main/Logo/pytool-logos.png" alt="Python Automation Tools Logo" width="250"/>
</div>


<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=flat-square&logo=python&logoColor=white) ![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square) ![Learning](https://img.shields.io/badge/Learning-Continuous-green?style=flat-square) ![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

</div>

---

## 🌱 Project Vision

This project is my way of learning automation by doing, not just reading. Each script solves a real problem—whether it's cleaning up files, checking system health, or managing remote servers.

I'm learning step by step, making mistakes, and getting better with each challenge.

---

## 💡 What This Project Does

**25 automation scripts** organized into 5 progressive phases:

- Automate system tasks (file management, backups, cleanup)
- Monitor and audit (logs, disk space, file integrity)
- Network automation (SSH, scanning, uptime checks)
- Cloud management (AWS resources, backups, inventory)

Each script is practical, reusable, and solves real-world problems.

---

## 🛠️ Skills & Tools Used

**Core Technologies**
- Python 3.x with standard libraries (`os`, `sys`, `subprocess`, `datetime`)
- System monitoring tools (`psutil`, `platform`)
- Network libraries (`socket`, `requests`, `paramiko`, `netmiko`)
- Cloud APIs (`boto3` for AWS)
- Task scheduling and automation

**What I'm Learning**
- Writing scripts that replace manual work
- Handling errors and edge cases gracefully
- Working with files, processes, and system resources
- Connecting to remote systems and APIs
- Structuring code so it's reusable and maintainable

---

## 📈 My Progress

### ✅ Phase 1: Foundational Automation

| Status | Challenge |
|--------|-----------|
| ✅ | System Info Script |
| ✅ | Directory Cleaner |
| ✅ | Auto Folder Organizer |
| 🔄 | Backup Script |
| 🔄 | Scheduled Script Runner |
| 🔄 | Service Health Checker |

### 🔲 Phase 2: User, Log, and File Automation

| Status | Challenge |
|--------|-----------|
| ⏳ | User Account Creator |
| ⏳ | Password Expiry Checker |
| ⏳ | Failed Login Detector |
| ⏳ | File Integrity Checker |
| ⏳ | Disk Usage Monitor |
| ⏳ | Log Archiver |

### 🔲 Phase 3: Networking & Remote Automation

| Status | Challenge |
|--------|-----------|
| ⏳ | Ping Sweep Tool |
| ⏳ | SSH Command Runner |
| ⏳ | Network Config Fetcher |
| ⏳ | Port Scanner |
| ⏳ | Remote Backup Puller |
| ⏳ | Website Status Checker |

### 🔲 Phase 4: Cloud & Infrastructure Automation

| Status | Challenge |
|--------|-----------|
| ⏳ | AWS EC2 Start/Stop Tool |
| ⏳ | AWS S3 Backup Uploader |
| ⏳ | Instance Inventory Generator |
| ⏳ | Infrastructure Audit Tool |

### 🔲 Phase 5: Security, Alerts & Smart Automation

| Status | Challenge |
|--------|-----------|
| ⏳ | Service Auto-Healer |
| ⏳ | Email Alert System |
| ⏳ | Central Log Dashboard |

**Legend**: ✅ Done | 🔄 In Progress | ⏳ Upcoming

---

## 📚 Key Learnings

**What's clicked so far:**
- Python can replace a lot of manual terminal work
- Good error handling makes scripts way more reliable
- Reading documentation carefully saves debugging time later
- Small, focused scripts are easier to maintain than big ones

**What I'm still figuring out:**
- Best practices for handling credentials and sensitive data
- How to make scripts work across different operating systems
- When to use external libraries vs. standard modules
- Organizing larger projects as they grow

---

## 📂 Project Structure

```
python-automation-journey/
│
├── phase1_foundation/
│   ├── system_info.py
│   ├── directory_cleaner.py
│   ├── folder_organizer.py
│   ├── backup_script.py
│   ├── scheduler.py
│   └── health_checker.py
│
├── phase2_admin/
│   └── (coming soon)
│
├── phase3_network/
│   └── (coming soon)
│
├── phase4_cloud/
│   └── (coming soon)
│
├── phase5_security/
│   └── (coming soon)
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/python-automation-journey.git
cd python-automation-journey
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run a script**
```bash
cd phase1_foundation
python system_info.py
```

**Note:** Some scripts may need elevated privileges depending on what they're doing.

---

## 🔮 Future Enhancements

Things I want to add as I learn more:

- Configuration files so scripts are easier to customize
- Logging to files instead of just printing to console
- Unit tests to catch bugs early
- A simple CLI tool that runs multiple scripts
- Docker setup for easier portability
- Web dashboard to visualize monitoring data

---

## 📋 Challenges Overview

<details>
<summary><b>Phase 1: Foundational Automation</b></summary>

| # | Challenge | What I'm Learning |
|---|-----------|-------------------|
| 1 | System Info Script | Get hostname, OS, uptime, CPU/memory/disk info |
| 2 | Directory Cleaner | Auto-delete old temp/log files |
| 3 | Auto Folder Organizer | Sort files by type into folders |
| 4 | Backup Script | Zip and copy important files |
| 5 | Scheduled Script Runner | Run commands every X minutes |
| 6 | Service Health Checker | Check if processes are running, restart if needed |

</details>

<details>
<summary><b>Phase 2: User, Log, and File Automation</b></summary>

| # | Challenge | What I'm Learning |
|---|-----------|-------------------|
| 7 | User Account Creator | Add users from CSV files |
| 8 | Password Expiry Checker | Alert when passwords are expiring |
| 9 | Failed Login Detector | Parse authentication logs |
| 10 | File Integrity Checker | Detect modified files using hashes |
| 11 | Disk Usage Monitor | Alert when storage exceeds thresholds |
| 12 | Log Archiver | Compress and move old logs |

</details>

<details>
<summary><b>Phase 3: Networking & Remote Automation</b></summary>

| # | Challenge | What I'm Learning |
|---|-----------|-------------------|
| 13 | Ping Sweep Tool | Check which IPs are alive |
| 14 | SSH Command Runner | Run commands on remote servers |
| 15 | Network Config Fetcher | Collect configs from network devices |
| 16 | Port Scanner | Check open ports on hosts |
| 17 | Remote Backup Puller | Copy files from remote systems |
| 18 | Website Status Checker | Monitor site uptime |

</details>

<details>
<summary><b>Phase 4: Cloud & Infrastructure Automation</b></summary>

| # | Challenge | What I'm Learning |
|---|-----------|-------------------|
| 19 | AWS EC2 Start/Stop Tool | Manage instances by tags |
| 20 | AWS S3 Backup Uploader | Automate cloud backups |
| 21 | Instance Inventory Generator | Create reports of cloud resources |
| 22 | Infrastructure Audit Tool | Verify config compliance |

</details>

<details>
<summary><b>Phase 5: Security, Alerts & Smart Automation</b></summary>

| # | Challenge | What I'm Learning |
|---|-----------|-------------------|
| 23 | Service Auto-Healer | Monitor and auto-restart services |
| 24 | Email Alert System | Send alerts when thresholds are hit |
| 25 | Central Log Dashboard | Aggregate logs into one view |

</details>

---

## 📝 Notes

This is a learning project. The code will improve as I learn better patterns and practices. Earlier scripts might be simpler than later ones—that's intentional. It shows progress.

I'm documenting this journey as a learner, not as someone who has all the answers. Feedback and suggestions are always welcome.

---

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and learn from it.

---

<div align="center">

**Built with curiosity and a lot of trial and error**

*Last Updated: November 2025*

</div>
