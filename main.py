import streamlit as st

import streamlit.components.v1 as components

from pathlib import Path

import html

# ==========================================================

# PAGE CONFIGURATION

# ==========================================================

st.set_page_config(

    page_title="Md. Mezan Mallik | Creative Portfolio",

    page_icon="✦",

    layout="wide",

    initial_sidebar_state="collapsed"

)

BASE_DIR = Path(__file__).parent

STATIC_DIR = BASE_DIR / "static"   # all media files live here

# ==========================================================

# HTML RENDER HELPER (FIXES THE "CODE SHOWING ON PAGE" ERROR)

# Markdown treats lines indented 4+ spaces as code blocks.

# This removes indentation and blank lines before rendering.

# ==========================================================

def render_html(markup: str):

    cleaned = "\n".join(

        line.strip() for line in markup.splitlines() if line.strip()

    )

    st.markdown(cleaned, unsafe_allow_html=True)

# ==========================================================

# MEDIA PATHS - CHANGE THESE PATHS MANUALLY

# ==========================================================

test_video = STATIC_DIR / "assets/reels/reel_01.mp4"

st.write("Static folder:", STATIC_DIR.exists())
st.write("Video exists:", test_video.exists())

if test_video.exists():
    st.write("Video size:", round(test_video.stat().st_size / (1024 * 1024), 2), "MB")

REELS = [

    "assets/reels/reel_01.mp4",

    "assets/reels/reel_02.mp4",

    "assets/reels/reel_03.mp4",

    "assets/reels/reel_04.mp4",

    "assets/reels/reel_05.mp4",

]

MOTION_GRAPHICS = [

    "assets/motion/motion_01.mp4",

    "assets/motion/motion_03.mp4",

]

THUMBNAILS = [

    "assets/thumbnails/thumbnail_01.jpg",

    "assets/thumbnails/thumbnail_02.jpg",

    "assets/thumbnails/thumbnail_03.jpg",

]

DOCUMENTARIES = [

    "assets/documentary/documentary_01.mp4",

    "assets/documentary/documentary_02.mp4",

    "assets/documentary/documentary_03.mp4",

]

UGC_ADS = [

    "assets/ugc/ugc_01.mp4",

    "assets/ugc/ugc_02.mp4",

]

PRODUCT_ADS = [

    "assets/product_ads/product_02.mp4",

    "assets/product_ads/product_03.mp4",

]

INVITATION_CARDS = [

    "assets/invitations/invitation_01.jpg",

    "assets/invitations/invitation_02.jpg",

    "assets/invitations/invitation_03.jpg",

    "assets/invitations/invitation_04.jpg",

]

AI_MODEL_LINK = "https://mezansky.netlify.app"

# Change contact information

EMAIL = "masudmallik99@gmail.com"

INSTAGRAM = "https://www.instagram.com/_mezan._.sky_?obrf=NDdnbmg3andqZGRx"

YOUTUBE = "https://youtube.com/"

# ==========================================================

# CUSTOM CSS

# ==========================================================

