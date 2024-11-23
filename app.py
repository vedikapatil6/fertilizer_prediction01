# # app.py (Flask Backend)
# import pickle
# import gunicorn
# from flask import Flask, render_template, request
# import numpy as np
# from sklearn.preprocessing import MinMaxScaler

# app = Flask(__name__)

# # Load the trained model
# with open('random_forest_model.pkl', 'rb') as model_file:
#     rf_model = pickle.load(model_file)

# with open('scaler.pkl', 'rb') as scaler_file:
#     scaler = pickle.load(scaler_file)

# # Initialize the MinMaxScaler with the expected feature range
# # scaler = MinMaxScaler(feature_range=(0, 1)j)














# articles = {
#     1: {
#         'title': "How to Improve Soil Fertility Naturally",
#         'content': "Soil fertility can be improved by using organic compost, practicing crop rotation, and minimizing soil disturbance. Organic matter not only enhances soil nutrients but also boosts microbial activity, ensuring sustainable growth. Mulching, cover crops, and adding manure can also protect the soil and promote a healthy ecosystem."
#     },
#     2: {
#         'title': "Understanding NPK: A Guide to Soil Nutrients",
#         'content': "NPK stands for Nitrogen, Phosphorus, and Potassium, the primary nutrients essential for plant health. Nitrogen supports leafy growth and photosynthesis, phosphorus aids in root and flower development, and potassium improves overall plant resistance. Balancing these nutrients is crucial for optimal crop yield."
#     },
#     3: {
#         'title': "Tips for Sustainable Fertilizer Use",
#         'content': "Sustainable fertilizer use starts with soil testing to understand its nutrient profile. Use organic fertilizers or slow-release formulations to minimize runoff and leaching. Avoid over-fertilizing, as it can harm the environment and reduce soil health. Apply fertilizers during dry conditions and consider precision agriculture techniques."
#     },
#     4: {
#         'title': "Benefits of Cover Crops for Soil Health",
#         'content': "Cover crops, such as clover and rye, prevent soil erosion, improve water retention, and enhance nutrient cycling. They act as a natural weed suppressant and contribute to organic matter when decomposed. Additionally, leguminous cover crops fix nitrogen in the soil, reducing the need for synthetic fertilizers."
#     },
#     5: {
#         'title': "The Role of Microbes in Soil Fertility",
#         'content': "Soil microbes decompose organic matter, fix nitrogen, and release nutrients for plant uptake. Beneficial fungi, like mycorrhizae, form symbiotic relationships with plants, enhancing root absorption of water and nutrients. Promoting microbial activity through composting and avoiding harmful chemicals boosts soil fertility."
#     },
#     6: {
#         'title': "Composting: A Natural Way to Enrich Soil",
#         'content': "Composting involves recycling organic waste, such as kitchen scraps and yard debris, into nutrient-rich humus. It improves soil structure, enhances moisture retention, and provides a balanced nutrient supply for plants. Proper aeration, moisture levels, and a mix of greens and browns are key to successful composting."
#     },
#     7: {
#         'title': "How Crop Rotation Benefits Soil",
#         'content': "Crop rotation involves planting different crops in a sequence to prevent soil nutrient depletion and reduce pests. For example, alternating legumes with cereals replenishes nitrogen levels. This practice enhances soil structure, boosts fertility, and promotes biodiversity within the farming ecosystem."
#     },
#     8: {
#         'title': "The Impact of Over-Fertilization on Soil",
#         'content': "Excessive fertilizer use leads to nutrient runoff, soil acidification, and water contamination. Over-fertilization harms soil microorganisms and causes imbalances in nutrient availability. Adopting sustainable practices, such as precision application and using organic amendments, can mitigate these effects."
#     },
#     9: {
#         'title': "The Importance of Soil pH in Agriculture",
#         'content': "Soil pH affects nutrient availability and microbial activity. Most crops thrive in slightly acidic to neutral soils (pH 6-7). Amending soil with lime or sulfur can adjust pH levels, ensuring optimal conditions for plant growth. Regular testing helps farmers maintain a balanced pH for their crops."
#     },
#     10: {
#         'title': "Organic vs. Synthetic Fertilizers: Pros and Cons",
#         'content': "Organic fertilizers, such as manure and compost, improve soil health and are eco-friendly but act slower. Synthetic fertilizers provide immediate nutrient availability but may degrade soil quality over time. A balanced approach, combining both types, ensures long-term soil fertility and sustainable farming."
#     },
#     # Add more articles here...
# }

