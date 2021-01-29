import os

# Style Models Data

style_models_file = ['mosaic.t7', 'starry_night.t7']

style_models_name = ['Mosaic', 'Starry_night']

model_path = 'models'

style_models_dict = {name: os.path.join(model_path, filee) for name, filee in zip(style_models_name, style_models_file)}

# Style Images Data

content_images_file = ['ancient_city.jpg', 'blue-moon-lake.jpg', 'Dawn Sky.jpg', 'Dipping-Sun.jpg', 'golden_gate.jpg', 'Japanese-cherry.jpg', 'jurassic_park.jpg', 'Kinkaku-ji.jpg', 'messi.jpg', 'sagano_bamboo_forest.jpg', 'Sunlit Mountains.jpg', 'tubingen.jpg', 'winter-wolf.jpg']

content_images_name = ['Ancient_city', 'Blue-moon-lake', 'Dawn sky', 'Dipping-sun', 'Golden_gate', 'Japanese-cherry', 'Jurassic_park', 'Kinkaku-ji', 'Messi', 'Sagano_bamboo_forest', 'Sunlit mountains', 'Tubingen', 'Winter-wolf']

images_path = 'images'

content_images_dict = {name: os.path.join(images_path, filee) for name, filee in zip(content_images_name, content_images_file)}
