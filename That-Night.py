from tkinter import*
root=Tk()
label=Label(root,text="THAT NIGHT",fg="white",bg="black")
label.config(font=("Arial",21))
label.pack()    
label_1=Label(root,text="We were very excited as we had been allotted a bungalow for a Party on Void Road.")
label_1.pack()
label_2=Label(root,text="The day to shift arrived but as we entered the new home. I felt a chill run down my spine.")
label_2.pack()
label_3=Label(root,text="I felt the presence of some paranormal force present in that house.")
label_3.pack()
label_4=Label(root,text="After supper, everyone went to their bedrooms. I went to mine too and soon everyone was asleep .")
label_4.pack()

def click():
  label_5=Label(root,text="After securing the bolts of all the doors, I finally readied my bed. To my horror the light went off. I had to light a candle.")
  label_6=Label(root,text="The candle was not long enough to last for a few hours. So, I blew it out and lay on the bed. Soon I fell asleep.")
  label_5.pack()
  label_6.pack()
  btn_2=Button(root,text="CONTINUE",command=click2,fg="white",bg="black")
  btn_2.pack()
btn=Button(root,text="CONTINUE",command=click,fg="white",bg="black")
btn.pack()
def click2():
  label_7=Label(root,text="In the middle of the night I was woken up by a strange sound. ")
  label_8=Label(root,text="As I opened my eyes and focused on the sound, I felt someone was walking up and down outside my room.")
  label_9=Label(root,text="My heart began palpitating uncontrollably!")
  label_10=Label(root,text="I dared to go to the window and see who could be walking up and down outside the room!")
  label_11=Label(root,text="What I saw temporarily sent me into a faint!")
  label_7.pack()
  label_8.pack()
  label_9.pack()
  label_10.pack()
  label_11.pack()
  btn_3=Button(root,text="CONTINUE",command=click3,fg="white",bg="black")
  btn_3.pack()

def click3():
  label_12=Label(root,text="Before fainting I had a glimpse of a woman standing with her back towards me just in front of the window I was looking through.")
  label_13=Label(root,text="As the woman turned slowly towards me,")
  label_14=Label(root,text=" I was transfixed with fear and stupefaction!")
  label_15=Label(root,text=" I was transfixed with fear and stupefaction!")
  label_16=Label(root,text="The woman had no face! There was a skull on her shoulders!")  
  label_17=Label(root,text="And as I looked at her skeleton hands, I fell onto the ground.")
  label_12.pack()
  label_13.pack()
  label_14.pack()
  label_15.pack()
  label_16.pack()
  label_17.pack() 
  btn_4=Button(root,text="CONTINUE",command=click4,fg="white",bg="black")
  btn_4.pack()
def click4():
  label_18=Label(root,text="The Next day,the Police have arrived to investigate the place and found blood almost all everywhere in bungalow and few heads and body parts scattered here and there.")
  label_19=Label(root,text="The only surviver was the....Boy.")
  label_20=Label(root,text="But he was really hurt,so they(all the nurses,doctors,etc.) lunged to the Hospital.")
  label_21=Label(root,text="The news about this incident spread everywhere on the Void state",fg="white",bg="black")
  label_22=Label(root,text="After few days,which when he recovered,the Police have introgated him and found a shocking truth!!",fg="white",bg="black")
  label_22.config(font=("Arial",16))
  label_23=Label(root,text="In The Next Series Of ----> THAT NIGHT",fg="white",bg="black")
  label_23.config(font=("Arial",18))
  label_24=Label(root,text="\t<<<<<<------THE END------>>>>>>",fg="white",bg="black")
  label_24.config(font=("Arial",21))
  label_18.pack()
  label_19.pack()
  label_20.pack()
  label_21.pack()
  label_22.pack()
  label_23.pack()
  label_24.pack() 
root.mainloop()    
