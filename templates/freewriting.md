# quick start
```
----
someone
----
i have a phonenon that i canot grasp knoledge very deeply!!!
----
python
-----
python class attribute have two type
that include 1. in  __init__ 2.in class level,but i have doubt that in class level i 
 can via self.classlevelattrubute to modeify . i affirm to access is good 
you can a=class(),a.classlevel to get value.you can refer to 
https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
.if you can in class to implement __getitem__ method,you will a[]
and result loop and reversed .so on,you can finish iterable  function such as
for 
doctest the number of item s is a problem.

---
how to install sikulix
----
https://www.youtube.com/watch?v=QiLkTP9Y_d4
use C:\SikuliX
----
someone
-----
now , my willing is to be expert in mysql and python.!!!before may
----
encode and decode
-------
about decode and encode ,the is connetction about convert byte to objetc that human can understand.
in unicode culture ,there is a way that convert charater,it is automatic unite of  a languge, to numbers
numbers converts to bit that was storaged in computer.from now my view,unicode define a large number to
corresponding alll kinds of charater.simple to say.unicode is like a table,you can map number to charater
in the world.about ascii,i want to say if i send you 65,you understand i send a A to you.from now,byte ,asingle
byte cannot slove to represent all kinds of symbol.i need to  understand python code how to convert machnie code.
-----
python
-----
from yangming's view ,when you use a=5 or b='yangmingishandosmor',when you run python
python will allocate memory according to size,besides,'yangmingishandsome' is convert to
byte according to  utf-8 encoding schema.i want to ask who  finish the encode ,is python ??
is the gcc???
-----
english 
------
that syas,
-----
living
-----
in your wall ,use 8 or 10 group swithc ,your ligth world is beatiful
---
python pep8
-----
1.always use import in .py file head.
2.even in same dir,you should aviod to use import bar
  should use from .  import bar(if must).when you should
  use form bar import bar
about pep8 ,imho,you ned tool to format and read more  about 
matrerail

PYTHON's unicode decode and encode is a pile of shit.
about a=b a and b all refer to same object
about c=a[2:3],c is a new list.from now, i think only a=b,a is b
all other situations,not same object,may values is same
item 5 is  ok ,i master.

---
python
-----
i need to read python pep8 example to format my python code
----
python runtime env
-----
thiis is that the env that make python code to machine code
you can use following code to lokk up:
import sys
print(sys.version_info)
print(sys.version)

---
someone
------
i feel that i was dependent  in caton
--------
load  balance
---------
load balance represent make too many traffic to all kinds of 
application server .(mr wang said).proxy server is a forwarding
request to different app server!!!
----
session and session id
-----
i understand session is paharase that  start client send request to server and server send 
reply data to client between the two pharase.from my view,i think ,ssesion is to slove 
the problem that how to slove http stateless  problem ,thatis,again http request ,you need to
write username and userpassword,but ssession id slove the problem,
a session id a connection.session is a data structure that 
save your username and password(hassed).besides,you can save another things in
session,session connect mode is the following:user use username and
 password to login in web server if authenticated,server make a session
datastructure that includes your username and your password and allocate
a session id to the session and keep the session id in cookie and
send it to client allong with http/s response,when client go on another request,
it will send request to server with session id.
when server receive the session id .server will to check the session id if exsit
and do responding action .if exist ,go on .or server will request client
to login.  but there is another view,session a period that between user login in and 
user login out.also session id and ssesion content is dictionary,eg,6374838834:{'username':yangming,
'password':xxxxxxxx(hashed)},about the form of session saved in server file system
or database or cache system.more things ,when more request were made ,you need
to send http request with session id in http body or head argments or cookie or usrl argument!!!
what i want to ask is the connection between cookie and http. another view,store too many data
in cilent-side will increse your traffic.i can use facebook  as example,when you first
login to server ,server check your passwod and username.if authenticated,fb will make 
ssession id and  return your main page,and you continue request another link in your
page ,you donot need authenticate ,in the hood,the browser will use the -styile link
http://en.mail.qq.com/cgi-bin/readmail?sid=YkCUuyVilYYnMRxE,
2,en_US&rank=2&mailid=ZC3212-rI46SNYOKzg0RGk~5fHZO64&t=readsubmail&mode=fake&s=r2&base=12.07&pf=0&folderid=3&folderkey= ,you can  sid =.............
3e281772..but you need note that the session id is encrypted in cooike sent to server,but when you in chrome ,you can read uncrypted sseion id.....i want to know
when you click  a link in fb ,who make your url's sid ,who encrypt it?????more,when
clear your browser  data you will must  login again!!!!now i can undestand the connection between period and  ssession ,because after logining,your cookie will always
be invoked!!!!!!when you login out ,your sseion id can not be used!!! 
----
hacker news
-----
it may does not connect to the issue by author,when thread was come up with
-----
project
------
draw a conclusion,every project need a why to use it page and
comparision to major compitor that do more good to our clients
but not damage our compeitor!!   features comparision  is important
the  project also need what is the project?????
----
nginx
-------
imho,nginx is a tool to increase web access to server to down memory and 
cpu,it is similiar to apache.from some opnion .it is used to load banlance
such as ,forward all kinds of request to all kinds of app server and do more 
opreation on  request,such as request size ,authen method .also another view ,
it is as a firewall ,for in a big rentepreter ,nginx act as fire wall to,for 
oiur developer  cannot touch in system.
------
python tech stack
-------
Qualifications: •Familiarity with our technology stack: 
Python, Django, PostgreSQL, Nginx, Varnish,
 Redis, JavaScript, Angular and Bootstrap – 
 all on Linux on a popular public IaaS or PaaS.
  •Experience working in DevOps environments. 
  •Understanding of security standards and concepts.
-----
someone
-------
i think i need to restructed  my view to end 
develop and it, i feel my knoledge is not sufficent
to develop my career.
---
open source 
-----
encrypt   
-----
english grammar
-------
Not that i donnot  welcome competition,i just donot 
see a real need in this field
---
python
----
imho,python is simpile ,python use list ,dictionary,set
as basic datatype ,in other worlds ,i just am familiar with these,
i understand python decorator is a packager that package gift
but gift does not chnage .origin function allso all ulity
,but origin function need to have have return value ,the return
value will be used to make somthings.for example ,i write a decorater 
function to print decorated function got arguments.i think that 
youtube and twitter or internet have good resource to help
you become more great pythoner .python also have a view,that is,
your code is pythonic..........from where i stand,i find that if you 
can not make use of anonoly to compare .after this time,you will forgrt
what you have understand........ 
----
open-source
------
about open source,i get information from yc,open source lassfication 
is following :game,frame ?????what i want to explore??????which type
there exists????from which drection to explore opensource?????i belive 
open source hidden a mout of fortune,but where i  start?????
---
someone
-------
my middle scholl time ,i have a habit to writting,but then,i have no
view on wirtting,i find  that in many point,you can be a genius,but 
after later.you will give up for all kinds resons and fact...M
---
english
-----
over also present the mean of about
---
genius
----
think oppositely
think in anonoly
learn from the little and error
these view from ........
---
methodlogy
----
make anology is a sign of genius ,this view is main and  popular
--
someone
----
in chirldhodd,i use yumi stem to build somethings ,imho,that is
a sign to reavel my character to create somethins,that is onnect 
to the view (what is a ginus)  
---
future
-----
waht i wanna lean is piano
----
methodlogy
-----
use the style is good ,you can get some classfied topcs
but you need to focus on some topcs or you r enrgy will
bw be wasted!!!!
----
direction
-----
konw yourself
math
english
health
economy
computer 
methoslogy
inner pysclology
.......
-----
conclusin of  it
---
from my opinon,it consiitof ,it also can  syas r&d,
version contorller,writting code,degsign frame,debug,log
,depoly(imho,that is shipping your code to production)
----
english
-----
my english spoken is poor ,i thing the reson is that i cannot 
read voice accent ,what i wanna say is ponetic symbol.in 7 grade
that some resons i donnot understand ,from then,i donnot get good start
,my accent is my english confiedence shortage ,....
-----
someone
------
i find that i donnot prefer to change my derection,,,,,,,,,,,,,,,,,,,,,,,,,
sometimes,i cannot chnage ,sometime,i lack driverness!!!
it is true!!!what i say is,fuck????i onluy can use some simple
english cluase ,but it is good????

----
english
-----
english's grammar for me only have cluase ,clause is not easy as i think in mid school
time,about clause ,i can drqwa draw a conclusin ,when you use that to as
subject ,it can not missed ,when you use it as object,it can be missed 
,how ever,bu reecent days ,i feel my cenlish work well,i think that there are some 
reason to explain ,thatis,my reading materaial is so easy,or my english get a little 
progress,as i said,my english env has a year,that is a good things.but when i read 
more complex acticle or book such as spical paper or some book,i will feel my body
not work with my mind,fuck ,waht i say is????
---
genius
-----
about genius,i read a author that may be a genius,
he said genius 's charater is to produce,in the most recently days , i
feel that my feling of years is more strong ,i feel 
time is so hugrry!!!
----
qsjkasjakskaskajkasjjka
-------
economy
----
get somethings to sale higer price that is more than it's price i bought
this is a good deal 
--
living
------
about living , i have sommany imagination
if i have a so luxury watch,that is so coll
if i have a so comforatable chair ,i will be
satisfied.this is iiiiiiiiiii,what is that iwant to say
these dayas, i feel so happy and sad becuase i feel sad
i met some frastrated problem that make me think myself 
is stupid,but the next days , i can figure out or slove the
problem,then ,i will feel that i am good.in addition to thses
good and bad,besdes,i feel that i need a macbook for well
wrtting ,but it is necessary???i will doubt,after all,the
lennove pc work with me that make me think taht it will
work more times and my income or to say that is ti waste????
i also feel that 2016 is a good year,fuck ,i can work with english
so a year,that is awesome,in addition to i can get so important or
insight views that do help me in the living,in fact ,to sloving a
 problem ,you can open ten chrome tab ,this do more for me,
 if i have so many tech is helping me be more great man1.chrome tab
 tech 2.wirtting............what else i cannot imagne!!!!!!
----
about health
-------
to increase blood-sugur level is a good method to keep control yourslef
and i feel worried about my health ,is following1,my weigh is ,is
it importtant???????my sex desire is not so high that i have no confidence 
to seek a girl ......i doubt that wheather my  shen work well.or my  maturbation
is so frequent so that ?????these years my weigh and my body-form is not satisfy
myself.but form other hands,my body donot get bad sick ,it is magic or luckily!
i need some info to change my health about sex disire ,tire,body-form....

-----
sommene
------
i find that i will doubt this world,i am willing to believe
the world that i belelive ,even if the research guide by the 
top agency and famous reseacher 1！！！！！

----
english
----
about english .i have fellowing  puzzle ,that is ,listenning skill
and poor spoken skill and unsuffient grammar ,that is my english 's 
gap that need to be filled by myself


---
prostocation
about th e psychelogy of procastion ,i wnat to say idraw a conlusin
,the viem i remenber is what you only to do is to do ,it is so scarefull
as you imagine!!1

---
future
-----
i have decide to devote my energy to math ,english ,computer,economy,problem
-sloving,if i have some fitness ,i will  get so many fortune  i thinkM

----
habit
----
inspired by someone,i get a view that he get greate succes via not wasting 
his ennegy and slways get somethings,

















```


