secret_number=9
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess=int(input('guess :'))
    guess_count=guess_count+1
    if guess==secret_number:
        print('you won!')
        break
    else:
        if guess_limit-guess_count==0:
            print('you faild!')
        else:
            print('enter anohter number you has '+str(guess_limit-guess_count)+' chance')
