from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    result = ""

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        skills = request.form["skills"]
        studies = request.form["studies"]
        experience = request.form["experience"]
        job = request.form["job"]

        action = request.form["action"]
        language = request.form["language"]

        # Génération CV
        if action == "cv":

            if language == "fr":

                result = f"""
CV PROFESSIONNEL

Nom : {name}
Email : {email}
Téléphone : {phone}

Compétences :
{skills}

Études :
{studies}

Expériences :
{experience}

Poste recherché :
{job}
"""

            else:

                result = f"""
PROFESSIONAL RESUME

Name: {name}
Email: {email}
Phone: {phone}

Skills:
{skills}

Education:
{studies}

Experience:
{experience}

Desired Position:
{job}
"""

        # Génération Lettre
        elif action == "lettre":

            if language == "fr":

                result = f"""
Objet : Candidature pour le poste de {job}

Madame, Monsieur,

Je souhaite présenter ma candidature pour le poste de {job}.

Grâce à ma formation et à mes compétences en {skills},
j'ai développé des connaissances solides dans ce domaine.

Mes études :
{studies}

Mes expériences :
{experience}

Je reste à votre disposition pour un entretien.

Cordialement,

{name}
"""

            else:

                result = f"""
Subject: Application for {job}

Dear Hiring Manager,

I would like to apply for the position of {job}.

Through my education and skills in {skills},
I have developed strong knowledge in this field.

Education:
{studies}

Experience:
{experience}

Sincerely,

{name}
"""

        # Création PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, result)

        pdf.output("generated/cv.pdf")

    return render_template("index.html", result=result)


@app.route("/download")
def download():
    return send_file("generated/cv.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)