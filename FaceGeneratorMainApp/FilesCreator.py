import os

import numpy as np
import json
import cv2


class FilesCreator:
    def __init__(self):
        self.feature_base = {}

    def cutFeature(self, input_image, extremes):
        height = input_image.shape[0]
        width = input_image.shape[1]
        mask = np.zeros((height, width), dtype=np.uint8)

        points = np.array([extremes])
        mask = cv2.fillPoly(mask, points, (255))

        res = cv2.bitwise_and(input_image, input_image, mask=mask)
        rect = cv2.boundingRect(points)  # returns (x,y,w,h) of the rect
        cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
        return cropped

    def cutFace(self, input_image, feature_pos):
        height = input_image.shape[0]
        width = input_image.shape[1]

        def cut_background(img, name):
            mask = np.full((height, width), 0, dtype=np.uint8)
            points = np.array([feature_pos[name]])
            mask = cv2.fillPoly(mask, points, (255))
            res = cv2.bitwise_and(img, img, mask=mask)
            return res

        def cut(img, name):
            mask = np.full((height, width), 255, dtype=np.uint8)
            points = np.array([feature_pos[name]])
            mask = cv2.fillPoly(mask, points, (0))
            res = cv2.bitwise_and(img, img, mask=mask)
            return res

        output_image = cut_background(input_image,'face')
        output_image = cut(output_image, 'l_eye')
        output_image = cut(output_image, 'r_eye')

        output_image = cut(output_image, 'mouth')
        output_image = cut(output_image, 'nose')
        output_image = cut(output_image, 'r_ear')
        output_image = cut(output_image, 'l_ear')
        output_image = cut(output_image, 'l_eyebrow')
        output_image = cut(output_image, 'r_eyebrow')
        return output_image

    def convertToRgba(self, image):
        tmp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
        b, g, r = cv2.split(image)
        rgba = [b, g, r, alpha]
        dst = cv2.merge(rgba, 4)
        return dst

    def createFiles(self, image, feature_pos, folder):
        def _path(relative):
            p = os.path.join(os.environ.get("_MEIPASS2", os.path.abspath(".")), relative)
            print("Path:", p)
            return p
        for key in feature_pos:
            path = "Files\\Features\\"+folder+"\\" + key + ".png"
            if not os.path.isdir("Files\\Features\\"+folder):
                try:
                    os.mkdir(_path("Files\\Features\\"+folder))
                except:
                    pass
            if key == 'face':
                # for better effect fill holes manually (using for example gimp)
                output = self.cutFace(image, feature_pos)
                output = self.convertToRgba(self.cutFeature(output, feature_pos['face']))
            else:
                output = self.convertToRgba(self.cutFeature(image, feature_pos[key]))
            self.feature_base[key] = output
            cv2.imwrite(path, output)
        return self.feature_base


if __name__ == "__main__":
    while True:
        f = FilesCreator()
        while True:
            img_path = input("Input image path: ")
            try:
                img = cv2.imread(img_path)
            except FileNotFoundError:
                img = None
                print("Image not found=", img_path)
                break
            feature_dict_path = input("feature dict: ")
            try:
                with open(feature_dict_path, 'r') as json_file:
                    feature_dict = json.load(json_file)
            except EnvironmentError:
                feature_dict = None
                print("File not found=", img_path)
                break
            dir_name = input("Output directory: ")
            if img is not None and feature_dict is not None:
                f.createFiles(img, feature_dict, dir_name)
            break
