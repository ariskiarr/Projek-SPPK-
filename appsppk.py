from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

app_bobot = {
    "App": {
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


@app.route('/', methods=['GET', 'POST'])
def index():
    results_topsis = {}
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
                    for app, weights in app_bobot.items():
                        available_cols = [c for c in df.columns if c in weights.keys()]
                        if len(available_cols) == len(weights):
                            sub_df = df[['Tempat Makan'] + available_cols]
                            # 1. Normalisasi SAW
                            X = sub_df.iloc[:, 1:].values.astype(float)
                            norm_saw = X / X.max(axis=0)
                            # 2. Perhitungan TOPSIS dari hasil normalisasi SAW
                            norm = norm_saw / np.sqrt((norm_saw**2).sum(axis=0))
                            weighted = norm * np.array(list(weights.values()))
                            ideal_pos = weighted.max(axis=0)
                            ideal_neg = weighted.min(axis=0)
                            d_pos = np.sqrt(((weighted - ideal_pos)**2).sum(axis=1))
                            d_neg = np.sqrt(((weighted - ideal_neg)**2).sum(axis=1))
                            score_topsis = d_neg / (d_pos + d_neg)
                            hasil_df = sub_df[['Tempat Makan']].copy()
                            hasil_df['Skor Akhir'] = score_topsis
                            hasil_df['Ranking Akhir'] = hasil_df['Skor Akhir'].rank(ascending=False)
                            hasil_df = hasil_df.sort_values('Ranking Akhir')
                            results_topsis[app] = hasil_df[['Tempat Makan', 'Skor Akhir', 'Ranking Akhir']].to_html(index=False, classes='table table-striped')
                        else:
                            error_message = f'Kolom untuk tempat makan tidak lengkap di file CSV.'
            except Exception as e:
                import traceback
                print('Error saat upload file:')
                traceback.print_exc()
                error_message = f'Gagal memproses file: {str(e)}'
    return render_template('index.html', results_topsis=results_topsis, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
