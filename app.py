from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/<gurih>')
def hello_world(gurih):
    return gurih

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/crot', methods=['POST'])
def login():
	return request.form['anu']

@app.route("/input/pekerjaan")
def pekerjaan():
	return jsonify(
	pekerjaan="Dokter",
	tempat_kerja="Rumah Sakit"
	)

@app.route("/input/pekerjaan2")
def pekerjaan2():
	return jsonify(
	pekerjaan="Dosen",
	tempat_kerja="Kampus"
	)