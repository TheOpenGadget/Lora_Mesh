import lcd
import time
import lora
from PIL import Image, ImageDraw,ImageFont


# Initialize Font Typs for the LCD
Font1 = ImageFont.truetype("Font/Font00.ttf",20)
Font2 = ImageFont.truetype("Font/Font02.ttf",25)

# Inittialize the LCD
disp = lcd.LCD()
disp.clear()
disp.init()

# Initialize the Serial Port with Comm Port ttyAMA0 and Initialize Lora 
# Change comm port to ttyUSB0 in case of USB communication
mesh = lora.LoraMesh(port='/dev/ttyAMA0', baudrate=115200)    
mesh.open()
mesh.read_module_info()

# Create a image layout for showing text or image on the LCD
img = Image.new("RGB", (disp.width, disp.height), "WHITE")
draw = ImageDraw.Draw(img)

# Read the module info and show it on LCD
draw.text((30,0), "Ex - Unicast Transmit", font = Font2, fill = "RED")
disp.show_image(img)

# Set Destination address and show
mesh.set_destination_addr(44556,0)
draw.text((0,35), "Dest Addr = 44556", font = Font1, fill = "BLUE")

# Set Communication mode to Unicast
mesh.set_comm_mode(1)
draw.text((0,55), "Mode = Unicast", font = Font1, fill = "BLUE")
disp.show_image(img)

# Send the data
response = mesh.send_LORA_data('123456789')
draw.text((0,75), f"Data Sent : {response}", font = Font1, fill = "BLUE")
disp.show_image(img)

