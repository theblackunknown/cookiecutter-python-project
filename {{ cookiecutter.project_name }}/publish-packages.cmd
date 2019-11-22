
setlocal

@for %%G IN (%~dp0modules\module-{{ cookiecutter.project_name }} %~dp0applications\application-{{ cookiecutter.project_name }}) do (
    call py -m twine upload --verbose^
     -r {{ cookiecutter.pypi_repository_name }}^
     %%G\dist\*^
     %*
)

