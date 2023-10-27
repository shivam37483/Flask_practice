from flask import Flask,redirect,render_template,url_for,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/results/<int:score>')
def results(score):
    answer = ""

    if score > 50:      
        answer = "PAss" 
    else:
        answer = "Fail"

    return render_template("result.html",result= answer)

@app.route('/judgement',methods=['POST','GET'])
def check():
    total_score = 0

    if request.method == 'POST':
        java = float(request.form['java'])
        js = float(request.form['js'])
        ruby = float(request.form['ruby'])
        python = float(request.form['python'])
    
        total_score = (java+js+ruby+python)/4

    return redirect(url_for('results',score=total_score))

if __name__=='__main__':
    app.run(debug=True)