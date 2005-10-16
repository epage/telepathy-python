#!/usr/bin/python2.4
import sys
import os
import inspect
import dbus

inspectmod=__import__(sys.argv[1],[],[],[])

doc={}

for (name,val) in inspectmod.__dict__.items():
    if inspect.isclass(val):
        doc[name]={}
        doc[name]["maintext"]=val.__doc__.replace('\n\n','<p>')
        doc[name]["methods"]={}
        for (mname, mval) in val.__dict__.items():
            if inspect.isfunction(mval) and mval.__dict__.has_key("_dbus_is_method"):
                doc[name]["methods"][mname]={}
                sigin=dbus.Signature(mval.__dict__["_dbus_in_signature"])
                argspec=inspect.getargspec(mval)
                args=', '.join(map(lambda tup: str(tup[0])+": "+tup[1], zip(sigin,argspec[0][1:]))) #chop off self
                doc[name]["methods"][mname]["in_sig"]=args
                if mval.__dict__["_dbus_out_signature"] == "":
                    doc[name]["methods"][mname]["out_sig"]="None"
                else:
                    doc[name]["methods"][mname]["out_sig"]=mval.__dict__["_dbus_out_signature"]
                doc[name]["methods"][mname]["text"]= mval.__doc__.replace('\n\n','<p>')

print '<html>'
print '<head>'
print '<title>Documentation for dbus interfaces defined in',inspectmod.__name__,'</title>'
print '<link rel="stylesheet" type="text/css" media="screen" href="style.css" />'
print '</head>'
print '<body>'
print '<div class="topbox">Telepathy</div>'
#print '<div class="sidebar">'
#
#for name in doc.keys():
#    for method in doc[name]["methods"].keys(): 
#        print '  <a href="#%s">%s</a>' % (method,method)
#print '</div>'

for name in doc.keys():
    print "<h1>"+name+"</h1>"
    print doc[name]["maintext"]
    print '<ul>'
    for method in doc[name]["methods"].keys(): 
        print '<li></a><div class="method" name="%s">' % method
        print '<h2>%s ( %s ) -> %s</h2>' % (method,doc[name]["methods"][method]["in_sig"], doc[name]["methods"][method]["out_sig"])

        print doc[name]["methods"][method]["text"]
        print '</div></li>'
    print '</ul>'
    print '<br>'
print '</body></html>'