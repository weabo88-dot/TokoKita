
from flask import Flask, render_template, redirect, url_for, abort, request

app = Flask(__name__)

# =====================================
# DATA PRODUK
# =====================================

PRODUK = {
    1: {
        "nama": "Kaos Basic",
        "harga": 75000,
        "kategori": "Fashion",
        "deskripsi": "Kaos basic nyaman untuk aktivitas sehari-hari."
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
        "deskripsi": "Tas selempang praktis untuk kebutuhan sehari-hari."
    },
    4: {
        "nama": "Topi Casual",
        "harga": 50000,
        "kategori": "Aksesoris",
        "deskripsi": "Topi casual dengan desain sederhana."
    }
}

# Username yang sudah terdaftar
USERNAME_TERDAFTAR = ["shavira", "galih", "nopal", "amsal"]


# =====================================
# 1. ROUTING STATIS
# =====================================

@app.route("/")
@app.route("/beranda")
def beranda():
    return render_template("beranda.html")


@app.route("/tentang")
def tentang():
    return render_template("tentang.html")


@app.route("/produk")
def produk():
    return render_template("produk.html")


@app.route("/kontak")
def kontak():
    return render_template("kontak.html")


# =====================================
# 2. DYNAMIC ROUTING CEK USERNAME
# =====================================

@app.route("/cek/<username>")
def cek_username(username):
    username = username.strip().lower()

    if len(username) < 4:
        return render_template(
            "cek.html",
            username=username,
            pesan="Username tidak valid. Minimal 4 karakter."
        ), 400

    elif username in USERNAME_TERDAFTAR:
        pesan = f"Username {username} sudah digunakan."

    else:
        pesan = f"Username {username} tersedia."

    return render_template(
        "cek.html",
        username=username,
        pesan=pesan
    )


# =====================================
# 3. DYNAMIC ROUTING PROFIL PELANGGAN
# =====================================

@app.route("/user/<username>")
def profil_user(username):
    username = username.strip().lower()

    if len(username) < 4:
        return "Username tidak valid. Minimal 4 karakter.", 400

    if username not in USERNAME_TERDAFTAR:
        return "Pelanggan tidak ditemukan.", 404

    return f"""
        <h1>Profil Pelanggan TokoKita</h1>
        <p>Username: {username}</p>
        <p>Status: Terdaftar</p>
        <a href="{url_for('beranda')}">Kembali ke Beranda</a>
    """


# =====================================
# 4. INTEGER CONVERTER DETAIL PRODUK
# =====================================

@app.route("/produk/<int:id>")
def detail_produk(id):
    if id not in PRODUK:
        abort(404)

    item = PRODUK[id]

    return f"""
        <h1>Detail Produk TokoKita</h1>
        <h2>{item['nama']}</h2>
        <p>Kategori: {item['kategori']}</p>
        <p>Harga: Rp{item['harga']:,}</p>
        <p>Deskripsi: {item['deskripsi']}</p>
        <a href="{url_for('produk')}">Kembali ke Produk</a>
    """


# =====================================
# 5. PENGECEKAN USERNAME QUERY STRING
# =====================================

@app.route("/cek")
def cek_query():
    username = request.args.get("u", "").strip().lower()

    if len(username) < 4:
        return render_template(
            "cek.html",
            username=username,
            pesan="Username tidak valid. Minimal 4 karakter."
        ), 400

    elif username in USERNAME_TERDAFTAR:
        pesan = f"Username {username} sudah digunakan."

    else:
        pesan = f"Username {username} tersedia."

    return render_template(
        "cek.html",
        username=username,
        pesan=pesan
    )


# =====================================
# 6. REDIRECT
# =====================================

@app.route("/home")
def home():
    return redirect(url_for("beranda"))


# =====================================
# 7. CUSTOM ERROR 404
# =====================================

@app.errorhandler(404)
def halaman_tidak_ditemukan(error):
    return render_template("404.html"), 404


# =====================================
# MENJALANKAN APLIKASI
# =====================================

if __name__ == "__main__":
    app.run(debug=True)
