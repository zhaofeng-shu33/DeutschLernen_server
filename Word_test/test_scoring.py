import sqlite3
def recv_result(request):
    db=sqlite3.connect("user")
    cu=db.cursor()
    t=datetime.now()
    time=t.strftime("%Y%m%d%H%M%S")
    rq=request.POST
    user=rq.get('User','$0')
    uid=0
    count=rq.get('Count','$1')
    words=rq.get('Words','$2')
    words=words.split(',')
    wid=""
    for i in range(count):
        cu.execute("select id from word where entry ='"+words[i]+"'")
        tempid=cu.fetchall[0][0]
        wid=wid+str(tempid)+","
    result=rq.get('Result','$3')
    cu.execute("insert into test(uid,time,count,wid,result) values("+uid+",'"+time+"',"+count+",'"+wid+"','"+result+"');")
    db.commit()
