
setlocal

@for %%G IN ("%~dp0modules\module-{{ cookiecutter.project_name }}" "%~dp0applications\application-{{ cookiecutter.project_name }}") do (
    call py -m pip install --editable %%G
)
