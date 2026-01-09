from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sor', methods=['POST'])
def sor():
    # Formdan gelen soruyu alıyoruz
    gelen_soru = request.form.get('soru', '').lower().strip()
    
    # Soru-Cevap Mantığı
    if "aşkın kim" in gelen_soru:
        cevap = "Zehra benim tek aşkım! ❤️"
    elif "naber" in gelen_soru or "nasılsın" in gelen_soru:
        cevap = "Bomba gibiyim! Spor ve kod arasında gidip geliyorum, sen nasılsın? 💪"
    elif "yaşın kaç" in gelen_soru or "kaç yaşındasın" in gelen_soru:
        cevap = "Ruhum hep 20, ama takvimler başka bir şey diyor olabilir... 😉"
    elif "ekrem" in gelen_soru:
        cevap = "Ekrem tombik g*t benim arkadaşım! 😂"
    else:
        cevap = f"'{gelen_soru}' sorusuna Halil henüz cevap vermedi. Ama üzerinde çalışıyor!"

    # Cevap Sayfası Tasarımı (HTML ve CSS beraber)
    return f"""
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Halil'in Cevabı</title>
            <style>
                body {{ font-family: sans-serif; text-align: center; padding: 40px; background-color: #f8f9fa; }}
                .box {{ background: white; padding: 30px; border-radius: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); display: inline-block; max-width: 90%; }}
                h2 {{ color: #333; }}
                p {{ font-size: 1.3em; color: #444; margin: 20px 0; }}
                .btn {{ text-decoration: none; background: #28a745; color: white; padding: 12px 24px; border-radius: 10px; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="box">
                <h2>Halil'in Cevabı:</h2>
                <p>{cevap}</p>
                <a href="/" class="btn">Tekrar Sor</a>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)