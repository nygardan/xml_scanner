# Python program to extract readable data from ProQuest XML files.
# Helpful for adding document info to the IR.
# Designed for Windows PC
# 1. Run the program. 2. Go to the XML file and shift+right click on it.
# 3. Select "Copy as path". 4. Paste the path into the Python terminal prompt and hit Enter.
# By Dan Nygard 9-10-2020

from xml.dom import minidom

while True:
    try:
        # Get the path to xml (shift+right-click on file in folder and "copy path")
        # Make an output text file path.
        # Use minidom to get the DOM object from XML.
        path = input("Enter the file path to XML: ")
        path = path.strip('"')
        output_path = path.replace('.xml', '.txt')
        mydoc = minidom.parse(path)

        # Pull the info we need from the XML DOM object.
        firstName = mydoc.getElementsByTagName("DISS_fname")[0].firstChild.data
        lastName = mydoc.getElementsByTagName("DISS_surname")[0].firstChild.data
        title = mydoc.getElementsByTagName("DISS_title")[0].firstChild.data
        comp_date = mydoc.getElementsByTagName("DISS_comp_date")[0].firstChild.data
        advisors = mydoc.getElementsByTagName("DISS_advisor")
        degree = mydoc.getElementsByTagName("DISS_degree")[0].firstChild.data
        program = mydoc.getElementsByTagName("DISS_inst_contact")[0].firstChild.data
        abstract = mydoc.getElementsByTagName("DISS_para")
        try:
            keywords = mydoc.getElementsByTagName("DISS_keyword")[0].firstChild.data
        except:
            keywords = "No keywords."
        try:
            embargo = mydoc.getElementsByTagName("DISS_sales_restriction")[0].attributes['remove'].value
        except:
            embargo = "No delayed release."
        try:
            orcid = mydoc.getElementsByTagName("DISS_orcid")[0].firstChild.data
        except:
            orcid = "No ORCID."
               
        # Print usable info to file!
        
        print(output_path)
        with open(output_path, 'w', encoding='utf8') as new_file:
            new_file.write(f"Student Name: {firstName} {lastName}\r\n")
            print(f"Student Name: {firstName} {lastName}")
            new_file.write(f"Title: {title}\r\n")
            new_file.write("Accepted: " + comp_date + "\r\n")
            for advisor in advisors:
                info = minidom.parseString(advisor.toxml())
                first = info.getElementsByTagName("DISS_fname")[0].firstChild.data
                last = info.getElementsByTagName("DISS_surname")[0].firstChild.data
                new_file.write(f"Advisor: {first} {last}\r\n")
            new_file.write(degree + "\r\n")
            new_file.write("Program: " + program + "\r\n")
            new_file.write("Keywords: " + keywords + "\r\n")
            new_file.write("Keywords: " + keywords.lower() + "\r\n")
            new_file.write("Abstract:\r\n")
            try:
                for para in abstract:
                    new_file.write(para.firstChild.data + "\r")
            except:
                print("Abstract failed to print.")
            new_file.write("\n" + "Delayed Release Exp Date: " + embargo)
            new_file.write("\r\n" + orcid + "\r\n")
            
            print("File complete.\n")
            new_file.close()

    # An invalid input will end the program.
    except:
        print("Invalid input. Halting program.")
        break




