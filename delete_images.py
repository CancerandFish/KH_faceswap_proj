import os

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Delete images')
    parser.add_argument('--path', '-p', type=str, default='images', help='path to images')
    args = parser.parse_args()
    return args


# list all the images in the folder
def list_images(path):
    for file in os.listdir(path):            
        if int(file[-7:-6]) % 5 != 0:
            os.remove(path + '/' + file)


if __name__ == '__main__':
    args = parse_args()
    list_images(args.path)
    
