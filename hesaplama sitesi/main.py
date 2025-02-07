from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        try:
            # Formdan doğru ve yanlış sayıları al
            dogru_counts = {
                'matematik': int(request.json['matematik_dogru']),
                'fen': int(request.json['fen_dogru']),
                'turkce': int(request.json['turkce_dogru']),
                'sosyal': int(request.json['sosyal_dogru']),
                'din': int(request.json['din_dogru']),
                'ingilizce': int(request.json['ingilizce_dogru']),
            }
            
        
            yanlis_counts = {
                'matematik': int(request.json['matematik_yanlis']),
                'fen': int(request.json['fen_yanlis']),
                'turkce': int(request.json['turkce_yanlis']),
                'sosyal': int(request.json['sosyal_yanlis']),
                'din': int(request.json['din_yanlis']),
                'ingilizce': int(request.json['ingilizce_yanlis']),
            }
            
            # Katsayılar
            katsayilar = {
                'matematik': 4.632500,
                'fen': 3.8900,
                'turkce': 4.107600,
                'sosyal': 1.729500,
                'din': 1.817400,
                'ingilizce': 1.53100,
            }

            # Net hesaplama
            net_counts = {}
            for ders in dogru_counts:
                net_counts[ders] = dogru_counts[ders] - (yanlis_counts[ders] / 3)

            # Puan hesaplama
            toplam_puan = 0  # Başlangıç puanı
            for ders in net_counts:
                toplam_puan += net_counts[ders] * katsayilar[ders]

            return jsonify({'puan': round(toplam_puan, 2), 'nets': net_counts})  # JSON yanıt
        except ValueError:
            return jsonify({'puan': "Lütfen tüm alanları düzgün doldurun."})
        
    return render_template('index.html', data=data)

@app.route('/', methods=['GET', 'POST'])
def puans():
    data = None





if __name__ == '__main__':
    app.run(debug=True)

render_template('puan.html')