massage = input ('put some text :')
if len(massage) > 50:
    try:
        raise ValueError
    except Exception:
        print('the massage is too long for the post-card')
        
elif len(massage) < 20:
    print('the massage is short enough for the post-card')
else:
    print('the massage is ok for the post-card')
    