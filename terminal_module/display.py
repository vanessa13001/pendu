from terminal_module.__settings__ import cursor
'''
    clear entire terminal from position 0,0
'''
def clear_print():
    print(f"{cursor["heavy_clear"]}",
        sep="", end="", flush=True)
