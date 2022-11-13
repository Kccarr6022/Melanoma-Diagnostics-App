###############################################
# TASK
# --------------------
#
# 1. import JPG file into python
# 2. pass the JPG into function testimage as an argument(final line)
# 3. Add model from kaggle to testimage function so that it returns a prediction
# 4. If model is working it shall return a number that is greater than 0
#
###############################################
import base64

image = ""


def testimage(image = None) -> int:
    """Test image and returns confidence level

    Args:
        base64image (str, optional): JPG image of mole. Defaults to None.

    Returns:
        int: percent chance of having melanoma as an int out of 100
    """
    test_result:int = 0
    
    # one line 
    # #################### 


    return int(test_result)

# test function
print(f" This image has a {testimage(image)}% chance of being melanoma")