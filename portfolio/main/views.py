# main/views.py

from django.shortcuts import render
from .models import Project
import datetime # Tambahkan ini untuk mendapatkan tahun saat ini

def index(request):
    dummy_projects = [
        {
            'title': 'Pemanfaatan Computer Vision dan Explainable Artificial Intelligence untuk Mendeteksi Cacat Mikro Hasil Produksi Manufaktur',
            'description': 'Proyek untuk keperluan lomba Datathon RISTEK UI dan berhasil meraih peringkat 21 dari 145 tim, dibuat dengan Python & Google Colab.',
            'tech_stack': 'Python, Tensorflow, Keras',
            'github_url': 'https://github.com/henrysalim/seleksi-datathon-2025',
            'live_url': None
        },
        {
            'title': 'Website Budaya Jawa Barat',
            'description': 'Sebuah website untuk memperkenalkan budaya jawa barat, mulai dari musik, tarian, rumah adat, cuaca terkini, terjemahan otomatis ke bahasa Sunda. Website ini dibuat untuk memenuhi projek akhir mata kuliah Perkenalan Teknologi Internet dan berhasil mendapat nilai A.',
            'tech_stack': 'HTML, CSS, ReactJs',
            'github_url': 'https://github.com/AgnesDevita/Final-Exam-Introduction-to-Internet-Technology',
            'live_url': "https://welcome-to-jawa-barat.vercel.app"
        },
        {
            'title': 'Titanic Data Analysis',
            'description': 'Proyek ini merupakan analisis sederhana terhadap dataset Titanic yang bertujuan untuk memahami karakteristik penumpang berdasarkan atribut seperti umur, jenis kelamin, dan status keselamatan. Project ini dibuat sebagai bagian dari pemenuhan tugas akhir Mini Bootcamp Digital Skill Fair 38.0 yang diselenggarakan oleh Dibimbing.id.',
            'tech_stack': 'Python, Pandas, Matplotlib, Powerpoint',
            'github_url': 'https://github.com/junikxz/Titanic-Data-Analysis',
            'live_url': None
        },
        {
            'title': 'Prediksi Biaya Konsumsi Listrik',
            'description': 'Proyek ini merupakan hasil analisis dan prediksi konsumsi listrik (regresi) yang diselenggarakan melalui kompetisi kaggle sebagai pemenuhan penyisihan Data Science Academy Compfest.',
            'tech_stack': 'Python, Pandas, Numpy, Scikit-Learn, CatboostRegressor',
            'github_url': 'https://github.com/junikxz/Electricity_consumption_prediction',
            'live_url': None
        },
        {
            'title': 'Website Event Management',
            'description': 'Sebuah website yang mengelola event, mulai dari registrasi user hingga pendaftaran event. Kemudian, ada juga role admin yang mengelola (CRUD) event secara berkala. Website ini dibuat untuk memenuhi projek akhir mata kuliah Web Programming dan berhasil mendapat nilai A.',
            'tech_stack': 'HTML, CSS, Laravel',
            'github_url': 'https://github.com/junikxz/uts_lec',
            'live_url': None
        }
    ]

    
    # Menyiapkan context dictionary dengan struktur data yang lebih lengkap
    context = {
        # --- Bagian Hero & Info Pribadi ---
        "name": "Livia Junike",
        "title": "Data, Machine Learning & AI Enthusiast", # BARU: Judul singkat di bawah nama
        "summary": "Seorang mahasiswi Universitas Multimedia Nusantara yang antusias dalam bidang data, kecerdasan buatan, dan desain antarmuka pengguna", # DISESUAIKAN: Deskripsi singkat untuk hero section
        "about_me": "Saya adalah seorang pembelajar yang bersemangat dengan fondasi yang kuat dalam ilmu komputer. Saya suka mengubah ide-ide kompleks menjadi solusi perangkat lunak yang elegan dan fungsional. Di luar coding, saya menikmati membaca tentang tren teknologi terbaru dan berkontribusi pada proyek-proyek kecil.", # BARU: Deskripsi lebih panjang untuk section "About Me"
        "quote": "\"Build with intent, grow with impact.\"",
        
        # --- Link Sosial Media ---
        "social": { # BARU: Dictionary untuk link sosial media
            "github": "https://github.com/junikxz", # Ganti dengan username Anda
            "linkedin": "https://linkedin.com/in/liviajunike", # Ganti dengan username Anda
            "email": "liviajunike1606@gmail.com" # Ganti dengan email Anda
        },
        
        # --- Daftar Skills ---
        "skills": [ # BARU: Daftar skill untuk ditampilkan sebagai tag
            "Python", "SQL (MySQL)", "R", "Java", "C", "UI/UX Design (Figma)", "HTML", "CSS"
        ],

        # --- Daftar Proyek (dari database) ---
        "projects": dummy_projects,
        
        # --- Info Tambahan ---
        "current_year": datetime.date.today().year # BARU: Untuk menampilkan tahun di footer secara dinamis
    }
    
    return render(request, 'main/index.html', context)