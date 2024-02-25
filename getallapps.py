import os
import webbrowser

def get_installed_software():
    software_list = []
    program_files_dirs = ["C:\\Program Files", "C:\\Program Files (x86)"]

    for program_files_dir in program_files_dirs:
        if os.path.isdir(program_files_dir):
            for dirpath, dirnames, filenames in os.walk(program_files_dir):
                for filename in filenames:
                    if filename.endswith(".exe"):
                        software_list.append(filename[:-4])
                    elif filename.endswith(".lnk"):
                        software_list.append(filename[:-4])

    return software_list

def list_of_software():
    installed_software = get_installed_software()
    return installed_software

def find_path(target_name):
    search_path = "C:\\"
    for root, dirs, files in os.walk(search_path):
        if target_name in dirs or target_name in files:
            return os.path.join(root, target_name)
    return None

def get_to_open(get_name):
    installed_software = get_installed_software()
    list_to_store = []
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "twitter": "https://www.twitter.com",
        "instagram": "https://www.instagram.com",
        "linkedin": "https://www.linkedin.com",
        "amazon": "https://www.amazon.com",
        "netflix": "https://www.netflix.com",
        "wikipedia": "https://www.wikipedia.org",
        "github": "https://www.github.com",
        "reddit": "https://www.reddit.com",
        "stackoverflow": "https://stackoverflow.com",
        "medium": "https://www.medium.com",
        "cnn": "https://www.cnn.com",
        "bbc": "https://www.bbc.co.uk",
        "nytimes": "https://www.nytimes.com",
        "walmart": "https://www.walmart.com",
        "target": "https://www.target.com",
        "etsy": "https://www.etsy.com",
        "flipkart": "https://www.flipkart.com",
        "gmail": "https://mail.google.com",
        "google drive": "https://drive.google.com",
        "google maps": "https://maps.google.com",
        "google map": "https://maps.google.com",
        "google news": "https://news.google.com",
        "google calendar": "https://calendar.google.com",
        "google photo": "https://photos.google.com",
        "google translate": "https://translate.google.com",
        "google docs": "https://docs.google.com",
        "google sheet": "https://sheets.google.com",
        "google slide": "https://slides.google.com",
        "google form": "https://forms.google.com",
        "google hangout": "https://hangouts.google.com",
        "google meet": "https://meet.google.com",
        "google classroom": "https://classroom.google.com",
        "google scholar": "https://scholar.google.com",
        "microsoft": "https://www.microsoft.com",
        "outlook": "https://outlook.live.com",
        "onedrive": "https://onedrive.live.com",
        "microsoft teams": "https://teams.microsoft.com",
        "word": "https://www.microsoft.com/en-us/microsoft-365/word",
        "excel": "https://www.microsoft.com/en-us/microsoft-365/excel",
        "powerpoint": "https://www.microsoft.com/en-us/microsoft-365/powerpoint",
        "onenote": "https://www.microsoft.com/en-us/microsoft-365/onenote",
        "sharepoint": "https://www.microsoft.com/en-us/microsoft-365/sharepoint",
        "microsoft edge": "https://www.microsoft.com/edge",
        "amazon prime video": "https://www.primevideo.com",
        "prime video": "https://www.primevideo.com",
        "hotstar": "https://www.hotstar.com",
        "disney+ hotstar": "https://www.hotstar.com",
        "sonyliv": "https://www.sonyliv.com",
        "zee5": "https://www.zee5.com",
        "zee": "https://www.zee5.com",
        "zeefive": "https://www.zee5.com",
        "voot": "https://www.voot.com",
        "mx player": "https://www.mxplayer.in",
        "alt balaji": "https://www.altbalaji.com",
        "jio cinema": "https://www.jiocinema.com",
        "jiocinema": "https://www.jiocinema.com",
        "eros now": "https://www.erosnow.com",
        "khan academy": "https://www.khanacademy.org",
        "coursera": "https://www.coursera.org",
        "edx": "https://www.edx.org",
        "udemy": "https://www.udemy.com",
        "codecademy": "https://www.codecademy.com",
        "mit opencourseware": "https://ocw.mit.edu",
        "harvard online learning": "https://online-learning.harvard.edu",
        "udacity": "https://www.udacity.com",
        "linkedin learning": "https://www.linkedin.com/learning",
        "skillshare": "https://www.skillshare.com",

    }
    opened_software = []

    for software in installed_software:
        list_to_store.append(software)

    if get_name in websites:
        webbrowser.open(websites[get_name])
    else:
        for software in list_to_store:
            if software.lower().startswith(get_name.lower()):
                opened_software.append(software)
                path = find_path(software + ".exe")
                if path:
                    os.startfile(path)
                else:
                    print(f"Path for {software} not found.")
                break
        else:
            print("Need to install the software")
