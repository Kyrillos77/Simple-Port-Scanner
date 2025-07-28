# Simple Port Scanner

A lightweight Python script for scanning open ports on a target IP address.

## Features

- Scans all ports (1–65535) on a given IP
- Uses raw socket connection attempts (TCP SYN)
- Displays all discovered open ports
- Minimal dependencies, cross-platform

## Requirements

- Python 3.x

## Usage

```bash
python port_scanner.py <target-ip>
