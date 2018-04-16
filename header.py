import binascii
import os.path
import time
import csv

filepath = input("What directory would you like to examine?\n")
csv_path = input("What would you like to call the csv?")
try:
    files = os.listdir(filepath)
except:
    print("Not a directory")
    exit()
header_num = {"4749": 6, "ffd8": 8, "504b" : 8, "4d5a" : 4, "8950" : 16, "2550": 8, "3842" : 8}
extensions = {"504b0304" : "xlsx, docx, zip, jar, odt, ods, pptx, vsdx, apk", "504b0506" : "xlsx, docx, zip, jar, odt, ods, pptx, vsdx, apk", "504b0708" : "xlsx, docx, zip, jar, odt, ods, pptx, vsdx, apk",
"474946" : "gif", "ffd8ffd8" : "jpg or jpeg", "ffd8ffe0": "jpg or jpeg", "ffd8ffe1" : "jpg or jpeg", "4d5a" : "exe", "89504e470d0a1a0a" : "png",
 "25504446" : "pdf",  "38425053" : "psd", }# Use for recommender
file_list = []
file_data = []
file_list.append(["Path", "Size", "Create Time", "Message", "Recommended Type"])
try:
    for f in files:
        #print(filepath+f)
        with open (filepath + "/" +f, "rb") as file:
            name = file.name
            size = str(int(os.path.getsize(filepath + "/" + f))/1000)
            #print("Size: " + str(int(os.path.getsize(filepath + "/" + f))/1000) + " KB")
            creation = os.path.getctime(filepath)
            now = time.ctime(int(creation))
            #print("Creation Time: " + now)
            header =file.read()
            header = binascii.hexlify(header)
            extension = os.path.splitext(file.name)[1].lower()
            #print(extension)
            header_dict_num = header[:4]
            header_dict_num = str(header_dict_num)
            header_dict_num = header_dict_num[2:6]
            try:
                num_char = header_num[header_dict_num]
            except:
                message = "Extension not found"
            #print(num_char)
            header = header[:num_char]
            header = str(header)
            header = header[2:num_char+2]
            #print("Hex header: " + header)

            if (header == "504b0304") or (header == "504b0506") or (header == "504b0708"):
                if (extension == ".xlsx") or (extension == ".zip") or (extension == ".jar") or (extension == ".odt") or (extension == ".ods") or (extension == ".docx") or (extension == ".pptx") or (extension == ".vsdx") or (extension == ".apk"):
                    # print("Extension matches header.")
                    message = "Extension matches header"
                else:
                    # print("Warning: file extension does not match.")
                    # print("Possible file type(s): " + extensions[header])
                    message = "Warning: file extension does not match."
            elif header == "474946":
                if (extension == ".gif"):
                    # print("Extension matches header.")
                    message = "Extension matches header"
                else:
                    # print("Warning: file extension does not match.")
                    # print("Possible file type(s): " + extensions[header])
                    message = "Warning: file extension does not match."
            elif (header == "ffd8ffd8") or (header == "ffd8ffe0") or (header == "ffd8ffe1"):
                if (extension == ".jpg") or (extension == ".jpeg"):
                    # print("Extension matches header.")
                    message = "Extension matches header"
                else:
                    # print("Warning: file extension does not match.")
                    # print("Possible file type(s): " + extensions[header])
                    message = "Warning: file extension does not match."
            elif (header == "4d5a"):
                if (extension == ".exe"):
                    # print("Extension matches header.")
                    message = "Extension matches header"
                else:
                    # print("Warning: file extension does not match.")
                    # print("Possible file type(s): " + extensions[header])
                    message = "Warning: file extension does not match."

            elif (header == "89504e470d0a1a0a"):
                if (extension == ".png"):
                    # print("Extension matches header.")
                    message = "Extension matches header"
                else:
                    # print("Warning: file extension does not match.")
                    # print("Possible file type(s): " + extensions[header])
                    message = "Warning: file extension does not match."
            elif (header == "25504446"):
                if (extension == ".pdf"):
                    # print("Extension matches header.")
                    message = "Extension matches header"
                else:
                    # print("Warning: file extension does not match.")
                    # print("Possible file type(s): " + extensions[header])
                    message = "Warning: file extension does not match."
            elif (header == "38425053"):
                if (extension == ".psd"):
                    # print("Extension matches header.")
                    message = "Extension matches header"
                else:
                    # print("Warning: file extension does not match.")
                    # print("Possible file type(s): " + extensions[header])
                    message = "Warning: file extension does not match."
            else:
                print("Extension not found")
            file_data.append(name)
            file_data.append(size)
            file_data.append(now)
            file_data.append(message)
            try:
                file_data.append(extensions[header])
            except:
                file_data.append("Extension not found")
            file_list.append(file_data)
            file_data = []
    print("Successfully run.  See csv for data")
    file.close()
except:
    print("File not found.")
    exit()

#Edit this to allow them to name the csv
with open(csv_path + ".csv", 'w', newline='') as f:
    thewriter = csv.writer(f)
    for s in file_list:
        thewriter.writerow(s)
    f.close()
