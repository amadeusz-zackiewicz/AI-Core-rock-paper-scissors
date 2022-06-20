from app.camera_rps import CameraRPS
from app.manual_rps import ManualRPS

if __name__ == "__main__":
    print("\nPlease pick which version of the you would like to play:")
    print("Input 'm' for manual version")
    print("Input 'c' for camera version")
    inp = input("[m / c]: ")
    if inp == "m":
        g = ManualRPS()
    elif inp == "c":
        g = CameraRPS()
    else:
        quit()

    while True:
        if not g.play():
            g.quit()
            break

    