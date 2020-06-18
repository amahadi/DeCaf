pwd=$(pwd)

if [ ! -d "$pwd/venv" ] 
then
    python3 -m venv venv
fi

source venv/bin/activate

pip install -r requirements.txt

python src/api.py