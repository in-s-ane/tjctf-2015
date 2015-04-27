from PIL import Image
import zbar
import os, glob

qr_files = [qr_file for qr_file in glob.glob("images/*") if os.path.isfile(qr_file)]
totps = []

for qr_file in qr_files:
    scanner = zbar.ImageScanner()
    scanner.parse_config('enable')
    image = Image.open(qr_file).convert('L')
    width, height = image.size
    raw = image.tostring()
    barcode = zbar.Image(width, height, 'Y800', raw)
    scanner.scan(barcode)
    for symbol in barcode:
        print 'Decoded', symbol.type, 'symbol:', '"%s"' % symbol.data
    del(image)
    totps.append(symbol.data)

print totps
