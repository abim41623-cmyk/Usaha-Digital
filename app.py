from flask import Flask, render_template, request

app = Flask(__name__)

# Data Produk (Halaman Produk)
products = [
    {"nama": "E-Book Strategi Marketing", "deskripsi": "Panduan lengkap memulai bisnis digital.", "harga": "Rp 150.000"},
    {"nama": "Kursus Web Development", "deskripsi": "Belajar membuat website dari nol hingga mahir.", "harga": "Rp 500.000"},
    {"nama": "Template Desain Canva", "deskripsi": "100+ template siap pakai untuk sosial media.", "harga": "Rp 75.000"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/produk')
def produk():
    return render_template('produk.html', products=products)

@app.route('/kontak', methods=['GET', 'POST'])
def kontak():
    if request.method == 'POST':
        nama = request.form.get('nama')
        email = request.form.get('email')
        return render_template('respon.html', nama=nama, email=email)
    return render_template('kontak.html')

if __name__ == '__main__':
    app.run(debug=True)
