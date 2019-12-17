import opencv


class CreditCardReader():
    def __init__(self, image):
        self.image = image

    def detect(self):
        # initialize a rectangular and square kernel
        rect_kernel = opencv.get_morphology_rect(size=(9, 3))
        square_kernel = opencv.get_morphology_rect(size=(5, 5))

        # Find light regions against a dark background (i.e., credit card numbers)
        gray = opencv.convert_to_gray_scale(self.image)
        tophat = opencv.morphology_tophat(gray, rect_kernel)

        # isolate digits
        grad_x = opencv.apply_scharr_gradient(tophat, dx=1, dy=0)
        grad_x = opencv.normalize_gradient(grad_x, opencv.GRADIENT_TYPE_UINT_8)

        # eliminate gaps in between credit card number digits
        grad_x = opencv.morphology_close(grad_x, rect_kernel)
        thresh = opencv.apply_otsus_threshold(grad_x, 0, 255)

        # apply close again for eliminate gaps
        thresh = opencv.morphology_close(thresh, square_kernel)

        # find grouped digits
        digits = self._find_digit_groups(thresh)

        output = self._draw_digits_contours(self.image, digits)
        opencv.show(output)

    @staticmethod
    def _draw_digits_contours(image, digits):
        output_image = opencv.resize(image, width=300)
        for (i, (gX, gY, gW, gH)) in enumerate(digits):
            opencv.draw_rectangle(output_image, (gX - 5, gY - 5), (gX + gW + 5, gY + gH + 5), (0, 0, 255), 2)
        return output_image

    @staticmethod
    def _find_digit_groups(image, sort=True):
        contours = opencv.grab_contours(image)

        digit_group_locations = []
        for (i, contour) in enumerate(contours):
            x, y, w, h = opencv.get_bounding_rect(contour)
            aspect_radio = w / float(h)

            if 2.5 < aspect_radio < 4.0:  # wider than it is tall (values found experimentally)
                if (40 < w < 55) and (10 < h < 20):
                    digit_group_locations.append((x, y, w, h))

        return sorted(digit_group_locations, key=lambda x: x[0]) if sort else digit_group_locations
