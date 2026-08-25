import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import urllib.request

url = "https://riselabs.one/events/register?code=THINKTG101"
assets_dir = os.path.join(PROJECT_ROOT, 'assets')
os.makedirs(assets_dir, exist_ok=True)
out_path = os.path.join(assets_dir, "qr_thinktg101.png")

# First try qrcode package
try:
    import qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(out_path)
    print(f"Generated QR code using qrcode package at: {out_path}")
except Exception as e:
    print(f"qrcode package failed ({e}), falling back to QR API...")
    qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=600x600&data={urllib.parse.quote(url)}"
    req = urllib.request.Request(qr_api_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as res:
        with open(out_path, "wb") as f:
            f.write(res.read())
    print(f"Downloaded QR code from API to: {out_path}")
