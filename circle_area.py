import math

def calculate_circle_area(radius):
    """
    円の面積を計算する関数
    
    :param radius: 円の半径
    :return: 円の面積
    """
    return math.pi * radius ** 2

if __name__ == "__main__":
    radius = 5
    area = calculate_circle_area(radius)
    print(f"半径 {radius} の円の面積は {area:.2f} です。")
