from PIL import Image, ImageDraw, ImageFont
import os

sizes = [72, 96, 128, 144, 152, 192, 384, 512]

for size in sizes:
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rounded rect background (blue gradient simulation)
    radius = size // 5
    draw.rounded_rectangle([0, 0, size-1, size-1], radius=radius, fill=(29, 78, 216, 255))
    
    # Inner accent
    pad = size // 8
    draw.rounded_rectangle([pad, pad, size-1-pad, size-1-pad], radius=radius//2, fill=(37, 99, 235, 180))
    
    # Book icon (simplified)
    cx, cy = size // 2, size // 2
    bw = size * 0.45
    bh = size * 0.5
    x0 = cx - bw // 2
    y0 = cy - bh // 2
    
    # Book body
    draw.rectangle([x0, y0, cx - size*0.02, y0 + bh], fill=(255, 255, 255, 240))
    draw.rectangle([cx + size*0.02, y0, x0 + bw, y0 + bh], fill=(226, 232, 240, 200))
    
    # Lines on book
    for i in range(1, 4):
        ly = y0 + (bh / 4) * i
        draw.line([x0 + size*0.05, ly, cx - size*0.06, ly], fill=(148, 163, 184, 180), width=max(1, size//64))
    
    img.save(f'icons/icon-{size}.png', 'PNG')
    print(f'Generated icon-{size}.png')

print("All icons generated!")
