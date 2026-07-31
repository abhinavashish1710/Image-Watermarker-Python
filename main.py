from PIL import Image, ImageDraw, ImageFont

image_path = input("Enter image path: ")

try:
    image = Image.open(image_path)

    draw = ImageDraw.Draw(image)

    text = input("Enter watermark text: ")

    font = ImageFont.load_default()

    width, height = image.size

    draw.text((width - 150, height - 30), text, fill="white", font=font)

    output = "watermarked_image.png"

    image.save(output)

    print(f"Watermarked image saved as {output}")

except Exception as e:
    print("Error:", e)
