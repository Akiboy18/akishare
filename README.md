# AkiShare
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green)
![Networking](https://img.shields.io/badge/Networking-Socket%20Programming-orange)
![License](https://img.shields.io/badge/License-Proprietary-red)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)



AkiShare is a **minimalistic Python-based file-sharing application** designed for quick and simple file transfers over a **local network (LAN)**.

The application converts **IP addresses and port numbers into human-readable codes**, making it easy for users to share files without needing technical knowledge of networking.

AkiShare is implemented using **Python socket programming** for communication and **Tkinter** for the graphical user interface.

---

# Abstract

This project aims to develop a minimalistic file-sharing application that enables simple and efficient transfer of files between devices on a local network.

Instead of manually sharing IP addresses and port numbers, AkiShare converts them into short readable codes. This allows users to easily share connection details while keeping the interface simple and user-friendly.

The system works without external servers and relies entirely on **peer-to-peer communication within the local network**.

---

# Features

* **Human-readable share codes** for IP address and port representation
* **Local network file transfer** without internet dependency
* **Lightweight and minimalistic design**
* **Cross-platform compatibility** (runs anywhere Python is supported)
* **Simple graphical interface using Tkinter**

---

# Technologies Used

* **Python**
* **Socket Programming**
* **Tkinter (GUI Framework)**
* **Threading**

---



# Installation

Clone the repository:

```
git clone https://github.com/Akiboy18/akishare.git
cd AkiShare
```


# Usage

## Sending a File

1. Launch the application.
2. Click **Send File (Start Server)**.
3. Select the file you want to share.
4. A **share code** will be generated.
5. Share this code with the recipient.

---

## Receiving a File

1. Launch the application.
2. Click **Receive File (Connect)**.
3. Enter the **share code** received from the sender.
4. Confirm the download.
5. Choose where to save the file.

---

# How the Share Code Works

AkiShare converts IP addresses and ports into readable character combinations.

Example process:

1. IP address is split into four octets.
2. Each octet maps to a predefined two-letter combination.
3. The port number maps to a single character.
4. These are combined to form a readable code.

The receiving device converts this code back into the original **IP address and port** to establish the connection.

---

# Advantages

* Easy to use even for non-technical users
* No external servers required
* Fast file transfers over LAN
* Lightweight Python implementation
* Works offline

---

# Limitations

* Works only within a **local network**
* No encryption for file transfer
* Limited port range (8000–8010)
* Basic error handling

---

# Future Improvements

* Add **file encryption for secure transfers**
* Extend the **port mapping range**
* Implement **automatic device discovery**
* Improve **error handling and connection reliability**

---

# Author

**Akhilesh R**


---

# License

This project is proprietary software.

Unauthorized copying, modification, distribution, or use of this software is strictly prohibited without permission from the author.

See the **LICENSE** file for details.
