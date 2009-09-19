import pygoogleearth

DESKTOP = "c:\\users\\posborne\\Desktop\\"

def test_save_screenshot():
    print 'Verify that \'pygoogleearth.jpg\' is present on the Desktop'
    ge = pygoogleearth.GoogleEarth()
    ge.save_screen_shot(DESKTOP + 'pygoogleearth.jpg', 100)
    
if __name__ == '__main__':
    test_save_screenshot()
