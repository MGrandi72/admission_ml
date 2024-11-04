import qrcode

url = "https://admission-app.streamlit.app/"

img = qrcode.make(url)

img.save("qr_code_example.png")
