from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

bobot_tempat_makan = {
    "Tempat Makan": {
        "Harga": 0.20,
        "Kualitas Rasa": 0.25,
        "Jarak": 0.15,
        "Kebersihan dan Kenyamanan": 0.10,
        "Kecepatan Pelayanan": 0.10,
        "Variasi Menu": 0.08,
        "Ketersediaan Tempat Duduk": 0.06,
        "Fasilitas": 0.06
    }
}

def topsis(data, weights):
    data = data.copy()
    X = data.iloc[:, 1:].values.astype(float)
    norm = X / np.sqrt((X**2).sum(axis=0))
    weighted = norm * np.array(list(weights.values()))
    ideal_pos = weighted.max(axis=0)
    ideal_neg = weighted.min(axis=0)
    d_pos = np.sqrt(((weighted - ideal_pos)**2).sum(axis=1))
    d_neg = np.sqrt(((weighted - ideal_neg)**2).sum(axis=1))
    score = d_neg / (d_pos + d_neg)
    data['Skor Akhir TOPSIS'] = score
    data['Ranking TOPSIS'] = data['Skor Akhir TOPSIS'].rank(ascending=False)
    return data.sort_values('Skor Akhir TOPSIS', ascending=False)

def saw(data, weights):
    data = data.copy()
    X = data.iloc[:, 1:].values.astype(float)
    norm = X / X.max(axis=0)
    weighted = norm * np.array(list(weights.values()))
    score = weighted.sum(axis=1)
    data['Skor Akhir SAW'] = score
    data['Ranking SAW'] = data['Skor Akhir SAW'].rank(ascending=False)
    return data.sort_values('Skor Akhir SAW', ascending=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    results_topsis = {}
    results_saw = {}
    error_message = None
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            error_message = 'File tidak ditemukan atau belum dipilih.'
        else:
            try:
                df = pd.read_csv(file)
                if df.empty:
                    error_message = 'File CSV kosong.'
                elif 'Tempat Makan' not in df.columns:
                    error_message = 'Kolom "Tempat Makan" tidak ditemukan pada file CSV.'
                else:
                    for tempat, weights in bobot_tempat_makan.items():
                        available_cols = [c for c in df.columns if c in weights.keys()]
                        if len(available_cols) == len(weights):
                            sub_df = df[['Tempat Makan'] + available_cols]
                            hasil_topsis = topsis(sub_df, weights)
                            hasil_saw = saw(sub_df, weights)
                            results_topsis[tempat] = hasil_topsis[['Tempat Makan', 'Skor Akhir TOPSIS', 'Ranking TOPSIS']].to_html(index=False, classes='table table-striped')
                            results_saw[tempat] = hasil_saw[['Tempat Makan', 'Skor Akhir SAW', 'Ranking SAW']].to_html(index=False, classes='table table-bordered')
                        else:
                            error_message = f'Kolom untuk tempat makan tidak lengkap di file CSV.'
            except Exception as e:
                import traceback
                print('Error saat upload file:')
                traceback.print_exc()
                error_message = f'Gagal memproses file: {str(e)}'
    return render_template('index.html', results_topsis=results_topsis, results_saw=results_saw, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
