import os
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import TextAreaField, RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '342DED'

def snake(text):
    text = text.replace(' ', '_')
    return text

def transform(text, operation):
    if operation == 'proper':
        return text.title()
    elif operation == 'lower':
        return text.lower()
    elif operation == 'upper':
        return text.upper()   
    elif operation == 'snake_upper':
        return snake(text).upper()   
    elif operation == 'snake_lower':
        return snake(text).lower()   

class formOperation(FlaskForm):
    input_string = TextAreaField('Input', validators=[DataRequired()])
    output_string = TextAreaField('Output')
    operation = RadioField('Operation', choices=[('upper', 'Upper'), 
                                                 ('lower', 'Lower'),
                                                 ('proper', 'Proper'),
                                                 ('snake_upper', 'Snake Upper'),
                                                 ('snake_lower', 'Snake Lower')
                                                ])

@app.route('/', methods=['GET','POST'])
def index():
    form = formOperation()
    if form.input_string.data:
        app.logger.info(form.operation.data)
        form.output_string.data = transform(form.input_string.data, form.operation.data)
        redirect('index')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
