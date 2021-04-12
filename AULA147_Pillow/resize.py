import os
from PIL import Image


def main(path, new_width=800):
    if not os.path.isdir(path):
        raise NotADirectoryError(f'{path} não existe')

    for root, dirs, files in os.walk(path):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)  # separando o nome do arquivo e da extensão

            converted_tag = '_CONVERTED'

            new_file = file_name + converted_tag + extension  # o nome do arquivo convertido
            new_file_full_path = os.path.join(root, new_file)

            if converted_tag in file_full_path:  # caso a foto já esteja convertida, ela não passa no laço novamente
                continue

            img_pillow = Image.open(file_full_path)

            width, height = img_pillow.size
            new_height = round(new_width * height / width) # calculando a nova altura

            new_image = img_pillow.resize((new_width, new_height), Image.LANCZOS)
            new_image.save(new_file_full_path, optimize=True, quality=70, exif=img_pillow.getexif())

            print(f'{file_full_path} convertido com sucesso!')
            new_image.close()
            img_pillow.close()


if __name__ == '__main__':
    main_images_folder = 'fotos'
    main(main_images_folder, new_width=640)
