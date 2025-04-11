import serial
import time

class LoraMesh:
    def __init__(self, port, baudrate=115200, timeout=1):
        """
        Initializes the serial communication settings for AT commands.
        
        :param port: COM port or device ('/dev/ttyUSB0' on Linux)
        :param baudrate: Baud rate for the communication (default: 115200)
        :param timeout: Timeout in seconds for reading from the serial port (default: 1 second)
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None
        self.info = None
    
    def open(self):
        """Opens the serial connection."""
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            print(f"Connected to {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
    
    def send_data(self, command, wait_for_response=True, delay=0.5):
        """
        Sends an AT command to the serial port and optionally waits for a response.
        
        :param command: The AT command to send (string)
        :param wait_for_response: Flag to wait for response after sending the command (default: True)
        :param delay: Delay before reading the response (default: 1 second)
        :return: The response received from the device, or None if no response is received
        """
        if self.ser and self.ser.is_open:
            # Send the AT command with a carriage return (CR) at the end
            # command = f"{command}\r"
            self.ser.write(command.encode())
            print(f"\nSent: {command.strip()}")
            
            if wait_for_response:
                time.sleep(delay)  # Wait for the response
                response = self.receive_data()
                return response
        else:
            print("Serial port is not open.")
            return None
    
    def receive_data(self, size=256):
        """
        Reads data from the serial port.
        
        :param size: Number of bytes to read (default: 256 bytes)
        :return: Data received as bytes
        """
        if self.ser and self.ser.is_open:
            data = self.ser.readall()
            if data:
                print(f"Received: {data.decode(errors='ignore')}", end="")
            else:
                print("No data received.")
            return data.decode(errors='ignore')
        else:
            print("Serial port is not open.")
            return ""
    
    def parse_command(command):
        """Parase AT Command"""
        print("Data = " + param)
        param = command.strip().split('=')
    
        if len(param) > 0:
            return param
        else:
            return False
    
    def close(self):
        """Closes the serial connection."""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print(f"Connection to {self.port} closed.")
        else:
            print("Serial port is not open.")

    # ================================ Read Module Info ===================================
    def read_module_info(self):
        """
        Read the module parameteres

        @Return
        Module all Info paramters
        """
        response = self.send_data('AT+INFO=?', wait_for_response = True)
        return(response)
    # ----------------------------------------------------------------------------------------

    # ================== Destination Address - Read/Write ===================================
    def set_destination_addr(self, address=0, flash=0):
        """
        Set the Destination address
        
        @Parameters
        address: It can be 0 ~ 65535
        flash: 0 (don't save in flash) or 1 (save in flash)
        
        @Return
        Success (True) or Failure (False)
        """ 
        command = f"AT+DST_ADDR={address},{flash};"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - Destination address set to : {address}")
            return(True)
        else:
            print(f"Error - Destination address")
            return(False)

    def read_destination_addr(self):
        """
        Read the Destination address
        
        @Return
        Address or False
        """
        command = 'AT+DST_ADDR=?'
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')
        print(f"Info - Destination Address is : {param[1]}")
        return(param[1])
    # ----------------------------------------------------------------------------------------

    # ============================ Communication Mode - Read/Write ============================
    def set_comm_mode(self, mode=3, flash=0):
        """
        Set the communication mode of the module
        
        @Parameters 
        mode: Four Modes (1 : Unicast),(2 : Multicast),(3 : Broadcast),(4 : Anycast)
        flash = 0 (Don't save in flash), 1 (Save in flash)

        @Return:
        Success (True) or Failure (False)
        """
        command = f"AT+OPTION={mode},{flash};"
        response = self.send_data(command, wait_for_response=True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - Source address is set to : {mode}")
            return(True)
        else:
            print(f"Error - Source address")
            return(False)

    def read_comm_mode(self):
        """
        Read the Communication Mode
        
        Return -
        Mode - (1 : Unicast),(2 : Multicast),(3 : Broadcast),(4 : Anycast)
        """
        command = 'AT+OPTION=?'
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')

        if(param[1] == '1'):
            print(f"Info - Communication Mode is : 1 - Unicast")
            return(param[1])
        elif(param[1] == '2'):
            print(f"Info - Communication Mode is : 2 - Multicast")
            return(param[1])
        elif(param[1] == '3'):
            print(f"Info - Communication Mode is : 3 - Broadcast")
            return(param[1])
        elif(param[1] == '4'):
            print(f"Info - Communication Mode is : 4 - Anycast")
            return(param[1])
        else:
            print(f"Error - Communication Mode Read")
            return(False)
    # ----------------------------------------------------------------------------------------

    # ======================== Source Address - Read/Write ====================================
    def set_source_addr(self, address=0, flash=0):
        """
        Set the source address
        
        @Parameters
        address: It can be 0 ~ 65535
        flash: 0 (don't save in flash) or 1 (save in flash)
        
        @Return
        Success (True) or Failure (False)
        """ 
        command = f"AT+SRC_ADDR={address},{flash};"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - Source address set to : {address}")
            return(True)
        else:
            print(f"Error - Source address")
            return(False)

    def read_source_addr(self):
        """
        Read the source address
        
        @Return
        Address 
        """
        command = 'AT+SRC_ADDR=?'
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')
        print(f"Info - Source Address is : {param[1]}")
        return(param[1])
    # -----------------------------------------------------------------------------------------

    # ========================= Send Data to Other LoraMesh Devices ========================
    def send_LORA_data(self, dataToSend, ):
        """
        Send the data to other LoraMesh devices
        
        @Return:
        
        """
        #self.ser.write(dataToSend.encode())
        
        response = self.send_data(dataToSend, wait_for_response = True, delay=2)
        return(response)
        '''
        if(response == "SUCCESS\r\n"):
            print(f"Data Sent : {response}")
            return(True)
        else:
            print(f"ERROR - Data sent - {response}")
            return(response)
        '''
        
    # ----------------------------------------------------------------------------------------

    # ==================================== Module RESET ======================================
    def reset_module(self):
        """
        Reset the LORA Mesh Module
        
        @Return:
        Success (True) or Failure (False)
        """
        command = "AT+RESET"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"\nInfo - Module Reset Done")
            return(True)
        else:
            print(f"\nError - Module Reset")
            return(False)
    # ----------------------------------------------------------------------------------------

    # ================================ Default Factory Settings =================================
    def reset_Factory(self):
        """
        Reset the Lora to factory settings
        
        @Return:
        Success (True) or Failure (False)
        """
        command = "AT+DEFAULT"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"\nInfo - Factory Reset Done")
            return(True)
        else:
            print(f"\nError - Factory Reset")
            return(False)
      
    # ----------------------------------------------------------------------------------------

    # ================================ Read MAC Address =================================
    def read_MAC_address(self):
        """
        Read the unique 32 bit address of the MCU of the LORA Module
        
        @Return:
        Address
        """
        command = "AT+MAC=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')
        print(f"Info - MAC Address is : {param[0]}")
        return(param[0])
        
    # ----------------------------------------------------------------------------------------

    # ================================ Type of Node (Routing / Terminal)=================================
    def read_node_type(self):
        """
        Read the type of the Node - Terminal or Routing
        
        @Return:
        Node Type
        """
        command = "AT+TYPE=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')

        if(param[1] == '0'):
            print(f"Info - Node Type (0) - Routing Node")
            return(param[1])
        elif(param[1] == '1'):
            print(f"Info - Node Type (1) - Terminal Node")
            return(param[1])
        else:
            print(f"Error - Node type")
    # ---------------------------------------------------------------------------------------------

    # ================================ RF Output Power (Read/Write)=================================
    def read_RF_power(self):
        """
        Read the type of the Node - Terminal or Routing
        
        @Return:
        Address or Failure (False)
        """
        command = "AT+POWER=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')

        print(f"Info - RF Power is : {param[1]}")
        return(param[1])
        
    def set_RF_power(self, power=0, flash=0):
        """
        Read the type of the Node - Terminal or Routing
        
        @Return:
        Address or Failure (False)
        """
        command = f"AT+POWER={power},{flash};"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - RF power set to : {power}")
            return(True)
        else:
            print(f"Error - RF power")
            return(False)
    # ---------------------------------------------------------------------------------------------

    # ============================ Frequency band/channel (Read/Write)==========================
    def read_freq_channel(self):
        """
        Read the frequency band
        E52-400NW22S frequency band: RF working channel (0 ~ 99)
        E52-900NW22S frequency band: RF working channel (0 ~ 79)
        
        @Return:
        Channel or Failure (False)
        """
        command = "AT+CHANNEL=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')

        print(f"Info - Frequency Channel : {param[1]}")
        return(param[1])
        
    def set_freq_channel(self, channel=0, flash=0):
        """
        Write the frequency channel
        
        @Parameters
        channel: E52-400NW22S frequency band: RF working channel (0 ~ 99)
                 E52-900NW22S frequency band: RF working channel (0 ~ 79)
        flash: 0 (Don't save to flash) or 1 (save to flash)

        @Return:
        Success (True) or Failure (False)
        """
        command = f"AT+CHANNEL={channel},{flash};"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - Frequency channel set to : {channel}")
            return(True)
        else:
            print(f"Error - Frequency channel")
            return(False)
    # ---------------------------------------------------------------------------------------------

    # ============================ Air Data Rate (Read/Write) ==================================
    def read_air_rate(self):
        """
        Read the air data rate
        (0 - 62.5K),(1 - 21.825K), (2 - 7K)
        
        @Return:
        Rate Value or Failure (False)
        """
        command = "AT+RATE=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')
    
        if(param[1] == '0'):
            print(f"Info - Air Data Rate (0) - 62.5K")
            return(param[0])
        elif(param[1] == '1'):
            print(f"Info - Air Data Rate (1) - 21.825K")
            return(param[0])
        elif(param[1] == '2'):
            print(f"Info - Air Data Rate (2) - 7K")
            return(param[0])
        else:
            print(f"Error - Read air data rate")
            return(False)
        
    def set_air_rate(self, rate=0):
        """
        Write the air data rate

        @Parameters
        rate: Use values (0 - 62.5K),(1 - 21.825K), (2 - 7K)

        """
        command = f"AT+RATE={rate}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - Air data rate set to : {rate}")
            return(True)
        else:
            print(f"Error - Air data rate")
            return(False)
    # --------------------------------------------------------------------------------------------

    # ================================ Frame Header (Enable/Disable) =============================
    def read_frame_header(self):
        """
        Read status of the data frame header
        
        @Return:
        Enable = 1 and Disable = 0
        """
        command = "AT+HEAD=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')

        print(f"Info - Frame Header status : {param[1]}")
        return(param[1])
        
    def set_frame_header(self, enable = 1):
        """
        Set the frame header packet enable/disable

        @Parameters
        enable: 1 for Enable and 0 for Disable
        flash: 0 (Don't save to flash) or 1 (save to flash)
        """
        command = f"AT+HEAD={enable};"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - Frame Header is : {enable}")
            return(True)
        else:
            print(f"Error - Air data rate")
            return(False)

