from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/test')
def TestREST():
    mhs = [
        {
            'nim': '12312',
            'nama': 'andi',
            'alamat': 'selong'
        },
        {
            'nim': '12333',
            'nama': 'Indah',
            'alamat': 'Praya'
        }
    ]
    return jsonify({
        'data': mhs
    })

@app.route('/')
def index():
    return '<h1 style="text-transform:uppercase">Halo selamat Datang</h1>'

@app.route('/mhs', methods=['GET', 'POST'])
def mahasiswa():
    if request.method == 'POST':
        data = request.method.POST
        print(data)

        return render_template('data_mahasiswa.html')
    return render_template('form_mahasiswa.html')

if __name__ == '__main__':
    app.run('0.0.0.0')
