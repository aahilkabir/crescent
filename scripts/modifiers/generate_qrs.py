import qrcode
import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)


assets_dir = os.path.join(PROJECT_ROOT, 'assets')
os.makedirs(assets_dir, exist_ok=True)

def generate_qr(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Make it stylish (white on black or standard black on white)
    # The presentation is dark mode, so a white background for the QR is usually best for scannability.
    img = qr.make_image(fill_color="black", back_color="white")
    
    out_path = os.path.join(assets_dir, filename)
    img.save(out_path)
    print(f"Saved {out_path}")

generate_qr("https://riselabs.one/events/register?code=Tagore", "qr_register.png")
generate_qr("https://riselabs.one/events/certificate?code=Tagore", "qr_certificate.png")