# @app.route('/article/<int:article_id>')
# def article_detail(article_id):
#     # Fetch the article by ID, if it exists
#     article = articles.get(article_id)

#     if article:
#         # Pass the article data to the template
#         return render_template('article.html', article=article)
#     else:
#         # If the article doesn't exist, render a 'not found' page
#         return render_template('article.html', article=None)






































# @app.route('/detail')
# def detail():
#     return render_template('detailp.html')

# @app.route('/home')
# def homee():
#     return render_template('indexpl.html')

# @app.route('/article')
# def article():
#     return render_template('indexart.html')

# @app.route('/', methods=['GET', 'POST'])
# def model():
#     if request.method == 'POST':
#         # Get input values from the form
#         temp = float(request.form['temp'])
#         humid = float(request.form['humid'])
#         mois = float(request.form['mois'])
#         soil_type = int(request.form['soil'])  # Categorical input
#         crop_type = int(request.form['crop'])  # Categorical input
#         nitro = float(request.form['nitro'])
#         pota = float(request.form['pota'])
#         phos = float(request.form['phos'])

#         # Prepare the input features for prediction
#         # input_data = np.array([[temp, humid, mois, soil_type, crop_type, nitro, pota, phos]])
#         input_data = np.array([[temp, humid, mois, soil_type, crop_type, nitro, pota, phos]])

#         # Normalize the input data using MinMaxScaler
#         input_data_norm = scaler.transform(input_data)  # Use the pre-fitted scaler
#  # Fit and transform for the incoming data

#         # Make the prediction
#         prediction = rf_model.predict(input_data_norm)

#         # Map the prediction to a fertilizer recommendation (14 types)
#         fertilizer_dict = {
#             0: "10-10-2010",
#             1: "10-26-26",
#             2: "14-14-14",
#             3: "14-35-14",
#             4: "15-15-15",
#             5: "17-17-17",
#             6: "20-20",
#             7: "28-28",
#             8: "DAP",
#             9: "Potassium Chloride",
#             10: "Potassium sulfate",
#             11: "Superphosphate",
#             12: "TSP",
#             13: "Urea"
#         }
        
#         # Get the fertilizer recommendation
#         recommended_fertilizer = fertilizer_dict.get(prediction[0], "Unknown Fertilizer")

#         return render_template('form.html', x=recommended_fertilizer)
    
#     return render_template('form.html', x="")

# if __name__ == "__main__":
#     app.run(debug=True)

# app.py (Flask Backend)
import pickle
import gunicorn
from flask import Flask, render_template, request
import numpy as np
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Load the trained model
with open('random_forest_model.pkl', 'rb') as model_file:
    rf_model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Initialize the MinMaxScaler with the expected feature range
# scaler = MinMaxScaler(feature_range=(0, 1)j)