st.markdown("""

<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

* {

    scroll-behavior: smooth;

}

.stApp {

    background:

        radial-gradient(ellipse at 10% 0%,

        rgba(255, 85, 0, 0.55), transparent 32%),

        radial-gradient(ellipse at 90% 25%,

        rgba(112, 42, 10, 0.16), transparent 35%),

        #080604;

    color: white;

    font-family: 'DM Sans', sans-serif;

}

header {

    visibility: hidden;

}

footer {

    visibility: hidden;

}

.block-container {

    max-width: 1450px;

    padding-top: 1rem;

    padding-bottom: 3rem;

}

/* NAVIGATION */

.navbar {

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 14px 25px;

    margin-bottom: 75px;

    border: 1px solid rgba(255,255,255,0.12);

    border-radius: 50px;

    background: rgba(20,15,12,0.75);

    backdrop-filter: blur(20px);

}

.logo {

    font-family: Manrope;

    font-size: 19px;

    font-weight: 800;

    color: white;

}

.logo span {

    color: #ff652b;

}

.nav-links {

    display: flex;

    gap: 30px;

}

.nav-links a {

    color: #c9bdb5;

    text-decoration: none;

    font-size: 12px;

    transition: .3s;

}

.nav-links a:hover {

    color: #ff7138;

}

.nav-button {

    background: white;

    color: black !important;

    padding: 11px 20px;

    border-radius: 30px;

    font-size: 12px !important;

    text-decoration: none;

}

/* HERO */

.hero {

    text-align: center;

    padding: 10px 0 20px;

}

.hero-tag {

    display: inline-block;

    padding: 8px 16px;

    border: 1px solid rgba(255,110,50,.4);

    border-radius: 30px;

    color: #ff9b70;

    background: rgba(255,90,30,.08);

    font-size: 11px;

    letter-spacing: 2px;

    text-transform: uppercase;

}

.hero h1 {

    font-family: Manrope;

    font-size: clamp(40px, 6vw, 76px);

    line-height: 1.1;

    font-weight: 800;

    letter-spacing: -4px;

    margin: 25px auto 20px;

    max-width: 950px;

}

.hero h1 span {

    color: #ff7138;

}

.hero p {

    color: #b9aaa0;

    font-size: 15px;

    line-height: 1.8;

    max-width: 650px;

    margin: auto;

}

.hero-buttons {

    display: flex;

    justify-content: center;

    gap: 12px;

    margin: 30px 0;

}

.hero-buttons a {

    text-decoration: none;

    padding: 13px 22px;

    border-radius: 30px;

    font-size: 12px;

    font-weight: 700;

    transition: .3s;

}

.btn-primary {

    color: white;

    background: linear-gradient(100deg,#ff7138,#d83e12);

}

.btn-secondary {

    color: white;

    border: 1px solid #784023;

    background: rgba(40,20,10,.5);

}

.hero-buttons a:hover {

    transform: translateY(-3px);

}

/* HERO IMAGE STRIP */

.hero-gallery {

    display: flex;

    gap: 15px;

    overflow-x: auto;

    padding: 25px 5px;

    scrollbar-width: none;

}

.hero-gallery::-webkit-scrollbar {

    display: none;

}

.hero-card {

    flex: 0 0 160px;

    height: 190px;

    border-radius: 16px;

    border: 1px solid #55301f;

    background:

        linear-gradient(145deg,#9b3c13,#24130b 65%,#080604);

    display: flex;

    align-items: end;

    padding: 15px;

    box-shadow: 0 15px 35px rgba(0,0,0,.4);

    transform: rotate(-2deg);

    text-align: left;

}

.hero-card:nth-child(even) {

    transform: rotate(2deg);

}

.hero-card {

    position: relative;

    overflow: hidden;

}

.hero-card img,

.hero-card video {

    position: absolute;

    inset: 0;

    width: 100%;

    height: 100%;

    object-fit: cover;

}

.hero-card.has-media::after {

    content: "";

    position: absolute;

    inset: 0;

    background: linear-gradient(to top, rgba(8,6,4,.92), rgba(8,6,4,.1) 65%);

}

.hero-card > div {

    position: relative;

    z-index: 2;

}

.hero-card b {

    font-size: 13px;

}

.hero-card small {

    display: block;

    color: #d5ad99;

    margin-top: 5px;

    font-size: 10px;

}

/* SERVICES PILLS */

.pills {

    display: flex;

    justify-content: center;

    gap: 12px;

    flex-wrap: wrap;

    margin: 15px 0 65px;

}

.pill {

    padding: 10px 16px;

    border: 1px solid #443025;

    border-radius: 30px;

    color: #d9c9be;

    font-size: 11px;

    background: #130d09;

}

/* SECTION HEADINGS */

.section-header {

    display: flex;

    justify-content: space-between;

    align-items: end;

    gap: 20px;

    margin: 75px 0 22px;

}

.section-number {

    color: #ff824e;

    font-size: 11px;

    letter-spacing: 2px;

    text-transform: uppercase;

    font-weight: 700;

}

.section-header h2 {

    font-family: Manrope;

    font-size: clamp(25px,3vw,38px);

    font-weight: 800;

    letter-spacing: -1.5px;

    margin: 8px 0 0;

    color: #fff5ef;

}

.section-description {

    color: #a99b92;

    font-size: 12px;

    max-width: 420px;

    text-align: right;

    line-height: 1.7;

}

/* VIDEO GALLERY */

.gallery-wrapper {

    border: 1px solid rgba(255,255,255,.10);

    background: rgba(20,14,10,.65);

    border-radius: 20px;

    padding: 12px;

}

.video-track {

    display: flex;

    gap: 14px;

    overflow-x: auto;

    padding: 5px 3px 15px;

    scroll-snap-type: x mandatory;

    scrollbar-color: #80462a #1b100b;

}

.video-card {

    flex: 0 0 210px;

    scroll-snap-align: start;

    border-radius: 15px;

    overflow: hidden;

    background: #100b08;

    border: 1px solid #493024;

    transition: .3s;

}

.video-card:hover {

    transform: translateY(-6px);

    border-color: #ff7138;

}

.video-card video {

    width: 100%;

    height: 290px;

    display: block;

    object-fit: cover;

    cursor: pointer;

    background: #20130c;

}

.video-placeholder {

    height: 290px;

    display: flex;

    align-items: center;

    justify-content: center;

    flex-direction: column;

    padding: 15px;

    text-align: center;

    background:

        radial-gradient(circle at 30% 20%,#803514,#21120b 70%);

}

.video-placeholder span {

    color: #ff7138;

    font-size: 30px;

}

.video-placeholder b {

    font-size: 13px;

    margin: 10px;

}

.video-placeholder small {

    font-size: 10px;

    color: #c8a895;

}

.video-caption {

    padding: 12px;

    font-size: 12px;

    color: #e8d8cf;

    display: flex;

    justify-content: space-between;

}

.video-caption span {

    color: #ff7138;

}

.gallery-hint {

    font-size: 10px;

    color: #93847a;

    padding: 8px 3px 0;

}

/* IMAGE GALLERY */

[data-testid="stImage"] img {

    border-radius: 12px;

    border: 1px solid #493024;

    transition: .3s;

}

[data-testid="stImage"] img:hover {

    border-color: #ff7138;

    transform: translateY(-5px);

}

[data-testid="stCaptionContainer"] {

    color: #e8d8cf;

    font-size: 11px;

}

/* AI MODEL */

.ai-card {

    display: flex;

    justify-content: space-between;

    align-items: center;

    gap: 25px;

    padding: 35px;

    border-radius: 22px;

    border: 1px solid #61351e;

    background:

        radial-gradient(circle at 90% 0%,#7a341d50,transparent 45%),

        #130d09;

}

.ai-card h3 {

    font-family: Manrope;

    font-size: 28px;

    font-weight: 800;

    margin: 8px 0;

}

.ai-card p {

    color: #b9aaa0;

    font-size: 13px;

    max-width: 550px;

    line-height: 1.8;

}

.ai-link {

    display: inline-block;

    padding: 13px 22px;

    border-radius: 30px;

    background: linear-gradient(100deg,#ff7138,#d83e12);

    color: white !important;

    text-decoration: none;

    white-space: nowrap;

    font-size: 12px;

    font-weight: 700;

}

/* CONTACT */

.contact-box {

    border: 1px solid #54301e;

    border-radius: 20px;

    padding: 35px;

    background: #130d09;

    text-align: center;

}

.contact-box h2 {

    font-family: Manrope;

    font-size: 36px;

    font-weight: 800;

}

.contact-box p {

    color: #b9aaa0;

    font-size: 13px;

}

/* FOOTER */

.footer {

    margin-top: 70px;

    border-top: 1px solid #35251b;

    padding: 25px 0;

    display: flex;

    justify-content: space-between;

    flex-wrap: wrap;

    color: #93847a;

    font-size: 11px;

}

/* PRICING */

.pricing-grid {

    display: grid;

    grid-template-columns: repeat(3, 1fr);

    gap: 18px;

}

.price-card {

    position: relative;

    display: flex;

    flex-direction: column;

    padding: 32px 26px 26px;

    border-radius: 20px;

    border: 1px solid #35251b;

    background:

        radial-gradient(ellipse at 50% 110%, rgba(255,90,30,.28), transparent 60%),

        #0d0907;

}

.price-card.featured {

    border-color: #ff7138;

    background:

        radial-gradient(ellipse at 50% 110%, rgba(255,90,30,.38), transparent 60%),

        #130d09;

}

.price-card h3 {

    font-family: Manrope;

    font-size: 24px;

    font-weight: 800;

    margin: 0 0 8px;

    color: #fff5ef;

}

.price-desc {

    color: #b9aaa0;

    font-size: 12px;

    min-height: 34px;

}

.price-amount {

    margin: 30px 0 28px;

    display: flex;

    align-items: baseline;

    gap: 8px;

}

.price-amount b {

    font-family: Manrope;

    font-size: 56px;

    font-weight: 800;

    letter-spacing: -2px;

    background: linear-gradient(100deg,#ff9b70,#d83e12);

    -webkit-background-clip: text;

    background-clip: text;

    color: transparent;

}

.price-amount span {

    color: #d9c9be;

    font-size: 14px;

}

.price-features {

    list-style: none;

    padding: 0;

    margin: 0 0 30px;

    flex-grow: 1;

}

.price-features li {

    display: flex;

    align-items: center;

    gap: 10px;

    margin-bottom: 14px;

    color: #e8d8cf;

    font-size: 12px;

}

.price-features li::before {

    content: "✓";

    flex: 0 0 16px;

    height: 16px;

    border-radius: 50%;

    background: #d8541c;

    color: white;

    font-size: 9px;

    font-weight: 800;

    display: flex;

    align-items: center;

    justify-content: center;

}

.price-button {

    display: block;

    text-align: center;

    padding: 13px;

    border-radius: 30px;

    border: 1px solid #55301f;

    background: rgba(40,20,10,.5);

    color: #e8d8cf !important;

    font-size: 12px;

    font-weight: 600;

    text-decoration: none;

    transition: .3s;

}

.price-card.featured .price-button {

    border: none;

    color: white !important;

    background: linear-gradient(100deg,#ff7138,#d83e12);

}

.price-button:hover {

    transform: translateY(-3px);

}

.contact-details {

    display: flex;

    justify-content: center;

    gap: 14px;

    flex-wrap: wrap;

    margin-top: 18px;

}

.contact-details a {

    color: #e8d8cf;

    text-decoration: none;

    font-size: 13px;

    padding: 10px 18px;

    border: 1px solid #54301e;

    border-radius: 30px;

    background: rgba(40,20,10,.5);

    transition: .3s;

}

.contact-details a:hover {

    border-color: #ff7138;

    color: #ff7138;

}

@media(max-width:900px) {

    .pricing-grid {

        grid-template-columns: 1fr;

    }

}

/* MOBILE */

@media(max-width:700px) {

    .navbar {

        border-radius: 18px;

        margin-bottom: 40px;

        padding: 12px;

    }

    .nav-links {

        gap: 12px;

    }

    .nav-links a {

        font-size: 10px;

    }

    .hero h1 {

        letter-spacing: -2px;

    }

    .section-header {

        display: block;

    }

    .section-description {

        text-align: left;

        margin-top: 10px;

    }

    .ai-card {

        display: block;

    }

    .ai-link {

        margin-top: 15px;

    }

    .contact-box h2 {

        font-size: 27px;

    }

}

</style>

""", unsafe_allow_html=True)

