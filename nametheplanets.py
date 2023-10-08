import cv2 
img= cv2.imread("C:/Users/dell/Desktop/name the planets/solar-system.jpg")
text_to_show="SUN" 
cv2.putText(img,text_to_show,(20,200),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,0))
text_to_show_planet_one= "MERCURY"
cv2.putText(img,text_to_show_planet_one,(40,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,0,0))
text_to_show_planet_two="VENUS"
cv2.putText(img,text_to_show_planet_two,(150,200),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,255,255))
text_to_show_planet_three="EARTH"
cv2.putText(img,text_to_show_planet_three,(250,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,0))
text_to_show_planet_four="MARS"
cv2.putText(img,text_to_show_planet_four,(350,200),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,0,0))
text_to_show_planet_five="JUPITER"
cv2.putText(img,text_to_show_planet_five,(500,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,255))
text_to_show_planet_six="SATURN"
cv2.putText(img,text_to_show_planet_six,(700,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,255,255))
text_to_show_planet_seven="URANUS"
cv2.putText(img,text_to_show_planet_seven,(950,200),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,255))
text_to_show_planet_eight="NEPTUNE"
cv2.putText(img,text_to_show_planet_eight,(1100,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,255,255))
text_to_show_title="OUR SOLAR SYSTEM"
cv2.putText(img,text_to_show_title,(400,400),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,0))
cv2.imshow("output",img)
cv2.waitKey(0) 