#Code By Harshit Ratan Shukla
#QR code stands for Quick Response Code. QR codes may look simple but they are capable of storing lots of data. 
#Irrespective of how much data they contain when scanned QR code allows the user to access information instantly. That is why they are called Quick Response Code.
#These are being used in many scenarios these days.
#QR codes can be used to store(encode) lots of data and that too of various types. 
#For example, they can be used to encode: Contact details, Facebook ids, Instagram ids, Twitter ids, WhatsApp ids,Event Details,Youtube links,Product details,Link #directly to download an app on the Apple App Store or Google Play.
#They are also being used in doing digital transactions by simply scanning QR codes.


#importing qrcode module
import qrcode

#Getting Information From the user
info = input("\033[1;31;40m Enter your Data to convert it into QR Code.\033 \n \033[1;32;40m For Example: \033 \n \033[1;34;40mContact details,Facebook ids,Instagram ids,Twitter ids,WhatsApp ids.\n Event Details\n Youtube links\n Product details\n Link directly to download an app on the Apple App Store or Google Play.\033 \n \033[1;31;40m Enter Here.....  \033")

#Generating Desired QR Code
img = qrcode.make(info)

#Saving this QR for future reference with the name "MyQR.jpg"
#you can also use ".pdf",".png" as per your requirement
print("\n\n")

path = input("\033[1;37;40m Please Enter the Path where you want to save this file. \033 \n \033[1;31;40m Default Path is /QRcode_Generator/MyQR.jpg.\033 \n \033[1;32;40m Press Enter To continue with Default Path....\033  ")

print("\n\n")

Name = input("\033[1;37;40m Please Enter Name of your file. \033 \n \033[1;31;40m Default Name is MyQR.jpg.\033 \n \033[1;32;40m Press Enter To continue with Default Name....  \033")
if(len(path) == 0 and len(Name) == 0):
	img.save("MyQR.jpg")

if(len(path) != 0 and len(Name) == 0):
	img.save(path + "/MyQR.jpg")

if(len(path) ==  0 and len(Name) != 0):
	img.save(Name)

if(len(path) != 0 and len(Name) != 0):
	img.save(path+Name)

#showing QR on Screen
img.show()
