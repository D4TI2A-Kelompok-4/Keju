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
	pekerjaan = [
		{
			'bidang':'pendidikan',
			'profesi':'dosen'
		},
		{
			'bidang':'kesehatan',
			'profesi':'dokter'
		},
		{
			'bidang':'pendidikan',
			'profesi':'guru'
		},
		{
			'bidang':'olahraga',
			'profesi':'pemain bulutangkis'
		},
		{
<<<<<<< HEAD
			'bidang':'olahraga',
			'profesi':'pemain sepak bola'
=======
			'bidang':'kesehatan',
			'profesi':'bidan'
>>>>>>> 9508c75c55811fa8cb56c178dad8c35e211e769a
		}
	]
	return jsonify({'daftar pekerjaan':pekerjaan})
	