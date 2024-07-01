## Virtual Environment

```
py -m venv .venv                   # create VE

.venv/Scripts/activate             # activate VE

deactivate                         # deactivate VE

```

## PIP

```
pip list                           # List all packages

pip install requests==2.30.0       # Install specific version

pip install -U requests            # Upgrade / Update:

pip uninstall requests             # Uninstall

pip show requests                  # View details of packages

pip freeze > requirements.txt      # to create a text file with a list of installed packages in the VE, with their versions:

```
