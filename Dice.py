# import tkinter 
# import PIL
# from PIL import ImageTk
# from PIL import Image
# # //from PIL import Image, ImageTK
# import random

# root = tkinter.Tk()
# root.geometry('400x400')
# root.title('Roll the Dice')


# root.mainloop()

# BlankLine = tkinter.Label(root, text="")
# BlankLine.pack()
# HeadingLabel = tkinter.Label(root, text="Hello from Mantasha" ,
#                           fg = "light green",
#                           bg = "dark green",
#                          font = "Times"
#                         #  font "Helvetica 16 bold italic"
#                             )
# HeadingLabel.pack()
# dice = ['die1.png','die2.png','die3.png','die4.png','die5.png', 'die6.png']
# DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# ImageLabel = tkinter.Label(root,image=DiceImage)
# ImageLabel.image=DiceImage
# ImageLabel.pack(expand=True)

# # def rolling_dice():
# #     DiceImage = ImageTK.PhotoImage(Image.open(random.choice(dice)))
# #     ImageLabel.configure(image=DiceImage)
# #     ImageLabel.image = DiceImage
# #     button = tkinter.Button(root, text='Roll the Dice', fg = 'blue' , command=rolling_dice)
# #     button.pack(expand=True)


from tkinter import * 
import random

root =Tk()
root.geometry('400x400')
root.title('Roll the Dice')

# BlankLine = tkinter.Label(root, text="")
# BlankLine.pack()
label =Label(root, text="Hello from Mantasha" ,
                          fg = "light green",
                          bg = "dark green",
                         font = "Times"
                        #  font "Helvetica 16 bold italic"
                            )


def rolling_dice():
  dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
  label.configure(text=f'{random.choice(dice)}')   
  label.pack()
  button =Button(root, text='Roll the Dice', fg = 'blue' , command=rolling_dice)
  button.pack(expand=True)
  root.mainloop()