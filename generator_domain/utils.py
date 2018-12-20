from math import floor


def font_size(img_w, max_w=1920, max_fsize=230):
    return floor(max_fsize * (img_w / max_w))
