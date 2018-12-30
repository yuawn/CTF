# 35C3 CTF 2018
## juggle
* There is many stack-based-like operation and some methods can do something like branch.
```
show        <plate><宫保鸡丁></宫保鸡丁></plate>
+           <plate><rösti></rösti></plate>
-           <plate><לאַטקעס></לאַטקעס></plate>
*           <plate><poutine></poutine></plate>
/           <plate><حُمُّص></حُمُّص></plate>

push        <plate><paella>0</paella></plate>
del         <plate><γύρος></γύρος></plate>
copy        <plate><불고기></불고기></plate>
insert      <plate><köttbullar></köttbullar></plate>
cmp arg     <plate><stroopwafels></stroopwafels></plate>
cmp cheif   <plate><ラーメン></ラーメン></plate>
branch      <plate><æblegrød></æblegrød></plate>

dec cheif   <plate><Борщ></Борщ></plate>
flag        <plate><दाल></दाल></plate>
```
* Use them to build binary search.
* `<flag>35C3_The_chef_gives_you_his_compliments</flag>`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<meal>
    <state>
        <drinks><value>0</value></drinks> <!-- L -->
        <drinks><value>4294967296</value></drinks> <!-- R -->
    </state>

    <course>
        <plate><paella>1</paella></plate>
        <plate><불고기></불고기></plate> <!--copy R-->

        <plate><paella>1</paella></plate> 
        <plate><불고기></불고기></plate> <!--copy L-->

        <plate><לאַטקעס></לאַטקעס></plate> <!-- L - R -->

        <plate><paella>-2</paella></plate>

        <plate><stroopwafels></stroopwafels></plate> <!--cmp (L - R) > -2 -->

        <plate><paella>1</paella></plate>
        <plate><paella>2</paella></plate>
        <plate><köttbullar></köttbullar></plate> <!--insert-->

        <plate><æblegrød></æblegrød></plate> <!--branch to course[3] if (L - R) == -1 (found)-->

        <plate><paella>1</paella></plate>
        <plate><불고기></불고기></plate> <!--copy R-->

        <plate><paella>1</paella></plate> 
        <plate><불고기></불고기></plate> <!--copy L-->

        <plate><rösti></rösti></plate> <!--add L R-->

        <plate><paella>1</paella></plate>
        <plate><paella>2</paella></plate>
        <plate><köttbullar></köttbullar></plate> <!--insert-->

        <plate><حُمُّص></حُمُّص></plate> <!--div mid-->

        <plate><paella>0</paella></plate>
        <plate><불고기></불고기></plate> <!--copy mid-->

        <plate><ラーメン></ラーメン></plate> <!--cmp chef-drinks-->

        <plate><paella>1</paella></plate>
        <plate><paella>1</paella></plate>
        <plate><köttbullar></köttbullar></plate> <!--insert-->
        
        <plate><æblegrød></æblegrød></plate> <!--branch to course[2] if(mid > chef-drinks)-->

        <plate><paella>1</paella></plate>
        <plate><γύρος></γύρος></plate> <!--del L -> L = mid -->

        <plate><paella>0</paella></plate>
        <plate><paella>1</paella></plate>
        <plate><æblegrød></æblegrød></plate> <!--branch to course[1]-->

    </course>

    <course>
        <plate><paella>2</paella></plate>
        <plate><γύρος></γύρος></plate> <!--del R-->

        <plate><paella>1</paella></plate>
        <plate><paella>1</paella></plate>
        <plate><köttbullar></köttbullar></plate> <!--insert-->

        <plate><köttbullar></köttbullar></plate> <!-- insert -> R = mid -->

        <plate><paella>0</paella></plate>
        <plate><paella>1</paella></plate>
        <plate><æblegrød></æblegrød></plate> <!--branch to course[1]-->
    </course>

    <course>
        <plate><Борщ></Борщ></plate> <!--dec chef-drinks-->

        <plate><दाल></दाल></plate> <!--flag-->

        <plate><paella>4294967296</paella></plate> <!--push R-->
        <plate><paella>0</paella></plate> <!--push R-->

        <plate><paella>0</paella></plate>
        <plate><paella>1</paella></plate>
        <plate><æblegrød></æblegrød></plate> <!--branch to course[1]-->
    </course>
</meal>
```