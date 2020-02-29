import numpy as np
import cv2


class FilesCreator:
    def __init__(self):
        self.feature_base = {}

    def cut_feature(self, input_image, extremes):
        height = input_image.shape[0]
        width = input_image.shape[1]
        mask = np.zeros((height, width), dtype=np.uint8)

        points = np.array([extremes])
        mask = cv2.fillPoly(mask, points, (255))

        res = cv2.bitwise_and(input_image, input_image, mask=mask)
        rect = cv2.boundingRect(points)  # returns (x,y,w,h) of the rect
        cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
        return cropped

    def cut_face(self, input_image, feature_pos):
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

        img = cut_background(input_image,'face')
        img = cut(img, 'l_eye')
        img = cut(img, 'r_eye')

        img = cut(img, 'mouth')
        img = cut(img, 'nose')
        img = cut(img, 'r_ear')
        img = cut(img, 'l_ear')
        img = cut(img, 'l_eyebrow')
        img = cut(img, 'r_eyebrow')
        # rect = cv2.boundingRect(points)  # returns (x,y,w,h) of the rect
        # cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
        return img

    def convert_to_rgba(self, image):
        tmp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
        b, g, r = cv2.split(image)
        rgba = [b, g, r, alpha]
        dst = cv2.merge(rgba, 4)
        return dst

    def create_files(self, image, feature_pos, folder):
        for key in feature_pos:
            path = folder+"\\" + key + ".png"
            if key == 'face':
                # wypełnianie przeprowadzić manualnie
                output = self.cut_face(image, feature_pos)
                output = self.convert_to_rgba(self.cut_feature(output, feature_pos['face']))
            else:
                output = self.convert_to_rgba(self.cut_feature(image, feature_pos[key]))
            self.feature_base[key] = output
            cv2.imwrite(path, output)
        return self.feature_base


if __name__ == "__main__":
    feature_dict = {}
    feature_dict['face'] = [[202, 218], [214, 252], [224, 266], [224, 294], [240, 324], [268, 353], [292, 340],
                            [324, 318],
                            [350, 297], [364, 276], [360, 259], [369, 236], [378, 213], [388, 218], [392, 203],
                            [401, 191],
                            [407, 162], [404, 137], [386, 143], [393, 103], [390, 74], [368, 37], [340, 17], [300, 5],
                            [248, 13], [212, 34], [199, 54], [182, 105], [192, 150], [174, 143], [171, 166], [180, 184],
                            [182, 198], [189, 216], [204, 210]]
    feature_dict['l_ear'] = [[195, 151], [173, 141], [172, 174], [185, 199], [193, 223], [204, 212]]
    feature_dict['r_ear'] = [[379, 213], [389, 219], [392, 202], [399, 190], [407, 178], [410, 162], [405, 138],
                             [391, 142],
                             [384, 146], [380, 178], [381, 195]]
    feature_dict['l_eye'] = [[224, 161], [244, 171], [262, 168], [269, 161], [262, 149], [245, 149], [228, 155],
                             [224, 160]]
    feature_dict['r_eye'] = [[309, 158], [324, 166], [343, 162], [349, 160], [351, 153], [336, 146], [320, 148],
                             [311, 150]]
    feature_dict['l_eyebrow'] = [[215, 152], [229, 145], [249, 144], [264, 144], [260, 135], [244, 135], [225, 138],
                                 [212, 147]]
    feature_dict['r_eyebrow'] = [[311, 142], [325, 140], [343, 141], [355, 147], [362, 151], [354, 134], [337, 132],
                                 [318, 133], [308, 135]]
    feature_dict['nose'] = [[282, 175], [270, 192], [257, 205], [255, 218], [266, 218], [280, 217], [287, 220],
                            [303, 216],
                            [311, 216], [316, 212], [315, 200], [308, 193], [299, 179], [296, 162], [284, 164]]
    feature_dict['mouth'] = [[245, 254], [270, 263], [280, 272], [306, 265], [316, 260], [322, 251], [330, 246],
                             [308, 240],
                             [290, 241], [282, 244], [275, 241], [260, 244], [248, 250], [248, 250]]
    feature_dict['hair'] = [[196, 150], [191, 125], [202, 114], [214, 103], [208, 91], [208, 62], [226, 55], [262, 54],
                            [291, 54], [320, 53], [346, 58], [354, 68], [360, 89], [364, 106], [372, 129], [382, 141],
                            [387, 141], [390, 124], [395, 94], [388, 64], [364, 36], [336, 16], [304, 6], [272, 6],
                            [225, 17], [192, 54], [178, 118], [188, 148]]
    feature_dict['suit'] = [[222, 296], [166, 320], [92, 348], [48, 386], [26, 480], [477, 477], [479, 356], [407, 317],
                            [387, 307], [364, 270], [354, 295], [339, 321], [305, 330], [268, 359], [234, 318],
                            [228, 298]]

    img = cv2.imread("samplephoto.png")
    f = FilesCreator()
    f.create_files(img, feature_dict['layers'], "face2")
