import numpy as np
import cv2


class Generator:
    def __init__(self):
        self.face_image = np.zeros((500, 500, 3), np.uint8)
        self.face_image[:] = (0, 0, 0)
        self.face_image = self.convert_to_rgba(self.face_image)

        self.features = {}
        self.model = {'face': {'size': {'x': 280, 'y': 350}, 'x_shift': 0, 'y_shift': 0},
                      'l_ear': {'size': {'x': 45, 'y': 75}, 'x_shift': -120, 'y_shift': 0},
                      'r_ear': {'size': {'x': 45, 'y': 75}, 'x_shift': 120, 'y_shift': 0},
                      'l_eye': {'size': {'x': 50, 'y': 25}, 'x_shift': -50, 'y_shift': -45},
                      'r_eye': {'size': {'x': 50, 'y': 25}, 'x_shift': 50, 'y_shift': -45},
                      'l_eyebrow': {'size': {'x': 55, 'y': 20}, 'x_shift': -50, 'y_shift': -65},
                      'r_eyebrow': {'size': {'x': 55, 'y': 20}, 'x_shift': 50, 'y_shift': -65},
                      'nose': {'size': {'x': 60, 'y': 70}, 'x_shift': 0, 'y_shift': 0},
                      'mouth': {'size': {'x': 90, 'y': 40}, 'x_shift': 0, 'y_shift': 85},
                      'hair': {'size': {'x': 250, 'y': 270}, 'x_shift': 10, 'y_shift': -60}}  #y 130 # x230

    def get_files(self, feature_list):
        for feature in feature_list:
            try:
                feature_img = cv2.imread(feature_list[feature], cv2.IMREAD_UNCHANGED)
                if feature == 'hair':
                    print("hair")
                    yh, xh, lh = feature_img.shape
                    target_x = xh
                    target_y = yh
                    yf, xf, lf = self.features['face'].shape

                    if self.model['face']['size']['x'] < xh:
                        target_x = self.model['face']['size']['x']+60 # na długie
                        print(self.model['face']['size']['x']," ? ",xh)
                        print("+70")
                    else:
                        target_x = self.model['face']['size']['x'] -30  # na krótkie
                        print(self.model['face']['size']['x'], " ? ", xh)
                    if self.model['face']['size']['y'] < yh:
                        target_y = self.model['face']['size']['y']
                        self.model['hair']['y_shift'] = -50
                    else:
                        target_y = self.model['face']['size']['y']-20
                        self.model['hair']['y_shift'] = -50
                    print(xf, yf)
                    feature_img = cv2.resize(feature_img, (target_x, target_y))
                    self.features[feature] = feature_img
                else:
                    feature_img = cv2.resize(feature_img,
                                             (self.model[feature]['size']['x'], self.model[feature]['size']['y']))
                    self.features[feature] = feature_img
            except Exception:
                print("e")

    def insert_feature(self, background, feature_img, x_shift=0, y_shift=0):
        def start_point(width, height, center_x, center_y, x_shift=0, y_shift=0):
            return center_x - int(width / 2) + x_shift, center_y - int(height / 2) + y_shift

        def draw_rects(image, rects, color):
            for x1, y1, x2, y2 in rects:
                cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)

        b_height, b_width, b_chan = background.shape
        f_height, f_width, f_chan = feature_img.shape
        p0 = start_point(f_width, f_height, int(b_width / 2), int(b_height / 2), x_shift=x_shift, y_shift=y_shift)
        x = p0[0]
        y = p0[1]
        # draw_rects(background, [[p0[0], p0[1], p0[0] + f_width, p0[1] + f_height]], 127)
        for i in range(f_height):
            for j in range(f_width):
                if feature_img[i, j, 3] == 255:  # sprawdzanie maski
                    try:
                        background[i + y, j + x] = feature_img[i, j]
                    except Exception:
                        break
        return background

    def insert_hair(self, background, feature_img, x_shift=0, y_shift=0):
        def start_point(width, height, center_x, center_y, x_shift=0, y_shift=0):
            return center_x - int(width / 2) + x_shift, center_y - int(height / 2) + y_shift

        def draw_rects(image, rects, color):
            for x1, y1, x2, y2 in rects:
                cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)

        b_height, b_width, b_chan = background.shape
        f_height, f_width, f_chan = feature_img.shape
        p0 = start_point(f_width, f_height, int(b_width / 2), int(b_height / 2), x_shift=x_shift, y_shift=y_shift)
        x = p0[0]
        y = p0[1]
        draw_rects(background, [[p0[0], p0[1], p0[0] + f_width, p0[1] + f_height]], 127)
        for i in range(f_height):
            for j in range(f_width):
                if feature_img[i, j, 3] == 255:  # sprawdzanie maski
                    try:
                        background[i + y, j + x] = feature_img[i, j]
                    except Exception:
                        break
        return background

    def convert_to_rgba(self, image):
        tmp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
        b, g, r = cv2.split(image)
        rgba = [b, g, r, alpha]
        dst = cv2.merge(rgba, 4)
        return dst

    def write_face(self, path):
        cv2.imwrite(path, self.face_image)

    def create_face(self, eye_distance=50):
        background = self.face_image
        background = self.insert_feature(background, self.features['face'])
        background = self.insert_feature(background, self.features['mouth'], y_shift=self.model['mouth']['y_shift'])
        background = self.insert_feature(background, self.features['nose'], y_shift=self.model['nose']['y_shift'])
        background = self.insert_feature(background, self.features['l_eye'], x_shift=-eye_distance, y_shift=self.model['l_eye']['y_shift'])
        background = self.insert_feature(background, self.features['r_eye'], x_shift=eye_distance, y_shift=self.model['r_eye']['y_shift'])
        background = self.insert_feature(background, self.features['l_eyebrow'], x_shift=-eye_distance, y_shift=self.model['l_eyebrow']['y_shift'])
        background = self.insert_feature(background, self.features['r_eyebrow'], x_shift=eye_distance, y_shift=self.model['r_eyebrow']['y_shift'])
        background = self.insert_feature(background, self.features['l_ear'], x_shift=self.model['l_ear']['x_shift'], y_shift=self.model['l_ear']['y_shift'])
        background = self.insert_feature(background, self.features['r_ear'], x_shift=self.model['r_ear']['x_shift'], y_shift=self.model['r_ear']['y_shift'])
        background = self.insert_feature(background, self.features['hair'], y_shift=self.model['hair']['y_shift'])
        self.face_image = background


if __name__ == "__main__":
    feature_list = {'face': "Files/Features/InputFace-00/face.png", 'l_ear': "Files/Features/InputFace-00/l_ear.png", 'r_ear': "Files/Features/InputFace-00/r_ear.png",
                    'l_eye': "Files/Features/InputFace-00/l_eye.png", 'r_eye': "Files/Features/InputFace-00/r_eye.png", 'l_eyebrow': "Files/Features/InputFace-00/l_eyebrow.png",
                    'r_eyebrow': "Files/Features/InputFace-00/r_eyebrow.png", 'nose': "Files/Features/InputFace-00/nose.png", 'mouth': "Files/Features/InputFace-00/mouth.png",
                    'hair': "Files/Features/InputFace-00/hair.png"}
    g = Generator()
    g.get_files(feature_list)
    g.create_face()
    cv2.namedWindow('Display image')
    cv2.imshow('Display image', g.face_image)
    cv2.waitKey(100000)
