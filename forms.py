from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class NETBOX_NEW_OBJECT(FlaskForm):
    api_attr = SelectField('Object Path ',choices=[('ipam.vlans', 'newVlan'),('newIP', '#'), ('newPrefix', '#')])
    filter_key = SelectField('Filter Key',choices=[('vid', 'Vlan Number')])
    filter_data = StringField('Filter Data', validators=[DataRequired()])
    input_data = StringField('Input Data',validators=[DataRequired()])

    submit = SubmitField('Submit')
