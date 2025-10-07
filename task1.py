import numpy as np
from PIL import Image

def create_black_image():
    """Создает полностью черное изображение"""
    H, W = 300, 400
    
    # Создаем матрицу нулей
    img = np.zeros((H, W), dtype=np.uint8)
    
    # Сохраняем изображение
    Image.fromarray(img, mode='L').save('black.png')
    print("✓ Создано черное изображение: black.png")

def create_white_image():
    """Создает полностью белое изображение"""
    H, W = 300, 400
    
    # Создаем матрицу со значениями 255
    img = np.full((H, W), 255, dtype=np.uint8)
    
    Image.fromarray(img, mode='L').save('white.png')
    print("✓ Создано белое изображение: white.png")

def create_red_image():
    """Создает полностью красное изображение"""
    H, W = 300, 400
    
    # Создаем 3-канальную матрицу
    img = np.zeros((H, W, 3), dtype=np.uint8)
    
    # Заполняем красный канал
    img[:, :, 0] = 255
    
    Image.fromarray(img, mode='RGB').save('red.png')
    print("✓ Создано красное изображение: red.png")

def create_gradient_image():
    """Создает изображение с градиентом"""
    H, W = 300, 400
    
    # Создаем матрицу для градиента
    img = np.zeros((H, W), dtype=np.uint8)
    
    # Заполняем значениями (x + y) % 256 через присвоение
    for y in range(H):
        for x in range(W):
            img[y, x] = (x + y) % 256

    Image.fromarray(img, mode='L').save('gradient.png')
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