articles = {
    1: {
        'title': "How to Improve Soil Fertility Naturally",
        'content': "Soil fertility can be improved by using organic compost, practicing crop rotation, and minimizing soil disturbance. Organic matter not only enhances soil nutrients but also boosts microbial activity, ensuring sustainable growth. Mulching, cover crops, and adding manure can also protect the soil and promote a healthy ecosystem."
    },
    2: {
        'title': "Understanding NPK: A Guide to Soil Nutrients",
        'content': "NPK stands for Nitrogen, Phosphorus, and Potassium, the primary nutrients essential for plant health. Nitrogen supports leafy growth and photosynthesis, phosphorus aids in root and flower development, and potassium improves overall plant resistance. Balancing these nutrients is crucial for optimal crop yield."
    },
    3: {
        'title': "Tips for Sustainable Fertilizer Use",
        'content': "Sustainable fertilizer use starts with soil testing to understand its nutrient profile. Use organic fertilizers or slow-release formulations to minimize runoff and leaching. Avoid over-fertilizing, as it can harm the environment and reduce soil health. Apply fertilizers during dry conditions and consider precision agriculture techniques."
    },
    4: {
        'title': "Benefits of Cover Crops for Soil Health",
        'content': "Cover crops, such as clover and rye, prevent soil erosion, improve water retention, and enhance nutrient cycling. They act as a natural weed suppressant and contribute to organic matter when decomposed. Additionally, leguminous cover crops fix nitrogen in the soil, reducing the need for synthetic fertilizers."
    },
    5: {
        'title': "The Role of Microbes in Soil Fertility",
        'content': "Soil microbes decompose organic matter, fix nitrogen, and release nutrients for plant uptake. Beneficial fungi, like mycorrhizae, form symbiotic relationships with plants, enhancing root absorption of water and nutrients. Promoting microbial activity through composting and avoiding harmful chemicals boosts soil fertility."
    },
    6: {
        'title': "Composting: A Natural Way to Enrich Soil",
        'content': "Composting involves recycling organic waste, such as kitchen scraps and yard debris, into nutrient-rich humus. It improves soil structure, enhances moisture retention, and provides a balanced nutrient supply for plants. Proper aeration, moisture levels, and a mix of greens and browns are key to successful composting."
    },
    7: {
        'title': "How Crop Rotation Benefits Soil",
        'content': "Crop rotation involves planting different crops in a sequence to prevent soil nutrient depletion and reduce pests. For example, alternating legumes with cereals replenishes nitrogen levels. This practice enhances soil structure, boosts fertility, and promotes biodiversity within the farming ecosystem."
    },
    8: {
        'title': "The Impact of Over-Fertilization on Soil",
        'content': "Excessive fertilizer use leads to nutrient runoff, soil acidification, and water contamination. Over-fertilization harms soil microorganisms and causes imbalances in nutrient availability. Adopting sustainable practices, such as precision application and using organic amendments, can mitigate these effects."
    },
    9: {
        'title': "The Importance of Soil pH in Agriculture",
        'content': "Soil pH affects nutrient availability and microbial activity. Most crops thrive in slightly acidic to neutral soils (pH 6-7). Amending soil with lime or sulfur can adjust pH levels, ensuring optimal conditions for plant growth. Regular testing helps farmers maintain a balanced pH for their crops."
    },
    10: {
        'title': "Organic vs. Synthetic Fertilizers: Pros and Cons",
        'content': "Organic fertilizers, such as manure and compost, improve soil health and are eco-friendly but act slower. Synthetic fertilizers provide immediate nutrient availability but may degrade soil quality over time. A balanced approach, combining both types, ensures long-term soil fertility and sustainable farming."
    },
    # Add more articles here...
}

@app.route('/article/<int:article_id>')
def article_detail(article_id):
    # Fetch the article by ID, if it exists
    article = articles.get(article_id)

    if article:
        # Pass the article data to the template
        return render_template('article.html', article=article)
    else:
        # If the article doesn't exist, render a 'not found' page
        return render_template('article.html', article=None)

@app.route('/detail')
def detail():
    return render_template('detailp.html')

@app.route('/homee')
def homee():
    return render_template('indexpl.html')

@app.route('/article')
def article():
    return render_template('indexart.html')

@app.route('/', methods=['GET', 'POST'])
def model():
    if request.method == 'POST':
        # Get input values from the form
        temp = float(request.form['temp'])
        humid = float(request.form['humid'])
        mois = float(request.form['mois'])
        soil_type = int(request.form['soil'])  # Categorical input
        crop_type = int(request.form['crop'])  # Categorical input
        nitro = float(request.form['nitro'])
        pota = float(request.form['pota'])
        phos = float(request.form['phos'])

        # Prepare the input features for prediction
        # input_data = np.array([[temp, humid, mois, soil_type, crop_type, nitro, pota, phos]])
        input_data = np.array([[temp, humid, mois, soil_type, crop_type, nitro, pota, phos]])

        # Normalize the input data using MinMaxScaler
        input_data_norm = scaler.transform(input_data)  # Use the pre-fitted scaler
 # Fit and transform for the incoming data

        # Make the prediction
        prediction = rf_model.predict(input_data_norm)

        # Map the prediction to a fertilizer recommendation (14 types)
        fertilizer_dict = {
            0: "10-10-2010",
            1: "10-26-26",
            2: "14-14-14",
            3: "14-35-14",
            4: "15-15-15",
            5: "17-17-17",
            6: "20-20",
            7: "28-28",
            8: "DAP",
            9: "Potassium Chloride",
            10: "Potassium sulfate",
            11: "Superphosphate",
            12: "TSP",
            13: "Urea"
        }
        
        # Get the fertilizer recommendation
        recommended_fertilizer = fertilizer_dict.get(prediction[0], "Unknown Fertilizer")

        return render_template('form.html', x=recommended_fertilizer)
    
    return render_template('form.html', x="")

if __name__ == "__main__":
    app.run(debug=True)
