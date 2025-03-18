# LoRa Mesh USB Dongle and HAT for Raspberry Pi 

LoRa MESH networking utilizes LoRa spread spectrum technology for long-range communication. It offers a maximum output power of +22dBm, with an air data rate of up to 62.5K. 

Equipped with advanced LoRa MESH networking technology, the board supports features such as decentralized communication, self-routing, network self-healing, and multi-level routing. These capabilities make it ideal for a variety of applications, including smart home systems, industrial sensors, wireless alarm and security systems, building automation, smart agriculture, and more

## Features
- Decentralized communication
- Self routing
- Network self-healing
- Multi-level routing
- Long Range communication upto 2.5 Km
- Upto 65535 Nodes can be connected (theoretically)
- Support Unicast and Broadcase communication
- Remote Configuration of modules
- Air transmission rate upto 62.5kbps
- Low-power consumption

<img src="https://i.kickstarter.com/assets/047/307/118/559cc8a2d7f8a4074757b4b0a32a1c41_original.jpeg?fit=scale-down&origin=ugc&q=92&v=1731868114&width=680&sig=GXlYUJglp7fabnFZFjS3N9HSLERxbvzh4SOiqPcZm9I%3D" alt="Mesh HAT and Dongle" width="50%"/>


## Hardware Overview
- **Lora Mesh Raspberry Pi HAT**: Compatible with all Raspberry Pi Models
- **Lora Mesh USB Dongle**: Compatible with all single board computers/Windows/Linux/Mac computers

## USB Driver
- **CH340**: The hardware is based on the CH340 chip, incase of driver you can download it from the official website. You can download the drivers for windows/Mac/linux using the below link.
https://www.wch-ic.com/downloads/CH341SER_ZIP.html#carousel-example-generic

## Table of Contents
1. [Documentation](Documentation/) - This directory contains the manual for AT-Commands of the module.
2. [Hardware](Hardware/) - This directory contains the STEP file and dimensional file of the hardwares.
3. [Software](Software/) - This directory contains all the codes like library and examples
4. [Tools](Tools/) - This directory contains serial communication tool (X-Com) for manual AT Commands

## Getting Started

### Clone the repository
To get started with this project, clone the repository:

   ```bash
   git clone https://github.com/theopengadget/lora_mesh.git

### Breakdown of Sections:

1. **Project Title**: Clearly state the project’s name (LoRa Mesh Network) at the top, possibly including a brief description.
2. **Features**: Highlight the major functionalities and advantages of your LoRa mesh network (long-range, low power, scalable, etc.).
3. **Table of Contents**: Helps users navigate the README easily, especially for larger projects.
4. **Installation**: Guides users through cloning the repository and installing necessary dependencies.
5. **Hardware and Software Requirements**: Helps users understand what physical components and software setups are needed.
6. **Usage**: Provides an overview of how to use your project, including sample code and setup instructions.
7. **Examples**: Show code snippets to demonstrate typical use cases (simple communication, mesh relay).
8. **Contributing**: If you want others to contribute, include a guide on how to do so (fork, branch, pull request).
9. **License**: Specify the project’s license (e.g., MIT, GPL).
10. **Acknowledgements**: Credit any libraries, contributors, or resources you’ve used.

This template covers everything necessary for a clear and comprehensive `README.md`. You can adapt it based on your project’s complexity and requirements!


