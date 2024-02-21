from PIL import Image, ImageDraw, ImageFont

width, height = 1920, 1080
canvas = Image.new("RGB", (width, height), color="black")  # Background color

font_path = "fonts/JetBrains Mono Bold Italic Nerd Font Complete Mono.ttf"
font = ImageFont.truetype(font_path, size=48)  # Adjust font size as needed

# user_string = input("Enter your message for the wallpaper: ")
user_string = """
My time table with awesome shit!!

asf


asd
"""

text_width, text_height = (max(map(lambda a: len(a), user_string.split('\n'))),  len(user_string.split('\n')))
if text_width > width - 20:  # Adjust margin
    lines = user_string.split()
    wrapped_text = "\n".join([line for i, line in enumerate(lines) if font.getsize(line)[0] < width - 20])
else:
    wrapped_text = user_string

draw = ImageDraw.Draw(canvas)
text_x = (width - text_width) // 2
text_y = (height - text_height) // 2

draw.text((text_x, text_y), wrapped_text, font=font, fill="white")  # Adjust text color

output_path = "my_wallpaper.png"
canvas.save(output_path)
print(f"Wallpaper created successfully: {output_path}")