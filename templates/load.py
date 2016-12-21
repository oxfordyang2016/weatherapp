import os
from datetime import datetime
import sys
sqlfilelist=[]
binfilelist=[]
import time
#-----------------via list to get bin and sql filename dir-----
def listfile(dirname):
    filenamedir=os.listdir(dirname)
    for filename in filenamedir:
        if "sql" in filename:
            sqlfilelist.append(dirname+filename)
        if "bin" in filename:
            binfilelist.append(dirname+filename)
    return [sqlfilelist,binfilelist]
#your path format is below
#getdirfilelist=listfile('/tmp/goodday/purebackdata/')
#print getdirfilelist[1]

#----------------------load database increlog--------------------
#mysqlbinlog /testdata/yangming-bin.000716| mysql -u root -pyangmingtestmysql
#mysqlbinlog /var/lib/mysql/yangming-bin.000945 | mysql -h 192.168.1.211 -u root -p503951 --port 15076

def increfileload(path,host,port,user,passwd):
    #path is backup dir,in these case ,it is /tmp/goodday/purebackdata
    #there error-deal capacity is bad
    bindir=(listfile(path))[1]
    loadfilepath=(sorted(bindir))[-1]
    commandline='mysqlbinlog '+loadfilepath+'| mysql -u '+str(user)+' -p'+str(passwd)
    os.system(commandline)

#-----------------------full load database---------------------------
#mysql -h 192.168.1.211 -u root -p  --port 15076 <201612161425.sql
# mysql -u root -pyangmingtestmysql</testdata/testincre.sql
def fullfileload(path,host,port,user,passwd):
    #path is backup dir,in these case ,it is /tmp/goodday/purebackdata
    #there error-deal capacity is bad
    sqldir=(listfile(path))[0]
    loadfilepath=(sorted(sqldir))[-1]
    commandline='mysql -h '+str(host)+'--port'+str(port)+ ' -u '+str(user)+' -p '+ str(passwd)+'<'+loadfilepath
    print 'i am loading %s'%loadfilepath
    os.system(commandline)

#------------------------load function local(you can work with crontab)-----------------
def run():
    if sys.argv[1]=="f":
        fullfileload('/tmp/goodday/purebackdata/',0,0)
    elif sys.argv[1]=="i":
        increfileload('/tmp/goodday/purebackdata/',0,0)
#---------------------outside api(more advanced )-------------------------------------------------------

def mysql_load(dir,host,port,user,passwd):
    while len(os.listdir(dir))!=0
        dir_file_name=os.listdir(dir)
        def con(filenamelist):
            return dir+filenamelist
        file_path_list=map(con,os.listdir(dir))
        print file_path_list
        def get_file_create_time(file):
            return os.path.getctime(file)
        file_create_time_list=map(get_file_create_time,file_path_list)
        print "---------file path list-----"+str(file_path_list)
        print "---------min time-------"+str(file_create_time_list)
        sorted_time_filetime=min(file_create_time_list)
        all_file_info={}
        for file_path in file_path_list:
            all_file_info[file_path]=os.path.getctime(file_path)
        for key, value in all_file_info.iteritems():
            if value==min(file_create_time_list):
               if "bin" in key:
                   commandline='mysqlbinlog '+key+'| mysql -h '+str(host)+' --port '+str(port)+' -u '+str(user)+' -p'+str(passwd)
                   os.system(commandline)
                   os.remove(key)
               elif "sql" in key:
                   commandline='mysql -h '+str(host)+' --port '+str(port)+ ' -u '+str(user)+' -p'+ str(passwd)+ ' < '+key
                   print(commandline)
                   os.system(commandline)
                   os.remove(key)
               break       




if __name__ == "__main__":
#if _name_=="_main_":
#    print "_ _name_ _ is "+_name_

    print "---------i am running load.py -time is --%s-----"%str( datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    run()



#loaddb.mysql_load('/load/','localhost',3306,'root','yangmingtestmysql')    