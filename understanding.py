from flask import Flask,redirect,url_for

app = Flask(__name__)                   #WSGI application, connection b/w web server and application; communicating with server

# print(__name__)
#__name__ -> set to name of module in which its used, here set to __main__ because we are running the script directly; This helps flask to find other files

@app.route('/')       #decorator; directed to root; whenever we enter root this will execute
def welcome():
    return "My application"

@app.route('/members')
def members():                         #function cannot be same
    return "Hello Members"

@app.route('/succ/<int:score>')
def success(score):
    return "Passed Succesfully with " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "Failed Succesfully with " + str(score)

@app.route('/judgement/<int:score>')
def judgement(score):
    result = ""
    if score < 80:
        result= "fail"
    else:
        result = "success"

    return redirect(url_for(result,score=score))                  #redirect -> redirect specific url; url-> making url for parameters, result is checking function name not page not


if __name__ == '__main__':                #starts a web server only if script is run directly
    app.run(debug=True)
