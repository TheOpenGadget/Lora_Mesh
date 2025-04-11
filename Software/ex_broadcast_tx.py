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

# Show text on LCD
draw.text((20,0), "Ex - Broadcast Transmit", font = Font2, fill = "RED")
disp.show_image(img)

# Set Communication mode to Broadcast ()
mesh.set_comm_mode(3)
draw.text((0,35), "Mode = Broadcast", font = Font1, fill = "BLUE")
disp.show_image(img)

# Send the data
response = mesh.send_LORA_data('1234')
draw.text((0,65), f"Data Sent : {response}", font = Font1, fill = "BLUE")
disp.show_image(img)

