"""
File: lcd.py
Author: LoraMesh
Description: This file handles all the function related to 1.14 LCD
"""

import time
import RPi.GPIO
import spidev
import numpy as np


class LCD:
    width = 240
    height = 135
    
    def __init__(self, spi = spidev.SpiDev(0,0), spi_freq = 40000000, reset_pin = 22, data_pin = 17, backlight_pin = 27, backlight_freq = 1000):
        """
        Initializes the SPI communication of Raspberry Pi
        
        @Parameters
        spi_freq: 40Mhz 
        reset_pin: GPIO 22
        data_pin: GPIO 17
        backlight_pin: GPIO 27
        backlight_freq: 1000 Hz 
        """
        self.np=np
        self.backlight_pin = backlight_pin
        self.backlight_freq = backlight_freq
        self.SPEED = spi_freq
        self.reset_pin = reset_pin
        self.data_pin = data_pin

        self.GPIO = RPi.GPIO
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)

        self.GPIO.setup(reset_pin, self.GPIO.OUT)
        self.GPIO.setup(data_pin, self.GPIO.OUT)
        self.GPIO.setup(backlight_pin, self.GPIO.OUT)
        self.GPIO.output(backlight_pin, self.GPIO.HIGH)

        self.SPI = spi
        if self.SPI != None:
            self.SPI.max_speed_hz = spi_freq
            self.SPI.mode = 0b00

    def __gpio_write(self, pin, status):
        self.GPIO.output(pin, status)

    def __gpio_read(self, pin):
        return self.GPIO.input(pin)
    
    def __spi_write(self, data):
        if self.SPI != None:
            self.SPI.writebytes(data)

    def __delay_ms(self, time):
        time.sleep(time / 1000)

    def __module_init(self):
        # Check this again..
        self.pwm = self.GPIO.PWM(self.backlight_pin, self.backlight_freq)
        self.pwm.start(100)
        if self.SPI != None:
            self.SPI.max_speed_hz = self.SPEED
            self.SPI.mode = 0b00
        return 0
    
    def __backlight_dutyCycle(self, duty):
        self.pwm.ChangeDutyCycle(duty)

    def __backlight_freq(self, freq):
        self.pwm.ChangeFrequency(freq)
    
    def __exit(self):
        if self.SPI != None:
            self.SPI.close()
        
        self.GPIO.output(self.reset_pin, self.GPIO.HIGH)
        self.GPIO_output(self.data_pin, self.GPIO.LOW)
        self.pwm.stop()
        time.sleep(0.001) # Check this point with delay_ms

    def __command(self, cmd):
        self.__gpio_write(self.data_pin, self.GPIO.LOW)
        self.__spi_write([cmd])

    def __data(self, data):
        self.__gpio_write(self.data_pin, self.GPIO.HIGH)
        self.__spi_write([data])

    def reset(self):
        self.GPIO.output(self.reset_pin, self.GPIO.HIGH)
        time.sleep(0.01)
        self.GPIO.output(self.reset_pin, self.GPIO.LOW)
        time.sleep(0.01)
        self.GPIO.output(self.reset_pin, self.GPIO.HIGH)
        time.sleep(0.01)

    def rotate(self, rotation):
        """Rotate display based on input: 0 (0°), 1 (90°), 2 (180°), 3 (270°)"""
        rotation_map = {
            0: (0x00, 135, 240),  # 0°
            1: (0x60, 240, 135),  # 90°
            2: (0xC0, 135, 240),  # 180°
            3: (0xA0, 240, 135)   # 270°
        }
        rotation_value, width, height = rotation_map.get(rotation, (0x00, 240, 135))
        self.__command(0x36)
        self.__data(rotation_value)
        self.width, self.height = width, height  # Adjust width and height dynamically


    def init(self):
        self.__module_init()
        self.reset()
        self.rotate(3)

        #self.__command(0x36)
        #self.__data(0x70)                
        self.__command(0x3A) 
        self.__data(0x05)

        self.__command(0xB2)
        self.__data(0x0C)
        self.__data(0x0C)
        self.__data(0x00)
        self.__data(0x33)
        self.__data(0x33)

        self.__command(0xB7)
        self.__data(0x35) 

        self.__command(0xBB)
        self.__data(0x19)

        self.__command(0xC0)
        self.__data(0x2C)

        self.__command(0xC2)
        self.__data(0x01)

        self.__command(0xC3)
        self.__data(0x12)   

        self.__command(0xC4)
        self.__data(0x20)

        self.__command(0xC6)
        self.__data(0x0F) 

        self.__command(0xD0)
        self.__data(0xA4)
        self.__data(0xA1)

        self.__command(0xE0)
        self.__data(0xD0)
        self.__data(0x04)
        self.__data(0x0D)
        self.__data(0x11)
        self.__data(0x13)
        self.__data(0x2B)
        self.__data(0x3F)
        self.__data(0x54)
        self.__data(0x4C)
        self.__data(0x18)
        self.__data(0x0D)
        self.__data(0x0B)
        self.__data(0x1F)
        self.__data(0x23)

        self.__command(0xE1)
        self.__data(0xD0)
        self.__data(0x04)
        self.__data(0x0C)
        self.__data(0x11)
        self.__data(0x13)
        self.__data(0x2C)
        self.__data(0x3F)
        self.__data(0x44)
        self.__data(0x51)
        self.__data(0x2F)
        self.__data(0x1F)
        self.__data(0x1F)
        self.__data(0x20)
        self.__data(0x23)
        
        self.__command(0x21)
        self.__command(0x11)
        self.__command(0x29)

    def set_window(self, Xstart, Ystart, Xend, Yend):
        #set the X coordinates
        self.__command(0x2A)
        self.__data((Xstart+40)>>8 & 0xff)             
        self.__data((Xstart+40)   & 0xff)      
        self.__data((Xend-1+40)>>8 & 0xff)       
        self.__data((Xend-1+40)   & 0xff) 
        
        #set the Y coordinates
        self.__command(0x2B)
        self.__data((Ystart+53)>>8 & 0xff)
        self.__data((Ystart+53)   & 0xff)
        self.__data((Yend-1+53)>>8 & 0xff)
        self.__data((Yend-1+53)   & 0xff)

        self.__command(0x2C)

    def show_image(self, image):
        """Set buffer to value of Python Imaging Library image."""
        """Write display buffer to physical display"""
                
        imwidth, imheight = image.size
        if imwidth != self.width or imheight != self.height:
            raise ValueError('Image must be same dimensions as display \
                ({0}x{1}).' .format(self.width, self.height))
        img = self.np.asarray(image)
        pix = self.np.zeros((self.height,self.width,2), dtype = self.np.uint8)
        
        pix[...,[0]] = self.np.add(self.np.bitwise_and(img[...,[0]],0xF8),self.np.right_shift(img[...,[1]],5))
        pix[...,[1]] = self.np.add(self.np.bitwise_and(self.np.left_shift(img[...,[1]],3),0xE0),self.np.right_shift(img[...,[2]],3))
        
        pix = pix.flatten().tolist()
        self.set_window(0, 0, self.width, self.height)
        self.__gpio_write(self.data_pin,self.GPIO.HIGH)
        for i in range(0,len(pix),4096):
            self.__spi_write(pix[i:i+4096])

    def clear(self):
        """Clear contents of image buffer"""
        _buffer = [0xff]*(self.width * self.height * 2)
        self.set_window(0, 0, self.width, self.height)
        self.__gpio_write(self.data_pin,self.GPIO.HIGH)
        for i in range(0,len(_buffer),4096):
            self.__spi_write(_buffer[i:i+4096])