# develop
```
client send data to server and server can store data
into database or deal with the data in function
,function 's operation always ocuur in data ,

```


# master math
```
imho,math is consit of daoshu ,jifen ,alege math
,from my opinoin ,i donot get idea,that is,i cannit 
get good position,this years,inned to rethink that why
form somoe pition,that i can not work hard but
i feel that i realy  work hard!

```
```
every day ,we need to get progress 
just a little is a important point
```
#  client and server model
```
 ## net work  by yangming

 flask can slove all kinds of problem s 
 i can abstract web develop is fellowing:
 client send  infomation to server ,server get the request 
 and deal with the request ,as usaual ,it get a url .it will 
 depath a url  to scratch to get all kinds of arguments.for example
 the url is http://wwww.goo.com/?queryyangming=234&ui=colorful
 .the server will get yangming and ui .after this,this argumewnts will be pass to corresponding function to deal with and get return value .
 after it,server return value send to client,and client do corresponding actions.imho,json in this course was used frequently 
 as info media at http body !!!!
```
 



[Greate acticle you need to read about wiriting and thinking ](http://www.dextronet.com/blog/accidental-genius-summary/)

# you have
```
this ia python a script

now ,i feel pride ,
because i have sloved sublime
install package problem

```
# sublime question
```
               i have sloved sdublime problelem of cannot install 

                package via a stackover flow link
```
```
living is all kind s os happiness and sad 
because of  sad ,happiness is chiresh

i neeed to slove sublime syntax launguge

if yesterday is sad,today is may be happy.it is so frequent
principle

i dislike limit -time in all kinds of task
it is a limit for myself
in create html page,i feel so tired in django


now,i have to activate the fellowing habit
1.make a link 
2.wirtting
3.................................................................
4.read
5.help others
6................................................
7.try toi answer stackoberflow problems


When you go with a thought, 
you assume that the thought is true, 
and you can take a series of logical steps.
 Just like this: If A is true, 
 that means B is true. And if B is true, that means C is true. And if C is true,

why markdown does not work in web page paster
i copy a pagrah from web but it not work in
markdown


Secret #6: Redirect Your Attention
When you run out of things to say, you can use “focus changer”. Focus changer is a question you ask yourself on paper that requires you to comment on something you’ve just written. It keeps you moving, and helps you focus on the yet unexplored parts of a situation.

Examples of focus changers include:

What was I thinking here?
How else can I say that?
Wha


```
```
        def helloworld(a,b):
            print 'hello wolrd'
        if __main__=='hello':

```

# i donnot like bad document ,becuase i have word with it

   thank you ,i lovw thee markdown ,i doubt that
 corect  markdown for wirting acticle isthat
 keep correct format that no need to do morethings
 every word have been input ,this way,it is evry line is filled ,i can not affirm it is ture nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

it is ture ,via the above experiment,it is usual wirting,in these 
case,you need to grasp how to control the frommat except ```````

&nbsp;&nbsp;This will appear with six space characters in front of it


```
   i belive that along the way,one can be more greate but in some
day,but i have no control my inner 
yes,i am so tired in these years


-----------------------------------------

in these dayas , i beleve metholodgy can change one's life
this way,to system to do somethings and think many things
but via feeling


i can use tree command to show the structure od dir 
in linux ,but i can use which tool to show these in
windows ???

```

   **[how to think via wirtting](http://www.dextronet.com/blog/accidental-genius-summary/)**


## About think
i wanna restart my think map ,but i care that i may stop
it
```
the best part of the workday is i have slove the 
sublime package  install problem,it frustrate me in
yesterday,i feel sad and think i was not a good slover 
of problem .even is not a  good programmer .but it 
encourage me



i want to show dir tree now ,this is below via linux tree comand
          /yangmingproject/
            ├── yangminggolang
            └── yangmingpython
                  └── yangmingflask



ifeel wangwangis handsome when he is patient to answer my question
this is i feel caton's energy



Prompt Your Thinking
Prompts are Freewriting exercise. When doing this exercise, you begin the Freewriting session with a pre-determined prompt.

Prompts are open-ended phrases to warm you up and to send your mind into unanticipated directions.

Prompts allow you to find many hidden jewels that you wouldn’t otherwise discover.

Some examples of prompts include:

The best part of my workday is…
Yesterday I saw a curious thing…
If I didn’t have to work, I’d…
I threw a stone and it landed…
I remember….
I’d love to learn about…
If I did the opposite of everything I normally do, my day would look like this…
I love…
I hate…
I should do more…
You know what I’d like to do again?
If I were guaranteed success, the project I’d take on would be…
The very generic ones can work wonders:

The storm
It was getting dark…
The birds were singing…
I opened the door…
Three days from now…
Prompts are somewhat similar to one of my long-time favorite techniques – question answered on paper. Basically, you write a question, and then start answering it. That’s it. It’s like querying your mind.

When you make the question very open-ended, you are not looking for specific answers, and it’s a prompt. The result will be a surprise. On the other hand, when the question is very specific, so will be the answers.




```

```
i eant to say in freewritting to that past=ing asome things
is very  stipud for aganinst it origin
```

[it  is a greate link about wiriting](http://www.dextronet.com/blog/accidental-genius-summary/)

```
may i have feel that i lack think in somethingsd because for 
i lack for writting ,it is a good point 
it exisit in my universty second  fresh year,i feel good  and 
it is used in 9 grade  time ,i write a post about chemistry
that i feel sad about ,result i get passed in the test


i belive that hte feeling i wrete is a base to influence my judgement

but i feel it is bullshit


all i have wittren up to this point about  how to use markdown 
is bullshit,the truth is that markdown is a luanguge  for writting
but a proamming language 
i find that my problem is not how to slobe the problem 
,my probelem is to understand problem  and understand what sloution 
says .it is key to slove most problems i faces now.imho,i need to up my english ability and understanding linux basic 



# using lying to eliminate error




```

#  writting can slove the problem that you can read it bbut 

   you can express it later


```
python is a kind of interpreter style languge ,that is ,

it can be run after  editting code,donot need to compile

at once.it will be compile when it is running.

------------------------------------------------------

WHAT I GET FROM LEARN STYLE BOOK is following

1.writiing is good
2.make a link is good
3.try fresh things is good
4.make a anonoly  is good
5.do different things is good
6.communicate with  a  somethings 

--------------------------------------------------------
what i get from 8000 hour is hte folloe=wing
1.help others is good
2.supporttive colleage is good

what i draw from life 
1. money is somithings you need to do too many things


the problem i face when i slove aproblem is the following 
a problem is relating to many things that i have mastered 
then,i feel so tired .



linux mount is my problem.i donnot like it for in shanghai 
qingsuansuo time.


i donnot  like to exact somethings becuase it is long

sometimes ,some greate opion that i undestand but i cannot convert

to my opion.this is bad




get focused on what you want !!!!!!

----
history
----
mongolia is a great contry that own most of continent
in the earth
----
inner
------
i feel that my disre for  back chengdu is get more strong..
is it sigin that i can not work hard,or i can not be used to
hard mode??????

```

# That i wll cherish and purse 
```
1.english 
2.math
3.economy
4.computer 
5.isiiisiiisiisiiisisiiisiisiiisisisisisisiisisisisisiisiisisisisisiisisiisiisisiisiiisiiiissiisisiiisiiisiis
5.health,energy and love

```




# what i get from slef-controller book by stanmford writer
1.need a good blood-sugar level



```
imho,it is a good opnion to persuit somethngs and it 's others 

will be  brought to you

```


# git basic

```
imho ,git or github is a repository that  save your code

git can work with github that work as repo ,make a anoly ,it 

is a pool you can place  a finish in it or fetch it,you can

update your finish.






```

```
i disleike chiken soup

i love the methodlogy that can land 




```
*[it may be a good link about person development](http://www.dextronet.com/blog/category/personal-development/)*

```
in a day ,if i have learn somethings ,i wili feel tired 
i donnot want to learn more ,this is usual

i think i have to figure out why my sex-disre is weak ??/


```

# python

```
python for me , i have some question and era to explore
1.python thread and process 
2.python asyn and syn
3.python network adn socket  programming
4.python work with c 



i feel not easy of python network .it is that 



```

# base  konelegdeg in 2017

```
1. master network  basic
2. linux basic comands 
i feel i  ahve master python basic 


```


```
# i will use -------- to block knowledge
python
---------------------
i feel that python 's diffcult part is 
python generaor ,python work with c,python network 
python iterator ,python decorator
------
network
-----------------------
abou tcp , i can undestand is a protocal to communicate
with infomation ,abou protocal i thing it is a guide that 
we all referece to dothings ,tcp work in transfer layer,but
i can not understand clearly what evry layer .from now,
application layer play  a role that forward infomation ,imho,
to approtiate application,when i have to learn the widershark 
too to grasp packet,the tool that give me unhappy feeling ,i
cannot  grasp .of course , i can abstract network to this sitiuation

,thst is ,a -----send infotion to-------->b ,about tcp ,i also 

know its tcp three-handshake,it is all .but the shake hands course
i have forget . 
--------
my  innner
---------
i doubt that there is no have good quick start to a area,so i donnot
get start happy,so that i cannot go deepth!!!!!

-----
network programming
-------
i think that  ,for example, a python flask 
frame will deal with all kinds of network request,
but we need to deal with security ,productivity ,etc that 
result all kinds of tech such  as sysn ,acsyn,tls.ssl .etc

----
living
-------
shanghai jiadinglibarray if have network,that is so beautiful things 
i want to live i=in near by shanghai libray
-----------


```















 