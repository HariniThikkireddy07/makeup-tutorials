from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tutorials")
def tutorials():
    tutorials = [
        {
            "title": "Everyday Natural Makeup",
            "level": "Beginner",
            "time": "15 Minutes",
            "description": "A simple natural makeup routine for everyday office, college, and casual looks."
        },
        {
            "title": "South Indian Wedding Makeup",
            "level": "Intermediate",
            "time": "45 Minutes",
            "description": "A traditional wedding makeup look with glowing skin, defined eyes, and long-lasting makeup."
        },
        {
            "title": "Party Glam Makeup",
            "level": "Intermediate",
            "time": "30 Minutes",
            "description": "Create a glamorous evening look with foundation, concealer, eyeshadow, eyeliner, and lipstick."
        },
        {
            "title": "Soft Pink Makeup",
            "level": "Beginner",
            "time": "20 Minutes",
            "description": "A soft feminine makeup look using pink tones for cheeks, eyes, and lips."
        }
    ]

    return render_template("tutorials.html", tutorials=tutorials)


@app.route("/products")
def products():
    products = [
        {
            "name": "Primer",
            "category": "Base",
            "description": "Helps create a smooth base before foundation."
        },
        {
            "name": "Foundation",
            "category": "Base",
            "description": "Evens out the skin tone and creates a uniform base."
        },
        {
            "name": "Concealer",
            "category": "Base",
            "description": "Helps cover dark circles, blemishes, and pigmentation."
        },
        {
            "name": "Compact Powder",
            "category": "Base",
            "description": "Sets makeup and helps control excess shine."
        },
        {
            "name": "Blush",
            "category": "Cheeks",
            "description": "Adds natural color and dimension to the cheeks."
        },
        {
            "name": "Lipstick",
            "category": "Lips",
            "description": "Completes the makeup look with your preferred lip shade."
        }
    ]

    return render_template("products.html", products=products)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
