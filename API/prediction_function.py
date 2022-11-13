import base64

image = ""

def init_model():
    pass
    


init_model()


def testimage(base64image:str = None) -> int:
    """Test image and returns confidence level

    Args:
        base64image (str, optional): JPG image of mole. Defaults to None.

    Returns:
        int: percent chance
    """
    image = base64.decode()
    test_result = 0
    
    

    return test_result

# test function
print(testimage(image))