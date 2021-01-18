import os

# Style Models Data

style_models_file = ['candy.t7', 'composition_vii.t7', 'feathers.t7', 'la_muse.t7', 'mosaic.t7', 'starry_night.t7', 'the_scream.t7', 'the_wave.t7', 'udnie.t7']

style_models_name = ['Candy', 'Composition_vii', 'Feathers', 'La_muse', 'Mosaic', 'Starry_night', 'The_scream', 'The_wave', 'Udnie']

model_path = 'models'

style_models_dict = {name: os.path.join(model_path, filee) for name, filee in zip(style_models_name, style_models_file)}

# Style Images Data

content_images_file = ['ancient_city.jpg', 'blue-moon-lake.jpg', 'Dawn Sky.jpg', 'Dipping-Sun.jpg', 'golden_gate.jpg', 'Japanese-cherry.jpg', 'jurassic_park.jpg', 'Kinkaku-ji.jpg', 'messi.jpg', 'sagano_bamboo_forest.jpg', 'Sunlit Mountains.jpg', 'tubingen.jpg', 'winter-wolf.jpg']

content_images_name = ['Ancient_city', 'Blue-moon-lake', 'Dawn sky', 'Dipping-sun', 'Golden_gate', 'Japanese-cherry', 'Jurassic_park', 'Kinkaku-ji', 'Messi', 'Sagano_bamboo_forest', 'Sunlit mountains', 'Tubingen', 'Winter-wolf']

images_path = 'images'

content_images_dict = {name: os.path.join(images_path, filee) for name, filee in zip(content_images_name, content_images_file)}
