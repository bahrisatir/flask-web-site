from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    cevap = ""

    if request.method == "POST":
        soru = request.form.get("soru")

        if "nasılsın" in soru.lower():
            cevap = "İyiyim, sen nasılsın?"
        elif "adın ne" in soru.lower():
            cevap = "Ben Halil'e Sor sistemiyim 😄"
        else:
            cevap = "Bu soruya henüz cevap vermeyi öğrenmedim."

    return render_template("index.html", cevap=cevap)

from flask import Flask, render_template, request

# ... (mevcut kodların) ...

@app.route('/sor', methods=['POST'])
def sor():
    gelen_soru = request.form.get('soru').lower()
    
    if "aşkın kim" in gelen_soru:
        cevap = "Benim tek aşkım zehra! "
    else:
        cevap = "Güzel soru! Halil buna yakında cevap verecek."
        
    return f"<h3>Cevap:</h3> <p>{cevap}</p> <a href='/'>Geri Dön</a>"

if __name__ == "__main__":
    app.run(debug=True)