# ==========================================================

# HERO CARD MEDIA - CHANGE THESE PATHS MANUALLY

# (title, subtitle, file path inside static/ or None for gradient only)

# ==========================================================

HERO_MEDIA = [

    ("Reels & Shorts",   "Short-form editing",   "assets/reels/reel_01.mp4"),

    ("Motion Graphics",  "Creative animation",   "assets/motion/motion_01.mp4"),

    ("Thumbnail Design", "Visual storytelling",  "assets/thumbnails/thumbnail_01.jpg"),

    ("Documentaries",    "Powerful stories",     "assets/documentary/documentary_01.mp4"),

    ("Product Ads",      "Creative campaigns",   "assets/product_ads/product_01.mp4"),

    ("AI Visuals",       "Next-gen creativity",  None),

]

def hero_cards_html():

    cards = []

    for title, subtitle, path in HERO_MEDIA:

        media = ""

        extra_class = ""

        if path and (STATIC_DIR / path).exists():

            extra_class = " has-media"

            src = f"/app/static/{path}"

            if path.lower().endswith((".mp4", ".webm")):

                media = (

                    f'<video src="{src}" autoplay muted loop '

                    f'playsinline preload="metadata"></video>'

                )

            else:

                media = f'<img src="{src}" alt="{html.escape(title)}">'

        cards.append(f"""

        <div class="hero-card{extra_class}">

            {media}

            <div>

                <b>{html.escape(title)}</b>

                <small>{html.escape(subtitle)}</small>

            </div>

        </div>

        """)

    return "".join(cards)

