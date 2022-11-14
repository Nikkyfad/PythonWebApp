from flask import Flask, render_template, url_for, request, send_file, Response
from business import ScrapeContent

app = Flask(__name__)

 

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    sc =ScrapeContent(username=output["uname"], tweet_count=output["tweet_count"])
    
    return Response(
        sc.scrape_content(),
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=results.csv"})





if __name__ == "__main__":
    app.run(debug=True)