def key_func(key, spin, turn_h, turn_v, angle_h, angle_v, render_quality):

    key = ord(key)
    # Esc para sair
    if key==27:
        exit(0)
    elif key==ord('s'):
        spin = not spin
    elif key==ord('a'):
        turn_h = -1
    elif key==ord('d'):
        turn_h = 1
    elif key==ord('w'):
        turn_v = 0.5
    elif key==ord('x'):
        turn_v = -0.5
    
    # Controle de render
    elif key==ord('+'):
        render_quality += 5
    elif key==ord('-'):
        render_quality -= 2
    
    else:
        angle_h = 300.0
        angle_v = 0
        turn_h = 1
        turn_v = 0
        render_quality = 100   