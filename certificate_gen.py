from PIL import Image, ImageDraw, ImageFont
import os
import json

output_dir = "certificates" #create a folder
os.makedirs(output_dir, exist_ok=True)

certificate_path = "certificate.png"
font_path = r"C:\Users\Syed Omar Albeez\Downloads\Poppins,Quicksand\Quicksand\static\Quicksand-SemiBold.ttf" #downlaod font folder whichever is needed

# Verify font file exists
if not os.path.exists(font_path):
    raise FileNotFoundError(f"Font file not found at {font_path}")

json_file_path = 'participants.json'
with open(json_file_path, 'r', encoding='utf-8') as file:
    participants = json.load(file)

font_size = 210
font_color = (255, 255, 255)

template_image = Image.open(certificate_path)
image_width, image_height = template_image.size

y = 1950

for participant in participants:
    full_name = f"{participant['name']}"
    # full_name = f"{participant['f_name']} {participant['l_name']}"

    image = Image.open(certificate_path).convert("RGBA")
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(font_path, font_size)
    except OSError as e:
        print(f"Error loading font: {e}")
        font = ImageFont.load_default()
    
    text_bbox = draw.textbbox((0, 0), full_name, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    x = (image_width - text_width) / 2

    draw.text((x, y), full_name, font=font, fill=font_color)
    
    output_path = os.path.join(output_dir, f"{participant['name']}.png")
    image.save(output_path)

print("Certificates generated successfully.")