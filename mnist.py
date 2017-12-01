mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)


MANN的
def transform_image(image_path, angle=0., s=(0,0), size=(20,20)):
    original = imread(image_path, flatten=True)
    rotated = np.maximum(np.minimum(rotate(original, angle=angle, cval=1.), 1.), 0.)
    shifted = shift(rotated, shift=s)
    resized = np.asarray(imresize(rotated, size=size), dtype=np.float32)/255
    inverted = 1. - resized
    max_value = np.max(inverted)
    if max_value > 0:
        inverted /= max_value
    return inverted
