def banner_text(text=" ",screen_width=80):
    if len(text)>screen_width - 4:
        raise ValueError("string {0} is larger than the specified width {1}".format(text,screen_width)) ##value error becaue the type is correct

        #print("PLEASE CHECK YOUR  BANNER SIZE")
        #print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text=="*":
        print('*'*screen_width)
        print("#"*screen_width)
    else:
        centred_text=text.center(screen_width-8)
        output_string="**##{0}##**".format(centred_text)
        print(output_string)


banner_text('*')
banner_text("Always look on the bright side of life....")
banner_text("If life seems jolly rotten,")
banner_text("Theres something you have forgotten!")
banner_text("And that to laugh and laugh and sing")
banner_text(screen_width=80)
banner_text("When you are feeling in the dumps,")
banner_text("Dont be silly chumps,")
banner_text("Just purse your lips and whistle - thats the thing!")
banner_text("And.... always look on the bright side of life...")
banner_text('*')


