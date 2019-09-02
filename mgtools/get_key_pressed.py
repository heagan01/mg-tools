from tkinter import Tk, Frame


def __set_key(e, root, key_pressed):
    """
    e - event with attribute 'char', the released key
    """
    if e.char:
        key_pressed['value'] = e.char
        root.destroy()


def get_key(msg="Press any key ...", time_to_sleep=3):
    """
    msg - set to empty string if you don't want to print anything
    time_to_sleep - default 3 seconds
    """
    if msg:
        print(msg)
    key_pressed = {"value": ''}
    root = Tk()
    root.overrideredirect(True)
    frame = Frame(root, width=0, height=0)
    frame.bind("<KeyRelease>", lambda f: __set_key(f, root, key_pressed))
    frame.pack()
    root.focus_set()
    frame.focus_set()
    frame.focus_force()  # doesn't work in a while loop without it
    root.after(time_to_sleep * 1000, func=root.destroy)
    try:
        root.mainloop()
    except KeyboardInterrupt as e:
            root.destroy()
            key_pressed['value'] = None
    root = None  # just in case
    return key_pressed['value']


def __main():
        c = ''
        while c == '':
                c = get_key("Choose your weapon ... ", 2)
        print(c)

if __name__ == "__main__":
    __main()
