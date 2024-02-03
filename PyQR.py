import pyqrcode
import png

def generate_qr_code(url):
    # Generate QR Code
    qr_code = pyqrcode.create(url)

    # Save as SVG
    svg_filename = "qr.svg"
    qr_code.svg(svg_filename, scale=8)
    print(f"QR Code saved as {svg_filename}")

    # Save as PNG
    png_filename = "qr.png"
    qr_code.png(png_filename, scale=8)
    print(f"QR Code saved as {png_filename}")

def main():
    # Get user input for URL
    user_input = input("Enter the URL: ").strip()


    # Generate and save QR Code
    generate_qr_code(user_input)

if __name__ == "__main__":
    main()


#########        
    #
    #
    #
    #
    #
    #
#########