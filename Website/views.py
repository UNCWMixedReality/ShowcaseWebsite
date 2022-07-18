from flask import Blueprint, render_template

views = Blueprint('views', __name__)




@views.route('/')
def home():
    return render_template("home.html")

@views.route('/VASCProject')
def Vasc():
    return render_template("VASC Project.html", text="Testing", user ="Testing2", boolean = True)

@views.route('/About')
def about():
    return render_template("About.html")

@views.route('/OtherProjects')
def OtherProj():
    return render_template("OtherProjects.html")

@views.route('/Publ')
def Publ():
    return render_template("Publ.html")

@views.route('/REU')
def REU():
    return render_template("REU.html")

@views.route('/VASCHome')
def VASCHome():
    return render_template("homeVASC.html")

@views.route('/TP') ##https://vr.uncw.edu/VASC/' ----- Teacher Portal Website
def TeacherPortal():
    return render_template("TP.html")

@views.route('/VASCPubl')
def VASCPubl():
    return render_template("PublVASC.html")

@views.route('/VASCAbout')
def VASCAbout():
    return render_template("AboutVASC.html")

@views.route('/VASCContributors')
def VASCContributors():
    return render_template("ContributorsVASC.html")

@views.route('/VASCPhotoGallery')
def VASCPhotoGallery():
    return render_template("PhotoGalleryVASC.html")


