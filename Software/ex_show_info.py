import lcd
import time
import lora
from PIL import Image, ImageDraw,ImageFont


# Initialize Font Typs for the LCD
Font1 = ImageFont.truetype("Font/Font00.ttf",20)
Font2 = ImageFont.truetype("Font/Font02.ttf",25)

# Inittialize the LCD
disp = lcd.LCD()
disp.init()

# Initialize the Serial Port with Comm Port ttyAMA0 and Initialize Lora 
# Change comm port to ttyUSB0 in case of USB communication
mesh = lora.LoraMesh(port='/dev/ttyAMA0', baudrate=115200)    
mesh.open()
mesh.read_module_info()

# Create a image layout for showing text or image on the LCD
img = Image.new("RGB", (disp.width, disp.height), "WHITE")
draw = ImageDraw.Draw(img)

# Read and the module info and show it on LCD


draw.text((80,0), "Lora Mesh", font = Font2, fill = "RED")
# Read Destination address and show 
draw.text((0,25), "Dest Addr = " + mesh.read_destination_addr(), font = Font1, fill = "BLUE")

# Read Source address and show
draw.text((0,45), "Src Addr = " + mesh.read_source_addr(), font = Font1, fill = "BLUE")

# Read Note type and show
nodeType = mesh.read_node_type()
if nodeType == '1':
    draw.text((0,65), "Node = 1 (Terminal)", font = Font1, fill = "BLUE")
elif nodeType == '0':
    draw.text((0,65), "Node = 0 (Routing)", font = Font1, fill = "BLUE")

# Read Communication mode and show
mode = mesh.read_comm_mode()
if mode == '1':
    draw.text((0,85), "Mode = 1 (Unicast)", font = Font1, fill = "BLUE")
elif mode == '2':
    draw.text((0,85), "Mode = 2 (Multicast)", font = Font1, fill = "BLUE")
elif mode == '3':
    draw.text((0,85), "Mode = 3 (Broadcast)", font = Font1, fill = "BLUE")
elif mode == '4':
    draw.text((0,85), "Mode = 4 (Anycast)", font = Font1, fill = "BLUE")

# Show all the data on the LCD    
disp.show_image(img)
