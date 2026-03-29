import segno

data = "https://github.com/settings/profile"

qr = segno.make(data)
qr.save("github_qr.png", scale=10)

print("QR generated successfully")