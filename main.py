import requests
from PIL import Image


def create_random_bmp():
    img = Image.new('RGB', (128, 128))
    pixels = img.load()
    total_pix = 128 * 128 * 3
    rnd_arr = []
    while True:
        if total_pix < 10000:
            rnd_arr += get_random_arr(total_pix, 0, 255)
            break
        else:
            rnd_arr += get_random_arr(10000, 0, 255)
        total_pix -= 10000
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = rnd_arr[img.size[0] * 3 * i + 3 * j]
            g = rnd_arr[img.size[0] * 3 * i + 3 * j + 1]
            b = rnd_arr[img.size[0] * 3 * i + 3 * j + 2]
            pixels[i, j] = (r, g, b)
    img.show()


def get_random_arr(n_num, min_num, max_num):
    """
    Input requirements for generating random numbers
    :return: an array of random numbers
    """
    params = {
        'num': n_num,
        'min': min_num,
        'max': max_num,
        'col': 1,
        'format': 'plain',
        'rnd': 'new',
        'base': 10
    }

    r = requests.get('https://www.random.org/integers/?', params=params)
    if r.status_code == 200:
        raw_arr = r.text.strip().split('\n')
        int_arr = list(map(lambda x: int(x), raw_arr))
        return int_arr
    else:
        print("Something goes wrong! Probably not enough quota or input parameters are wrong")
        return []


def get_random_num():
    str1 = input("How many random numbers do you want to generate? Should be less than 10,000:\n")
    num1 = int(str1)

    str2 = input('Each number should have a value bigger or equal to:\n')
    num2 = int(str2)

    str3 = input('Each number should have a value smaller or equal to:\n')
    num3 = int(str3)

    res = get_random_num(num1, num2, num3)
    print(res)


if __name__ == '__main__':
    create_random_bmp()
