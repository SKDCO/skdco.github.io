import urllib.requestimport datetime
now = datetime.datetime.now()conn = urllib.request.urlopen("http://localhost:3185/monitor.htm") # + req)
#p = ['4.0 Transitional','LABAZDC','WRUMOSB044','Guardant Net II','Dongle license limit','Loginom Studio Pro','Loginom Viewer Pro','Loginom Studio Ent','Loginom Viewer Ent','Deductor Studio Ent','XXX']
p = ['Deductor Studio Ent']p1 = u"""b'<img align="middle" src="license.gif">&nbsp;<a href="viewobject_id0000000B.htm" target="objectparams">Deductor Studio Pro ( 0 /  0)</a>'"""p2 = u"""b'<img align="middle" src="license.gif">&nbsp;<a href="viewobject_id0000000C.htm" target="objectparams">Deductor Viewer Pro ( 0 /  0)</a>'"""p3 = u"Deductor Studio Ent"p4 = u"Deductor Viewer Ent"#print('1')li = []a = []for line in conn:    #row = row +str(line.strip())    if str(line.strip())==p2 or str(line.strip())==p1:        continue    a.append(str(line.strip()))    l = len(a)k = 0for j in range(0,l):    #print(a[j])    for i in range(0,len(p)):        #print( a[j])        if k > 0 and a[j]!="b''"and a[j]!="b'</ol>'" and a[j]!="b'<ol>'" and a[j]!="b'</html>'" and a[j]!="b'</body>'" and a[j]!="b'</font>'":            #print(a[j])            #for ii in range(0,len(l)):            li.append(str(a[j]))              #print (a[j],"_________",p[i])        if p[i] in a[j] and k==0:            #if a[j].find(p[i])!=-1:            li.append(str(a[j]))            #print('!!!!',a[j])            k = 1            break                   #print('2')#n = len(li)#for g in range(0,n):#    print(li[g],end='\n') 
st = u""row = u""f = open('D:\\Program Files (x86)\\BaseGroup\\Deductor\\Deductor.txt', 'a')for index in range(0,len(li)):    #print(li[index]    s = li[index].split(""""objectparams">""")    s = s[1].replace("</a>'","")    s = s.replace(" (TCP/IP: ",";")    if p3 in s:        st = s    elif p4 in s:        st = s    else:        row = str(now)+u';'+st + u';'+s.upper()        print(row)    if index == len(li):        f.write(row)    else:        f.write(row+'\n')    #print(row)f.close()