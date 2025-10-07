from PIL import Image

def create_black_image():
    """Создает полностью черное изображение"""
    W, H = 400, 300
    
    # Создаем черное изображение (0 = черный)
    black_image = Image.new('L', (W, H), color=0)
    black_image.save('black.png')
    print("✓ Создано черное изображение: black.png")

def create_white_image():
    """Создает полностью белое изображение"""
    W, H = 400, 300
    
    # Создаем белое изображение (255 = белый)
    white_image = Image.new('L', (W, H), color=255)
    white_image.save('white.png')
    print("✓ Создано белое изображение: white.png")

def create_red_image():
    """Создает полностью красное изображение"""
    W, H = 400, 300
    
    # Создаем красное изображение (RGB режим)
    red_image = Image.new('RGB', (W, H), color=(255, 0, 0))
    red_image.save('red.png')
    print("✓ Создано красное изображение: red.png")

def create_gradient_image():
    """Создает изображение с градиентом"""
    W, H = 400, 300
    # Создаем новое изображение в режиме 'L'
    grad_image = Image.new('L', (W, H))
    pixels = grad_image.load()  # Получаем объект для изменения пикселей

    for x in range(W):
        for y in range(H):
            # Значение пикселя = (x + y) % 256
            pixels[x, y] = (x + y) % 256

    grad_image.save('gradient.png')
    print("✓ Создано градиентное изображение: gradient.png")

def main():
    """Основная функция, выполняющая все задания"""
    print("Выполнение задания 1: Работа с изображениями")
    print("=" * 50)
    
    create_black_image()
    create_white_image()
    create_red_image()
    create_gradient_image()
    
    print("=" * 50)
    print("Все изображения созданы успешно!")
    print("Проверьте файлы в папке с программой:")

if __name__ == "__main__":
    main()