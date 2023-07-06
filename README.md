# datadownloader backend

git clone https://github.com/finepik/datadownloader.git backend
cd backend
python -m venv venv
sudo -s
source venv/bin/activate
pip install -r requirements.txt
cd downloader
python manage.py migrate
python manage.py runserver