# ==========================================================

# NAVIGATION

# ==========================================================

render_html("""

<div class="navbar">

    <div class="logo">

        <span>✦</span> Mezan.creative

    </div>

    <div class="nav-links">

        <a href="#services">Services</a>

        <a href="#work">Work</a>

        <a href="#pricing">Pricing</a>

        <a href="#about">About</a>

        <a href="#contact">Contact</a>

    </div>

    <a href="#contact" class="nav-button">Get Started ↗</a>

</div>

""")

# ==========================================================

# HERO SECTION

# ==========================================================

render_html(f"""

<div class="hero" id="services">

    <div class="hero-tag">

        ✦ Creative Video Editor & Visual Designer

    </div>

    <h1>

        Visual stories that<br>

        <span>actually get attention.</span>

    </h1>

    <p>

        Hi, I'm Md. Mezan Mallik. I transform raw ideas into

        engaging videos, stunning visuals and creative designs.

        Helping brands and creators stand out through powerful

        storytelling and visual experiences.

    </p>

    <div class="hero-buttons">

        <a href="#contact" class="btn-primary">

            Start a Project ↗

        </a>

        <a href="#work" class="btn-secondary">

            Explore My Work ↓

        </a>

    </div>

    <div class="hero-gallery">

        {hero_cards_html()}

    </div>

    <div class="pills">

        <div class="pill">▣ Short-form Editing ◆</div>

        <div class="pill">◈ Motion Graphics ◆</div>

        <div class="pill">✧ Creative Design ◆</div>

        <div class="pill">↗ AI Visuals</div>

    </div>

</div>

""")

