# blog
Static blog generator based on Pelican (https://github.com/getpelican/pelican) and used for https://blog.nrbrt.com

## Setup

 1. Clone repository: `git clone git@github.com:stueken/blog.git`
 2. Change to directory: `cd blog`
 3. Create a virtualenv: `pyenv virtualenv [PYTHON_VERSION] blog`
 4. Activate virtualenv for local directory: `pyenv local blog`
 5. Install packages: `pip install -r requirements.txt`
 6. Copy environment example file: `cp .env_sample .env`
 7. Adjust paremeters in `.env`
 8. Add image directory for photos plugin: `mkdir -p content/images`
 9. Build local version of site: `invoke build`
10. Serve site locally under http://localhost:8000: `invoke serve`
