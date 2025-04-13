from flask import Flask, render_template, request
from wtforms import Form, FloatField, SubmitField, SelectField, StringField, DateField
from wtforms.validators import InputRequired
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ganti dengan secret key yang kuat

class ShippingForm(Form):
    # Pilihan Jenis Barang (single select)
    item_type = SelectField('Jenis Barang', choices=[
        ('', 'Pilih Jenis Barang'),
        ('Makanan', 'A. Makanan'),
        ('Minuman', 'B. Minuman'),
        ('Dokumen', 'C. Dokumen'),
        ('Pakaian', 'D. Pakaian'),
        ('Peralatan Rumah Tangga', 'E. Peralatan Rumah Tangga'),
        ('Peralatan Permesinan', 'F. Peralatan Permesinan'),
        ('Perhiasan', 'G. Perhiasan'),
        ('Lainnya', 'H. Lainnya')
    ], validators=[InputRequired()])
    
    # Input untuk Nama
    name = StringField('Nama', validators=[InputRequired()])
    
    # Input untuk Nomor Whatsapp
    whatsapp = StringField('Nomor Whatsapp', validators=[InputRequired()])
    
    # Tanggal Keberangkatan (membatasi pilihan tanggal)
    departure_date = DateField('Tanggal Keberangkatan', format='%Y-%m-%d', validators=[InputRequired()])
    
    # Berat Barang
    weight = FloatField('Berat Barang (kg)', validators=[InputRequired()])
    
    submit = SubmitField('Hitung Biaya Pengiriman')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ShippingForm(request.form)
    shipping_cost = None
    item_summary = []

    today = datetime.today().strftime('%Y-%m-%d')
    
    address = "Kettwiger Strasse 15, 45468 Mulheim an der Ruhr"
    google_maps_link = f"https://www.google.com/maps/search/?q={address.replace(' ', '+')}"
    
    valid_dates = ['2025-04-15', '2025-04-22']  # Tanggal yang valid

    # Memeriksa arah pengiriman
    shipping_direction = request.form.get("shipping_direction", "")  # Arah pengiriman yang dipilih

    if request.method == 'POST' and form.validate():  
        weight = form.weight.data
        shipping_cost = calculate_shipping_cost(weight)
        item_summary = form.item_type.data
    
    return render_template('index.html', form=form, shipping_cost=shipping_cost,
                           item_summary=item_summary, address=address, 
                           google_maps_link=google_maps_link, today=today, 
                           valid_dates=valid_dates, name=form.name.data, 
                           whatsapp=form.whatsapp.data, departure_date=form.departure_date.data,
                           shipping_direction=shipping_direction)

def calculate_shipping_cost(weight):
    price_per_kg = 14  # Biaya pengiriman per kg dalam Euro
    total_cost = weight * price_per_kg
    return total_cost

if __name__ == '__main__':
    app.run(debug=True)