# ==========================================================

# SECTION HEADER FUNCTION

# ==========================================================

def section_header(number, title, description, anchor_id=None):

    id_attr = f'id="{anchor_id}"' if anchor_id else ""

    render_html(f"""

    <div class="section-header" {id_attr}>

        <div>

            <div class="section-number">

                SELECTED WORK / {number}

            </div>

            <h2>{html.escape(title)}</h2>

        </div>

        <div class="section-description">

            {html.escape(description)}

        </div>

    </div>

    """)

# ==========================================================

# VIDEO GALLERY FUNCTION

# ==========================================================

def video_gallery(video_paths, title, carousel=False):

    cards = []

    for i, relative_path in enumerate(video_paths):

        video_path = STATIC_DIR / relative_path

        video_title = f"{title} {i+1:02d}"

        if video_path.exists():

            # Served by Streamlit's static file server (no base64 needed)

            video_src = f"/app/static/{relative_path}"

            media = f"""

            <video

                src="{video_src}"

                muted

                loop

                playsinline

                preload="metadata">

            </video>

            """

        else:

            media = f"""

            <div class="video-placeholder">

                <span>✦</span>

                <b>{html.escape(video_title)}</b>

                <small>Add your video here</small>

                <small>{html.escape(relative_path)}</small>

            </div>

            """

        cards.append(f"""

        <div class="video-card">

            {media}

            <div class="video-caption">

                {html.escape(video_title)}

                <span>↗</span>

            </div>

        </div>

        """)

    # NOTE: components.html runs in its own iframe, so the page CSS

    # does not apply there. The same CSS is injected inside the iframe.

    iframe_css = """

    <style>

    body { margin: 0; background: transparent; color: white;

           font-family: 'DM Sans', sans-serif; }

    .gallery-wrapper {

        position: relative;

        border: 1px solid rgba(255,255,255,.10);

        background: rgba(20,14,10,.65);

        border-radius: 20px;

        padding: 12px;

    }

    .video-track {

        display: flex;

        gap: 14px;

        overflow-x: auto;

        padding: 5px 3px 15px;

        scroll-snap-type: x mandatory;

        scrollbar-color: #80462a #1b100b;

    }

    .video-card {

        flex: 0 0 210px;

        scroll-snap-align: start;

        border-radius: 15px;

        overflow: hidden;

        background: #100b08;

        border: 1px solid #493024;

        transition: .3s;

    }

    .video-card:hover {

        transform: translateY(-6px);

        border-color: #ff7138;

    }

    .video-card video {

        width: 100%;

        height: 290px;

        display: block;

        object-fit: cover;

        cursor: pointer;

        background: #20130c;

    }

    .video-placeholder {

        height: 290px;

        display: flex;

        align-items: center;

        justify-content: center;

        flex-direction: column;

        padding: 15px;

        text-align: center;

        background: radial-gradient(circle at 30% 20%,#803514,#21120b 70%);

    }

    .video-placeholder span { color: #ff7138; font-size: 30px; }

    .video-placeholder b { font-size: 13px; margin: 10px; }

    .video-placeholder small { font-size: 10px; color: #c8a895; }

    .video-caption {

        padding: 12px;

        font-size: 12px;

        color: #e8d8cf;

        display: flex;

        justify-content: space-between;

    }

    .video-caption span { color: #ff7138; }

    .gallery-hint {

        font-size: 10px;

        color: #93847a;

        padding: 8px 3px 0;

    }

    .carousel-btn {

        position: absolute;

        top: 170px;

        z-index: 5;

        width: 38px;

        height: 38px;

        border-radius: 50%;

        border: 1px solid #784023;

        background: rgba(20,14,10,.85);

        color: #ff7138;

        font-size: 16px;

        cursor: pointer;

        transition: .3s;

    }

    .carousel-btn:hover {

        background: #ff7138;

        color: white;

    }

    .carousel-btn.prev { left: 6px; }

    .carousel-btn.next { right: 6px; }

    .video-track { scroll-behavior: smooth; }

    </style>

    """

    arrows = (

        '<button class="carousel-btn prev" aria-label="Previous">❮</button>'

        '<button class="carousel-btn next" aria-label="Next">❯</button>'

        if carousel else ""

    )

    gallery_html = iframe_css + """

    <div class="gallery-wrapper">

        """ + arrows + """

        <div class="video-track">

    """ + "".join(cards) + """

        </div>

        <div class="gallery-hint">

            ← Scroll sideways to explore · Hover to preview ·

            Click to watch fullscreen →

        </div>

    </div>

    <script>

        const videos = document.querySelectorAll("video");

        videos.forEach(video => {

            // Play automatically on hover

            video.addEventListener("mouseenter", () => {

                video.play().catch(() => {});

            });

            // Stop when cursor leaves

            video.addEventListener("mouseleave", () => {

                if (!document.fullscreenElement) {

                    video.pause();

                    video.currentTime = 0;

                }

            });

            // Click to watch fullscreen

            video.addEventListener("click", async () => {

                try {

                    if (video.requestFullscreen) {

                        await video.requestFullscreen();

                    }

                    else if (video.webkitEnterFullscreen) {

                        video.webkitEnterFullscreen();

                    }

                    video.controls = true;

                    await video.play();

                }

                catch(error) {}

            });

            // Restore preview after fullscreen

            document.addEventListener("fullscreenchange", () => {

                if (!document.fullscreenElement) {

                    video.controls = false;

                    video.pause();

                    video.currentTime = 0;

                }

            });

        });

    </script>

    """

    carousel_script = """

    <script>

    (function () {

        const track = document.querySelector(".video-track");

        const prev = document.querySelector(".carousel-btn.prev");

        const next = document.querySelector(".carousel-btn.next");

        if (!track || !prev || !next) return;

        const step = () => {

            const card = track.querySelector(".video-card");

            return card ? card.offsetWidth + 14 : 224;

        };

        const goNext = () => {

            if (track.scrollLeft + track.clientWidth >= track.scrollWidth - 5) {

                track.scrollTo({ left: 0 });

            } else {

                track.scrollBy({ left: step() });

            }

        };

        const goPrev = () => {

            if (track.scrollLeft <= 5) {

                track.scrollTo({ left: track.scrollWidth });

            } else {

                track.scrollBy({ left: -step() });

            }

        };

        next.addEventListener("click", goNext);

        prev.addEventListener("click", goPrev);

        let timer = setInterval(goNext, 3500);

        const stop = () => clearInterval(timer);

        const start = () => { stop(); timer = setInterval(goNext, 3500); };

        track.addEventListener("mouseenter", stop);

        track.addEventListener("mouseleave", start);

        track.addEventListener("touchstart", stop, { passive: true });

        prev.addEventListener("mouseenter", stop);

        next.addEventListener("mouseenter", stop);

    })();

    </script>

    """

    if carousel:

        gallery_html += carousel_script

    # st.iframe is the new replacement for components.html

    if hasattr(st, "iframe"):

        st.iframe(gallery_html, height=390)

    else:

        components.html(gallery_html, height=390, scrolling=False)

