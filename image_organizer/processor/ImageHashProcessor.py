import glob
import pickle

from PIL import Image
from PIL import ImageStat


class ImageHashProcessor():
    """Class for handling processing images into hashes"""

    @classmethod
    def hash_image_64bit(cls, image_file_name):
        """Hash an image into a 64bit integer"""
        image = cls._get_image(image_file_name)

        resized = cls._resize_to_8_8(image) 
        grey = cls._convert_to_greyscale(resized)

        mean_grey_color_value = cls._get_mean_color(grey)

        bit_string = ""
        for i in range(8):
            for j in range(8):
                if grey.getpixel((i,j)) > mean_grey_color_value:
                    bit_string =  bit_string + "0"
                else:
                    bit_string = bit_string + "1"
        hash =  int(bit_string, 2)

        return hash

    @classmethod
    def _get_image(cls, image_file_name):
        """Open the image from PIL"""
        return Image.open(image_file_name)

    @classmethod
    def _resize_to_8_8(cls, image):
        """Adjust the image to be an 8x8 image"""
        return image.resize([8,8]) 

    @classmethod
    def _convert_to_greyscale(cls, image):
        """Convert the image to grayscale"""
        return image.convert("L")

    @classmethod
    def _get_mean_color(cls, image):
        """Return the average color of the image"""
        stat = ImageStat.Stat(image)
        mean =  stat.mean
        return mean[0]
