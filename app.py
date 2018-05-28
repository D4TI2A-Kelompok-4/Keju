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
			'bidang':'olahraga',
			'profesi':'pemain voli'
		},
		{
			'bidang':'olahraga',
			'profesi':'pemain sepak bola'
		},
		{
			'bidang':'kesehatan',
			'profesi':'bidan'
		},
		{
			'bidang':'kesehatan',
			'profesi':'Suster'
		},
		{
			'bidang':'hukum',
			'profesi':'pengacara'
		},
		{
			'bidang':'pemerintahan',
			'profesi':'polisi'
		},
		{
			'bidang':'hukum',
			'profesi':'hakim'
		},
		{
			'bidang':'hukum',
			'profesi':'jaksa'
		},
		{
			'bidang':'wiraswasta',
			'profesi':'petani'
		},
		{
			'bidang':'kesehatan',
			'profesi':'apoteker'
		},
		{
			'bidang':'kesehatan',
			'profesi':'ahli gizi'
		},
		{
			'bidang':'wiraswasta',
			'profesi':'pedagang'
		},
	]
	return jsonify({'daftar pekerjaan':pekerjaan})
	