# ==========================================================

# IMAGE GALLERY FUNCTION

# ==========================================================

def image_gallery(image_paths, title):

    existing_images = []

    for path in image_paths:

        full_path = STATIC_DIR / path

        if full_path.exists():

            existing_images.append(full_path)

    if not existing_images:

        st.info(

            f"Add your {title} images to the configured folder paths."

        )

        for path in image_paths:

            st.caption(f"Image path: {path}")

        return

    columns = st.columns(3, gap="medium")

    for i, image_path in enumerate(existing_images):

        with columns[i % 3]:

            st.image(

                str(image_path),

                width="stretch"

            )

            st.caption(f"{title} {i+1:02d}")

# ==========================================================

# 01 - REELS & SHORT-FORM VIDEO EDITING

# ==========================================================

section_header(

    "01",

    "Reels & Short-form Video Editing",

    "Engaging Instagram Reels, TikToks and YouTube Shorts with dynamic transitions, captions and storytelling.",

    anchor_id="work"

)

video_gallery(

    REELS,

    "Short-form video",

    carousel=True

)

# ==========================================================

# 02 - MOTION GRAPHICS

# ==========================================================

section_header(

    "02",

    "Motion Graphics",

    "Creative animations, kinetic typography, animated titles and motion design."

)

video_gallery(

    MOTION_GRAPHICS,

    "Motion graphics",

)

