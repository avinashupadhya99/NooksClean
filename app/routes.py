from flask import Flask, flash, request, redirect, url_for, render_template
from app import app

@app.route('/')
def index():
    return render_template('lander.html')

@app.route('/photo')
def photomenu():
    return render_template('photo.html')

@app.route('/output', methods = ['POST'])
def output():
    print(request)
    if 'file' not in request.files:
        print('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        print('No selected file')
        return redirect(request.url)
    if file:
        # Call the model and return the output to output.html here
        result = predict(file)

    return render_template('output.html', label = result)

def predict(image):
    loaded_model = model_from_json(loaded_model_json)
# load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    img=cv.imread(filepath)
    img=cv.resize(img,(250,250))
    img.shape
    img=np.array([img])
    resultant_prediction=loaded_model.predict(img)
    return(resultant_prediction)