"""AVC"""
"""

        Everyday. Runs check in the morning? Emails before lunch. Runs check in the afternoon after lunch. Email at 2.
            Dont leave code running. Run from windpws scheduler
        1. Recursive list the folder with all files inside.
        2. Before checking for vid compliance stuff. Check if checked BEFORE...
            2.1 This could be done by Checking if the name of the video exists in a "files_done.txt".
                However this wouldn't help if its the same name file has been re uploaded.
                Check date of upload!

        3. Check every video in list that doesnt exist in "files_done.txt" OR has a more recent upload date than the one on file.

            3.2 After Checking each video and applying ALERTS where necesary. Add too "files_done.txt"
            3.3 Re-enter upload date into "files_done.txt" AFER.
                Format : (FILENAME)+(\n)+(DATE_OF_UPLOAD)
        4. ALERTS
            Send Email too Schedulers. Same alert as email sent too FTP user. But also includes user info??
            Send Email to user.
                The email can be the same format but replace "your" wwith "the"?
                EG. The file in the folder : user9. \nIs not compatible for broadcast because... This could be because....They have been notified to try....to fix the issue
                EG. Your file in the folder : user9. \nIs not compatible for broadcast because... This could be because....You could try....to fix the issue
"""

import os.path, time
from folderlist import *
from datetime import datetime as dt
from datetime import timedelta as tidelt
import subprocess
from pathlib import Path
import shutil

media_info_filename_AND_extension = "mediainfo.txt"
checked_before_list = "files_done.txt"
logfilloc = "AVC_LOG.txt"

scriptlocAVC = os.path.abspath(os.path.dirname(sys.argv[0]))

