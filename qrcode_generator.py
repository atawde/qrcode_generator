import qrcode
from PIL import Image
from flask import Flask, render_template, request, send_file, url_for
from jinja2 import Environment, FileSystemLoader
import logging

# Data to encode
data = {
        "name":"",
        "address":"",
        "mobile": "",
        "land_line": "",
        "emergency-contact-1":"",
        "emergency-contact-2":"",
        "blood-group":"",
        "med-history": "",
        "insurance-provider": "",
        "policy-number": "",
    }

env = Environment(loader = FileSystemLoader('templates'))
logging.basicConfig(level=logging.DEBUG)

#def main():
app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = True  # Show errors

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('qr_details.html', img_file="placeholder.png")

@app.route("/submit-form", methods=['GET', 'POST'])
def generate_qr():
        if request.method == 'POST':
            data["name"] = request.form.get('name')
            data["address"] = request.form.get('address')
            data["mobile"] = request.form.get('mobile')
            data["land_line"] = request.form.get('landl')
            data["emergency-contact-1"] = request.form.get('emer1')
            data["emergency-contact-2"] = request.form.get('emer2')
            data["blood-group"] = request.form.get('bgrp')
            data["med-history"] = request.form.get('medh')
            data["insurance-provider"] = request.form.get('insp')
            data["policy-number"] = request.form.get('polnum')
            

            generate_qrcode()
            return render_template('qr_details.html', img_file="my_qrcode.png")
        
        return render_template('qr_details.html', img_file="my_qrcode.png")  #for Get method display the same form

@app.errorhandler(500)
def handle_internal_error(e):
    app.logger.exception("Internal Server Error: %s", e)
    return f"Internal Server Error: {e}", 500

def generate_qrcode():
# Create QR code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # size of each box in pixels
        border=4,  # border in boxes
    )

# Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

# Create an image from the QR Code instance
    my_qrcode = qr.make_image(fill_color="black", back_color="white")
# Save the image
    my_qrcode.save("./static/my_qrcode.png")

if __name__== "__main__":
    app.run()
    
