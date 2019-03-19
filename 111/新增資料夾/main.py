from flask import Flask , render_template,request
form horoscopeapi import zodiac_sign, get_horoscope
app = Flask("Test")

def calculate_gen(year_parameter) :
    gen='Unknow'

    # add logic here to identify generation
    if year_parameter >= 1964 and year_parameter <=1978:
        gen='very OLD'
    if year_parameter > 1979 and year_parameter <= 1995:
         gen='Y - Millenials'
    if year_parameter > 1996 and year_parameter <= 2012:
        gen='Z'

    return gen


@app.route("/")
def default():
    m = "Welcome to my page"
    return render_template("index.html", message=m)

@app.route("/<vistor>")
def hello(vistor):
    m = "Welcome to my page:" + vistor.title()
    return render_template("index.html", message=m)
    #return "hello"



@app.route("/gen",methods=["POST"])
def showgeneration():
    form_data=request.form
    year =form_data["dob"]
    day =form_data["day"]
    month =form_data["month"]
     gen=calculate_gen(int(year))

    return render_template("gen.html",generation=gen)


@app.route("/horoscope",methods=["POST"])
def handle_horoscope():
    form_data=request.form
    year =form_data["dob"]
    day =form_data["day"]
    month =form_data["month"]
     zsign= zodiac_sign(int(day),int(month))
     data= get_horoscope(sign)


    return render_template("gen.html",generation=gen)


app.run()