# ==========================================================

# 03 - THUMBNAIL DESIGN

# ==========================================================

section_header(

    "03",

    "Thumbnail Design",

    "Eye-catching thumbnail designs that attract viewers and increase clicks."

)

image_gallery(

    THUMBNAILS,

    "Thumbnail design"

)

# ==========================================================

# 04 - DOCUMENTARY VIDEO EDITING

# ==========================================================

section_header(

    "04",

    "Documentary Video Editing",

    "Professional storytelling, cinematic pacing, sound design and documentary editing."

)

video_gallery(

    DOCUMENTARIES,

    "Documentary"

)

# ==========================================================

# 05 - UGC AD CREATION

# ==========================================================

section_header(

    "05",

    "UGC Ad Creation",

    "Authentic creator-style advertisements designed to engage audiences and promote brands."

)

video_gallery(

    UGC_ADS,

    "UGC advertisement"

)

# ==========================================================

# 06 - PRODUCT AD CREATION

# ==========================================================

section_header(

    "06",

    "Product Ad Creation",

    "High-quality product advertisements with creative visuals and professional editing."

)

video_gallery(

    PRODUCT_ADS,

    "Product advertisement"

)

# ==========================================================

# 07 - AI MODEL VISUALS

# ==========================================================

section_header(

    "07",

    "AI Model Visuals",

    "Explore AI-generated models, digital characters and creative AI-powered visuals."

)

render_html(f"""

<div class="ai-card" id="about">

    <div>

        <div class="section-number">

            AI POWERED CREATIVITY

        </div>

        <h3>

            Explore My AI Model World.

        </h3>

        <p>

            Discover my AI model visuals, digital characters

            and experimental creative projects in a separate

            interactive experience.

        </p>

    </div>

    <a class="ai-link"

       href="{AI_MODEL_LINK}"

       target="_blank">

        Explore AI Models ↗

    </a>

</div>

""")

# ==========================================================

# 08 - INVITATION CARD DESIGN

# ==========================================================

section_header(

    "08",

    "Invitation Card Design",

    "Beautiful digital invitations for birthdays, weddings, celebrations and special occasions."

)