## Make Log File
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open(logfilloc, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass

sys.stdout = Logger()
## Make Log File

def cpit(from22, to22):
    print("Copying "+str(from22)+" TOO "+str(to22))
    shutil.copy(from22, to22)

def get_file_creation_and_modified_date(fileloc):
    print("Last modified: %s" % time.ctime(os.path.getmtime(fileloc)))
    LM_date = time.ctime(os.path.getmtime(fileloc))
    print("Created: %s" % time.ctime(os.path.getctime(fileloc)))
    C_date = time.ctime(os.path.getctime(fileloc))
    return LM_date, C_date

def message(message, string_to_print):
    #timap = Time at present
    timap = dt.today().strftime('%X')
    print("MESSAGE : "+str(timap)+" "+message+" "+str(string_to_print))


def make_media_info_file(Media_Info_filename):
    print(dt.today().strftime('%X')+" : Making Media Info Dimensions File : "+str(Media_Info_filename))
    with open(Media_Info_filename, "w") as fl:
        fl.write(" ")
        fl.close()

def rename_newfile_delete_oldfile(newfile, oldfile):
    os.remove(oldfile)
    os.rename(newfile, oldfile)

def delete_all_past_line_in_text_file(textfileloc, stringtosearch):
    newtextfile = split_fileloc_return_filename_with_full_path_without_extension(textfileloc)
    newtextfile = newtextfile+"NEW.txt"
    with open(newtextfile, "w+") as createfile:
        createfile.write("")
    createfile.close()
    with open(textfileloc, "r") as oldfile:
        line = oldfile.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = oldfile.readline()
            cnt += 1
            message("delete_all_past_line_in_text_file STARTING : ", textfileloc)
            message("newtextfile is : ", newtextfile)
            with open(newtextfile, "a") as newfile:
                message("oldlineread is : ", line)
                #line = oldline.readline()
                message("stringtosearch is : ", stringtosearch)
                if stringtosearch in line:
                    break
                newfile.write(line)
            newfile.close()
        oldfile.close()
    rename_newfile_delete_oldfile(newtextfile, textfileloc)

def replace_a_line(original_line, new_line, filein, fileout):
    with open(filein) as fin, open(fileout, 'w') as fout:
        for line in fin:
            lineout = line
            if line.strip() == original_line:
                lineout = f"{new_line}\n"
            fout.write(lineout)
    fin.close()
    fout.close()

def search_for_string_in_CheckedBeforeList_file(string):
    with open(checked_before_list) as fin:
        for line in fin:
            message("search_for_string. line checking is : ", line)
            if line.strip() in str(string):
                message("FOUND : search_for_string. string searching for is : ", string)
                fin.close()
                return True
        fin.close()
        message("search_for_string. string searching for is : ", string)
        print("COULD NOT FIND STRING. RETURNING FALSE")
        return False

def search_for_MODdate_in_CheckedBeforeList_file(filetosearchfor, date):
    print("search for mod date starting")
    with open(checked_before_list) as fin:
        for line in fin:
            message("line check is : ", line)
            if line.strip() in str(filetosearchfor):
                message("File has been checked before. NOW CHECKING FOR MOD DATE : ", filetosearchfor)
                for i in range(1):
                    the_new_line = next(fin).strip()
                    message("the_new_line is : ", the_new_line)
                    if i == 0:
                        print("line 1 : MOD DATE")
                        message("Previous mod date is : ", the_new_line)
                        if the_new_line in date:
                            print("MOD DATE MATCHED! :")
                            fin.close()
                            return True
                        else:
                            print("MOD DATE DOESNT MATCH.\nMOD DATE ON FILE : "+str(the_new_line)+"\nMOD DATE CHECKED : "+str(date))
                            fin.close()
                            return False
                    print(".................. THIS SHOULDN'T PRINT ..................")

        fin.close()
        return False

def search_for_CREATEdate_in_CheckedBeforeList_file(filetosearchfor, date):
    print("search for create date starting")
    with open(checked_before_list) as fin:
        for line in fin:
            message("line check is : ", line)
            if line.strip() in str(filetosearchfor):
                message("File has been checked before. NOW CHECKING FOR CREATE DATE : ", filetosearchfor)
                for i in range(2):
                    the_new_line = next(fin).strip()
                    message("the_new_line is : ", the_new_line)
                    if i == 1:
                        print("line 1 : MOD DATE")
                        message("Previous create date is : ", the_new_line)
                        if the_new_line in date:
                            print("CREATE DATE MATCHED! :")
                            fin.close()
                            return True
                        else:
                            print("CREATE DATE DOESNT MATCH.\nCREATE DATE ON FILE : "+str(the_new_line)+"\nCREATE DATE CHECKED : "+str(date))
                            fin.close()
                            return False
                    print(".................. THIS SHOULDN'T PRINT ..................")

        fin.close()
        return False

def update_checked_before_list(fileloc, moddate, createdate):
    with open(checked_before_list, "a") as files_checked_list2:
        files_checked_list2.write(str(fileloc)+"\n")
        files_checked_list2.write(moddate+"\n")
        files_checked_list2.write(createdate+"\n")
        files_checked_list2.close()

"""

Check if checked BEFORE : search_for_string_in_file
if return true from file check search for create_date and mod_date SEPERATELY underneath that specific file name in file


"""


def check_if_checked_before(fileloc):
    mod_date, creat_date = get_file_creation_and_modified_date(fileloc)
    message("File Checking is : ", fileloc)
    message("mod_date is : ", mod_date)
    message("creat_date is : ", creat_date)
    if search_for_string_in_CheckedBeforeList_file(fileloc) == False:
        print("FILE not mentioned in Checked before list. RETURNING FALSE")
        return False
    elif search_for_MODdate_in_CheckedBeforeList_file(fileloc, mod_date) == False:
        print("MOD DATE ISNT CORRECT / UP TO DATE ON FILE. RETURNING FALSE")
        return False
    elif search_for_CREATEdate_in_CheckedBeforeList_file(fileloc, creat_date) == False:
        print("CREATE DATE ISNT CORRECT / UP TO DATE ON FILE. RETURNING FALSE")
        return False
    else:
        print("FILE HAS BEEN CHECK BEFORE AND ALL DETAILS ARE CORRECT. RETURNING TRUE")
        return True


def put_media_info_in_media_info_file(fileloc, Media_Info_filename):
    """ REQUIRES MEDIAINFO EXE IN OPERATING FOLDER """
    print(dt.today().strftime('%X')+" : STARTING : MediaInfo")
    command = "MediaInfo \""+str(fileloc)+"\" > \""+Media_Info_filename+"\""
    message("Command is : ", command)
    subprocess.call(command, shell=True)

""" MEDIA INFO FILE IS SEPERATE FROM RECURSIVE LIST OF FILES. CREATED AT WILL AND DELETED. THE MEDIA INFO FILE IS ANALYSED, THE RESULTS ARE EMIALED IF NEED BE,  IT IS DELETED, THE MODIFIED / CREATEION DATE IS UPDATED """

def split_fileloc_return_filename_with_full_path_without_extension(fileloc):
    P = os.path.splitext(fileloc)
    P = P[0]
    message("Taking Extension of full location. Filename is : ", P)
    return P

def return_only_filename(fileloc):
    #filnam11 = os.path.splitext(fileloc)
    message("filnam11 is : ", fileloc)
    filnam11 = fileloc.split("\\")
    message("filnam11 is : ", filnam11)
    message("filnam11[-1] is : ", filnam11[-1])
    filnam11 = filnam11[-1]
    return str(filnam11)

def error_in_compliance_check(error_line):
    global Error_in_Compliance_Check
    Error_in_Compliance_Check = error_line

def runcheck(line, Error_Count):
    if "Format                                   :" in line:
        if "Format                                   : MPEG-PS" not in line and "Format                                   : MPEG Video" not in line:
            message("Format is incorrect. : \n", line)
            error_in_compliance_check(line)
            return False
    elif "Overall bit rate mode                    :" in line:
        if "Overall bit rate mode                    : Constant" not in line:
            message("Overall bit rate mode is incorrect. : \n", line)
            error_in_compliance_check(line)
            return False
    elif "Bit rate mode                            :" in line:
        if "Bit rate mode                            : Constant" not in line:
            message("Bit rate mode is incorrect. : \n", line)
            error_in_compliance_check(line)
            return False
    elif "Width                                    :" in line:
        if "Width                                    : 720 pixels" not in line:
            message("Width is incorrect. : \n", line)
            error_in_compliance_check(line)
            return False
    elif "Height                                   :" in line:
        if "Height                                   : 576 pixels" not in line:
            message("Height is incorrect. : \n", line)
            error_in_compliance_check(line)
            return False
    elif "Display aspect ratio                     :" in line:
        if "Display aspect ratio                     : 16:9" not in line:
            message("Display aspect ratio is incorrect. : \n", line)
            error_in_compliance_check(line)
            return False
    elif "Frame rate                               :" in line:
        if "Frame rate                               : 25.000 FPS" not in line:
            message("Frame rate is incorrect. : \n", line)
            error_in_compliance_check(line)
            return False
    elif "Scan type                                :" in line:
        if "Scan type                                : Interlaced" not in line:
            message("Scan type is incorrect. : \n", line)
            error_in_compliance_check(line)
            return False
    elif "Scan order                                :" in line:
        if "Scan order                               : Top Field First" not in line:
            message("Scan order is incorrect. : \n", line)
            error_in_compliance_check(line)
            return False
    elif "Time code of first frame                 :" in line:
        if "Time code of first frame                 : 00:00:00:00" not in line:
            message("Time code of first frame is incorrect. : \n", line)
            error_in_compliance_check(line)
            return False


def check_compliance(Media_Info_filename):
    message("Checking Compliance on : ", Media_Info_filename)
    with open(Media_Info_filename) as fp:
        line = fp.readline()
        cnt = 1
        Error_Count = 1
        Are_There_Errors = "False"
        Errors_list = []
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
            if runcheck(line, Error_Count) == False:
                Are_There_Errors = "True"
                Error_Count += 1
                Errors_list.append(str(Error_in_Compliance_Check))
        if Are_There_Errors == "True":
            global the_errors_list
            the_errors_list = Errors_list
            return False

def alert_schedulers_and_client(fileloc):
    message("alert_schedulers_and_client on : ", fileloc)
    print("Errors are : \n")
    message_details = set()
    error_results_comped = set()
    for error_inf in the_errors_list:
        if "Format" in str(error_inf):
            message_details.add("\nThe Format of the file was incorrect. All files should be provided as .mpg. Otherwise known as MPEG-S. More details provided at the bottom of the email.")
            error_results_comped.add(error_inf)
        elif "Overall bit rate" in str(error_inf):
            message_details.add("\nThe Overall Bitrate of the file was incorrect. All files should be provided with a CONSTANT bitrate. NOT a VARIABLE Bitrate. More details provided at the bottom of the email.")
            error_results_comped.add(error_inf)
        elif "Bit rate mode" in str(error_inf):
            message_details.add("\nThe Bitrate of the file was incorrect. All files should be provided with a CONSTANT bitrate. NOT a VARIABLE Bitrate. More details provided at the bottom of the email.")
            error_results_comped.add(error_inf)
        elif "Width" in str(error_inf):
            message_details.add("\nThe Width of the file was incorrect. All files should be provided in the dimensions 720 X 576. More details provided at the bottom of the email.")
            error_results_comped.add(error_inf)
        elif "Height" in str(error_inf):
            message_details.add("\nThe Height of the file was incorrect. All files should be provided in the dimensions 720 X 576. More details provided at the bottom of the email.")
            error_results_comped.add(error_inf)
        elif "Display aspect ratio" in str(error_inf):
            message_details.add("\nThe Display aspect ratio was incorrect. All files should be provided Display Aspect Ratio should be set at 16:9. More information can be found at the bottom of the email.")
            error_results_comped.add(error_inf)
        elif "Frame rate" in str(error_inf):
            message_details.add("\nThe Frame Rate was incorrect. All files should be provided at 25 Frames Per Second. More information can be found at the bottom of the email.")
            error_results_comped.add(error_inf)
        elif "Scan type" in str(error_inf):
            message_details.add("\nThe Scan Type was incorrect. All files should be provided as interlaced. Your file was probably provided as Progressive. More information can be found at the bottom of the email.")
            error_results_comped.add(error_inf)
        elif "Scan order" in str(error_inf):
            message_details.add("\nThe Scan Order was incorrect. All files should be provided in the scan order \"Top Field First\". More information can be found at the bottom of the email.")
            error_results_comped.add(error_inf)
        elif "Time code of first frame" in str(error_inf):
            message_details.add("\nThe Time code of first frame was not set too 00:00:00.00 . All files should be provided with the first frame at 00:00:00.00. These errors usually occur when your video edit doesnt start from the very first frame or the timeline. More information can be found at the bottom of the email.")
            error_results_comped.add(error_inf)
        #print(error_inf)
    error_message = "The file : "+str(fileloc)+" has been provided in a non compliant format. Meaning that it cannot be broadcast in its current state. Please see details below.. \n\n"
    for mess in message_details:
        error_message = error_message+str(mess)
    message("Final error_message is : ", error_message)
    results_comped = ""
    for err in error_results_comped:
        results_comped = results_comped+str(err)
    message("Final error_results_comped is : ", results_comped)


include_suffix = (".mp4", ".mpg")
def check_file(fileloc):
    fileloc = fileloc[2:-1]
    fileloc = Path(fileloc)
    message("Checking File : ", fileloc)
    if str(fileloc).endswith(include_suffix):
        if not check_if_checked_before(fileloc) == True:
            if str(fileloc).endswith(include_suffix):
                cpit(fileloc, scriptlocAVC)
                only_filename = return_only_filename(str(fileloc))
                newfilelocation = os.path.join(scriptlocAVC, only_filename)

                filnam = split_fileloc_return_filename_with_full_path_without_extension(newfilelocation)
                media_info_filename = filnam+media_info_filename_AND_extension
                message("Making media_info_filename : ", media_info_filename)
                make_media_info_file(media_info_filename)
                put_media_info_in_media_info_file(newfilelocation, media_info_filename)
                delete_all_past_line_in_text_file(media_info_filename, "Audio")
                if check_compliance(media_info_filename) == False:
                    alert_schedulers_and_client(fileloc)
                mod_date, creat_date = get_file_creation_and_modified_date(fileloc)
                update_checked_before_list(fileloc, mod_date, creat_date)
                os.remove(newfilelocation)

get_list_go("F:/PRIMARY/- SCRIPTING/Auto_Video_Compliance/testfootage")
with open ("Files_list.txt", "r") as filelist:
    line = filelist.readline()
    cnt = 1
    while line:
        print("Checking FILE {}: {}".format(cnt, line.strip()))
        check_file(str(line.strip()))
        line = filelist.readline()
        cnt += 1
print("FINISHED")
