from PIL import Image
import pillow_avif
import os

i=1
dataset = os.listdir('./dataset')
for pasta in dataset:
    animal = os.listdir(f'./dataset/{pasta}')
    print(animal)
    for foto in animal:
        img = Image.open(f'./dataset/{pasta}/{foto}')
        img.save(f'./animais/animal{i}.png')
        i += 1



