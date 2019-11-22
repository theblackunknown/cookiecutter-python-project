
setlocal

@for %%G IN (%~dp0modules\module-{{ cookiecutter.project_name }} %~dp0applications\application-{{ cookiecutter.project_name }}) do (
    pushd %%G
    call py setup.py sdist bdist_wheel
    @popd
)

rem TODO Add git commit hash to built packages
