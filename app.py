from flask import Flask, render_template, redirect, url_for, abort, request

app = Flask(__name__)

# Data produk
PRODUK = {
    1: {
        "nama": "Kaos Basic",
        "harga": 75000,
        "kategori": "Fashion",
        "deskripsi": "Kaos basic nyaman untuk penggunaan sehari-hari."
    },
    2: {
        "nama": "Hoodie Casual",
        "harga": 150000,
        "kategori": "Fashion",
        "deskripsi": "Hoodie casual dengan desain modern."
    },
    3: {
        "nama": "Tas Selempang",
        "harga": 95000,
        "kategori": "Aksesoris",
        "deskripsi": "Tas selempang praktis untuk aktivitas sehari-hari."
    },
    4: {
        "nama": "Topi Casual",
        "harga": 50000,
        "kategori": "Aksesoris",
        "deskripsi": "Topi casual dengan desain sederhana."
    }
}

# Data username pelanggan
USERNAME_TERDAFTAR = ["shavira", "galih", "nopal", "amsal"]


# ROUTING STATIS

@app.route("/")
@app.route("/beranda")
def beranda():
    return render_template("beranda.html")


@app.route("/tentang")
def tentang():
    return render_template("tentang.html")


@app.route("/produk")
def produk():
    return render_template("produk.html", produk=PRODUK)


@app.route("/kontak")
def kontak():
    return render_template("kontak.html")


@app.route("/pelanggan")
def pelanggan():
    return render_template(
        "pelanggan.html",
        pelanggan=USERNAME_TERDAFTAR
    )


@app.route("/registrasi")
def registrasi():
    return render_template("registrasi.html")


# DETAIL PRODUK DENGAN INTEGER CONVERTER

@app.route("/produk/<int:id>")
def detail_produk(id):
    if id not in PRODUK:
        abort(404)

    return render_template(
        "detailprodu.html",
        item=PRODUK[id],
        id=id
    )


# PROSES PENGECEKAN USERNAME

def proses_cek_username(username):
    username = username.strip().lower()

    valid = len(username) >= 4
    tersedia = valid and username not in USERNAME_TERDAFTAR

    status_code = 200 if valid else 400

    return (
        render_template(
            "cek.html",
            username=username,
            valid=valid,
            tersedia=tersedia
        ),
        status_code
    )


# DYNAMIC ROUTING USERNAME

@app.route("/cek/<username>")
def cek_username(username):
    return proses_cek_username(username)


# QUERY STRING

@app.route("/cek")
def cek_query():
    username = request.args.get("u", "")
    return proses_cek_username(username)


# PROFIL PELANGGAN

@app.route("/user/<username>")
def profil_user(username):
    username = username.strip().lower()

    if len(username) < 4:
        return "Username tidak valid. Minimal 4 karakter.", 400

    ditemukan = username in USERNAME_TERDAFTAR

    return render_template(
        "user.html",
        username=username,
        ditemukan=ditemukan
    ), 200 if ditemukan else 404


# REDIRECT

@app.route("/home")
def home():
    return redirect(url_for("beranda"))


# CUSTOM ERROR 404

@app.errorhandler(404)
def halaman_tidak_ditemukan(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)