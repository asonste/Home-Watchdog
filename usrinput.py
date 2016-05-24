#/usr/bin/python
"""
asonste 09/jan-2016
User input. Takes one parameter: usrinput(promt)
Will loop until user enteres a value.
"""
def usrinput(promt):
#   string = str(raw_input("%s >>  "%promt))
   string = ""
   while string =="":
        string = str(raw_input("%s >>  "%promt))
        if string == "":
            print "Invalid input"
   return string

#--- For testing -------------
if __name__ == "__main__":
   print "RUNNING EXAMPLE"
   print usrinput("Write a question here")
