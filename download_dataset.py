from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

response().download('Rhipidura phoenicura', 655)
response().download('Pteruthius flaviscapis', 655)
response().download('Cochoa azurea', 655)
response().download('Ficedula hyperythra', 655)

# print(response().urls('Nisaetus bartelsi', 655))