from PIL import Image

src = 'photos/8129-logo-t.png'
out = 'favicon.ico'

img = Image.open(src).convert('RGBA')
# Ensure a square canvas by padding transparent background if needed
size = max(img.size)
if img.size[0] != img.size[1]:
    square = Image.new('RGBA', (size, size), (0,0,0,0))
    square.paste(img, ((size - img.size[0]) // 2, (size - img.size[1]) // 2))
    img = square

# Save multi-size ICO
img.save(out, sizes=[(64,64),(48,48),(32,32),(16,16)])
print('Created', out)
