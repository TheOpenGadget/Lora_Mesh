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
<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDrJdN6geXsRcTNCT8rtlzwCDyTX2gNLxin0JOQVQgF8VnjiW3Zvp8bOZdDhNQibhjxhb1LesbrYUomOtYP7bvBxjb-9jRCzSULoCX1Em-FEjKA9HaQ15CfN7o-mA5BP6xzk0yZ8RQSdyY0vBl4LmXr2ARMhNA9GmZyrDYAWyGS4OD6IFkl1sqNy9dcck/s1600/Long%20Range%20MESH.jpg" alt="Mesh HAT" width="50%"/>

1. SMA Connector for the Antenna
2. USB-C: This can be used for power supply to the module or the data communication. For data communication the jumper settings must be set as the USB text.
3. Bootloader Button
4. Button 1 - Programmable button linked with Raspberry Pi GPIO PIN -
5. Module Rest Button
6. Button 2 - Programmable button linked with Raspberry Pi GPIO PIN -
7. Raspberry Pi Stacking header
8. 1.14" TFT display
9. LoRa Mesh Module
10. Jumper Settings for selecting the serial communication via USB or GPIO pins of Raspberry Pi

- **Lora Mesh USB Dongle**: Compatible with all single board computers/Windows/Linux/Mac computers
<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjimGkkRhyphenhyphenZ2xbkyBmzovxoRSoGXV1MVB9hCw7OE0lMUOFSjtgu3pcWOmV_kZNmeHzkpDRAAVTTjiME0o9XKAhu_aPbWTGHwzeR3oVG7b4C0EPzzv1RMO94-m9OBiHKpGM6LvCVm3rVLRq-vA6rAg-Bkn9i07kuvKdajaCRbU8yJ2wLRT7T8h5NSykFjCk/s1600/17.jpg" alt="Mesh Dongle" width="50%"/>

1. SMA connector for the Antenna
2. Module Reset Button
3. Bootloader Button
4. LoRa Mesh Module
5. USB-A for communication

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
   ```

### Network Topology
The LoRa Mesh network adopts a decentralized structure and the entire network is composed of - Routing Nodes and Terminal Nodes
- **Routing Node**: Routing node receives data in the network for routing updates and data forwarding
- **Terminal Node**: Terminal nodes do not have routing functions and are generally deployed at the edge of the network
<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmB7V7_tDHuGQ5AXGW-IyVleqwTMM_ni3qlPGpj3341psHMqlpaPzTeUGMKBBGumkNYhTRGI6FKxBVby2GC0EDFhUxqH1FLGOuYy7ZLen67MfJEkYC9KkCQq5uuWAUArwCG0NGKq3_opa7qfB4UriEBqNzIblatdJdWIVjU_wL1euamayhbPzl7OhnqvY/s1600/e%20routing.png" alt="Mesh Dongle" width="70%"/>

### Communication Modes
The network supports four communication methods - Unicast, Multicast, Broadcast and Anycast. 
You can choose different communication methods according to different application scenarios. Among them, unicast and broadcast are the simplest and most basic communication methods. 

- **Unicast mode**: This is like a point to point communication and for this mode you should know the address of the target module. The routes will be automatically established and request responses will be returned to determine the data transmission path.
- **Broadcast mode**: This method is used for broadcasting the data without knowing the address of the module. There is no need to establish a route, but all receiving
modules will forward the data again after receiving it. The module's built-in CSMA avoidance mechanism and broadcast filtering mechanism can effectively prevent data collision and secondary forwarding.
- **Multicast mode**: This communication method requires group management of target modules in advance. All target modules need to be grouped in advance using commands. Group can be understood as a public address, and each module can set up to 8 group addresses. Also, Routing needs to be re-established every time. It is recommended that the interval between consecutive multicast initiations be about 5 seconds.
- **Anycast Mode**: This communication is generally used for communication between different networks, and different networks have different network identification codes. Unicast, multicast, and broadcast communication methods cannot directly interact with data between networks. In this case, anycast can be used to interact with data between different networks. Anycast communication can send data to a single or all nodes within the single-hop coverage according to the set target address. Data cannot be relayed and responded to in anycast mode.

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNGjFXQMeVvU9D3qW-cVq524wn_YzU-8nZk3c2k7qugF8yLD10heNsHq4uk4zGb63Di0pDHR4FoiAmZ3jfOdtuObwE7aFseeKbsLrWU6sFiq2l-Jd-G6LKugmEfCjRUjw29xyu7Tgfntz5AdWgIE3bb9I2UQON3EOkmEp5UWvBEvFWg8phKqir9EbkIkQ/s1600/Broadcast.png" alt="Mesh Dongle" width="50%"/>

### Manual Configuration of the Module
Using RF settings tool [Tools](Tools/), you can easily configure all the parameters of the module. GUI is very simple and easy to use. For more information you can check the video.

### Serial Communication Tool (X-Com) for AT Commands
This is serial communication tool  [Tools](Tools/) showed in the documents for sending AT commands to the module. You can also use any serial software. For more information you can checkout the video.




