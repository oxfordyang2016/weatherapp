# quick start
```
-------
fudan
---------


2011
1. 输入3个子串， 输出这3个子串的最大公共子串 。
2. 输入树的中序和后序排列，输出树的层次遍历。上机要求和评分规则：
第一题、黑盒测试，只要求程序按格式输出结果正确。
第二题、按照思路，规范编程，代码三方面综合考虑得分。
-------
2012
三道题。
1第一道题目是排序问题。1000个成绩输出前30%。最好的做法是用最大堆吧。我用QSORT的。算了一下效率差不多。要是数据量的再大话估计不行了。
2.第二道题目是二叉树问题。比如节点是ABCDE编号是01234，给出每个左右子树的编号。求最大叶子间距。我是先建树，然后左右子树深度相加的。
3.第二道是英文题目，为了响应JYB的号召。加强英文考核啊。不过是水题。就是给一个字符串比如ABC 再给一个整数比如3.输出AAABBBCCC就行了。
第一第三道是黑盒测试。按结果给分。第二道根据算法思想步骤给分。要写注释。
明天还要面试。给自己加人品吧。
欢迎补充.

2013
复旦大学计算机科学技术学院
专业硕士复试上机考试题（2013-03-27）
建议时间：120分钟。

评分方法和注意事项：
1.按考场老师指示的方法和要求提交源代码文件。按题目编号命名和上传源代码文件problem1.cpp、problem2.cpp、problem3.cpp。提交不必要的文件、建不必要的文件夹、不必要的压缩、不按要求命名文件，而导致评测程序找不到对应文件的，将得0分。
2.第一、二题我们拟只采用黑盒测试，因此：可以不书写注释；更不必美化程序。
3.第三题我们对未通过黑盒测试的程序，将检查其程序，因此推荐写解题思路、注释，保持良好的编程风格。解题思路以注释的形式，放在源代码文件的开始，建议采用伪代码风格。如果您不能完成全部代码，书写正确的解题思路可能得部分分数。
4.仔细阅读题目要求，一定要确保您的输入输出严格符合要求。如输入输出格式不严格遵循题目的要求，会导致被判断为结果错误而不得分。没有特别说明的，输入为标准输入（键盘），输出为标准输出（屏幕）。
5.提交的源代码必须保持无编译错误，提交有编译错误的程序该题直接得-10分。
6.除题目另有要求外，程序执行时间应在1秒之内，程序中的死循环恕不等待。
7.不要编写破坏性程序，否则产生的结果对您也是破坏性的，即取消评分资格。
Problem1: 字符串匹配
对于主串M和模式串P，找到P在M中出现的所有子串的第一个字符在P中的位置。P中第一个字符所在的位置为0。首行的数字表示有多少组字符串。
[输入及示例]
2
ababababa
ababa
aaa
aa
[输出及示例]
0 2 4
0 1
(相邻位置之间用一个空格隔开)
Problem2:A Famous ICPC Team 
Mr. B, Mr. G, Mr. M and their coach Professor S are planning their way for the ACM-ICPC World Finals. Each of the four has a square-shaped suitcase with side length Ai (1<=i<=4) respectively. They want to pack their suitcases into a large square box. The heights of the large box as well as the four suitcases are exactly the same. So they only need to consider the large box’s side length. Of course, you should write a program to output the minimum side length of the large box, so that the four suitcases can be put into the box without overlapping. 
[Input] 
There are N test cases. The first line is N.
Each test case contains only one line containing 4 integers Ai (1<=i<=4, 1<=Ai<=1,000,000,000) indicating the side length of each suitcase. 
[Output] 
For each test case, display a single line containing the case number and the minimum side length of the large box required. 
[Sample Input] 
2
2 2 2 2 
2 2 2 1 
[Output for Sample Input] 
Case 1: 4 
Case 2: 4 
[Explanation] 
For the first case, all suitcases have size 2x2. So they can perfectly be packed in a 4x4 large box without wasting any space. 
For the second case, three suitcases have size 2x2 and the last one is 1x1. No matter how you rotate or move the suitcases, the side length of the large box must be at least 4. 
Problem3：A Famous Grid
Mr. B has recently discovered the grid named "spiral grid". 
Construct the grid like the following figure. (The grid is actually infinite. The figure is only a small part of it.) 

Considering traveling in it, you are free to any cell containing a composite number or 1, but traveling to any cell containing a prime number is disallowed. You can travel up, down, left or right, but not diagonally. Write a program to find the length of the shortest path between pairs of nonprime numbers, or report it's impossible. 

[Input] 
There are N test cases. The first line is N.
Each test case is described by a line of input containing two nonprime integer 1 <=x, y<=10,000. 
[Output] 
For each test case, display its case number followed by the length of the shortest path or "impossible" (without quotes) in one line. 
[Sample Input] 
3
1 4 
9 32 
10 12 
[Output for Sample Input] 
Case 1: 1 
Case 2: 7 
Case 3: impossible 



2014
复旦大学计算机科学技术学院 专业硕士复试上机考试题（2014-03-26） 
1. 按考场老师指示的方法和要求提交源代码文件。提交不必要的文件、建不必要的文件夹、不必要的压缩、不按要求命名文件，而导致评测程序找不到对应文件的，将得0分。没有特别说明的，输入和输出均为文本文件，存放在当前目录，即不要指定文件路径。文件命名如下：
源代码文件 输入文件  输出文件
第一题 p1.cpp  p1.in p2.out
第二题 p2.cpp  p2.in p2.out
第三题 p3.cpp  p3.in p3.out
第四题 p4.cpp  p4.in p4.out

 
2. 代码需使用标准C或C++语法，源代码内不要包含不必要的头文件(允许使用STL库)，一道题的所有代码都要放到同一个.cpp文件中，不要自己写其他头文件。程序的main函数请严格按照以下格式书写，不要使用编程环境自动生成的框架。程序入口必须为main，程序中没有main函数或不符合规定格式导致源码无法被机器正确评阅，将作0分处理。
//只包含必须的头文件
//不要使用IDE自动生成的代码框架
intmain() {
//此处填写代码
return 0;
}
3. 我们基本采用黑盒测试，因此不完全正确的程序，将可能只得到0分。
4. 仔细阅读题目要求，一定要确保您的输入输出严格符合要求。如输入输出格式不严格遵循题目的要求，会导致被判断为结果错误而不得分。输入输出示例中的注释文字，不是输入输出的组成部分。
5. 提交的源代码必须保持无编译错误，提交有编译错误的程序该题直接得-10分。
6. 除题目另有要求外，程序执行时间应在0.1秒之内，程序中的死循环恕不等待；内存占用不得超过128MB，超过限制的程序将不能通过测试。
7. 所有题目的测试数据不保证数据具有生活常识上的合理性。
8. 不要编写破坏性程序，否则产生的结果对您也是破坏性的，即取消评分资格。


第一题:  二分查找
问题定义
大家一定都能熟练掌握二分查找啦！那么来计算二分的次数吧！
约定二分的中点mid = (left + right) / 2。
输入：
第一行输入一个整数N（N<=10000）。
第二行输入N个升序整数。
第三行输入一个待查找的整数（必定在第二行中出现过）。
输出：
输出二分查找该整数时，进行过多少次二分。
输入样例
5
18 53 54 74 99 
53
输出样例
2

#include<iostream>
#include<stdio.h>
using namespace std;
int count=0,input[10001];
void search(int s,int e,int key)
{
    count++;
  int mid=(s+e)/2;
  if(input[mid]==key) return;
  else if(input[mid]>key) search(s,mid,key);
  else search(mid,e,key);
}
int main()
{
  freopen("p1.in","r",stdin);
  freopen("p1.out","w",stdout);
  int N,key;
  cin>>N;
  for(int i=0;i<N;i++) cin>>input[i];
  cin>>key;
  search(0,N-1,key);
  cout<<count<<endl;
  fclose(stdin);
  fclose(stdout);
    return 0;
}

第二题:  计算两个字符串的编辑距离
问题定义
把两个字符串变成相同的三个基本操作定义如下：
1.  修改一个字符（如把a  变成b）
2.  增加一个字符(如abed  变成abedd)
3.  删除一个字符（如jackbllog  变成jackblog）
针对于jackbllog 到jackblog  只需要删除一个或增加一个l  就可以把两个字符串变为相同。
把这种操作需要的最小次数定义为两个字符串的编辑距离L。
编写程序计算指定文件中字符串的距离。输入两个长度不超过512 字节的ASCII 字符串，在
屏幕上输出字符串的编辑距离。
输入样例
Hello world!
Hello word!
输出样例
13 
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
using namespace std;
int count;
int get_len(char *p)
{
  int len=0;char *t=p;
  while(*t++) len++;
  return len;
}

void  search(char *s,char *d,int step)
{
  if(step>512||step>count) return;//剪枝
  while(*s==*d&&*d&&*s) s++,d++;
  if((*s=='\0')&&(*d=='\0'))
  { 
    count=min(count,step);
  }
  if(*s=='\0')
  {
    count=min(count,step+get_len(d));//增加s
    return;
  }
  else if(*d=='\0')
  {
    count=min(count,step+get_len(s)); //删除s
    return;
  }
  search(s+1,d+1,step+1);//修改s
  search(s,d+1,step+1);//增加s
  search(s+1,d,step+1);//删除s
}
int main()
{
  
  freopen("p1.in","r",stdin);
  freopen("p1.out","w",stdout);
  char *p1=new char[520];
  char *p2=new char[520];
  gets(p1);
  gets(p2);
  count=512;
  search(p1,p2,0);
  cout<<count<<endl;
  fclose(stdin);
  fclose(stdout);
  return 0;

}

第三题：二叉树遍历
问题定义
输入一棵二叉树，输出树的前、中、后序遍历结果。
输入一个整数N（N<= 10000)，表示树中有N个结点（编号0~N-1）。
接下来N行，依次为结点0~结点N-1的左右孩子情况。
每行3个整数，F,L,R。L,R为F的左右孩子。L,R如果为-1表示该位置上没有孩子。
分三行分别输出树的前中后序遍历。
同一行中的数字，用一个空格间隔。
输入样例
5
0 3 1
1 2 -1
2 -1 4
3 -1 -1
4 -1 -1
输出样例
0 3 1 2 4
3 0 2 4 1
3 4 2 1 0
#include<iostream>
#include<stdio.h>
using namespace std;
bool spaceflag;
struct Node
{
    int L,R;
};
Node info[10001];
void visit(int key)
{
  if(spaceflag) cout<<" "<<key;
  else 
  {
    spaceflag=true;
      cout<<key;
  }
}
void preorder(int root)
{
    if(root==-1) return;
  visit(root);
  preorder(info[root].L);
  preorder(info[root].R);
}
void inorder(int root)
{
    if(root==-1) return;
  inorder(info[root].L);
  visit(root);
  inorder(info[root].R);
}
void postorder(int root)
{
    if(root==-1) return;
  postorder(info[root].L);
  postorder(info[root].R);
  visit(root);
}
int main()
{
  freopen("p1.in","r",stdin);
  freopen("p1.out","w",stdout);
  int N,t;
  cin>>N;
  while(N--)
  {
      cin>>t;
    cin>>info[t].L>>info[t].R;
  }
  spaceflag=false; preorder(0);  cout<<endl;
  spaceflag=false; inorder(0);   cout<<endl;
  spaceflag=false; postorder(0); cout<<endl;
  fclose(stdin);
  fclose(stdout);
    return 0;
}

第四题：Hanoi 塔
问题定义
Hanoi 塔问题是印度的一个古老的传说。开天辟地的神勃拉玛在一个庙里留下了三根金刚石的棒，第一根上面套着64 个圆的金片，最大的一个在底下，其余一个比一个小，依次叠上去，庙里的众僧不倦地把它们一个个地从这根棒搬到另一根棒上，规定可利用中间的一根棒作为帮助，但每次只能搬一个，而且大的不能放在小的上面。
请编写程序，把A 柱上的n 个金片，搬动到C 柱（中间可以使用B 柱），使得搬动的次数最少。输入金片的个数n（1<=n<=64），输出总搬动次数，以及最后100 次搬动。如果搬动次数小于等于100 则全部输出；每个搬动占一行，加上是这第几次搬动的数字和”:”，格式见示例。
输入样例
2
输出样例
3
1:A->B
2:A->C
3:B->C
#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int acount=1 ,ccount=0;
void hanoi(int n,char a, char b, char c)
{
    if(n==1) 
  {   
    if((acount-ccount++)<=100) 
      cout<<ccount<<':'<<a<<"->"<<c<<endl;
  }
  else 
  {
      hanoi(n-1,a,c,b);
      if((acount-ccount++)<=100)
        cout<<ccount<<':'<<a<<"->"<<c<<endl;
      hanoi(n-1,b,a,c);
  }
}
int main()
{
  freopen("p1.in","r",stdin);
  freopen("p1.out","w",stdout);
  int n;
  cin>>n;
  for(int i=0;i<n;i++) acount*=2;
  acount--;
  cout<<acount<<endl;
    hanoi(n,'A','B','C');
  fclose(stdin);
  fclose(stdout);
  return 0;
}



2015
今年3道题，比起上交浙大的题真的是简单多了，看没人发帖说一说，来凑个热闹哈
1.给出长方形的长和宽，每次从长方形里撕去最大的正方形，输出最后能得到多少正方形
2.给出a,b,c（3个整数），判断a,b能否通过+-*/得到c，ab可以交换位置，可以输出YES，不行输出NO
3.给出优先队列的实现，实现4个操作

    ADD N P：往队列里加入id为N的优先级为P的任务
    NEXT:输出下一个最高优先级的任务的id，如果优先级相同输出id小的任务，若队列中没有任务输出-1
    REMOVE N：移除id为N的任务
    COUNT：输出队列中的任务数量



今年上机用的oj，可以多次提交，但每道题只能看前两次提交的分数，oj挺坑的，中间还有会出bug，结果lz也不知道，一直提交，把查看的次数用完了


第一道水题劳资居然超时啊，后来看不到分不敢提交啊，坑
第二道也是水题，第三道直接用priority_queue感觉REMOVE可能会超时，我用的set和map做的





--------
2016
第一题 给定两个字符串，求最大公共字串的长度 ：   长度小于1000，两个for+string.find暴力可解

第二题 给定一个后缀序列，要求求值，只有加减（后缀倒是无所谓）：
   水题，后缀直接用栈做就好了，人家复试都是给前缀，要转换的，复旦真是给面子


第三题 是给定一个字符串，求哈夫曼编码的最短长度：
    哈夫曼树做，没什么特别要注意的，有好解法，因为你会发现就是求哈夫曼树的非根结点权值之和，或者所有非叶结点之和，想通了这题异常简单，
    笨方法建树求高度乘上节点的值也可以，建立指针为叶子指向父结点的树型结构，具体题目要求忘了，记得的可以补充一下

今年的题真的水啊，也就是浙大前三题的难度，今年用了正常的OJ无限次提交，两个小时，因为中间在填志愿收材料所以多加了5分钟

今年的oj可以选择c++的版本，有c++11哦，也就是说unordered_map/set这种神器是可以用的

据我所知一般都是A两道，3道全A的有两个人，全没有AC的也有















-----
network
-------
i have no strong desire to study my internetwork,mr wang's problem-driven
is the key of desire.
=======
------
uc-berkely
---------
i fell uc berkely 's influence.for them remove youtube 's course have influence 
so many people in hacker news.
------
health
--------
i should vare about my throat situation,for it  last 3 years.
-----
someone
----------
i wnat to write a konwledge map engine.
------
someone
--------
i find that i lost my way sometimes in the internet ,i donot feel
my eenrgy and interest.

------
someone
------
i need to live in international hotel to bring  new story to my life
------
algorithm
--------
i understand algorithm is about :sort ,search,heap,queqe,stack,link list,graph,my view is form
yanweimin,i can remember sort is very importtant ,sort algorithm has so many types:bubble sort,
bucket sort,heap sort ,iterate sort,or so on, i canot remember ,bubble sort 's principle is very simple,in ervery iteration,you need  to make the corresponding element to correct position.if there is 1,3,4,2,5'
for 5>2,you left position ,for 2<4,2 will be in 4  origin postion ,for 2<3,2 will  be in 3's position ,for 
2>1, i will go 1,i 's left position has no number .first sort is ok!!!!!iin algorithm ,i dislike complixity
analysis.for i feel that i cannot grasp math and logic in these algorithm.i believe 5,4,3,2,1 is the 
shit  case of bubble sort.this is o(n*n)! i remember there is another and usual sort algorithm............


-----
cs science
--------
My advice to self-learners is: never engage in "cargo-cult programming". This means: do not touch or reuse code that you do not understand. Force yourself to understand. If you lack the time, write it down and follow up later






>>>>>>> e447faf1447c7729fd2dc8bfb53c0e2be02f0b26
----
someone
-----
i used to repeat myself in diffcult or complix problem.
-----
someone
-------
once i grasped code , i can use top reascher agency's
paper to develop my ability and bussiness!!!
------
someone
-------
chance is great , i can get somethings from paper from
top university.this is great!!i believe my fortune will from there.i can use machnie to help my english spoken.
i can make appp  that every one can send a luanguge to the server and the server will response a native language to help language leaner.


------
someone
--------
from some view,i have no good rest to lead to my bad status of today!!
------
interview
--------
in interview,i feel that my konwlege is not enough.so .i donot get 
great job.
----
hbr living
-------
https://hbr.org/2017/03/if-you-want-to-be-happy-at-work-have-a-life-outside-of-it
------
python
-------
i think my python consists :before outputing result,what deos python interpreter do??string and byte,unicode,python all method.what in-memory 
actions is??

-----
python
--------
python interpreter is composed of compiler and vm.compiler produce 
bytecode ,vm excute bytecode to produce result.

----
resume
-------
strong english read ability.
database buckup project
database lookup tool 

-----
python
--------
heroku run the step pip install -r requirements.txt
------
interpreter
---------
in  interpreter  ,there is all kinds of interpretes,usual implement is 
lisp interpreter.i believe python implement python interpreter is
very usual.
-----
resume
---------
i can implement a python interpreter using go lang
i understand the classical python interpreter how run source code 
i understand run a python program in mmemory all actions.
i understand python program call graph.
i grasp all python algorithm 
i write a lisp interpreter use python
------
someone
-------
from now view,i want to get things ,so,this things will  occur ,
for example,i want to understand
how python excute a  .py ,
and the internet and youtube give me how to implement a interpreter.
python
-------
there are intepreter and compiler ,the interpreter will proccess source code
and run the result of processing,donot need to transform source code
to machine code ,the aboving machine code is compiler work by compiler.
-------
python 
-------
i think i need to know python interpreter how to work ,becuase , i donot be get 
used to gap the stage of how python file to be excute?
https://ruslanspivak.com/lsbasi-part1/
http://jayconrod.com/posts/40/a-simple-interpreter-from-scratch-in-python-part-4
http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html
http://stackoverflow.com/questions/16808387/writing-my-own-python-parser-and-interpreter
https://csl.name/post/vm/
https://morepypy.blogspot.jp/2011/04/tutorial-writing-interpreter-with-pypy.html




-----
idiom
------
“If you don’t know how compilers work, then you don’t know how computers work. If you’re not 100% sure whether you know how compilers work, then you don’t know how they work.” — Steve Yegge
------
python
-------
.py -----> lexicial analysis  generate token stram------->paser use token stream to make abrstract  tree------>ast will be transformed to bytecode--------vitrual machine run bytecode



------
someone
-------
i feel that recently i donot be trusted by caton's nomal people!




------
someone
-------
i have find that some one 's view donot let me feel softly!!!!!i need to 
absorb all people's view.
------
why 
-----
why the world is so many genius ,but am not  i ???
------
someone
------
i findthat china have so many chance in web innovation.
but i canot do more encourage step.



-----
i understand why my  web have no advance ,from my view, ihave no a suit for me  database that is free.i beeleive database i have solution that is i use weatherapp send data to tencent database!!!
!!!



-----
someone
-------
i understand my disre of  create a simple appp  ,for 
i  think i may  not hold or say, i have no so many energy 
to do  more complix things.
---
someoene
------
once i believe that i need a clean body and bed room  and cup
,if own these things ,i will be satisfied.i donot need to worry about my next food and next shoes and so on.
----
someone3
--------
i will  adopt just a littlite  advance ,i believe this method is healthy
!!!!

------
web 
-------
i need to rearrange my we b everyday ,i need to updown the web make new days occur in the topest
web.
------
someone
--------
i must to rethink my communicate  problem ,such as with mr jin ,
------
future
-------
i want to  become apple developer!because i want to connect  apple device to server 
!!!!i wnat to  set all kinds  of data in apple device.



------
python
------
i need to rethink ,what is my purpose of i want to grasp well python?/??

-----
english
------
i diske english pro ,such as ,as,down,with,i dislike as.



-----
freewriting
-----
the freeewriting tech do help to understand so many things ,but i hvave no desire to
rearrange it , i feel so tired!!!!i donot get more stroong disre to improve it



------
someone
--------
i want to look for a way to improve and level up my pythotn tech 
but in the one of three of march ,ialmost switch all kinds of python books,
i  donnot get suitable python books,i may need to rethink  mrs wang 's
problem-driven to learn.' 
and i want to set up  a company to host my calender and to do list app 's disre 
is having bee n so strong.!!!!'
-----
python
-------
i wnat to jnow python excute a .py script ?what memory occur?????this is my care about problem!!!
in the most recent,i want to know.when i run  a python  program
a=1
b=2
def test(a,b):
    reutrn (a+b)
from csapp view , ithin k memory donot have acllocte for name inly allocate space for value
when meet a function test,which  will vuild a stack ,i understand that is another space 
in memory,thet will use csapp theory.FROM  PHD ZHANG,I GET A VIEW ,a=1,a is  not cllocated space and 
whe python call a test function ,that is ,then,it will allocate a space.     






-----
python
------
python reserved some word ,we called keywords.
------
ivp
-------
first ,i understand ivp is  a hardware that receiver data ,processing data,output data.form now,receive
data is satelite or brodcat signal to deal with. i understand that  signal as network 's first layer 
.paser will unsrstand ------->signal-------->deal signal---------->ouput-------->..fro now,my routeline 
is :what is ivp? how to receive salite signal?there is a view,vedio codec is that ,from now
my task ,is to konw that in ivp 's all kins noun is what mean>??????from now , i only need to  call
get method to get infomation,i need to figure out all kinds of items.




-----
python and cs
-------
use mit with python introduce ,or it is a goood ideal
-----
python
-------
may it be ,reference and variable and name is same thing in python
-------
problem sloving
----------
say with a robot or a thing,you can understand /orgnize your puzzle.

------
python
------
i can let my heroku to run my code in  server forever via write code in main.py!!!!
python main.py in hthe hood ,i guess this is the mechinism of heroku

------
python
------
about python ,i need to build a map of kownledge,my current method is to




-----
future
------
mr wangwang supply great view about problem-driving ,
----
someone
------
ifeel thet my main problem is that  manage my energy to a things 2.explore all kinds of 
direcretion 3.how to applied my owning konledge to a things that will work.



-----
python
-------
in the inner of class ,you call class method,you should use self.method()
it is a good way ,class method also return self.
------
python
-------
i understand python context manager ,that is,it is used to manage context,it is
when you open a file ,you need to ,close a file,when you open a database connect ,you should close a connect.contexanager is to say ,oh ,if you are in north ,you need to open 
a door and you need to close a door.and the context manager will use the __enter__ and
the __exit__ method to implement it .and you can use with door() this form to do this things

------
someone
-----
when i have carros primary or /start stage ,i havenot get more progress.

------
someone
-------
i have a trend that i believe opinion by i believe he is a great pepole
------
python class 
-------
you can figure out python instance attribute must be arranged.
not have to be in __init__ constuctor.beswides.in python 2,class
Someone(object),in python 3 ,you can use class Someone: not subclass
object.i find that pythonn  

-------
python
--------
python requirements.txt used to install corresponding your package
when you distribute your code.as,pip install -e requirements.
------
cs
------
i need to make a  frame to orgnize my python konwledge.
-----
someone
-----
python




------
python
------
i konw that python class level variale is called class attribute ,and in __init__
methos we call instance attribute




-----
foture
=======
use video to recird your life ,it is a great ideal,i have find it in university
but i donot apply it,i will use it in next days.

------
SOMEONE
---------
connect the world is the way you feel your exsistence.
-----
someone
-------
i need to check or other my  love view

------
cs finance
---
i can convert pdf and download youtube to bussiness.



-------
finance
------
finnace is on time and crisis.


------
some one
-------
i have a feeling ,thet is real ,finnace safety ,i have not been owning it 
from these years,this point ,i have must to noted.

-----
self improving
-----
i have learned a great view,anythings if you need todo,you only
three seconds to thinks ,if yo exceed 3 secnds,you will not
----
slef improving
------
1.keep your blood sugar level
2.sleep in designated time 
3.set a break interval during 90-120 /or depend on yourself.
4.
-----
english  read
------
for read view,you dont have to gigure out every word,you only need to guess
,if the word occur again,you need to figure out via tools book
-------
english
______
many executives don’t find ways to practice consistently healthy behaviors, given all the other demands in their lives
GIVEN ====because.



------
someone
-------
sleep early and getting up early ,these yeaers i have not succeddd.
------
someone
---------
look for enengy of myslef solution is a good ideal ,because
i feel these years i hav been being  tired!!!!!
------
somone
-------
i feel that  the period  of caton isno longer time.for i will not get more
my duty，icannotfind more accute position in caton.

-----
problem slove
-----
in a book about complixity,it use divide and conquer method to
test volume.

-------



                    problem sloving

                 math    economy     cs 

                   english    people  


------
book
------
from self contorl view,add blood sugar is very good level.
------
pythonlist
----------
python list concentrate action is composed
by l1+l2 it will produce a new list ,we set a empty list
it is..........[],
for elem in l1:
    a.appended(elem)
for elem in l2:
    a.appended(elem)    
also,i see mit algorithm course ,them say in list operation ,many action
is o(1) complixity.
-----
python
------
detect a class leevl ,you can ask sb how to restrict class instance attribute
,such as a.b or a.b=3 if you need to gurantee this attibute >0????
my now answer is to use descriptor.
------
python
-------
python protocal is a set of method........

-----
python class
------
python class self ,best understand is  that,if a instance was created ,self
is simialr to a instance.in fact ,i feel ,eeven if you created a class,when 
define a instance ,you can add a instance attribute,for axample:
class A:
    def __init__(self,bi,lu):
        self.author=bi
        self.title=lu
you can use a=A(67,78),YOU CAN USE a.io='yangmingishandsome'        

----
python
-----
if  i define a class ,i can use a.attribute=5 to reassign a class attribut????
in fact ,it is real ,you can that i have via experiement,read ooficial document
's difficulty is that you may donot have a bluprint of the concept.'
-----
python
-----
imho ,python operator is such as + - /％　ｅｔｃ..
-----
resume
-------
i have bug database of python ,mysql
i can use source control tool

---
someone
---
my opiniopn is that i can use python do anything.
----
openspource
-------
i need opensource to open my career.which director i need?????my
ideal is tohelp others and get  a bunch  of
 margin,now i need to yhink  what can i do use machining learning,what can i do 
 via python for marigin?????for nmore great career.

----
nginx
-----
i need to  konw what nginx can do???????
------
python
------
python all object was inplemented by class ideal by doctor zhang
-----
python 
-----
python interpreter run  a .py file located in disk and ask os to allocate space in
memory to run the program.before compiling,there is a paser ,it will parser grammar 
to syntax tree,comiple the tree to bytecode.there  are more discuss,in compile,that is
,.py------>.pyc that is,in fact,import sector will convert to .pyc .for example.a.by 
include import b(b.py),that is ,b.py-------b.pyc.but a will not compile.but in the runtime a.py will be compile to .pyc in memory.........but when you exit ,it will
delete .pyc file..
-----
python
------
form now,i feel that python all kinds of methods implemented by class method
aalso,class method main include magical method,this is main method to implement
such as len(), d[k],in so on .yeah .of course,i doubt that string ,list ,dict is
some subclass ,just  a guess ,such as ,collection,object .......balbala.about class method ,there is a mechinism called fall back to ,it is, when you invoke a method ,the method doesnot exist ,it will invoke another method.
------
python
-------
python array 's exsistence let me feel annonyed ,bacause 
my c foudation is weak.
------
someone
------
i think that this summer is the time i left caton
----
image recognization
------
i find the this that it locate the position to find the position's function
when again you stop the postion (coordinate),it will detect the function value is
corresponding the value.
------
python
------
i just want to say that if you  import a moudle that moudle include print('balalabalala')
when you import,the print will  be excute.
-----
python
------
python running a script 's process is that complie a .py ----->.pyc (or other)
bytecode file and python intepreter excute the .pyc file.but i want to know
.py how to be complied and by who??????what i need know is that if python run 
a .py file ,for example in a project,python run a hello.py but he invoke other 
module,how it work with he hello.py????why open a file and you need close the file???
.of course ,i understand .pyc file is a binary file.
----
world
-----
the worls seem to seek more quick speed.more speed.
----
someone
-----
i find that when i slove a probem ,when it related to many things
i will be distracted,so may be my cause for can not finish a
things totaly ,it may be that forget why start?????
----
someone
-----
i wanna listen other and i wanna cultivate the habit that make me
do one thing at once. 
----
python 
------
i feel that list in memory is  a array.or it is notassciated
with c's array,i need to understand it vi asking phd zhang.
-----
someone
-----
about distraction.my solution is that place my time in a bucket that 
including math,cs,english,and economy.that will do well,i guess,but
there are a problem that how can i can i orginize the konedege that
i donot drown in the ocean of konelege????
----
someone
-----
i feel like that my the shit problem is stop a things in half way
many things i donot perserve anfd i cannot go on,why?this is 
my biggest problem.
----
python 
-----
i can feel that python interpreter actions when you run a script or a program ,a=3,allocate memory
??????????????????????????????????????????????a=Classexample(6,7,8).same ,allocate for the instance
,when you can use len(a)(the class implement __len()__ mwthod ),the interpreter see what a is ???
fuck it is a class (i doubt there it activate a mechinism that check  the type object,for instance,
the checked result is string ,it will understnd string class have implemented __len__ method,it will
invoke it,a.__len__() and the return value.) ,it will check if the class include a __len__() method,
if it  include,it will  get the value.if not,it will  give callback error or say it is exception!!!!
.about garabage collection  mechnism ,tha is another thing!!!!!!
-----
someone
-----
when you want to say in writting,you can access your inner.
----
python
--------
i doubt all python object implemented by class
phd sai that python object in python shell(or interpreter ) life circle
is exit python shell.but in function ,wehn function end,the object end ,but 
also observe reference count.another info a=[1,23,4,5],when i use a[3]=1,i only in-place (origin list position) change list rather than create a list,but also
spicial situation.you must notice.from my opinion,a=[1,2,3,4,5,6].you can understand that
list is common mutable consequnce,but string and tuple ,string is immutable,what is immutable,
immutable is a[3] if can change origin consequnce value. i can undestand ,when you a=a+b ,id(a) donot equal 
origin id(a),but you use a+=[2],id(a) is oriign value.this is same in literaly.you can understand that in-place 
as same position but new is not at same position.__iadd__ is the former ,by visrce.
-----
someone
-----
i always believe that there is a method or think tool to help people to slove any question!
-------
book
-----
it may be  a book https://news.ycombinator.com/item?id=12459216
---
network
-----
i feel sad with network??i undestand layer as n protocal in a layer
---
about algorithm
------
https://news.ycombinator.com/item?id=4783301
----------------
how to read a book
------
https://news.ycombinator.com/item?id=12209446
-----
sf  scope
------
I somehow cannot understand the trends, altough I checked following sites and utilized Twitter stats/trends.

* http://www.google.com/trends

* http://www.trendsresearch.com

* http://www.worldtrendsresearch.com/major-trends.php

Here is a general list of ideas that I'd like to pick 2 to 3 from the topics to create a project that is mashing them up in a Ruby On Rails project. It's important to choose only key features of each topic and merge them into one idea.

I don't see the problem that people seem to have according to trends, so I cannot solve it.

Can you please help me with that? I'm searching for a project idea.

Here's a list of Project Ideas I found in the net.

==================================================

1. Business Performance Reporting

2. Case Management for Government Agencies

3. Classroom Management

4. Clinical Trial Initiation and Management

5. Competitive Analysis Web Site

6. Discussion Forum website

7. Disputed Invoice Management

8. Employee Training Scheduling and Materials

9. Equity Research Management

10. Integrated Marketing Campaign Tracking

11. Manufacturing Process Managements

12. Product and Marketing Requirements Planning

13. Request for Proposal Software

14. Sports League Management

15. Absence Request and Vacation Schedule Management

16. Budgeting and Tracking Multiple Projects

17. Bug Database Management

18. Call Center Management Software

19. Change Request Management

20. Compliance Process Support Site

21. Contacts Management Software

22. Document Library and Review

23. Event Planning and Management

24. Expense Reimbursement and Approval

25. Help Desk and Ticket Management

26. Inventory Tracking

27. I T Team Workspace

29. Job Requisition and Interview Management

28. Knowledge Base

29. Lending Library

30. Physical Asset Tracking and Management

31. Project Tracking Workspace

32. Shopping Cart

33. Knowledge Base 34 Lending Library

35. Physical Asset Tracking and Management

36. Project Tracking Workspace

37. Room and Equipment Reservations

38. Sales Lead Pipeline

39. Yellow Pages & Business Directory

40. Time & Billing

41. Class Room Management

42. Expense Report Database

43. Sales Contact Management Database

44. Inventory Management Database

45. Issue Database

46. Event Management Database

47. Service Call Management Database

48. Accounting Ledger Database

49. Asset Tracking Database

50. Cycle Factory Works Management

51. Sales Corporation Management

52. Business Directory

53. Education Directory

54. Dental Clinic Management

55. Fund Raising Management

56. Clinic/ Health Management

57. Cable Management System

58. Survey Creation and Analytics

59. Museum Management System

60. Multi-Level Marketing System

61. Learning Management System

62. Knowledge Management System

63. Missing Person Site

64. Disaster Management Site

65. Job Management Site

66. Financial Portfolio Management

67. Market Research Management

68. Order Management System

69. Point of Sale

70. Advertisement /Banner Management and Analytics

71. Export Management System

72. Invoice Management

73. Recruitment Management System

74. Articles / Blog / Wiki Web site

75. Online Planner

76. Mock Tests and Examination Management

77. Examination System

78. Practice Test Management.

79. Asset Management System

80. Travel Agency System.

81. Placement Management System.

82. Polls Management

83. Customer Management

84. Project Management System.

85. Network Marketing System

86. Yoga Health Care Management

87. Personal Finance Management System

88. Real Estate Management System

89. Stock Mutual Funds Management

90. Careers and Employment Management System

91. Music Albums Management System

92. Classified Ads Managements

93. Property Management System

94. Sales & Retail Management

95. Dating Site

96. Hotel Management System

97. Search Engine

98. Online News Paper Site

99. Image Gallery 100. Staffing and Human Capital Management

101. Address Book

102. Inventory Management System

103. Newspaper Classifieds

104. Hostel Management 105Music , Lyrics Website .

106. Wildlife Safari Trip Management

107. Wildlife Sanctuary Management

108. Wild life Flora and Fauna Statistics Management

109. Animal Hospital Management

110. Zoo Management System

111. Agro-Forestry Management System

112. Bus Depot Management System

113. Even t Management System

114. Clinical Research Management System

115. Food Technology Management System

116. Circus Management System

117. ResortManagement System

118. Bugs/IssuesManagement System

119. Life /MotorInsurance Management System

120. Exam Scheduler

121. Ad CampaignManagement System

123. Internet Banking Management System

124. Ad Agency Management System

125. Vechical Traffic Management System

126. Web Traffic Analytics Management System

127. Solid Waste Management System

128. Peer-To –Peer File Sharing System

129. Chat Application

130. Crisis Management System

131. Disaster Management System

132. Document Management System

133. Security Threats Evolution Software

134. Digital Rights Management System

135. Games ,Single , Multi-Player

136. Content /Document Management System

137. Archaeological Survey Management System

138. Market Research Management System

139. Crime Management System

140. Jail/Prisonmanagement System

141. Telephone Traffic Monitoring Management System

142. School Drop Out Statistics and Analytics System

143. Lost & Found Management System

144. Online Tutorials Management System

145. Bulk Sms Application

146. Criminal Records management System

147. Email Campaign Management System

148. Political Campaign Management System

149. Skill Competence and Mapping Application

150. Ontology based Web Crawler (source: http://goo.gl/Du3ow)
-----
python 
------
python switch variable 
a,b=b,a
-----
python tuple
-----
tuple 's element is all kinds of types,but immutable
from now,memory is big problem ,when related to redis and python generator
----
login and autication
--------
i undestand that authentication sys is user send username and password,if username and password doesnot 
exsit in database,return register html page,user fill info (via form) and click submit(register) ,send info
to server ,and server store info in database,return login page.about  password style in db,imho,should use 
hash code style,from my  now,i donot hash and donnot set password policy ,and donnot restrict or say that i donot
know how to protect info 's secure. html.page you can refer to https://github.com/oxfordyang2016/flask-help/blob/master/hello.py
----
html
-----
when you use html form,you can use from element to  implement the function 
in from element .there was a things called action,you can use the example to
implement this function .at the same time ,you also note that method can be specify
,imho,post only fro more secure=ly upload data
<form action="http://global.bing.com/?FORM=HPCNEN&setmkt=en-us&setlang=en-us" method="POST">
        <div class="login">
                <div class="login-screen">
                        <div class="app-title">
                                <h1>Login</h1>
                        </div>

                        <div class="login-form">
                                <div class="control-group">
                                <input type="text" class="login-field" value="" placeholder="username" name="username">
                                <label class="login-field-icon fui-user" for="login-name"></label>
                                </div>

                                <div class="control-group">
                                <input type="password" class="login-field" value="" placeholder="password" name="password">
                                <label class="login-field-icon fui-lock" for="login-pass"></label>
                                </div>

                <input type="submit" value="Log in" class="btn btn-primary btn-large btn-block" >
                            <br>
                        </div>
                </div>
        </div>
</form>
of course ,you need to think that when you first send data to  which url?????????you can verify form data 
via in python to get form data
----
cs
---
login,regester,logout,all take actions that includes send 
data to server ,server deal with data ,return html,when data sent to server will be store database or verify .
-----
someone
------
i need a heart state that when i finish all tasks,i need rest!!!!!but i face all situation is that tasks cannot be donw or i dnonot want to stop. 
----
cs
---
what i understand the internet is the c/s ,sustomer
send data to server ,server detect data if need be deal with,such as user if login,if data written to database,
server's function do deal with the data and return data
to customer,from send data view,i understand what style to
be used to send data ,it related to network ,i can go on  abstarct transmit data(via internet ,forward data to corresponding function),encript data,deal data,imho ,coreesonding network and algorithm,languge.of course ,i find that you must note there is data store problem. 
data problem
---
---
authication 
-----
from path,i find to check a user if login in ,if not
it will stop login page--
python
---
via implement a __getitem__ and __len__ method,i can implent a sequence (or list )
most method,susch as len ,a[3],balabalbala......but i cannot change the sequece
's position  and value.imho,when you implement python __getitem__ method,when use len()
function,implecitly  invoke the __getitem__ method,other functions seem to be same!!!you must know python interpreter invoke this spicial methos,interpreter is 
python version......i want to say that __repr__ and __str__ 's effect is same .but we advise you use __repr__method
imho,sequence is somthings such as animal include pepole 
,monkey ,dog,pig,sequence include list.string etc
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















 