while True:
    width = int(input("w"))
    height = int(input("h"))

    print(
        f"╔{"═"*width}╗",
        sep="", end="\n", flush=True)
    while height>0:
        print(
            f"║{" "*width}║",
        sep="", end="\n", flush=True)
        height-=1
    print(
        f"╚{"═"*width}╝",
        sep="", end="\n", flush=True)