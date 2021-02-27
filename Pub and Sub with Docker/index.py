# import redis
from flask import Flask,render_template,request

# connect to the redis
# r = redis.Redis(host='redis',port=6379,db=0,charset='utf-8',decode_responses=True)

app = Flask(__name__)

# inital the publish that will contain all the publish message from every user
publish = {}

# def renew function that re-new the publish from current data
# def renew():
#     global publish
#     for i in r.keys():
#         a = eval(r.get(i))
#         publish[i] = a

# initial the subList, that subList will contain current user's Sub topic
subList = []

# run the renew funciton in the beginning of the program that publish will receive all current publish messages that
# database have
# renew()

# inital the html web page with inital information
@app.route('/')
def Home():
    return render_template('index.html',subList=subList,publishList=publish)

# define the html page that when user click the any submit button and information post
@app.route('/',methods=['POST'])
def getPostByOne():

    # if one of the submit button click and some information post
    if request.method == "POST":

        # if the button is submit and message and the message textarea and topic selection is not empty
        # then writeData with topic and message into databse and renew the publish List and return the new
        # html page with new information
        if request.form['submit'] == 'Submit':
            if request.form['topic']!="" and request.form['message']!="":
                topic = request.form['topic']
                message = request.form['message']
                writeData(topic,message)
                renew()
                return render_template('index.html',subList=subList,publishList=publish)
            else:
                return render_template('index.html',subList=subList,publishList=publish)
        # if the button is Sub then the topic of selection will add to the current user's subList and call renew function
        # to re-new the publish List and return the new html page with new information
        elif request.form['submit'] == 'Sub':
            topic = request.form['subTopic']
            if(topic not in subList):
                subList.append(topic)
            renew()
            return render_template('index.html',subList=subList,publishList=publish)

        # if the button is notify then will call renew function to re-new the publish List and return the new html page with new information
        elif request.form['submit'] == 'Notify':
            renew()
            return render_template('index.html',subList=subList,publishList=publish)



# define writeData function, use to write data with topic and message into current database
def writeData(topic,message):
    if r.exists(topic):
        m = r.get(topic)
        now = eval(m)
        now.append(message)
        r.set(topic,now)
    else:
        m = [message]
        r.set(topic,m)


# sql = "INSERT INTO information (Topic, Messages) VALUES (%s, %s)"
# val = ("Animal","You are dog")
#
# mycursor.execute(sql,val)
#
# # mycursor.execute("SHOW DATABASES")
#
# mycursor.execute("SELECT * FROM information")
#
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)
#
# mydb.commit()
if __name__ == "__main__":
    app.debug = True
    app.run()
