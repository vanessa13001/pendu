import string
upper_letters = string.ascii_uppercase
letters = string.ascii_letters
cursor = {
    "heavy_clear" : "\033[3J\033[1;0H\033[0J",
}
def cursor_line(y,x=0):
    coordinate = "\033[" + str(y) + ";" + str(x) + "H"
    return coordinate