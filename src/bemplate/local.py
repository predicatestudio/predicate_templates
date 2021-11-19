## REQUIREMENTS
# Package with required versions
pins = [
    # "sample_package==1.0"
]
# Put most packages here
reqs = [
    "setuptools",
    "click",
]
# For convenience and development, not required for production
extras = [
    "pytest",
    "pytest-cov",
    "radon",
    "black",
    "flake8",
]

## Package Documentation (for pypi)
setup_author = ("Terminal Labs",)
setup_author_email = ("solutions@terminallabs.com",)
setup_license = "see LICENSE file"
setup_url = "https://github.com/predicatestudio/predicate_templates"
package_link = "src"

# ## Additional Configuritaion
# reponame = "code"
# SETUP_NAME = reponame
# EGG_NAME = SETUP_NAME.replace("_", "-")
# PAYLOADPATH = SITEPACKAGESPATH  # noqa: F841
# server_port = 5000
# socket_host = "0.0.0.0"
# PAYLOADPATH = resolve_payload_path(EGG_NAME, PROJECT_NAME)  # noqa: F821
# POSTGRES_URL = get_env_variable("POSTGRES_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")
# DB_URL = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(
#     user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB
# )
# MONGO_DB = PROJECT_NAME  # noqa: F821
# UPLOAD_FOLDER = "uploads"
# ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif", "zip"])
# BASEDIR = os.path.abspath(os.path.dirname(__file__))
# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# TEMPLATE_DIR = os.path.join(PAYLOADPATH, "templates")
# STATIC_DIR = os.path.join(PAYLOADPATH, "static")
# PERSISTENT_WORKING_DIRS = "stub"
# CONFIG_DIC = {
#     "POSTGRES_URL": POSTGRES_URL,
#     "POSTGRES_USER": POSTGRES_USER,
#     "POSTGRES_PW": POSTGRES_PW,
#     "POSTGRES_DB": POSTGRES_DB,
# }
# tempfile.tempdir = TEMPDIR  # noqa: F821

# ##
FRAMEWORK_VERSION = "0.0.1"
PRINT_VERBOSITY = "high"
EXCLUDED_DIRS = [".DS_Store"]
TEMPDIR = ".tmp/scratch"
DIRS = [f"{TEMPDIR}"]
TEXTTABLE_STYLE = ["-", "|", "+", "-"]

# Minimum version for this package
MINIMUM_PYTHON_VERSION = (3, 6, 0)
