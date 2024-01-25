import qrcode

features = qrcode.QRCode(version=1,box_size=30,border=2)
features.add_data('https://starlord7544.github.io/Bootcamp-Portfolio/')

features.make(fit=True)

generate_image = features.make_image(fill_color="black",back_color =" white") 
generate_image.save("portfolio.png")