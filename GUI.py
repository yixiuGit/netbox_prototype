from flask import Flask, render_template, url_for, flash, redirect
from forms import NETBOX_NEW_OBJECT
import netboxInit
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/new_object", methods=['GET', 'POST'])
def create_new_object():
    form = NETBOX_NEW_OBJECT()
    if form.validate_on_submit():
        api_attr = form.api_attr.data
        filter_key = form.filter_key.data
        filter_data = form.filter_data.data.split()
        input_data = json.loads(form.input_data.data)
        netboxInit.new_netbox_instance("http://127.0.0.1:8000","ac0045b34d40b36b57c8987512b05f5ba0a27817").create_new_request(api_attr,filter_key, filter_data,input_data)

    return render_template('new_vlan.html', title='Login', form=form)




if __name__ == '__main__':
    app.run(debug=True)