image_gallery(

    INVITATION_CARDS,

    "Invitation card"

)

# ==========================================================

# PRICING

# ==========================================================

PRICING_PLANS = [

    {

        "name": "Starter",

        "description": "Perfect for creators just getting started",

        "price": "$2",

        "unit": "/ video",

        "featured": False,

        "features": [

            "Short-form video editing",

            "Basic editing + captions",

            "Max 30s video length",

            "Platform-ready formats (Reels, TikTok, Shorts)",

            "Standard export quality",

            "Email support",

        ],

    },

    {

        "name": "Professional",

        "description": "For creators & brands ready to grow consistently",

        "price": "$5",

        "unit": "/ video",

        "featured": True,

        "features": [

            "Advanced editing + captions",

            "Motion graphics & effects",

            "Hook & storytelling optimization",

            "Max 60s video length",

            "Priority export (HD 1080p)",

            "2 free revisions",

        ],

    },

    {

        "name": "Business",

        "description": "Best for teams scaling content at volume",

        "price": "$8",

        "unit": "/ video",

        "featured": False,

        "features": [

            "Full editing + content optimization",

            "Custom motion graphics",

            "Sound design & color grading",

            "Strategy support & content planning",

            "Priority delivery (48hr)",

            "Unlimited revisions & dedicated support",

        ],

    },

]

render_html("""

<div class="section-header" id="pricing">

    <div>

        <div class="section-number">PRICING</div>

        <h2>Simple, transparent pricing.</h2>

    </div>

    <div class="section-description">

        Choose the plan that fits your content needs.

        Custom packages are available on request.

    </div>

</div>

""")

plan_cards = []

for plan in PRICING_PLANS:

    features_html = "".join(

        f"<li>{html.escape(item)}</li>" for item in plan["features"]

    )

    featured_class = " featured" if plan["featured"] else ""

    button_text = "Get Started Now ↗" if plan["featured"] else "Get Started Now"

    plan_cards.append(f"""

    <div class="price-card{featured_class}">

        <h3>{html.escape(plan["name"])}</h3>

        <div class="price-desc">{html.escape(plan["description"])}</div>

        <div class="price-amount">

            <b>{html.escape(plan["price"])}</b>

            <span>{html.escape(plan["unit"])}</span>

        </div>

        <ul class="price-features">{features_html}</ul>

        <a class="price-button" href="#contact">{button_text}</a>

    </div>

    """)

render_html(

    '<div class="pricing-grid">' + "".join(plan_cards) + "</div>"

)

# ==========================================================

# CONTACT SECTION

# ==========================================================

render_html("""

<div class="section-header" id="contact">

    <div>

        <div class="section-number">

            LET'S WORK TOGETHER

        </div>

        <h2>

            Have a project in mind?

        </h2>

    </div>

    <div class="section-description">

        Let's transform your ideas into creative

        videos and stunning visual experiences.

    </div>

</div>

""")

render_html(f"""

<div class="contact-box">

    <div class="section-number">

        GET IN TOUCH

    </div>

    <h2>

        Let's create something amazing.

    </h2>

    <p>

        Have an idea? Let's bring it to life.

    </p>

    <div style="margin-top:25px;">

        <a href="mailto:{EMAIL}"

           class="btn-primary"

           style="padding:13px 25px;

                  border-radius:30px;

                  text-decoration:none;

                  color:white;

                  font-size:12px;

                  font-weight:bold;">

            Contact Me ↗

        </a>

    </div>

    <div class="contact-details">

        <a href="mailto:{EMAIL}">✉ {EMAIL}</a>

        <a href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer">Instagram ↗</a>

        <a href="https://drive.google.com/file/d/1oM9ki5aR2GiuyWsBG7y3UQQwtWAU_GOy/view?usp=drivesdk" target="_blank" rel="noopener noreferrer">More Details ↗</a>

    </div>

</div>

""")

# ==========================================================

# FOOTER

# ==========================================================

render_html("""

<div class="footer">

    <div>

        © 2026 Md. Mezan Mallik. All rights reserved.

    </div>

    <div>

        Designed with creativity ✦

    </div>

</div>

""")

# ==========================================================
# ADDITIONAL LINKS & CLOSING MESSAGE
# ==========================================================

