import qrcode
from PIL import Image
from flask import Flask, render_template, request, send_file, url_for
from jinja2 import Environment, FileSystemLoader

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

#def main():
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
#    template = env.get_template('qr_details.html')
#    img_url = url_for('static', filename='placeholder.png')
#    output = template.render()
#    print(output)
    return render_template('qr_details.html', img_file="placeholder.png")
#    return template.render(root_url="", imgurl='placeholder.png')

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
            

            generate_qr()
#        return f'Processing QR for {data["name"]}'
#            return send_file(generate_qr(), mimetype='image/png')
#            return send_file('my_qrcode.png', mimetype='image/png')
            return render_template('qr_details.html', img_file="my_qrcode.png")

def generate_qr():
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
#    return my_qrcode

#    pil_img = Image.open('my_qrcode.png')
#    pil_img.show()

if __name__== "__main__":
#    main()
    app.run()
    
"""
to create json object of qrcode
import qrcode
import json
from PIL import Image
import io
import base64

# Data to encode in QR code
data = "Your data here"

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')

# Save image to a bytes buffer
buffer = io.BytesIO()
img.save(buffer, format="PNG")
img_bytes = buffer.getvalue()

# Encode image bytes to base64 string
img_base64 = base64.b64encode(img_bytes).decode('utf-8')

# Create JSON object
json_obj = {
    'qr_code': img_base64
}

# Convert to JSON string
json_str = json.dumps(json_obj)

print(json_str)
........................
to create qrcode from json object----
import json
import base64
from PIL import Image
import io
import qrcode

# Example JSON string received
json_str = '{"qr_code": "<base64-encoded-image>"}'  # Replace with your JSON string

# Parse the JSON
json_obj = json.loads(json_str)

# Extract the base64 image string
img_base64 = json_obj['qr_code']

# Decode the base64 string to bytes
img_bytes = base64.b64decode(img_base64)

# Load image from bytes
image = Image.open(io.BytesIO(img_bytes))
image.show()  # To display the image if needed

# If you want to recreate the QR code from the image, you can do so (though this is usually unnecessary)
# For demonstration, if the image contains encoded data, you'd need OCR or decode method
# Alternatively, if you only want to just display/save the image, this is sufficient
image.save("decoded_qr.png")
"""
