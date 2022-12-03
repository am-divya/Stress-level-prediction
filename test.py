from flask import Flask, request,render_template,redirect,url_for
from flask_cors import CORS
from datetime import datetime
app = Flask(__name__,instance_relative_config=True)
app.config['SECRET_KEY'] = "SATYASAIRAZOLE"
cors = CORS(app, resourses={"/*": {"orgins": "/*"}})
import pandas as pd 
from sklearn.metrics import accuracy_score 
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
#df = np.loadtxt('stressdataset.csv', delimeter = ',')
import matplotlib.pyplot as plt
df= pd.read_csv("E:\cc\divya\DataSet_Stress1 - Sheet1.csv")
df.head()
from sklearn import tree

clf = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
X = [[5,3,5,2,3,5,5], [2,2,2,1,1,4,2], [2,3,1,0,0,1,1], [1,2,2,2,2,4,4], [4,3,5,2,1,3,5],
     [5,1,1,1,2,2,4], [1,2,3,2,1,5,3],
     [4,1,4,1,0,4,5], [5,3,2,1,1,5,2], [3,3,2,2,2,5,4], [3,2,3,0,2,5,4], [1,3,0,1,0,4,2],
     [2,2,1,0,0,5,1], [1,1,3,2,0,3,2], [2,2,5,2,0,4,3], [1,3,4,1,2,3,2], [1,2,4,1,2,4,3],
     [3,2,3,0,2,5,4], [3,3,2,1,1,4,3], [4,2,1,2,1,5,4], [3,1,5,2,1,4,3], [2,1,4,2,3,5,4],
     [3,1,3,2,2,4,3], [4,3,4,1,2,3,3], [2,2,2,1,1,5,3], [1,3,4,1,0,1,4], [3,2,3,1,0,2,5],
     [2,2,1,2,3,2,5], [4,2,0,2,2,2,5], [2,2,0,1,1,3,4], [3,2,0,1,2,2,5], [1,3,2,0,3,4,4],
     [3,3,3,0,2,2,3], [2,3,4,0,1,3,3], [4,2,1,2,1,2,2], [5,2,2,0,3,3,2], [5,2,1,0,3,2,1],
     [5,3,2,0,0,5,2]]

Y = ['high', 'low', 'low', 'low', 'high', 'low', 'low', 'high',
     'high', 'high', 'high', 'low', 'low', 'low', 'low', 'low', 'low', 'high', 'low',
     'high', 'high', 'high', 'low', 'high', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low',
     'low', 'low', 'low', 'low', 'low', 'low']



@app.route('/')
def leela():
    #return "hello world";
    return render_template('index.html');

@app.route('/home')
def home():
    return render_template('home.html');

""" @app.route('/test')
def test():

    return render_template('index.html'); """

@app.route('/stress_form',methods=['GET','POST'])
def stress_form():
    stressvalue=""
    if request.method=='POST':
        x1= request.form.get('sleep')
        x2= request.form.get('headache')
        x3= request.form.get('dizz')
        x4= request.form.get('caffine')
        x5= request.form.get('alcohol')
        x6= request.form.get('thinking')
        x7= request.form.get('overthinking')
        #---------------------------------------------
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(X, Y)

        tree.plot_tree(clf)
        #tree.plot_tree(X,Y)
        #prediction = clf.predict([[3,3,2,2,2,5,4]])[0]
        prediction = clf.predict([[x1,x2,x3,x4,x5,x6,x7]])[0]

        stressvalue=prediction+"stress"

        #---------------------------------------------
    return render_template('form.html',stress=stressvalue)

@app.route('/addMainCat',methods=["POST"])
def addMainCat():
    v = request.form.get('main_category')
    
    if v != None:
        print(v)
        return redirect(url_for('home'))
        #return {'status': 'success','message':'main category added'}
    else:
        return redirect(url_for('home'))
       # return {"status": "fail", "message": "main category not added"}


@app.route('/addSubCat',methods=["POST"])
def addSubCat():
    m = request.form.get('main_category')
    s = request.form.get('sub_category')
    if m != None and s != None:
        print(m)
        print(s)
        #return {'status': 'success','message':'main category added'}
        return redirect(url_for('home'))

    else:
        return redirect(url_for('home'))
        #return {"status": "fail", "message": "main category not added"}

@app.route("/uploadArticle",methods=["POST"])
def upload_article():
    title = request.form.get("title")
    pub_date = request.form.get("pubDate")
    content = request.form.get("content")
    #display_position = request.form.get("display_position")
    category =  request.form.get("category")
    author = request.form.get("author")
    author = request.form.get("tags")
    imageUrl = request.form.get('image_url')
    postUrl = request.form.get("post_url")
    # image_link = ""
    # print(post_tag,category)
    dt_obj = datetime.datetime.strptime(pub_date,
                           '%Y-%m-%dT%H:%M:%S%f')
    millisec = dt_obj.timestamp() * 1000

    data = {"title":title,"pubDate":millisec,"content":content,"display_position":display_position,"category":category,"author":author,'image_link': imageUrl,"post_link":postUrl}
    print(data)
    return {'status':'success','message':'article uploaded'}


@app.route("/uploadObiterDicta",methods=["POST"])
def upload_obiter_dicta():
    caption = request.form.get("caption")
    pub_date = request.form.get("pubDate")
    dt_obj = datetime.datetime.strptime(pub_date,
                           '%Y-%m-%dT%H:%M:%S%f')
    image = request.form.get("imageUrl")

    data = {"imageLink":image,"caption":caption, "pubDate": dt_obj}
    print(data)
    return {"status": "success",'message': 'obiter dicta uploaded'}


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")