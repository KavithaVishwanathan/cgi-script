import cgi, cgitb
import commands

# print the html headers to standard output
print "Content-type:text/html"
print ""
print
print '<head>'
print '<!--custom css -->'
print '<link rel="stylesheet" type="text/css" href="custom.css" />'
print '<!-- bootstrap -->'
print '<link rel="stylesheet" href="bootstrap.min.css">'
print '<title>'
print 'Contents of a users websys directory'
print '</title>'
print '</head>'
print '<body>'


form=cgi.FieldStorage()
if "userid" not in form:
   print "<H1>Error</H1>"
   print "userid field not provided"
print '<h1 style="text-align:center"> The User: ' + form["userid"].value +'</h1>'

# retrieve the value of the userid field from the form
Userid =form["userid"].value
Fchar = Userid[0]

# Now construct the full path to their websys directory
# it should be  /homedir/grad/fchar/userid/public_html/websys
# where FCHAR is the first character of the userid
# type 'pwd' at the unix prompt to see you full path

# Note that we can treat strings as an array of characters
# with the first element at location 0

webSysPath = "/homedir/grad/" + Fchar + "/"  + Userid + "/public_html/websys"
print '<h2 style="text-align: center">List of user ' + Userid + "'s" + ' websys directory</h2>'

lscommand = 'ls ' + webSysPath
#
# tell html the next stuff is preformatted
# otherwise it ignores line breaks and will ruin it all together
#
print '<pre>'
status,lsresults = commands.getstatusoutput(lscommand)
lsresult = lsresults.split("\n")

if status == 0:
  print '<div class="col-md-4 col-md-offset-4">'
  print '<table class="table custom-table table-striped">'
  print '<th class="centercapitalize"> File /Folder Name </th> '
  classname=""
  for result in lsresult:
    if result.find(".html") != -1:
      classname="htmlcolor"
    elif result.find(".css") != -1:
      classname="csscolor"
    elif result.find(".pdf") != -1:
      classname="pdfcolor"
    elif result.find(".cgi") != -1:
      classname = "cgicolor"
    elif result.find(".") == -1:
      classname="foldercolor"
    filepath = "/~" + Userid + "/websys/" + result
    print "<tr><td><a href ='"+  filepath + "' class='"+ classname +"'>" +  result + "</a></td></tr>"
    classname=""
  print '</table> </div>'
else:
  print "This is not a valid userid.<br>Please enter valid user id to see their contents.<br>Thanks"
print '</pre>'
print '</body>'
print '</html>'
               