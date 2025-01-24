import string
upper_letters = string.ascii_uppercase
cursor = {
    "save" : "\033[s",
    "load" : "\033[u",

    "line_clear" : "\033[2K",
    "light_line_clear" : "\033[0K",
    "light_clear" : "\033[0J",
    "heavy_clear" : "\033[3J\033[1;0H\033[0J",

    "bold_start" : "\033[1m",
    "dim_start" : "\033[2m",
    "bold_dim_end" : "\033[22m",

    "underline_start" : "\033[4m",
    "underline_end" : "\033[24m",

    "calc_box_style_start" : "\033[0;1;38;5;129m",
    "historic_data_style_start" : "\033[0;1;2;38;5;82m",
    "results_data_style_start" : "\033[0;1;38;5;82m",

    "instructions_style_start" : "\033[0;37m",
    "result_message_style_start" : "\033[0;1;37m",
    "error_message_style_start" : "\033[0;6;1;31m",
    "happy_message_style_start" : "\033[0;6;1;38;5;201m",

    "style_finish" : "\033[0m"
}
def cursor_line(y,x=0):
    coordinate = "\033[" + str(y) + ";" + str(x) + "H"
    return coordinate