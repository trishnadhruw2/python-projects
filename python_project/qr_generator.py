import qrcode as qr
img=qr.make("https://www.youtube.com/results?search_query=acharya+prashant")
img.save("acharya_prashant.png")